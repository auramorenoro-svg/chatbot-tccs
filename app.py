# app.py
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from database.db import init_db
from bot.handler import procesar_mensaje
from scheduler.reminders import iniciar_scheduler
from config import Config
import atexit
import os
import requests

app = Flask(__name__)
app.secret_key = Config.FLASK_SECRET_KEY

# 🔴 CONFIG META
VERIFY_TOKEN = "123456"
ACCESS_TOKEN = "EAAXim2ZAhFH4BRT6ZAqwXEW8Exsxv5d1O1DTZCnFZACiqvOuG5BegkZAoEVsyaK39XkXc2yaV80hqhCGsZAB5aZAZAteOYuXnZA5gL5BBAcjxEhUar2niVYevUjj6M442ZArb7HAJuqSHY6O37uEZB7jqINQj77lbE3yFZBEvYWDy7XPPMtN1GVb7QIGk7aj0ZBkZALC4VfD4IAjQXYazZCaZC00rMbsCX3lbgHuOlBr0E6ZC8SXSjETiisLH2LtzvVDuhxvmeNn3fXMZC2ZCQsz0LgISwW9D2ATgm6kEj5j74sAkOXkgZDZD"
PHONE_NUMBER_ID = "1066131316591755"

with app.app_context():
    init_db()

scheduler = iniciar_scheduler()
atexit.register(lambda: scheduler.shutdown())


@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    # 🔴 VERIFICACIÓN META (ESTO ERA LO QUE FALTABA BIEN)
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        print("[META VERIFY] mode:", mode, "token:", token)

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("✅ Webhook verificado correctamente")
            return challenge, 200
        else:
            print("❌ Error en verificación")
            return "error", 403

    # 🔴 MENSAJES
    if request.method == "POST":

        # 🟢 TWILIO
        if request.form.get("From"):
            numero_remitente = request.form.get("From", "")
            mensaje_recibido = request.form.get("Body", "").strip()

            if not numero_remitente or not mensaje_recibido:
                return "", 204

            print(f"[TWILIO] {numero_remitente}: {mensaje_recibido}")

            respuesta_texto = procesar_mensaje(numero_remitente, mensaje_recibido)

            respuesta_twiml = MessagingResponse()
            respuesta_twiml.message(respuesta_texto)

            return str(respuesta_twiml), 200, {"Content-Type": "text/xml"}

        # 🔵 META
        data = request.get_json()
        print("[META RAW]:", data)

        try:
            entry = data.get("entry", [])[0]
            changes = entry.get("changes", [])[0]
            value = changes.get("value", {})
            messages = value.get("messages")

            if messages:
                mensaje = messages[0]
                numero_remitente = mensaje["from"]
                texto = mensaje.get("text", {}).get("body", "")

                print(f"[META] {numero_remitente}: {texto}")

                respuesta = procesar_mensaje(numero_remitente, texto)

                print(f"[RESPUESTA BOT] {respuesta}")

                url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

                headers = {
                    "Authorization": f"Bearer {ACCESS_TOKEN}",
                    "Content-Type": "application/json"
                }

                payload = {
                    "messaging_product": "whatsapp",
                    "to": numero_remitente,
                    "type": "text",
                    "text": {
                        "body": respuesta
                    }
                }

                r = requests.post(url, headers=headers, json=payload)

                print("[META SEND STATUS]:", r.status_code, r.text)

        except Exception as e:
            print("[ERROR META]:", e)

        return "ok", 200


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