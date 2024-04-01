#and, or, not

valor = input("Ingrese valor: ")

valorInt = int(valor)

gas = True
encendido = True



if not gas and encendido or valorInt > 0:  # si el valor de la primera expresion es verdadero continua evaluando de izq a der
    print("Puedes seguir")