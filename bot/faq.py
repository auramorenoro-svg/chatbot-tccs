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
        "respuesta": """*Restriccion de Sueno - TCC-I*

La restriccion de sueno es una de las tecnicas mas efectivas de la TCC-I.

Consiste en limitar el tiempo en cama al tiempo real que duermes, para consolidar el sueno.

Por ejemplo, si duermes en promedio 5 horas, solo te quedas en cama esas 5 horas, aunque estes despierto.

Esto genera presion de sueno, que mejora la profundidad y continuidad del sueno con el tiempo.

Tu terapeuta calculara tu ventana de sueno personalizada basandose en tu diario.

Habla con tu terapeuta antes de aplicar esta tecnica por tu cuenta."""
    },
    {
        "palabras_clave": [
            "control de estimulos", "estimulos", "asociacion cama",
            "cama solo para dormir", "no leer en la cama"
        ],
        "respuesta": """*Control de Estimulos*

Esta tecnica busca que tu cerebro asocie la cama SOLO con el sueno.

Reglas del control de estimulos:

1. Usa tu cama unicamente para dormir. Nada de pantallas, leer, comer, trabajar.
2. Vete a la cama solo cuando tengas sueno real (ojos pesados, cabeceos).
3. Si no te duermes en 20 minutos, levantate. Ve a otro cuarto. Regresa cuando tengas sueno.
4. Levantate siempre a la misma hora, sin importar cuanto dormiste.
5. No duermas siesta hasta que tu sueno mejore.

Esta tecnica tarda 1-2 semanas en dar resultados. Es normal que al principio el sueno empeore un poco."""
    },
    {
        "palabras_clave": [
            "higiene del sueno", "habitos", "habitos de sueno",
            "que hacer antes de dormir", "preparacion para dormir"
        ],
        "respuesta": """*Higiene del Sueno - Habitos recomendados*

Antes de acostarte:
- Apaga pantallas 30-60 minutos antes
- Haz una rutina fija: lavarse los dientes, lectura tranquila, relajacion
- Mantén el cuarto fresco (18-20 grados ideal)
- Oscuridad total o antifaz
- Silencio o ruido blanco

Durante el dia:
- Ejercicio regular (no en las 3 horas previas al sueno)
- Exposicion a luz natural en la manana
- No cafeina despues de las 2pm
- No alcohol: aunque induce sueno, lo fragmenta en la segunda mitad de la noche

Siesta:
- Evitar siestas si tienes insomnio
- Si es necesaria, maximo 20 minutos, antes de las 3pm"""
    },
    {
        "palabras_clave": [
            "pensamientos", "pensamientos negativos", "no puedo dejar de pensar",
            "mente activa", "rumiacion", "preocupaciones antes de dormir"
        ],
        "respuesta": """*Manejo de Pensamientos en la Noche*

Es muy comun que la mente se active cuando intenta dormir. Aqui hay estrategias:

*1. Tiempo de preocupacion*
Reserva 20 minutos durante el dia para escribir tus preocupaciones y posibles soluciones. Cuando lleguen en la noche, recuerdate: "ya las atendi hoy".

*2. Tecnica del tren*
Imagina que tus pensamientos son vagones de un tren que pasan. No te subas al tren, solo observalos pasar.

*3. Reencuadre*
Si piensas "si no duermo manana sere un desastre", sustituyelo por:
"Aunque no duerma perfecto, mi cuerpo se va a recuperar. No dormir una noche no es una catastrofe."

*4. Imagery*
Imagina un lugar tranquilo con mucho detalle: colores, sonidos, texturas, olores."""
    },
    {
        "palabras_clave": [
            "paradoja del sueno", "intentar dormir", "esfuerzo por dormir",
            "cuanto mas intento mas me desvelo"
        ],
        "respuesta": """*La Paradoja del Sueno*

Mientras mas te esfuerzas por dormirte, mas dificil se vuelve. Esto se llama "hiperactivacion".

El truco es la intencion paradojica: intenta quedarte despierto con los ojos abiertos.

Esto reduce la ansiedad por el sueno y, paradojicamente, ayuda a que llegue el sueno naturalmente.

Recuerdate: el sueno no se puede forzar, solo se pueden crear las condiciones para que llegue."""
    },
    {
        "palabras_clave": [
            "pastilla", "medicamento", "somnifero", "zolpidem",
            "clonazepam", "melatonina"
        ],
        "respuesta": """*Medicamentos para el Sueno*

Este chatbot no puede darte recomendaciones medicas sobre medicamentos.

Lo que si puedo decirte es que la TCC-I ha demostrado ser mas efectiva que los medicamentos a largo plazo para el insomnio cronico.

Si tienes dudas sobre tu medicacion actual, consulta directamente con tu medico o terapeuta."""
    },
    {
        "palabras_clave": [
            "mindfulness", "atencion plena", "meditacion"
        ],
        "respuesta": """*Mindfulness para el Sueno*

El mindfulness o atencion plena te ayuda a reducir la activacion mental antes de dormir.

Pasos:
1. Siéntate o acuestate comodamente
2. Cierra los ojos y lleva tu atencion a tu respiracion
3. Observa como entra y sale el aire, sin intentar cambiarlo
4. Cuando tu mente se distraiga, vuelve suavemente a la respiracion
5. Practica durante 5 a 10 minutos

Video guia:
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