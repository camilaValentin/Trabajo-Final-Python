# 1. Crear un menú interactivo
# Crear un menú interactivo utilizando bucles while y condicionales if-elif-else:
# ● El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas con la gestión de productos.
# ● Entre las opciones, deben incluirse: agregar productos al inventario y mostrar los productos registrados.
# 2. Agregar productos al inventario
# Implementar la funcionalidad para agregar productos a una lista:
# ● Cada producto debe ser almacenado en una lista, y debe tener al menos un nombre y una cantidad asociada.
# 3. Mostrar el inventario
# Mostrar los productos ingresados:
# ● Al seleccionar la opción correspondiente, el sistema debe permitir visualizar los productos almacenados hasta el
# momento.

productos = []

print("\n=====================")
print("   MENU DE GESTIÓN")
print("=====================")
print("1.Agregar Producto")
print("2.Mostrar Productos")
print("3.Salir")
print("=====================")

seleccion = int(input("Seleccione una opción: "))
print("=====================")

while seleccion != 1 and seleccion != 2 and seleccion != 3:

    print("\n=====================")
    print("   MENU DE GESTIÓN")
    print("=====================")
    print("1.Agregar Producto")
    print("2.Mostrar Productos")
    print("3.Salir")
    print("=====================")

    seleccion = int(input("Seleccione una opción: "))
    print("=====================")


while seleccion != 3:
    if seleccion == 1:
        ingresar = 1
        while ingresar == 1:
            nombre = str(input("\nIngrese el nombre del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))

            while (cantidad < 0):
                cantidad = int(input("\nNo se puede ingresar esa cantidad, por favor ingrese una cantidad válida: "))

            print(f"\nSe ingresaron {cantidad} unidades de {nombre}")
            productos.append([nombre, cantidad])
            ingresar = int(input("\nDeseas ingresar otro producto?\n1.Si\n2.No\nSeleccione una opción: "))
    
    if seleccion == 2:
        contador = 0
        print("\n--------------------")
        print("PRODUCTOS INGRESADOS")
        print("--------------------")
        while contador < len(productos):
            producto = productos[contador]
            print(f"Nombre: {producto[0]} Cantidad: {producto[1]}")
            contador +=1 
        # for producto in productos:
        #     print("Nombre: ", producto[0], " Cantidad: ", producto[1])
        print("--------------------")

    print("\n=====================")
    print("   MENU DE GESTIÓN")
    print("=====================")
    print("1.Agregar Producto")
    print("2.Mostrar Productos")
    print("3.Salir")
    print("=====================")

    seleccion = int(input("Seleccione una opción: "))
    print("=====================")

if seleccion == 3:
    print("\n=====================")
    print("PROGRAMA FINALIZADO")
    print("=====================\n")