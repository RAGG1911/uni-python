#Raúl Gómez 4-827-1289

#firstNum = int(input("Enter the first number: "))
#secondNum = int(input("Enter the second number: "))
#
#try:
#    print(firstNum / secondNum)
##except:
#except ZeroDivisionError as e:
#    print("Error: Division by zero is not allowed.", e)

#title = "Estoy aprendiendo Python"
#try: 
#    print(tite)
#except NameError as msg:
#    print("Tipo de error:", msg)

#dia = input("\nEscriba un día comprendido entre 1-31: ")
#try:
#    if int(dia) > 31:
#        raise ValueError("El día debe estar entre 1 y 31.")
#        print("numero invalido")
#
#except ValueError as msg:
#    print("Error:", msg)
#finally:
#    print("Se aprende de los errores")

cedula = input("Escriba su numero de cedula usando guiones:")
try:
    partes = cedula.split("-")
    if len(partes) != 3:
        raise ValueError("La cédula debe tener el formato XXX-XXXXXXX-X.")
    for parte in partes:
        if not parte.isdigit():
            raise ValueError("La cédula debe contener solo números y guiones.")
    print("Cedula valida: ", cedula)
except ValueError as error:
    print("Error:", error)
finally:
    print("Cuidadito Wazowski")