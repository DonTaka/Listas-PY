lista = []

for i in range (3):
    nombre = input("Ingrese su nombre: ")
    lista.append(nombre)

lista.sort(key=len)
print(lista[-1])


