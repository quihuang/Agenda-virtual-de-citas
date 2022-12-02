
# import os

# w     write
# r     read
# a     add
# x     verify exist, write

# Lista de listas, matriz
matriz = [ [3, 8, 1], [-1, 4, 7], [3, 2, 0], [9, 12, 65] ]

archivo = open("D:/Franklin/Escritorio/uc/archivos/matrices.txt","a")
for fila in matriz:
    fila.reverse()
    archivo.write( str(fila) + "\n")
    print(str(fila) + "\n")
archivo.close()


#Leer archivo
#Eval convierte al tipo de datos que se evalua
archivoL = open("D:/Franklin/Escritorio/uc/archivos/matrices.txt","r")
matrizL = []
for linea in archivoL:
    print(eval(linea[0:-1]))
    matrizL.append(eval(linea[0:-1]))
archivoL.close()
print(matrizL)
