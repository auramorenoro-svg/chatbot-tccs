# bot/sheets.py
import gspread
from google.oauth2.service_account import Credentials
import json
import os

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def get_sheet():
    creds_json = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
    creds_dict = json.loads(creds_json)
    creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet_id = os.getenv("GOOGLE_SHEET_ID")
    spreadsheet = client.open_by_key(sheet_id)
    return spreadsheet.sheet1


def obtener_resumen_paciente(nombre: str) -> str:
    try:
        sheet = get_sheet()
        registros = sheet.get_all_records()
        
        datos_paciente = [
            r for r in registros
            if str(r.get("¿Cuál es tu nombre?", "")).strip().lower() == nombre.strip().lower()
        ]
        
        if not datos_paciente:
            return "No encontré registros de tu diario todavía. Recuerda llenarlo cada mañana."
        
        ultimos = datos_paciente[-3:]
        resumen = "📊 *Tus últimas noches:*\n\n"
        
        for r in ultimos:
            fecha = r.get("Fecha de hoy", "Sin fecha")
            latencia = r.get("¿Cuánto tiempo tardaste en quedarte dormido/a?", "?")
            calidad = r.get("¿Cómo calificarías la calidad de tu sueño?", "?")
            descanso = r.get("¿Qué tan descansado/a te sentiste al despertar?", "?")
            
            resumen += f"📅 *{fecha}*\n"
            resumen += f"- Tardaste en dormirte: {latencia} min\n"
            resumen += f"- Calidad: {calidad}/5\n"
            resumen += f"- Descanso: {descanso}\n\n"
        
        return resumen
    
    except Exception as e:
        print(f"[ERROR SHEETS] {e}")
        return "No pude obtener tu diario en este momento. Intenta más tarde."