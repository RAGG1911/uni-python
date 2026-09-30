status = input("C´odigo de estado: ")
match status:
    case 200:
        print("Petici´on Exitosa")
    case 403:
        print("Petici´on Denegada")
    case 404:
        print("No encontrado")
    case 410:
        print("No disponible")
    case 500:
        print("Error inesperado")