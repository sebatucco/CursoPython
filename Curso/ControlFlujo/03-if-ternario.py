#obtener datos del usuario
edad = input("Ingrese Edad: ")

#convertir datos
edadLocal = int(edad)

# if edadLocal > 17 :
#     mensaje = "Es mayor"
# else:
#     mensaje = "Es menor"

mensaje = "Es mayor" if edadLocal > 17 else "Es menor"
print(mensaje)