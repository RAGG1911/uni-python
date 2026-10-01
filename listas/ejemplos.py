nuevos = ["Martin", "Pedro", "Christian"]
estudiantes = ["Juan", "Isaac", "Angélica", "Raúl", "Ian"]

#ejemplo 1
#estudiantes.append("Anthony")
#print(estudiantes)

#ejemplo 2
#estudiantes.extend(nuevos)
#print(estudiantes)

#ejemplo 3
#print(estudiantes.count("Juan"))

#ejemplo 4
print(estudiantes.pop(3))
print(estudiantes)

#ejemplo 5
estudiantes.insert(3, "Javier")
print(estudiantes)

#ejemplo 6
print(estudiantes.index("Ian"))

#ejemplo 7
estudiantes.sort()
print(estudiantes)
estudiantes.append("25")
estudiantes.sort()
print(estudiantes)

#ejemplo 8
estudiantes.reverse()
print(estudiantes)
