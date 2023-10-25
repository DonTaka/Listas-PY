lista = []

opcion = 1

while opcion!=2:
    nombre = input("Ingrese su nombre: ")
    lista.append(nombre)

    print("Desea seguir agregando? ")
    opcion = int(input("1.- Si \n 2.- No "))

lista.sort(key=len)
print(lista)
lista.pop(0)
print(lista)