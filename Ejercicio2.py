import numpy as np

# Simulación de datos
estudiantes = np.array([
    [123, "Juan Perez", 1995, 3.8, "001"],
    [124, "Ana Martinez", 1989, 3.5, "002"],
    [125, "Carlos Gomez", 1988, 4.2, "003"],
    [126, "Lucia Suarez", 1990, 4.5, "002"],
    [127, "Pedro Diaz", 1985, 4.0, "001"]
])

# 1. Filtrar por carrera y promedio acumulado
codigo_carrera = input("Ingrese el código de la carrera a listar: ")
filtro1 = estudiantes[(estudiantes[:, 4] == codigo_carrera) & (estudiantes[:, 3].astype(float) >= 4.0)]
print("\nEstudiantes con promedio igual o mayor a 4:")
for estudiante in filtro1:
    print(estudiante[0], estudiante[1])
print(f"Total: {len(filtro1)} estudiantes")

# 2. Filtrar por ingreso antes de 1990 y condición académica
filtro2 = estudiantes[(estudiantes[:, 2].astype(int) < 1990) & (estudiantes[:, 3].astype(float) < 3.0)]
print("\nEstudiantes que ingresaron antes de 1990 y están condicionales:")
for estudiante in filtro2:
    print(estudiante[0], estudiante[1])
