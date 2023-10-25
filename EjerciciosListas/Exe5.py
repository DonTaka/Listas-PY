import random

lista1 = []

for i in range(10):
    lista1.append(random.randint(1,100))

lista2 = lista1.copy()
lista3 = lista1.copy()

lista2.sort()
lista3.sort(reverse=True)



print(lista1)
print(lista2)
print(lista3)