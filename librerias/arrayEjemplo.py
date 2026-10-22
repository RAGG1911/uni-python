import array as arr

edades = arr.array('i', [21, 23, 19, 24, 25])

suma = 0
for valor in edades:
    suma += valor
print("La suma de las edades es:", suma)