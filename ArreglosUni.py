import numpy as np;

lista = [1,2,3,4,5,6]
array = np.array(lista)

#print(lista)
print(array)

#ndim = dimension del arreglo
print(array.ndim)

#len(arreglo) = Largo del arreglo
print(len(array))

#shape = Estructura del arreglo
print(array.shape)

#[Start:Stop:Step] = Slice
#Start = Indica desde donde empiezo a mostrar el arreglo
#Stop = Hasta donde mostramos el arreglo Menos 1
#Step = De cuanto en cuanto mostramos el arreglo
#Mostramos arreglo desde el inicio hasta posicion 2(2 Menos 1)
print(array[0:2])

#Mostramos los datos del arreglo de 2 en 2
print(array[::2])

#Si uso posicion en negativo , cuento de final al inicio
print(array[-2])

#AutoRellenar una lista con numeros con ciclo for
lista2 = [i for i in range(1,11)]
#print(lista2)
array2 = np.array(lista2)
print(array2)

#recorrer y mostrar los valores de un arreglo 1 por 1 
for i in range(len(array2)):
    print(f"Numero {array2[i]} esta en la posicion {i}")

#arange(inicio,termino,paso) : Relleno un array con la dimension indicada
array3 = np.arange(1,11)
print(array3)

#Sumarle 5 a todos los registros del arreglo 1 
array3+=5
print(array3)
#Si resto 5 a todos los registros
array3-=5
print(array3)
#Si multiplicar oor 10 todos los registros
array3*=10
print(array3)
#Ones = rellena el arreglo de unos , segun dimension
array4 = np.ones(10)
print(array4)

#Igualdad o mayor que entre arreglos

print(array3>array4)

#Sum() : Retorna la suma de todos los valores del arreglo
print(array4.sum())
#Mean() : Retorna el promedio de valores del arreglo
print(array3.mean())
#min() : Retorna el numero menor del arreglo
print(array3.min())
#max() : Retorna el numero mas alto del arreglo
print(array3.max())

