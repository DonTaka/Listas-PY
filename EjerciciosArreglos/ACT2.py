import numpy as np

#Funcion random genera numeros aleatorios
#randint nos devuelven valores aleatorios segun rango
#(Inicio,Termino,tamaño del arreglo)
array = np.random.randint(1,101,10)
print(array)

#Mayor
print(f"El numero mayor es: {array.max()}")
#Menor
print(f"El numero menor es: {array.min()}")
#Suma
print(f"La suma de todos los valores es: {array.sum()}")
#Menor
print(f"El promedio de valores es: {array.mean()}")
#Mostrar todo
for i in range(0,len(array)):
    print(f"Numero {i} es {array[i]}")
