# app.py
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from database.db import init_db
from bot.handler import procesar_mensaje
from scheduler.reminders import iniciar_scheduler
from config import Config
import atexit
import os

app = Flask(__name__)
app.secret_key = Config.FLASK_SECRET_KEY

with app.app_context():
    init_db()

scheduler = iniciar_scheduler()
atexit.register(lambda: scheduler.shutdown())


@app.route("/webhook", methods=["POST"])
def webhook():
    numero_remitente = request.form.get("From", "")
    mensaje_recibido = request.form.get("Body", "").strip()
    
    if not numero_remitente or not mensaje_recibido:
        return "", 204
    
    print(f"[MENSAJE RECIBIDO] De: {numero_remitente} | Texto: {mensaje_recibido}")
    
    respuesta_texto = procesar_mensaje(numero_remitente, mensaje_recibido)
    
    respuesta_twiml = MessagingResponse()
    respuesta_twiml.message(respuesta_texto)
    
    print(f"[RESPUESTA ENVIADA] A: {numero_remitente} | Texto: {respuesta_texto[:80]}...")
    
    return str(respuesta_twiml), 200, {"Content-Type": "text/xml"}


@app.route("/", methods=["GET"])
def salud():
    return jsonify({
        "status": "activo",
        "proyecto": "ChatBot TCC-I para WhatsApp",
        "version": "1.0"
    })


@app.route("/pacientes", methods=["GET"])
def ver_pacientes():
    from database.db import get_db
    from database.models import Paciente
    
    db = get_db()
    try:
        pacientes = db.query(Paciente).all()
        datos = []
        for p in pacientes:
            datos.append({
                "id": p.id,
                "nombre": p.nombre,
                "numero": p.numero_whatsapp,
                "modulo_actual": p.modulo_actual,
                "activo": p.activo,
                "recordatorios": p.recordatorios_activados,
                "fecha_registro": str(p.fecha_registro),
                "ultima_interaccion": str(p.ultima_interaccion)
            })
        return jsonify({"total": len(datos), "pacientes": datos})
    finally:
        db.close()


@app.route("/borrar_paciente/<int:paciente_id>", methods=["POST"])
def borrar_paciente(paciente_id: int):
    from database.db import get_db
    from database.models import Paciente
    
    db = get_db()
    try:
        paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
        if not paciente:
            return jsonify({"error": "Paciente no encontrado"}), 404
        db.delete(paciente)
        db.commit()
        return jsonify({"mensaje": "Paciente borrado correctamente"})
    finally:
        db.close()


@app.route("/avanzar_modulo/<int:paciente_id>", methods=["POST"])
def avanzar_modulo_admin(paciente_id: int):
    from database.db import get_db
    from database.models import Paciente
    from bot.modules import avanzar_modulo
    
    db = get_db()
    try:
        paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
        if not paciente:
            return jsonify({"error": "Paciente no encontrado"}), 404
        
        resultado = avanzar_modulo(paciente)
        db.commit()
        
        return jsonify({
            "mensaje": resultado,
            "paciente": paciente.nombre,
            "modulo_nuevo": paciente.modulo_actual
        })
    finally:
        db.close()


@app.route("/progreso/<nombre>", methods=["GET"])
def ver_progreso(nombre: str):
    from bot.progreso import get_datos_paciente
    from bot.template_progreso import generar_html_progreso
    datos = get_datos_paciente(nombre)
    html = generar_html_progreso(nombre, datos)
    return html, 200, {"Content-Type": "text/html"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False, use_reloader=False)