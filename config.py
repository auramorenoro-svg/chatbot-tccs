# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Twilio
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

    # App
    FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")
    
    # Google Form (Diario de Sueño)
    GOOGLE_FORM_URL = os.getenv("GOOGLE_FORM_URL")

    # Hora del recordatorio diario (formato 24h)
    REMINDER_HOUR = 8
    REMINDER_MINUTE = 0

    # Recordatorio nocturno
    EVENING_REMINDER_HOUR = 20
    EVENING_REMINDER_MINUTE = 0

    # Base de datos
    DATABASE_URL = "sqlite:///chatbot_tccs.db"