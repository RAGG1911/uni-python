lvl = 1

while lvl < 5:
    print("Tu Pikachu es nivel", lvl)
    ans = input("¿Pelear o Huir?: ").lower()
    match ans:
        case "pelear":
            print("Pikachu gana la pelea y sube de nivel")
            lvl += 1
        case "huir":
            print("Pikachu huye y bajó de nivel")
            lvl -= 1
    if lvl == 0:
        print("Pikachu se desmayó y perdió todos sus niveles")         
print("Tu Pikachu llegó a nivel 5")
