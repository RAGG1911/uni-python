edad = 66
pais = "Mexico"

match (edad, pais):
    case(x, "España") if x >=18 and x< 65:
        print("Adulto en España")
    case(x, "Mexico") if x >=65:
        print("Adulto mayor en Mexico")
    case(_, "Japon"):
        print("Residente en Japon")
    case _:
        print("No coincide")
    