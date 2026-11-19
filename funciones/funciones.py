#def pares(numero):
#    if numero % 2 == 0:
#        return True
#    else:
#        return False
#print(pares(9))
#respuesta = pares(10)
#print("La respuesta fue:", respuesta)
#
#def square(num):
#    if not num.isdigit():
#        return "Error: El valor ingresado no es un número válido."
#    num = int(num)
#    return num * num
#num = input("Ingrese un número para calcular su cuadrado: ")
#print(f"Para el número {num}, su cuadrado es: {square(num)}")
#
#def cubeRoot(num=1):
#    if not num.isdigit() and num > 0:
#        return "Error: El valor ingresado no es un número válido."
#    num = int(num)
#    return num ** (1/3)
#num = input("Ingrese un número para calcular su raíz cúbica: ")
#print(f"Para el número {num}, su raíz cúbica es: {cubeRoot(num)}")

global_var = 1
local_var = 10

def my_vars():
    print("Variable global:", global_var)
    local_var = 2
    print("Variable local:", local_var)
    return local_var
my_vars()
print("**Nueva Global:", local_var)
print("=>Nueva Global: ", my_vars())