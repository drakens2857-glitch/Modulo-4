nombre = "Ana García"
curso = "Python Básico"
nivel = "Intermedio"

linea = "-" * 30
encabezado = f"\n{'REPORTE DE PROGRESO'}\n{linea}"

cuerpo = f"\nEstudiante: {nombre}\nCurso: {curso}\nNivel: {nivel}"

reporte = encabezado + cuerpo
print(reporte)
