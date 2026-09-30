pin = 1234
enteredPin = int(input("Ingrese el pin: "))
for i in range(3):
    if enteredPin != pin:
        print("Pin incorrecto, intentos restantes: ", 2-i)
        enteredPin = int(input("Ingrese el pin: "))
        print(i)
    else:        
        print("Acceso permitido, Bienvenido")
        break

