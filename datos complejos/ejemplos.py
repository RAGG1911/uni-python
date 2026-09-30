#transformacion mayus/minus

#print("HELLo".lower())
#print("hello".upper())
#print("hello world".capitalize())
#print("hello world".title())

#limpieza y modificacion

#print("  hello  ".strip())
#print("one, three".replace("e", "i"))

#comprobacion

#print("hello".startswith("he"))
#print("hello".endswith("lo"))
#print("12345".isnumeric())

#division y union

#divide en lista usando ,
#print("one, two, three".split(","))

#une en lista usando -
#print("-".join(["a", "b", "c"]))

#busqueda y conteo

#print("hello world".find("e"))
#print("hello".index("el"))
#print("hello world".count("o"))

#manejo de strings
mensaje = "El principito atravesó el desierto y no encontró más que una flor"
print(len(mensaje))
print(mensaje[3])
print(mensaje[3:14])
print(mensaje[::2])
print(mensaje[14:22:2])
print(mensaje[:7])
print(mensaje[:-1])
print(mensaje[-1:])
print(mensaje[-12:-8])
print(mensaje[-8:0])
print(mensaje[::-1])