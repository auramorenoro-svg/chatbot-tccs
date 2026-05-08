# bot/messages.py
from config import Config

FORM_URL = Config.GOOGLE_FORM_URL

BIENVENIDA = """Hola, bienvenido/a al programa de acompañamiento para el manejo del insomnio con Terapia Cognitivo-Conductual (TCC-I).

Soy tu asistente y estaré aquí para ayudarte durante tu proceso terapéutico.

Para comenzar, necesito saber tu nombre. Por favor escribe solo tu nombre."""

BIENVENIDA_REGISTRADO = lambda nombre: f"""Bienvenido/a de nuevo, {nombre}.

Estoy aquí para ayudarte. Puedes escribir una de estas opciones o hacerme una pregunta:

1. Módulo actual
2. Diario de sueño
3. Técnicas de relajación
4. Preguntas frecuentes
5. Desactivar recordatorios
6. Activar recordatorios
7. Ver mi progreso de sueño

O escribe tu pregunta directamente."""

RECORDATORIO_MANANA = lambda nombre, url: f"""Buenos días, {nombre}.

Es momento de llenar tu Diario de Sueño de ayer.

Registrar tu sueño diariamente es una parte fundamental de tu terapia. Solo toma 2 minutos.

Accede aquí:
{url}

Recuerda: cada registro cuenta para tu mejoría. Si tienes dudas, escríbeme."""

RECORDATORIO_NOCHE = lambda nombre: f"""Buenas noches, {nombre}.

En unos momentos te prepararás para dormir. Aquí tienes un recordatorio de tus hábitos de higiene del sueño para esta noche:

- Apaga pantallas 30 min antes de acostarte
- Mantén tu cuarto fresco (18-20 grados)
- Si no tienes sueño, no te vayas a la cama todavía
- Haz tu ejercicio de respiración (escribe "respiracion" si quieres el recordatorio)

Buenas noches. Mañana te esperaré para tu diario."""

LINK_DIARIO = lambda url: f"""Aquí está el enlace para llenar tu Diario de Sueño de hoy:

{url}

Recuerda llenarlo cada mañana, registrando cómo dormiste la noche anterior.

Los datos que registras son fundamentales para que tu terapeuta pueda seguir tu progreso."""

LINK_PROGRESO = lambda nombre: f"""Aquí está tu página de progreso de sueño:

https://web-production-e55ce9.up.railway.app/progreso/{nombre}

Podrás ver tu eficiencia de sueño y tu registro diario. Se actualiza cada vez que llenas el diario."""

TECNICAS_RELAJACION = """Aquí tienes las principales técnicas de relajación para antes de dormir:

*1. Técnicas de respiración*
- Inhala lentamente por la nariz durante 4 segundos
- Mantén el aire 4 segundos
- Exhala lentamente por la boca durante 4 segundos
- Repite el ciclo varias veces hasta sentirte tranquilo/a

Video guía:
https://www.youtube.com/watch?v=Gq3PuDz6tBs

*2. Relajación muscular progresiva*
- Tensa cada grupo muscular durante 5 segundos
- Suelta y siente la relajación durante 10 segundos
- Comienza por los pies y sube hasta la cara

Video guía:
https://www.youtube.com/watch?v=IjIw0ZUvUcA

*3. Mindfulness*
- Siéntate cómodamente y cierra los ojos
- Lleva tu atención a tu respiración, sin intentar cambiarla
- Cuando tu mente se distraiga, vuelve suavemente a la respiración
- Practica durante 5 a 10 minutos

Video guía:
https://www.youtube.com/watch?v=QHNJyiMUgnQ

Escribe el número de la técnica para más detalles, o "menu" para volver."""

RESPIRACION_DETALLE = """*Técnicas de Respiración - Instrucciones completas*

La respiración controlada es una herramienta muy eficaz para reducir la ansiedad antes de dormir.

Pasos:
1. Siéntate o acuéstate cómodamente
2. Cierra los ojos y relaja los hombros
3. Inhala lentamente por la nariz contando 4 segundos
4. Mantén el aire contando 4 segundos
5. Exhala lentamente por la boca contando 4 segundos
6. Repite el ciclo varias veces hasta sentirte tranquilo/a

Video guía:
https://www.youtube.com/watch?v=Gq3PuDz6tBs

Practica esto cada noche antes de dormir, idealmente sentado/a o acostado/a en tu cama."""

MENU_PRINCIPAL = """Puedo ayudarte con:

1. Ver mi módulo actual
2. Llenar el diario de sueño (enlace)
3. Técnicas de relajación
4. Preguntas frecuentes
5. Desactivar recordatorios
6. Activar recordatorios
7. Ver mi progreso de sueño

Escribe el número o tu pregunta directamente."""

NO_ENTENDIDO = """No estoy seguro de entender tu pregunta. Puedes escribir:

- "menu" para ver las opciones
- "diario" para el enlace del diario de sueño
- "relajacion" para las técnicas
- "modulo" para ver tu módulo actual
- "progreso" para ver tu progreso de sueño
- "preguntas" para preguntas frecuentes

O escribe tu duda y haré lo posible por ayudarte."""

RECORDATORIOS_DESACTIVADOS = """De acuerdo. Ya no recibirás recordatorios automáticos.

Si cambias de opinión, escribe "activar recordatorios" en cualquier momento."""

RECORDATORIOS_ACTIVADOS = """Listo. Volverás a recibir recordatorios:
- Mañana a las 8:00 AM para tu diario de sueño
- Noche a las 8:00 PM para tu higiene del sueño"""