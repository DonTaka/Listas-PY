lista = []
suma = 0 
#Agrego valores a la lista
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    lista.append(numero)

#Recorro y sumo
# i toma el valor de cada registro de la lista
#Cada iteracion variable i toma un valor de la lista
for i in lista:
    suma+=i

print(f"La suma de los 10 valores de la lista es {suma}")
print(f"El promedio de valores de la lista es {suma/10}")


