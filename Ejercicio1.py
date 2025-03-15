import numpy as np

# Simulación de votos
np.random.seed(0)  # Fijar semilla para reproducibilidad
candidatos = np.arange(1, 31)
votos = np.random.randint(0, 500, size=30)

# Ordenar de mayor a menor
orden = np.argsort(votos)[::-1]
candidatos_ordenados = candidatos[orden]
votos_ordenados = votos[orden]

# Imprimir resultados
print("Listado de candidatos según número de votos (de mayor a menor):")
for i in range(len(candidatos)):
    print(f"Candidato {candidatos_ordenados[i]}: {votos_ordenados[i]} votos")
