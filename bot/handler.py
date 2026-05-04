# bot/handler.py
from database.db import get_db
from database.models import Paciente, RegistroMensaje
from bot.messages import (
    BIENVENIDA, BIENVENIDA_REGISTRADO, LINK_DIARIO,
    TECNICAS_RELAJACION, MENU_PRINCIPAL, NO_ENTENDIDO,
    RECORDATORIOS_DESACTIVADOS, RECORDATORIOS_ACTIVADOS,
    RESPIRACION_DETALLE
)
from bot.faq import buscar_respuesta_faq
from bot.modules import (
    obtener_descripcion_modulo,
    obtener_tareas_modulo,
    avanzar_modulo
)
from config import Config
from datetime import datetime


def registrar_mensaje(db, numero: str, direccion: str, contenido: str):
    registro = RegistroMensaje(
        numero_whatsapp=numero,
        direccion=direccion,
        contenido=contenido,
        timestamp=datetime.utcnow()
    )
    db.add(registro)
    db.commit()


def obtener_o_crear_paciente(db, numero: str) -> Paciente:
    paciente = db.query(Paciente).filter(
        Paciente.numero_whatsapp == numero
    ).first()
    
    if not paciente:
        paciente = Paciente(
            numero_whatsapp=numero,
            sesion_activa="esperando_nombre"
        )
        db.add(paciente)
        db.commit()
        db.refresh(paciente)
    
    paciente.ultima_interaccion = datetime.utcnow()
    db.commit()
    
    return paciente


def procesar_mensaje(numero: str, mensaje: str) -> str:
    db = get_db()
    mensaje_limpio = mensaje.strip()
    mensaje_lower = mensaje_limpio.lower()
    
    try:
        registrar_mensaje(db, numero, "entrada", mensaje_limpio)
        paciente = obtener_o_crear_paciente(db, numero)
        
        if paciente.sesion_activa == "esperando_nombre":
            paciente.nombre = mensaje_limpio.title()
            paciente.sesion_activa = "activo"
            db.commit()
            
            respuesta = (
                f"Mucho gusto, {paciente.nombre}. Estas registrado/a en el programa.\n\n"
                f"Recibiras recordatorios cada manana a las 8:00 AM para llenar tu diario de sueno "
                f"y cada noche a las 8:00 PM con consejos de higiene del sueno.\n\n"
                + MENU_PRINCIPAL
            )
            
            registrar_mensaje(db, numero, "salida", respuesta)
            return respuesta
        
        nombre = paciente.nombre or "Participante"
        
        if any(x in mensaje_lower for x in ["menu", "menú", "inicio", "opciones", "ayuda"]):
            respuesta = BIENVENIDA_REGISTRADO(nombre)
            
        elif any(x in mensaje_lower for x in [
            "diario", "llenar", "formulario", "sueno", "sueño",
            "registro", "enlace", "link", "liga", "2"
        ]):
            respuesta = LINK_DIARIO(Config.GOOGLE_FORM_URL)
        
        elif any(x in mensaje_lower for x in [
            "relajacion", "relajación", "relax", "relajar", "tecnicas", "3"
        ]):
            respuesta = TECNICAS_RELAJACION
        
        elif any(x in mensaje_lower for x in [
            "respiracion", "respiración", "respirar"
        ]):
            respuesta = RESPIRACION_DETALLE
        
        elif any(x in mensaje_lower for x in [
            "mindfulness", "meditacion", "atencion plena"
        ]):
            respuesta = """*Mindfulness para el Sueno*

El mindfulness o atencion plena te ayuda a reducir la activacion mental antes de dormir.

Pasos:
1. Siéntate o acuestate comodamente
2. Cierra los ojos y lleva tu atencion a tu respiracion
3. Observa como entra y sale el aire, sin intentar cambiarlo
4. Cuando tu mente se distraiga, vuelve suavemente a la respiracion
5. Practica durante 5 a 10 minutos

Video guia:
https://www.youtube.com/watch?v=QHNJyiMUgnQ"""
        
        elif any(x in mensaje_lower for x in [
            "modulo", "módulo", "sesion", "sesión", "semana", "donde estoy", "1"
        ]):
            respuesta = obtener_descripcion_modulo(paciente.modulo_actual)
        
        elif any(x in mensaje_lower for x in [
            "tareas", "que debo hacer", "actividades", "mis tareas"
        ]):
            respuesta = obtener_tareas_modulo(paciente.modulo_actual)
        
        elif "avanzar modulo" in mensaje_lower or "siguiente modulo" in mensaje_lower:
            resultado = avanzar_modulo(paciente)
            db.commit()
            respuesta = resultado + "\n\n" + obtener_descripcion_modulo(paciente.modulo_actual)
        
        elif any(x in mensaje_lower for x in [
            "preguntas", "frecuentes", "faq", "4"
        ]):
            respuesta = """Puedes preguntarme sobre estos temas directamente:

- Respiracion
- Mindfulness
- Control de estimulos
- Higiene del sueno
- Pensamientos en la noche
- Restriccion de sueno
- Paradoja del sueno
- Medicamentos para el sueno

Escribe el tema directamente o haz tu pregunta."""
        
        elif any(x in mensaje_lower for x in [
            "desactivar", "pausar recordatorio", "no quiero recordatorios",
            "detener recordatorio", "5"
        ]):
            paciente.recordatorios_activados = False
            db.commit()
            respuesta = RECORDATORIOS_DESACTIVADOS
        
        elif any(x in mensaje_lower for x in [
            "activar", "reactivar", "quiero recordatorios",
            "volver recordatorio", "6"
        ]):
            paciente.recordatorios_activados = True
            db.commit()
            respuesta = RECORDATORIOS_ACTIVADOS
        
        else:
            respuesta_faq = buscar_respuesta_faq(mensaje_lower)
            if respuesta_faq:
                respuesta = respuesta_faq
            else:
                respuesta = NO_ENTENDIDO
        
        registrar_mensaje(db, numero, "salida", respuesta)
        return respuesta
    
    except Exception as e:
        print(f"[ERROR] Error procesando mensaje de {numero}: {e}")
        return "Ocurrio un error. Por favor intenta de nuevo o escribe 'menu'."
    
    finally:
        db.close()