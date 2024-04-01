def imprimir(apellido="", nombre=""):  # si no se pasa valor toma ""
    print(f"Datos de la persona: {apellido} - {nombre}")

print("ingresa nombre: ")
vNombre = input()

print("ingresa apellido: ")
vApellido = input()
imprimir(nombre = vNombre, apellido = vApellido) # argumento nombrado