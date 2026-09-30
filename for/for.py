#ejemplo 1
for tarea in range(5):
    print("Completando tarea", tarea)

#ejemplo 2
for turno in range(3, 8):
    print("Turno", turno, ". ¿Quien es el impostor?")

#ejemplo 3
for numero in range(1, 13, 3):
    print("Ronda", numero, ". El impostor fingió hacer una tarea.")

#ejemplo 4
for i in range(1, 5):
    print("Numero #", i)

#ejemplo 5
for i in range(1, 10):
    if i ==5:
        break
    print(i)

#ejemplo 6
import math
for i in range(1, 6):
    raiz = math.sqrt(i)
    print(f"La raíz cuadrada de {i} es {raiz:.2f}")