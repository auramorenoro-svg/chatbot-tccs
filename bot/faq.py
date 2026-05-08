# bot/faq.py
from bot.messages import RESPIRACION_DETALLE

FAQS = [
    {
        "palabras_clave": [
            "respiracion", "respirar", "respira", "respiro",
            "ejercicio de respiracion", "tecnica de respiracion"
        ],
        "respuesta": RESPIRACION_DETALLE
    },
    {
        "palabras_clave": [
            "restriccion de sueno", "restriccion", "restringir",
            "cuantas horas debo dormir", "ventana de sueno"
        ],
        "respuesta": """*Restricción de Sueño - TCC-I*

La restricción de sueño es una de las técnicas más efectivas de la TCC-I.

Consiste en limitar el tiempo en cama al tiempo real que duermes, para consolidar el sueño.

Por ejemplo, si duermes en promedio 5 horas, solo te quedas en cama esas 5 horas, aunque estés despierto/a.

Esto genera presión de sueño, que mejora la profundidad y continuidad del sueño con el tiempo.

Tu terapeuta calculará tu ventana de sueño personalizada basándose en tu diario.

Habla con tu terapeuta antes de aplicar esta técnica por tu cuenta."""
    },
    {
        "palabras_clave": [
            "control de estimulos", "estimulos", "asociacion cama",
            "cama solo para dormir", "no leer en la cama"
        ],
        "respuesta": """*Control de Estímulos*

Esta técnica busca que tu cerebro asocie la cama SOLO con el sueño.

Reglas del control de estímulos:

1. Usa tu cama únicamente para dormir. Nada de pantallas, leer, comer, trabajar.
2. Vete a la cama solo cuando tengas sueño real (ojos pesados, cabeceos).
3. Si no te duermes en 20 minutos, levántate. Ve a otro cuarto. Regresa cuando tengas sueño.
4. Levántate siempre a la misma hora, sin importar cuánto dormiste.
5. No duermas siesta hasta que tu sueño mejore.

Esta técnica tarda 1-2 semanas en dar resultados. Es normal que al principio el sueño empeore un poco."""
    },
    {
        "palabras_clave": [
            "higiene del sueno", "habitos", "habitos de sueno",
            "que hacer antes de dormir", "preparacion para dormir"
        ],
        "respuesta": """*Higiene del Sueño - Hábitos recomendados*

Antes de acostarte:
- Apaga pantallas 30-60 minutos antes
- Haz una rutina fija: lavarse los dientes, lectura tranquila, relajación
- Mantén el cuarto fresco (18-20 grados ideal)
- Oscuridad total o antifaz
- Silencio o ruido blanco

Durante el día:
- Ejercicio regular (no en las 3 horas previas al sueño)
- Exposición a luz natural en la mañana
- No cafeína después de las 2pm
- No alcohol: aunque induce sueño, lo fragmenta en la segunda mitad de la noche

Siesta:
- Evitar siestas si tienes insomnio
- Si es necesaria, máximo 20 minutos, antes de las 3pm"""
    },
    {
        "palabras_clave": [
            "pensamientos", "pensamientos negativos", "no puedo dejar de pensar",
            "mente activa", "rumiacion", "preocupaciones antes de dormir"
        ],
        "respuesta": """*Manejo de Pensamientos en la Noche*

Es muy común que la mente se active cuando intenta dormir. Aquí hay estrategias:

*1. Tiempo de preocupación*
Reserva 20 minutos durante el día para escribir tus preocupaciones y posibles soluciones. Cuando lleguen en la noche, recuérdate: "ya las atendí hoy".

*2. Técnica del tren*
Imagina que tus pensamientos son vagones de un tren que pasan. No te subas al tren, solo obsérvalos pasar.

*3. Reencuadre*
Si piensas "si no duermo mañana seré un desastre", sustitúyelo por:
"Aunque no duerma perfecto, mi cuerpo se va a recuperar. No dormir una noche no es una catástrofe."

*4. Imagery*
Imagina un lugar tranquilo con mucho detalle: colores, sonidos, texturas, olores."""
    },
    {
        "palabras_clave": [
            "paradoja del sueno", "intentar dormir", "esfuerzo por dormir",
            "cuanto mas intento mas me desvelo"
        ],
        "respuesta": """*La Paradoja del Sueño*

Mientras más te esfuerzas por dormirte, más difícil se vuelve. Esto se llama "hiperactivación".

El truco es la intención paradójica: intenta quedarte despierto/a con los ojos abiertos.

Esto reduce la ansiedad por el sueño y, paradójicamente, ayuda a que llegue el sueño naturalmente.

Recuérdate: el sueño no se puede forzar, solo se pueden crear las condiciones para que llegue."""
    },
    {
        "palabras_clave": [
            "pastilla", "medicamento", "somnifero", "zolpidem",
            "clonazepam", "melatonina"
        ],
        "respuesta": """*Medicamentos para el Sueño*

Este chatbot no puede darte recomendaciones médicas sobre medicamentos.

Lo que sí puedo decirte es que la TCC-I ha demostrado ser más efectiva que los medicamentos a largo plazo para el insomnio crónico.

Si tienes dudas sobre tu medicación actual, consulta directamente con tu médico o terapeuta."""
    },
    {
        "palabras_clave": [
            "mindfulness", "atencion plena", "meditacion"
        ],
        "respuesta": """*Mindfulness para el Sueño*

El mindfulness o atención plena te ayuda a reducir la activación mental antes de dormir.

Pasos:
1. Siéntate o acuéstate cómodamente
2. Cierra los ojos y lleva tu atención a tu respiración
3. Observa cómo entra y sale el aire, sin intentar cambiarlo
4. Cuando tu mente se distraiga, vuelve suavemente a la respiración
5. Practica durante 5 a 10 minutos

Video guía:
https://www.youtube.com/watch?v=QHNJyiMUgnQ"""
    },
]


def buscar_respuesta_faq(mensaje: str):
    mensaje_lower = mensaje.lower().strip()
    for faq in FAQS:
        for palabra in faq["palabras_clave"]:
            if palabra.lower() in mensaje_lower:
                return faq["respuesta"]
    return None