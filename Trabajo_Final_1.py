""" Este proyecto consiste en una aplicación con Python
que permita gestionar el inventario de una pequeña
tienda o comercio. La aplicación debe ser capaz de
registrar, actualizar, eliminar y mostrar productos
en el inventario. Además, debe incluir funcionalidades
para realizar búsquedas y generar reportes de stock.
 """

""" Desarrollar un pequeño script que permita al
usuario ingresar datos (por ejemplo, el nombre
y la cantidad de un producto) y luego mostrar
esos datos de manera simple.
Utilizar funciones input() para la entrada y
print() para la salida, siguiendo el modelo de
Entrada-Proceso-Salida discutido en clases
anteriores.
 """

print("\nSistema de stock\n")
nombre_producto = str(input("\nIngrese el nombre del producto: "))
cantidad_producto = float(input("\nIngrese la cantidad del producto: "))

print("\n\nSe ingresaron",cantidad_producto,"unidades de",nombre_producto,"\n")