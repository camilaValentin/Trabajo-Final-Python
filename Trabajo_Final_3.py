productos = []

def menu():
    print("\n=====================")
    print("   MENU DE GESTIÓN")
    print("=====================")
    print("1.Agregar producto")
    print("2.Mostrar productos")
    print("3.Registrar venta producto")
    print("4.Actualizar productos")
    print("5.Eliminar productos")
    print("5.Buscar producto")
    print("0.Salir")
    print("=====================")

    seleccion = int(input("Seleccione una opción: "))
    print("=====================")
    return seleccion


def registrar_producto():
    ingresar = 1
    while ingresar == 1:
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))

        while (cantidad < 0):
            cantidad = int(input("\nNo se puede ingresar esa cantidad, por favor ingrese una cantidad válida: "))

        print(f"\nSe ingresaron {cantidad} unidades de {nombre} al precio de {precio}")
        productos.append([nombre, cantidad,precio])
        ingresar = int(input("\nDeseas ingresar otro producto?\n1.Si\n2.No\nSeleccione una opción: "))


def mostrar_productos():
    print("\n--------------------")
    print("PRODUCTOS INGRESADOS")
    print("--------------------")
    for producto in productos:
        print("Nombre: ", producto[0], "- Cantidad: ", producto[1], "- Precio: ", producto[2])
    print("--------------------")


def actualizar_producto():
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    if (id_producto < 0 or id_producto >= len(productos)):
        print("ID de producto inválido.")
        return
    else:
        opcion = -1
        while (opcion != 0):
            opcion = int(input("\n1.Nombre del producto\n2.Precio del producto\n3.Cantidad del producto\n0.Salir\nIngrese que dato desea modificar: "))
            if (opcion == 1):
                nuevo_Nombre = input("Ingrese el nuevo nombre del producto: ")
                productos[id_producto]["nombre"] = nuevo_Nombre
            elif (opcion == 2):
                nuevo_Precio = float(input("Ingrese el nuevo precio del producto: "))
                productos[id_producto]["precio"] = nuevo_Precio
            elif (opcion == 3):
                nueva_Cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                productos[id_producto]["cantidad"] = nueva_Cantidad


def ingresar_venta():
    print("\n--------------------")
    print("INGRESO DE VENTA")
    print("--------------------")


def eliminar_producto():
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    if (id_producto < 0 or id_producto >= len(productos)):
        print("ID de producto inválido.")
        return
    else:
        productos.pop(id_producto)
        print("Producto eliminado correctamente.")


def buscar_producto():
    id_producto = int(input("Ingrese el ID del producto a buscar: "))
    if (id_producto < 0 or id_producto >= len(productos)):
        print("ID de producto inválido.")
        return
    else:
        producto = productos[id_producto]
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")


opcion = menu()

while opcion != 0:
    if opcion == 1:
        registrar_producto()
    elif opcion == 2:
        mostrar_productos()
    elif opcion == 3:
        ingresar_venta()
    elif opcion == 4:
        actualizar_producto()
    elif opcion == 5:
        eliminar_producto()
    elif opcion == 6:
        buscar_producto()
    opcion = menu()


if opcion == 0:
    print("\n=====================")
    print("PROGRAMA FINALIZADO")
    print("=====================\n")