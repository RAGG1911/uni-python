#Taller Grupal Raúl Gómez y Alberto Ávila

print("Taller Grupal Raúl Gómez y Alberto Ávila")
prob = int(input("1. Conversor de temperatura \n2. Monitoreo IOT\n3. Sensor de Movimiento\n4. Sensor de humedad\nIngrese el número del problema a realizar: "))
match prob:
    case 1:
        print("Conversor de temperatura")
        temp = input("Ingrese la unidad inicial a convertir (C/F): ")
        match temp:
            case "C":
                c = float(input("Ingrese la temperatura en Celsius: "))
                f = (c * 1.8)+32
                print("La temperatura en Fahrenheit es: ", f)
            case "F":
                f = float(input("Ingrese la temperatura en Fahrenheit: "))
                c = (f - 32) / 1.8
                print("La temperatura en Celsius es: ", c)
            case _:
                print("Unidad no válida")
    case 2:
        print("Monitoreo IOT")
        temp_A = int(input("Ingrese la temperatura para el sensor A en valor entero:"))
        temp_B = int(input("Ingrese la temperatura para el sensor B en valor entero:"))
        if temp_A > temp_B:
            print("El sensor A tiene una temperatura mayor que el sensor B")
            if temp_A > 0:
                print("Está dentro del rango seguro")
        else:
            print("El sensor B tiene una temperatura mayor que el sensor A")
            if temp_B > 0:
                print("Está dentro del rango seguro")
        if temp_A+1 >= temp_B:
            print("Sensor A+1 entra en Condición Crítica")
        if temp_B%2 == 0:
            print("Sensor B, temperatura par, sincronizando...")
    case 3:
        print("Sensor de Movimiento")
        dist=float(input("Ingrese la distancia del sensor de movimiento: "))
        if dist < 50:
            print("Alerta Roja: Intruso Detectado a", dist , "centimetros,", dist/100, "metros, revisar cámaras")
        elif dist >= 50 and dist < 100:
            print("Alerta Amarilla: Movimiento Cercano a", dist , "centimetros,", dist/100, "metros, proceder con precaución")
        elif dist >= 101 and dist < 200:
            print("Alerta Verde: Movimiento detectado pero lejano a", dist , "centimetros,", dist/100, "metros, tranquilo")
        else:
            print("Estado normal, sin amenazas")
    case 4:
        print("Sensor de humedad")
        avg = 0
        urgente=0
        bien=0
        no=0
        for i in range(5):
            humedad = int(input("Medición " + str(i) + "\nPorcentaje de humedad del sensor: "))
            avg += humedad
            if humedad < 30:
                print("Regar urgentemente")
                urgente+=1
            elif humedad >= 30 and humedad < 60:
                print("Humedad adecuada")
                bien+=1
            else:
                print("No regar")
                no+=1
        avg /= 5
        print("Promedio de humedad: ", avg)
        print("Cantidad de alertas urgentes: ", urgente)
        print("Cantidad de alertas de humedad adecuada: ", bien)
        print("Cantidad de alertas de no regar: ", no)
        