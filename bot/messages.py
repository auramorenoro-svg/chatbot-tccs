# bot/messages.py
from config import Config

FORM_URL = Config.GOOGLE_FORM_URL

BIENVENIDA = """Hola, bienvenido/a al programa de acompañamiento para el manejo del insomnio con Terapia Cognitivo-Conductual (TCC-I).

Soy tu asistente y estare aqui para ayudarte durante tu proceso terapeutico.

Para comenzar, necesito saber tu nombre. Por favor escribe solo tu nombre."""

BIENVENIDA_REGISTRADO = lambda nombre: f"""Bienvenido/a de nuevo, {nombre}.

Estoy aqui para ayudarte. Puedes escribir una de estas opciones o hacerme una pregunta:

1. Modulo actual
2. Diario de sueno
3. Tecnicas de relajacion
4. Preguntas frecuentes
5. Desactivar recordatorios
6. Activar recordatorios

O escribe tu pregunta directamente."""

RECORDATORIO_MANANA = lambda nombre, url: f"""Buenos dias, {nombre}.

Es momento de llenar tu Diario de Sueno de ayer.

Registrar tu sueño diariamente es una parte fundamental de tu terapia. Solo toma 2 minutos.

Accede aqui:
{url}

Recuerda: cada registro cuenta para tu mejoria. Si tienes dudas, escribeme."""

RECORDATORIO_NOCHE = lambda nombre: f"""Buenas noches, {nombre}.

En unos momentos te prepararas para dormir. Aqui tienes un recordatorio de tus habitos de higiene del sueno para esta noche:

- Apaga pantallas 30 min antes de acostarte
- Mantén tu cuarto fresco (18-20 grados)
- Si no tienes sueno, no te vayas a la cama todavia
- Haz tu ejercicio de respiracion (escribe "respiracion" si quieres el recordatorio)

Buenas noches. Mañana te esperare para tu diario."""

LINK_DIARIO = lambda url: f"""Aqui esta el enlace para llenar tu Diario de Sueno de hoy:

{url}

Recuerda llenarlo cada manana, registrando como dormiste la noche anterior.

Los datos que registras son fundamentales para que tu terapeuta pueda seguir tu progreso."""

TECNICAS_RELAJACION = """Aqui tienes las principales tecnicas de relajacion para antes de dormir:

*1. Tecnicas de respiracion*
- Inhala lentamente por la nariz durante 4 segundos
- Manten el aire 4 segundos
- Exhala lentamente por la boca durante 4 segundos
- Repite el ciclo varias veces hasta sentirte tranquilo/a

Video guia:
https://www.youtube.com/watch?v=Gq3PuDz6tBs

*2. Relajacion muscular progresiva*
- Tensa cada grupo muscular durante 5 segundos
- Suelta y siente la relajacion durante 10 segundos
- Comienza por los pies y sube hasta la cara

Video guia:
https://www.youtube.com/watch?v=IjIw0ZUvUcA

*3. Mindfulness*
- Siéntate comodamente y cierra los ojos
- Lleva tu atencion a tu respiracion, sin intentar cambiarla
- Cuando tu mente se distraiga, vuelve suavemente a la respiracion
- Practica durante 5 a 10 minutos

Video guia:
https://www.youtube.com/watch?v=QHNJyiMUgnQ

Escribe el numero de la tecnica para mas detalles, o "menu" para volver."""

RESPIRACION_DETALLE = """*Tecnicas de Respiracion - Instrucciones completas*

La respiracion controlada es una herramienta muy eficaz para reducir la ansiedad antes de dormir.

Pasos:
1. Siéntate o acuestate comodamente
2. Cierra los ojos y relaja los hombros
3. Inhala lentamente por la nariz contando 4 segundos
4. Manten el aire contando 4 segundos
5. Exhala lentamente por la boca contando 4 segundos
6. Repite el ciclo varias veces hasta sentirte tranquilo/a

Video guia:
https://www.youtube.com/watch?v=Gq3PuDz6tBs

Practica esto cada noche antes de dormir, idealmente sentado/a o acostado/a en tu cama."""

MENU_PRINCIPAL = """Puedo ayudarte con:

1. Ver mi modulo actual
2. Llenar el diario de sueno (enlace)
3. Tecnicas de relajacion
4. Preguntas frecuentes
5. Desactivar recordatorios
6. Activar recordatorios

Escribe el numero o tu pregunta directamente."""

NO_ENTENDIDO = """No estoy seguro de entender tu pregunta. Puedes escribir:

- "menu" para ver las opciones
- "diario" para el enlace del diario de sueno
- "relajacion" para las tecnicas
- "modulo" para ver tu modulo actual
- "preguntas" para preguntas frecuentes

O escribe tu duda y haré lo posible por ayudarte."""

RECORDATORIOS_DESACTIVADOS = """De acuerdo. Ya no recibiras recordatorios automaticos.

Si cambias de opinion, escribe "activar recordatorios" en cualquier momento."""

RECORDATORIOS_ACTIVADOS = """Listo. Volveras a recibir recordatorios:
- Manana a las 8:00 AM para tu diario de sueno
- Noche a las 8:00 PM para tu higiene del sueno"""