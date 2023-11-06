import numpy as np

matriz = np.arange(1,101).reshape([10,10])
#Primer [] = Vertical de 0 en adelante
#SLice [Inicio:Termino:Paso]
#Primeros 5 numeros de las primeras 5 filas
print(matriz[0:5,0:5])
#Suma de todos los valores de la primera fila
print(matriz[0,:].sum())

#Concatenate
arr1 = np.arange(1,7).reshape([2,3])
arr2 = np.arange(7,13).reshape([2,3])

print(f"Arreglo 1 \n{arr1}")
print(f"Arreglo 2 \n{arr2}")
#Axis dirige la orientacion de la fusion
#Axis = 0 Vertical , se agregan los datos
#Al final del primer arreglo
#Axis = 1 Horizontal, se agregan de forma horizontal continuando cada piso de arreglo
arr1 = np.concatenate((arr1,arr2),axis=1)
print(f"Arreglo combinado vertical \n{arr1}")