print("ingrese valor: ")
valor = input()
valorInt = int(valor)
contador = 0
while contador < valorInt:
    contador +=2
    print(f"el nuemero es: {contador}")

comando = ""
while comando.lower() != 'salir':
    comando = input("$ ")
    print(comando)      
