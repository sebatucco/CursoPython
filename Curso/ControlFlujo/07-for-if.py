valor = input("Ingrese valor: ")
valorInt = int(valor)

valorDos = input("Ingrese valor a buscar: ")
valorDosInt = int(valorDos)

for i in range(0, valorInt): #valorInt -1
    print(f"""Numero de veces: {i}""")


for i in range(valorInt): #valorInt -1
    if i == 2:
        print(i, "Encontro valor")
        break
else:
    print("No se encontro numero")