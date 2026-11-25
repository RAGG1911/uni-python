#ejemplo 1: open sencillo con ruta absoluta

#archivo = open("/home/ragg/Documents/uni-python/microtest.py", "r")
#contenido = archivo.read()
#print(contenido)
#archivo.close()

#ejemplo 2: with open
#with open("/home/ragg/Documents/uni-python/microtest.py", "r") as archivo:
#    contenido = archivo.readline()
#    contenido1 = archivo.readline()
#    print(contenido)
#    print(contenido1)
    
#ejemplo 3: creacion y escritura
with open("text_test.txt", "w") as archivo:
    archivo.write("Linea 1\n")
    archivo.write("Linea 2\n")