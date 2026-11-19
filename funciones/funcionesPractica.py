#notas = []
#
#def promedio(notas):
#    try:
#        if len(notas) != 5:
#            raise ValueError("La lista de notas debe contener exactamente 5 elementos.")
#        return sum(notas) / len(notas)
#    except ValueError as e:
#        print(f"Error: {e}")
#        return 0
#
#
#for i in range(5):
#    nota = float(input(f"Ingrese la nota {i + 1}: "))
#    notas.append(nota)
#
#print(f"El promedio es: {promedio(notas)}")

coord1 = ()
coord2 = ()

def distancia(coord1, coord2):
    try:
        if len(coord1) != 2 or len(coord2) != 2:
            raise ValueError("Cada coordenada debe contener exactamente 2 elementos (x, y).")
        x1, y1 = coord1
        x2, y2 = coord2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    except ValueError as e:
        print(f"Error: {e}")
        return None
  
  
  
coord1 = (float(input("Ingrese la coordenada x1: ")), float(input("Ingrese la coordenada y1: ")))
coord2 = (float(input("Ingrese la coordenada x2: ")), float(input("Ingrese la coordenada y2: ")))
distancia_calculada = distancia(coord1, coord2)
if distancia_calculada is not None:
    print(f"La distancia entre los puntos es: {distancia_calculada}")