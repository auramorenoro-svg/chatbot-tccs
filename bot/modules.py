# bot/modules.py

MODULOS = {
    1: {
        "nombre": "Evaluación y Psicoeducación",
        "semana": 1,
        "descripcion": """Módulo 1 - Evaluación y Psicoeducación del Sueño

Objetivo: Entender cómo funciona el sueño y qué factores están afectando el tuyo.

Esta semana aprendiste:
- Los dos sistemas que regulan el sueño: ritmo circadiano y presión de sueño
- Por qué las soluciones que usas (quedarte en cama más tiempo, siestas) pueden empeorar el insomnio
- La importancia del diario de sueño para guiar tu terapia

Tus tareas esta semana:
- Llenar el diario de sueño cada mañana (enlace en el recordatorio)
- Anotar tus pensamientos sobre el sueño
- Observar tus patrones sin intentar cambiarlos todavía

Para ver el enlace del diario de sueño escribe "diario"
Para ver técnicas de relajación escribe "relajacion"
Para preguntas escribe "preguntas"
""",
        "tareas": [
            "Llenar el diario de sueño cada mañana",
            "Observar tus horarios de dormir y despertar",
            "Anotar pensamientos que aparezcan en la noche"
        ]
    },
    2: {
        "nombre": "Higiene del Sueño y Control de Estímulos",
        "semana": 2,
        "descripcion": """Módulo 2 - Higiene del Sueño y Control de Estímulos

Objetivo: Establecer hábitos que favorezcan el sueño y re-entrenar tu cerebro para que asocie la cama con el sueño.

Esta semana aprendiste:
- Qué conductas del día afectan el sueño de la noche
- La técnica de control de estímulos
- Cómo crear un ambiente ideal para dormir

Tus tareas esta semana:
1. Usa la cama solo para dormir
2. Si no te duermes en 20 min, levántate y vuelve cuando tengas sueño
3. Levántate siempre a la misma hora aunque hayas dormido poco
4. Sigue llenando tu diario de sueño

Para detalles del control de estímulos escribe "control de estimulos"
Para higiene del sueño escribe "higiene del sueno"
""",
        "tareas": [
            "Usar la cama solo para dormir",
            "Levantarse a la misma hora todos los días",
            "Salir de la cama si no te duermes en 20 min",
            "Llenar el diario de sueño cada mañana"
        ]
    },
    3: {
        "nombre": "Restricción de Sueño",
        "semana": 3,
        "descripcion": """Módulo 3 - Restricción de Sueño

Objetivo: Consolidar el sueño limitando el tiempo en cama para generar presión de sueño.

Esta semana aprendiste:
- Qué es la restricción de sueño y por qué funciona
- Cómo calcular tu ventana de sueño con base en tu diario
- Que al principio puede ser difícil pero es la técnica más efectiva

Tus tareas esta semana:
1. Respetar la ventana de sueño que tu terapeuta calculó contigo
2. Levantarte a la hora acordada aunque tengas sueño
3. Evitar siestas
4. Continuar con el diario de sueño para ajustar la ventana

Para detalles de la restricción escribe "restriccion de sueno"
""",
        "tareas": [
            "Respetar la ventana de sueño indicada por el terapeuta",
            "No hacer siestas",
            "Levantarse a la hora acordada todos los días",
            "Llenar el diario de sueño cada mañana"
        ]
    },
    4: {
        "nombre": "Reestructuración Cognitiva",
        "semana": 4,
        "descripcion": """Módulo 4 - Reestructuración Cognitiva

Objetivo: Identificar y modificar los pensamientos que alimentan el insomnio.

Esta semana aprendiste:
- Cómo los pensamientos sobre el sueño generan ansiedad
- A identificar pensamientos catastróficos sobre no dormir
- La técnica del experimento conductual para probar tus creencias
- Cómo el perfeccionismo del sueño puede mantener el insomnio

Tus tareas esta semana:
1. Registrar pensamientos negativos sobre el sueño y cuestionarlos
2. Practicar el diálogo interno alternativo
3. Continuar con el control de estímulos y la ventana de sueño
4. Diario de sueño cada mañana

Para estrategias con pensamientos escribe "pensamientos"
Para la paradoja del sueño escribe "paradoja del sueno"
""",
        "tareas": [
            "Registrar y cuestionar pensamientos sobre el sueño",
            "Practicar pensamientos alternativos",
            "Continuar control de estímulos y ventana de sueño",
            "Llenar el diario de sueño cada mañana"
        ]
    },
    5: {
        "nombre": "Técnicas de Relajación y Manejo de Activación",
        "semana": 5,
        "descripcion": """Módulo 5 - Técnicas de Relajación

Objetivo: Reducir la activación fisiológica y mental que interfiere con el sueño.

Esta semana aprendiste:
- Técnicas de respiración para reducir la activación del sistema nervioso
- Relajación muscular progresiva
- Mindfulness aplicado al sueño
- El tiempo de preocupación para manejar rumia nocturna

Tus tareas esta semana:
1. Practicar una técnica de relajación cada noche antes de dormir
2. Hacer el tiempo de preocupación diariamente (20 min durante el día)
3. Continuar con las técnicas previas
4. Diario de sueño cada mañana

Para las técnicas de relajación escribe "relajacion"
""",
        "tareas": [
            "Practicar relajación cada noche",
            "Hacer tiempo de preocupación diario (20 min durante el día)",
            "Continuar con control de estímulos y ventana de sueño",
            "Llenar el diario de sueño cada mañana"
        ]
    },
    6: {
        "nombre": "Prevención de Recaídas y Cierre",
        "semana": 6,
        "descripcion": """Módulo 6 - Prevención de Recaídas y Consolidación

Objetivo: Consolidar los aprendizajes y prepararte para mantener los logros.

Esta semana aprendiste:
- Cómo mantener los avances a largo plazo
- Qué hacer si el insomnio regresa temporalmente
- Señales de alerta tempranas y cómo actuar

Plan de mantenimiento:
1. Sigue con tu hora fija de despertar, incluso los fines de semana
2. Si tienes una mala noche, aplica las técnicas que aprendiste, no entres en pánico
3. El diario de sueño ocasional te ayudará a monitorear tu progreso
4. Una mala noche no significa recaída: es normal y pasajero

¡Felicidades por completar el programa!
""",
        "tareas": [
            "Mantener hora fija de despertar",
            "Continuar hábitos de higiene del sueño",
            "Usar las técnicas si hay noches difíciles",
            "No entrar en pánico ante una mala noche"
        ]
    }
}


def obtener_modulo(numero_modulo: int) -> dict:
    return MODULOS.get(numero_modulo, MODULOS[1])


def obtener_descripcion_modulo(numero_modulo: int) -> str:
    modulo = obtener_modulo(numero_modulo)
    return modulo["descripcion"]


def obtener_tareas_modulo(numero_modulo: int) -> str:
    modulo = obtener_modulo(numero_modulo)
    tareas = modulo["tareas"]
    texto = f"*Tus tareas del Módulo {numero_modulo} ({modulo['nombre']}):*\n\n"
    for i, tarea in enumerate(tareas, 1):
        texto += f"{i}. {tarea}\n"
    return texto


def avanzar_modulo(paciente) -> str:
    if paciente.modulo_actual < 6:
        paciente.modulo_actual += 1
        return f"Has avanzado al Módulo {paciente.modulo_actual}: {MODULOS[paciente.modulo_actual]['nombre']}"
    else:
        return "Ya has completado todos los módulos del programa. ¡Felicidades!"