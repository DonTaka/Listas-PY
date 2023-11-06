import numpy as np
#Creacion de arreglo 3x3 con numeros aleatorios de 1 a 100
#random.randint = nos permite generar numeros aleatorios en un rango
#random.randint(inicio,fin,tamañoArreglo)
#con reshape rearmamos la forma del arreglo en bidimensional
matriz1 = np.random.randint(1,101,9).reshape([3,3])
print(matriz1)

#Promedio de datos
print(matriz1.mean())
#Suma
print(matriz1.sum())
#Mayor
print(matriz1.max())
#Menor
print(matriz1.min())
#Diagonal principal
for i in range(matriz1[:,0].size):
    print(matriz1[i,i])

#Declaramos matriz llena de ceros de 3x3
matriz2 = np.zeros([3,3])
#Llenamos la diagonal con los primeros 3 numeros
matriz2 = np.diag([1,2,3])
print(matriz2)
