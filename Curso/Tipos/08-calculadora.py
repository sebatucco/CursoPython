#obtener datos del usuario
numero1 = input("Ingrese Primer Numero")
numero2 = input("Ingrese Segundo Numero")

#convertir datos
n1 = int(numero1)
n2 = int(numero2)

#operaciones
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2  #float

#mostrar resultados
mensaje = f"""
para los numeros {n1} y {n2}
el resultado de la suma: {suma}
el resultado de la resta: {resta}
el resultado de la multiplicacion: {multiplicacion}
el resulrado de la division: {division}
"""
print(mensaje)