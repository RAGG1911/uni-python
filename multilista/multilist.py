#multilist = [[1, 2, 3], [7, 5, 6], [8, 9], ["a", "b"]]
#print("bottom right 1, 2:", multilist[1][2])

#menu = [["Ensalada Cesar", "Sopa del día", "Gazpacho"], ["Pasta Alfredo", "Lasaña", "Pollo Cordon Bleu"], ["Tiramisu", "Cheesecake", "Flan"]]

#categoria = ["Entradas", "Platos Principales", "Postres"]

#for fila in menu:
#    for plato in fila:
#        print(plato, end="---")
#    print()


#for i in range(len(menu)):
#    print(f" * {categoria[i]} *")
#    for j in range(len(menu[i])):
#        print(f"{j+1}. {menu[i][j]}")
#    print()
    
postres = [
    ["Cheesecake", 12, 3.50],
    ["Tres leches", 8, 2.75],
    ["Flan", 15, 1.50],
    ["Brownie", 20, 1.25],
    ["Tiramisu", 6, 4.00], 
 ]   

print(postres[2][0], postres[2][1], postres[2][2])
print(postres[0][0], postres[0][1], postres[0][2]) 

print("Lista de postres y precios:")
for aux in postres:
    print(aux[0], "-", aux[1], "cada unidad a $", aux[2]) 