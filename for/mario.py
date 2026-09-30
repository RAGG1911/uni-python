h=int(input("Ingrese la altura de la bandera: "))
jumps=0
while h != 1:
    if h >=0:
        if h %3 ==0 and h != 0:
            jumps += 1
            print("Mario hizo un salto largo")
            h/= 3
        else:
            jumps += 1
            print("Mario hizo un salto corto")
            h+= 1
    else:
        print("La altura de la bandera no puede ser negativa")
        h=int(input("Ingrese la altura de la bandera: "))
print("Cantidad de saltos: ", jumps)