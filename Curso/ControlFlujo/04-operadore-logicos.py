#and, or, not

valor = input("Ingrese valor: ")

valorInt = int(valor)

if valorInt > 0 and valorInt < 10:
    print("es positivo y menor a 10")
elif valorInt > 10:
    print("es positivo")
else:
    print("es negativo")


gas = True
encendido = True

if gas and encendido:
    print("Puedes seguir")


if not gas or encendido:
    print("Puedes seguir")

if gas and encendido and (valorInt > 0):
    print("Puedes seguir")