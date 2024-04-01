valor = input("Ingrese valor: ")

valorInt = int(valor)

for i in range(0, valorInt): #valorInt -1
    print(f"""Numero de veces: {i}""")


for i in range(valorInt): #valorInt -1
    print(i, i * "Hola Mundo ")