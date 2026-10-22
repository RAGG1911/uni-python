import numpy as np

notas = np.array([[80, 75, 90], [85, 90, 90], [70, 65, 95]])

suma_por_estudiante = np.sum(notas, axis=1)
prom_por_estudianteA = np.mean(notas, axis=1)
prom_por_estudianteB = np.average(notas, axis=1)
desv_estandar = np.std(notas)

print(f"*** valor desviacion estandar: {desv_estandar} ***")

suma_por_asignatura = np.sum(notas, axis=0)

print("Notas de los estudiantes:")
print(notas)
print("\nSuma de notas por estudiante:", suma_por_estudiante)
print("Promedio de notas por estudiante (Método A):", np.round(prom_por_estudianteA, 2))
print("Promedio de notas por estudiante (Método B):", np.round(prom_por_estudianteB, 2))
print("Suma de notas por asignatura:", suma_por_asignatura)