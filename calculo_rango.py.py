#cálculamos un rango de un conjunto de datos.
#Cálculo del Rango en Estadística Descriptiva 

#solicitamos al usuario que ingrese los datos y los almacenamos en la lista.
n = int(input("Ingrese la cantidad de datos para la lista 1(0 para salir del programa): "))

#definimos un conjunto de datos como una lista vacía
#para que el usuario pueda ingresar los datos y que estos queden guardados en la lista.
datos = []
datos_2 = []

#creamos dos bucles for para guardar los datos ingresados por el usuario en las listas correspondientes.
for i in range(n):
    dato = int(input("Ingrese el dato {}: ".format(i+1)))
    if dato == 0:
        print("salir del programa")
        break
    datos.append(dato)

#solicitamos al usuario que ingrese los datos para la segunda lista y los almacenamos en la lista correspondiente.
m = int(input("Ingrese la cantidad de datos para la lista 2(0 para salir del programa): "))
for j in range(m):
    dato_2 = int(input("Ingrese el dato {}: ".format(j+1)))
    if dato_2 == 0:
        print("salir del programa")
        break
    datos_2.append(dato_2)

#Aplicamos el manejo de excepciones para evitar errores al calcular el rango si las listas están vacías.
try:
    #verificamos que las listas no estén vacías antes de calcular el rango.
    if len(datos) == 0:
        raise ValueError("La lista 1 está vacía. No se puede calcular el rango.")
    else:
        if len(datos_2) == 0:
            raise ValueError("La lista 2 está vacía. No se puede calcular el rango.")
except ValueError as e:
    print(e)
    exit()

#definimos variable para almacenar el rango
calcular_rango = max(datos) - min(datos)
calcular_rango_2 = max(datos_2) - min(datos_2)

print("El rango de la  lista 1 es:", calcular_rango)
print("El rango de la  lista 2 es:", calcular_rango_2)