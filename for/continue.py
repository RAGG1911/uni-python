for i in range(1, 4):
    for j in range(1, 4):
        if i == 1 and j == 1:
            print("Pasa a la siguiente iteración si i=1 y j=1")
            continue
        if i == 2 and j == 1:
            print("Interrupcion del ciclo si i=2 y j=1")
            break
        print("Ejecutando i=", i, "y j=", j)