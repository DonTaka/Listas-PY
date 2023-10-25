import random

lista = []

for i in range(30):
    lista.append(random.randint(1,100))

lista.sort()
print(lista)

print(f"El numero menor es {lista[0]}")
print(f"El numero mayor es {lista[-1]}")