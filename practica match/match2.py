import sys

if(sys.version_info >= (3,10)):
    print("disponible match case sintaxis")
    
num = int(input("Ingrese un numero entero: "))
match num:
    case 0:
        print("El numero es 0")
    case 1:
        print("El numero es 1")
    case 5 | 6:
        print("El numero es 5 o 6")
    case _:
        print("Es otro numero")