#Crear Lista
#[] == Arreglo
lista = []
lista = [1,5,10,50,100,500]
#Numero positivo = Cuenta de principio a final
#Numero negativo = Cuenta desde el ultimo al principio
print(lista[-1])

#Append = Agregar un dato en la ultima posicion de la lista
lista.append(1000)
print(lista[-1])

#Extends = permite fusionar una lista con otra
lista2 = [5000,9999]
lista.extend(lista2)
print(lista)

#Insert(Posicion,dato) = Insertar un dato en la posicion especifica
lista.insert(4,99)
print(lista)

#remove(dato) = Elimina un dato de la lista
lista.remove(99)
print(lista)

#pop() = Elimina el ultimo registro de la lista
#pop(posicion) = Elimina la posicion indicada
lista.pop()
print(lista)

#Reverse = Invierte el orden de los datos
lista.reverse()
print(lista)

#Sort = Ordena la lista de menor a mayor
lista.sort()
print(lista)

#Sort(Reverse=True) = Ordena la lista de mayor a menor
lista.sort(reverse=True)
print(lista)
