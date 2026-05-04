# scheduler/reminders.py
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from twilio.rest import Client
from database.db import get_db
from database.models import Paciente
from bot.messages import RECORDATORIO_MANANA, RECORDATORIO_NOCHE
from config import Config
import pytz

ZONA_HORARIA = pytz.timezone("America/Mexico_City")


def get_twilio_client():
    return Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)


def enviar_mensaje_whatsapp(numero: str, mensaje: str):
    try:
        client = get_twilio_client()
        message = client.messages.create(
            body=mensaje,
            from_=Config.TWILIO_WHATSAPP_NUMBER,
            to=f"whatsapp:{numero}" if not numero.startswith("whatsapp:") else numero
        )
        print(f"[RECORDATORIO] Enviado a {numero}: SID {message.sid}")
        return True
    except Exception as e:
        print(f"[ERROR] No se pudo enviar recordatorio a {numero}: {e}")
        return False


def recordatorio_manana():
    print("[SCHEDULER] Ejecutando recordatorio matutino...")
    db = get_db()
    try:
        pacientes = db.query(Paciente).filter(
            Paciente.activo == True,
            Paciente.recordatorios_activados == True,
            Paciente.sesion_activa == "activo"
        ).all()
        
        enviados = 0
        for paciente in pacientes:
            nombre = paciente.nombre or "Participante"
            mensaje = RECORDATORIO_MANANA(nombre, Config.GOOGLE_FORM_URL)
            exito = enviar_mensaje_whatsapp(paciente.numero_whatsapp, mensaje)
            if exito:
                enviados += 1
        
        print(f"[SCHEDULER] Recordatorio matutino enviado a {enviados} pacientes.")
    except Exception as e:
        print(f"[ERROR SCHEDULER] {e}")
    finally:
        db.close()


def recordatorio_noche():
    print("[SCHEDULER] Ejecutando recordatorio nocturno...")
    db = get_db()
    try:
        pacientes = db.query(Paciente).filter(
            Paciente.activo == True,
            Paciente.recordatorios_activados == True,
            Paciente.sesion_activa == "activo"
        ).all()
        
        enviados = 0
        for paciente in pacientes:
            nombre = paciente.nombre or "Participante"
            mensaje = RECORDATORIO_NOCHE(nombre)
            exito = enviar_mensaje_whatsapp(paciente.numero_whatsapp, mensaje)
            if exito:
                enviados += 1
        
        print(f"[SCHEDULER] Recordatorio nocturno enviado a {enviados} pacientes.")
    except Exception as e:
        print(f"[ERROR SCHEDULER] {e}")
    finally:
        db.close()


def iniciar_scheduler():
    scheduler = BackgroundScheduler(timezone=ZONA_HORARIA)
    
    scheduler.add_job(
        func=recordatorio_manana,
        trigger=CronTrigger(
            hour=Config.REMINDER_HOUR,
            minute=Config.REMINDER_MINUTE,
            timezone=ZONA_HORARIA
        ),
        id="recordatorio_manana",
        name="Recordatorio matutino diario de sueno",
        replace_existing=True
    )
    
    scheduler.add_job(
        func=recordatorio_noche,
        trigger=CronTrigger(
            hour=Config.EVENING_REMINDER_HOUR,
            minute=Config.EVENING_REMINDER_MINUTE,
            timezone=ZONA_HORARIA
        ),
        id="recordatorio_noche",
        name="Recordatorio nocturno higiene del sueno",
        replace_existing=True
    )
    
    scheduler.start()
    print(f"[SCHEDULER] Iniciado. Recordatorio manana: {Config.REMINDER_HOUR}:00 AM | Noche: {Config.EVENING_REMINDER_HOUR}:00 PM")
    return scheduler