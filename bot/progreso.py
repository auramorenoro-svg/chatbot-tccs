# bot/progreso.py
import gspread
from google.oauth2.service_account import Credentials
import json
import os

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def get_datos_paciente(nombre: str) -> list:
    try:
        creds_json = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
        creds_dict = json.loads(creds_json)
        creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
        client = gspread.authorize(creds)
        sheet_id = os.getenv("GOOGLE_SHEET_ID")
        spreadsheet = client.open_by_key(sheet_id)
        sheet = spreadsheet.sheet1
        registros = sheet.get_all_records()
        
        datos = [
            r for r in registros
            if str(r.get("¿Cuál es tu nombre?", "")).strip().lower() == nombre.strip().lower()
        ]
        return datos
    except Exception as e:
        print(f"[ERROR PROGRESO] {e}")
        return []


def calcular_eficiencia(hora_cama, hora_levantarse, latencia, tiempo_despierto):
    try:
        from datetime import datetime
        fmt = "%I:%M %p"
        t_cama = datetime.strptime(str(hora_cama).strip(), fmt)
        t_levanta = datetime.strptime(str(hora_levantarse).strip(), fmt)
        
        diff = t_levanta - t_cama
        if diff.total_seconds() < 0:
            from datetime import timedelta
            diff = diff + timedelta(days=1)
        
        tiempo_en_cama = diff.total_seconds() / 60
        tiempo_dormido = tiempo_en_cama - float(latencia or 0) - float(tiempo_despierto or 0)
        
        if tiempo_en_cama > 0:
            eficiencia = round((tiempo_dormido / tiempo_en_cama) * 100, 1)
            return max(0, min(100, eficiencia))
        return 0
    except:
        return None