
#obtener datos del usuario
edad = input("Ingrese Edad: ")

#convertir datos
edadLocal = int(edad)

if edadLocal > 60:
    print("uede ingresar con descuento")
elif edadLocal > 17:
    print("Puede ingresar")
else:
    print("Prohibido el ingreso")