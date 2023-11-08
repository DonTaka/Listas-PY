#IVA = agregar el 0.19%
#Crear funcion
#def [nombrFuncion]():
#   Instrucciones
def calcular_IVA(precio):
    total = precio*1.19
    #total = precio + (precio*0.19)
    return total

#valorIVA = calcular_IVA(5000)
#print(f"El valor con IVA del producto es {valorIVA}")


#Descuento
def calcular_Descuento(precio,descuento):
    desc = precio*(descuento/100)
    total = precio-desc
    print(f"Se le desconto la cantidad de ${desc}")
    print(f"Total de la compra: ${total}")

#calcular_Descuento(5000,30)


#IMC
def IMC(peso,estatura):
    valorIMC = peso/(estatura**2)
    print(valorIMC)
    if(valorIMC<18.5):
        print("Bajo Peso")
    elif (valorIMC>18.5 and valorIMC<=24.9):
        print("Adecuado")
    elif(valorIMC>=25 and valorIMC<=29.9):
        print("Sobrepeso")
    elif(valorIMC>=30 and valorIMC<=34.9):
        print("Obesidad Grado 1")
    elif(valorIMC>=35 and valorIMC<=39.9):
        print("Obesidad Grado 2")
    elif(valorIMC>=40):
        print("Obesidad Grado 3")

#IMC(55,1.70)