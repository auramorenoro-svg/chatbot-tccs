# bot/modules.py

MODULOS = {
    1: {
        "nombre": "Evaluacion y Psicoeducacion",
        "semana": 1,
        "descripcion": """Modulo 1 - Evaluacion y Psicoeducacion del Sueno

Objetivo: Entender como funciona el sueno y que factores estan afectando el tuyo.

Esta semana aprendiste:
- Los dos sistemas que regulan el sueno: ritmo circadiano y presion de sueno
- Por que las soluciones que usas (quedarte en cama mas tiempo, siestas) pueden empeorar el insomnio
- La importancia del diario de sueno para guiar tu terapia

Tus tareas esta semana:
- Llenar el diario de sueno cada manana (enlace en el recordatorio)
- Anotar tus pensamientos sobre el sueno
- Observar tus patrones sin intentar cambiarlos todavia

Para ver el enlace del diario de sueno escribe "diario"
Para ver tecnicas de relajacion escribe "relajacion"
Para preguntas escribe "preguntas"
""",
        "tareas": [
            "Llenar el diario de sueno cada manana",
            "Observar tus horarios de dormir y despertar",
            "Anotar pensamientos que aparezcan en la noche"
        ]
    },
    2: {
        "nombre": "Higiene del Sueno y Control de Estimulos",
        "semana": 2,
        "descripcion": """Modulo 2 - Higiene del Sueno y Control de Estimulos

Objetivo: Establecer habitos que favorezcan el sueno y re-entrenar tu cerebro para que asocie la cama con el sueno.

Esta semana aprendiste:
- Que conductas del dia afectan el sueno de la noche
- La tecnica de control de estimulos
- Como crear un ambiente ideal para dormir

Tus tareas esta semana:
1. Usa la cama solo para dormir
2. Si no te duermes en 20 min, levantate y vuelve cuando tengas sueno
3. Levantate siempre a la misma hora aunque hayas dormido poco
4. Sigue llenando tu diario de sueno

Para detalles del control de estimulos escribe "control de estimulos"
Para higiene del sueno escribe "higiene del sueno"
""",
        "tareas": [
            "Usar la cama solo para dormir",
            "Levantarse a la misma hora todos los dias",
            "Salir de la cama si no te duermes en 20 min",
            "Llenar el diario de sueno cada manana"
        ]
    },
    3: {
        "nombre": "Restriccion de Sueno",
        "semana": 3,
        "descripcion": """Modulo 3 - Restriccion de Sueno

Objetivo: Consolidar el sueno limitando el tiempo en cama para generar presion de sueno.

Esta semana aprendiste:
- Que es la restriccion de sueno y por que funciona
- Como calcular tu ventana de sueno con base en tu diario
- Que al principio puede ser dificil pero es la tecnica mas efectiva

Tus tareas esta semana:
1. Respetar la ventana de sueno que tu terapeuta calculo contigo
2. Levantarte a la hora acordada aunque tengas sueno
3. Evitar siestas
4. Continuar con el diario de sueno para ajustar la ventana

Para detalles de la restriccion escribe "restriccion de sueno"
""",
        "tareas": [
            "Respetar la ventana de sueno indicada por el terapeuta",
            "No hacer siestas",
            "Levantarse a la hora acordada todos los dias",
            "Llenar el diario de sueno cada manana"
        ]
    },
    4: {
        "nombre": "Reestructuracion Cognitiva",
        "semana": 4,
        "descripcion": """Modulo 4 - Reestructuracion Cognitiva

Objetivo: Identificar y modificar los pensamientos que alimentan el insomnio.

Esta semana aprendiste:
- Como los pensamientos sobre el sueno generan ansiedad
- A identificar pensamientos catastroficos sobre no dormir
- La tecnica del experimento conductual para probar tus creencias
- Como el perfeccionismo del sueno puede mantener el insomnio

Tus tareas esta semana:
1. Registrar pensamientos negativos sobre el sueno y cuestionarlos
2. Practicar el dialogo interno alternativo
3. Continuar con el control de estimulos y la ventana de sueno
4. Diario de sueno cada manana

Para estrategias con pensamientos escribe "pensamientos"
Para la paradoja del sueno escribe "paradoja del sueno"
""",
        "tareas": [
            "Registrar y cuestionar pensamientos sobre el sueno",
            "Practicar pensamientos alternativos",
            "Continuar control de estimulos y ventana de sueno",
            "Llenar el diario de sueno cada manana"
        ]
    },
    5: {
        "nombre": "Tecnicas de Relajacion y Manejo de Activacion",
        "semana": 5,
        "descripcion": """Modulo 5 - Tecnicas de Relajacion

Objetivo: Reducir la activacion fisiologica y mental que interfiere con el sueno.

Esta semana aprendiste:
- Tecnicas de respiracion para reducir la activacion del sistema nervioso
- Relajacion muscular progresiva
- Mindfulness aplicado al sueno
- El tiempo de preocupacion para manejar rumia nocturna

Tus tareas esta semana:
1. Practicar una tecnica de relajacion cada noche antes de dormir
2. Hacer el tiempo de preocupacion diariamente (20 min durante el dia)
3. Continuar con las tecnicas previas
4. Diario de sueno cada manana

Para las tecnicas de relajacion escribe "relajacion"
""",
        "tareas": [
            "Practicar relajacion cada noche",
            "Hacer tiempo de preocupacion diario (20 min durante el dia)",
            "Continuar con control de estimulos y ventana de sueno",
            "Llenar el diario de sueno cada manana"
        ]
    },
    6: {
        "nombre": "Prevencion de Recaidas y Cierre",
        "semana": 6,
        "descripcion": """Modulo 6 - Prevencion de Recaidas y Consolidacion

Objetivo: Consolidar los aprendizajes y prepararte para mantener los logros.

Esta semana aprendiste:
- Como mantener los avances a largo plazo
- Que hacer si el insomnio regresa temporalmente
- Senales de alerta tempranas y como actuar

Plan de mantenimiento:
1. Sigue con tu hora fija de despertar, incluso los fines de semana
2. Si tienes una mala noche, aplica las tecnicas que aprendiste, no entres en panico
3. El diario de sueno ocasional te ayudara a monitorear tu progreso
4. Una mala noche no significa recaida: es normal y pasajero

Felicidades por completar el programa.
""",
        "tareas": [
            "Mantener hora fija de despertar",
            "Continuar habitos de higiene del sueno",
            "Usar las tecnicas si hay noches dificiles",
            "No entrar en panico ante una mala noche"
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
    texto = f"*Tus tareas del Modulo {numero_modulo} ({modulo['nombre']}):*\n\n"
    for i, tarea in enumerate(tareas, 1):
        texto += f"{i}. {tarea}\n"
    return texto


def avanzar_modulo(paciente) -> str:
    if paciente.modulo_actual < 6:
        paciente.modulo_actual += 1
        return f"Has avanzado al Modulo {paciente.modulo_actual}: {MODULOS[paciente.modulo_actual]['nombre']}"
    else:
        return "Ya has completado todos los modulos del programa. Felicidades."