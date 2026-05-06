# bot/template_progreso.py

def generar_html_progreso(nombre: str, datos: list) -> str:
    if not datos:
        return f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Mi Progreso - {nombre}</title>
            <style>
                body {{ font-family: Arial, sans-serif; background: #f0f4f8; color: #2c3e50; text-align: center; padding: 40px; }}
                .card {{ background: white; border-radius: 12px; padding: 30px; max-width: 500px; margin: auto; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>Hola, {nombre}</h2>
                <p>Todavía no tienes registros en tu diario de sueño.</p>
                <p>Recuerda llenarlo cada mañana.</p>
            </div>
        </body>
        </html>
        """

    filas_tabla = ""
    fechas = []
    eficiencias = []

    for r in datos:
        fecha = r.get("Fecha de hoy", "")
        hora_cama = r.get("¿A qué hora te fuiste a la cama?", "")
        hora_levantarse = r.get("¿A qué hora te levantaste de la cama?", "")
        latencia = r.get("¿Cuánto tiempo tardaste en quedarte dormido/a?", 0)
        despertares = r.get("¿Cuántas veces te despertaste durante la noche?", "")
        tiempo_despierto = r.get("¿Cuánto tiempo estuviste despierto/a durante esas veces?", 0)
        calidad = r.get("¿Cómo calificarías la calidad de tu sueño?", "")
        descanso = r.get("¿Qué tan descansado/a te sentiste al despertar?", "")

        from bot.progreso import calcular_eficiencia
        eficiencia = calcular_eficiencia(hora_cama, hora_levantarse, latencia, tiempo_despierto)
        
        if eficiencia is not None:
            if eficiencia >= 85:
                color_ef = "#2ecc71"
                emoji_ef = "✅"
            elif eficiencia >= 70:
                color_ef = "#f39c12"
                emoji_ef = "⚠️"
            else:
                color_ef = "#e74c3c"
                emoji_ef = "❗"
            ef_texto = f'<span style="color:{color_ef};font-weight:bold;">{emoji_ef} {eficiencia}%</span>'
            fechas.append(str(fecha))
            eficiencias.append(eficiencia)
        else:
            ef_texto = "—"

        filas_tabla += f"""
        <tr>
            <td>{fecha}</td>
            <td>{hora_cama}</td>
            <td>{hora_levantarse}</td>
            <td>{latencia} min</td>
            <td>{despertares}</td>
            <td>{ef_texto}</td>
            <td>{calidad}/5</td>
            <td>{descanso}</td>
        </tr>
        """

    puntos_grafica = ""
    if eficiencias:
        max_ef = max(eficiencias) if eficiencias else 100
        for i, (f, e) in enumerate(zip(fechas, eficiencias)):
            x = 50 + i * (700 / max(len(eficiencias), 1))
            y = 200 - (e / 100 * 160)
            puntos_grafica += f'<circle cx="{x}" cy="{y}" r="5" fill="#3a7cc1"/>'
            if i > 0:
                x_prev = 50 + (i-1) * (700 / max(len(eficiencias), 1))
                y_prev = 200 - (eficiencias[i-1] / 100 * 160)
                puntos_grafica += f'<line x1="{x_prev}" y1="{y_prev}" x2="{x}" y2="{y}" stroke="#3a7cc1" stroke-width="2"/>'
            puntos_grafica += f'<text x="{x}" y="{y-10}" font-size="10" text-anchor="middle" fill="#2c3e50">{e}%</text>'

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi Progreso - {nombre}</title>
        <style>
            * {{ box-sizing: border-box; margin: 0; padding: 0; }}
            body {{ font-family: Arial, sans-serif; background: #f0f4f8; color: #2c3e50; padding: 20px; }}
            h1 {{ color: #3a7cc1; text-align: center; margin-bottom: 5px; }}
            h2 {{ color: #3a7cc1; margin: 25px 0 10px; font-size: 1.1em; }}
            .subtitulo {{ text-align: center; color: #7f8c8d; margin-bottom: 20px; font-size: 0.9em; }}
            .card {{ background: white; border-radius: 12px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); overflow-x: auto; }}
            table {{ width: 100%; border-collapse: collapse; font-size: 0.85em; }}
            th {{ background: #3a7cc1; color: white; padding: 10px 8px; text-align: center; }}
            td {{ padding: 8px; text-align: center; border-bottom: 1px solid #e8edf2; }}
            tr:nth-child(even) {{ background: #f0f4f8; }}
            .info-box {{ background: #e8f0fb; border-left: 4px solid #3a7cc1; padding: 15px; border-radius: 8px; margin-top: 15px; font-size: 0.88em; line-height: 1.6; }}
            svg {{ width: 100%; height: auto; }}
        </style>
    </head>
    <body>
        <h1>📊 Mi Progreso de Sueño</h1>
        <p class="subtitulo">Hola, <strong>{nombre}</strong> — aquí puedes ver cómo has dormido</p>

        <div class="card">
            <h2>📈 Eficiencia del sueño</h2>
            <svg viewBox="0 0 800 220" xmlns="http://www.w3.org/2000/svg">
                <line x1="50" y1="40" x2="50" y2="200" stroke="#ccc" stroke-width="1"/>
                <line x1="50" y1="200" x2="750" y2="200" stroke="#ccc" stroke-width="1"/>
                <line x1="50" y1="64" x2="750" y2="64" stroke="#2ecc71" stroke-width="1" stroke-dasharray="4"/>
                <text x="10" y="68" font-size="10" fill="#2ecc71">85%</text>
                <text x="10" y="120" font-size="10" fill="#f39c12">70%</text>
                <line x1="50" y1="112" x2="750" y2="112" stroke="#f39c12" stroke-width="1" stroke-dasharray="4"/>
                {puntos_grafica}
            </svg>
            <div class="info-box">
                <strong>¿Qué es la eficiencia del sueño?</strong><br>
                Es el porcentaje del tiempo que realmente dormiste del total que estuviste en cama.<br>
                ✅ <strong>85% o más</strong> = Muy buena<br>
                ⚠️ <strong>70–84%</strong> = Aceptable, en mejora<br>
                ❗ <strong>Menos de 70%</strong> = Área de trabajo en tu terapia
            </div>
        </div>

        <div class="card">
            <h2>📋 Registro diario</h2>
            <table>
                <thead>
                    <tr>
                        <th>Fecha</th>
                        <th>Me acosté</th>
                        <th>Me levanté</th>
                        <th>Tardé en dormirme</th>
                        <th>Despertares</th>
                        <th>Eficiencia</th>
                        <th>Calidad</th>
                        <th>Descanso</th>
                    </tr>
                </thead>
                <tbody>
                    {filas_tabla}
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """