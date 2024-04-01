print("bienvenido")
print("para salir escribe Salir")

resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese el primer numero")
        if resultado.lower() == 'salir':
            break
        resultado = int(resultado)
    op = input ("ingrese la operacion")
    if op.lower() == 'salir':
        break
    n2 = input("ingresa el segundo numero")
    if n2 == 'salir':
        break
    n2 = int(n2)
    if op =="suma":
        resultado += n2
    if op == "resta":
        resultado -= n2
    if op == "producto":
        resultado *= n2
    if op == "divicion":
        resultado /= n2
    print(resultado)
