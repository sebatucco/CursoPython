mascotas = ["pelusa", "pulga", "copito"]
print(mascotas[1])
mascotas[1] = "vicho"
print(mascotas[:3]) # imprime de 0 a 2 (3-1)
print(mascotas[1:]) # imprime de 1 a la ultima
print(mascotas[-1]) # imprime el valor de la ultima posicion
print(mascotas[::2]) # imprime de 0 a la ultima con saltos de 2 en 2
print(mascotas[1::2]) # imprime de 1 a la ultima con saltos de 2 en 2


numeros = list(range(21))
print(numeros[::2]) # imprime de 0 a la ultima con saltos de 2 en 2
print(numeros[:1:2]) # imprime de 0 a la ultima con saltos de 2 en 2
