# bot/progreso.py
import gspread
from google.oauth2.service_account import Credentials
import json
import os
import traceback

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def get_datos_paciente(nombre: str) -> list:
    try:
        creds_json = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
        creds_dict = json.loads(creds_json)
        creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
        client = gspread.authorize(creds)
        sheet_id = os.getenv("GOOGLE_SHEET_ID")
        spreadsheet = client.open_by_key(sheet_id)
        sheet = spreadsheet.worksheet("Respuestas de formulario 1")
        registros = sheet.get_all_records()
        
        datos = [
            r for r in registros
            if str(r.get("¿Cuál es tu nombre?", "")).strip().lower() == nombre.strip().lower()
        ]
        return datos
    except Exception as e:
        print(f"[ERROR PROGRESO DETALLE] {traceback.format_exc()}")
        return []


def parsear_hora(hora_str):
    from datetime import datetime
    hora_str = str(hora_str).strip()
    hora_normalizada = hora_str.replace("a.m.", "AM").replace("p.m.", "PM").replace("a. m.", "AM").replace("p. m.", "PM")
    formatos = [
        "%I:%M:%S %p",
        "%I:%M %p",
        "%H:%M:%S",
        "%H:%M"
    ]
    for fmt in formatos:
        try:
            return datetime.strptime(hora_normalizada, fmt)
        except:
            continue
    return None


def calcular_eficiencia(hora_cama, hora_levantarse, latencia, tiempo_despierto):
    try:
        from datetime import timedelta
        t_cama = parsear_hora(hora_cama)
        t_levanta = parsear_hora(hora_levantarse)
        
        if not t_cama or not t_levanta:
            return None
        
        diff = t_levanta - t_cama
        if diff.total_seconds() < 0:
            diff = diff + timedelta(days=1)
        
        tiempo_en_cama = diff.total_seconds() / 60
        tiempo_dormido = tiempo_en_cama - float(latencia or 0) - float(tiempo_despierto or 0)
        
        if tiempo_en_cama > 0:
            eficiencia = round((tiempo_dormido / tiempo_en_cama) * 100, 1)
            return max(0, min(100, eficiencia))
        return 0
    except:
        return None