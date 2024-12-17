import sqlite3
from colorama import init, Fore, Back, Style
init() 
init(autoreset=True)

#----------------------------------------------------------------
def crear_tabla_productos():
    # Función para crear la tabla
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Productos (ID INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, descripcion TEXT, cantidad INTEGER NOT NULL, precio REAL NOT NULL, categoria TEXT) ''')
    conexion.commit()
    conexion.close()


#----------------------------------------------------------------
def menu_principal():
    #Función para el menu principal del programa
    print("")
    print(Fore.MAGENTA + "=====================".center(50," "))
    print(Style.BRIGHT + Fore.MAGENTA + "MENU DE GESTIÓN".center(50," "))
    print(Fore.MAGENTA + "=====================".center(50," "))
    print(Fore.GREEN + "\t1.Registrar producto")
    print(Fore.GREEN + "\t2.Mostrar todos los productos")
    print(Fore.GREEN + "\t3.Actualizar un producto")
    print(Fore.GREEN + "\t4.Eliminar un producto")
    print(Fore.GREEN + "\t5.Buscar un producto por ID")
    print(Fore.GREEN + "\t6.Buscar productos por nombre")
    print(Fore.GREEN + "\t7.Buscar productos por categoría")
    print(Fore.GREEN + "\t8.Generar reporte de bajo stock")
    print(Fore.RED + "\t0.Salir")
    print(Fore.MAGENTA+"\t----------------------------------")

    seleccion = int(input(Style.BRIGHT + Fore.MAGENTA + "\tSeleccione una opción: "))
    print(Fore.MAGENTA+"\t----------------------------------")
    return seleccion


#----------------------------------------------------------------
def printProducto(producto):
    #Función para mostrar un producto en pantalla
    print(Fore.MAGENTA + "\t----------------------------------")
    print(Fore.CYAN + f"\tID: {producto[0]}")
    print(Fore.CYAN + f"\tNombre: {producto[1]}")
    print(Fore.CYAN + f"\tDescripción: {producto[2]}")
    print(Fore.CYAN + f"\tCantidad: {producto[3]}")
    print(Fore.CYAN + f"\tPrecio: ${producto[4]}")
    print(Fore.CYAN + f"\tCategoría: {producto[5]}")
    print(Fore.MAGENTA + "\t----------------------------------")


#----------------------------------------------------------------
def registrar_producto():
    #Función para agregar productos
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    print(Fore.MAGENTA + "\t----------------------------------")
    print(Style.BRIGHT + Fore.MAGENTA + "REGISTRO DE PRODUCTO".center(50," "))
    print(Fore.MAGENTA + "\t----------------------------------")

    nombre = input(Style.DIM + Fore.CYAN + "Nombre: ")
    descripcion = input(Style.DIM + Fore.CYAN + "Descripción: ")
    cantidad = int(input(Style.DIM + Fore.CYAN + "Cantidad: "))
    precio = float(input(Style.DIM + Fore.CYAN + "Precio: "))
    categoria = input(Style.DIM + Fore.CYAN + "Categoría: ")

    cursor.execute("INSERT INTO Productos(nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",(nombre, descripcion, cantidad, precio, categoria))

    print(Style.RESET_ALL + Fore.GREEN + "\t----------------------------------")
    print(Back.GREEN + Fore.BLACK + "Producto creado correctamente".center(50," "))
    print(Fore.GREEN + "\t----------------------------------")

    conexion.commit()
    conexion.close()


#----------------------------------------------------------------
def mostrar_productos():
    #Función para mostrar todos los productos
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos")
    resultados = cursor.fetchall()

    print("")
    print(Fore.MAGENTA + "\t----------------------------------")
    print(Style.BRIGHT + Fore.MAGENTA + "TODOS LOS PRODUCTOS".center(50," "))
    print(Fore.MAGENTA + "\t----------------------------------")

    if len(resultados) == 0:
        print(Fore.RED + "No hay productos registrados.")
        return
    
    for registro in resultados:
        printProducto(registro)
    conexion.close()


#----------------------------------------------------------------
def actualizar_producto():
    #Función para modificar productos, eligiendo que dato modificar 
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    print(Fore.MAGENTA + "\t----------------------------------")
    print(Style.BRIGHT + Fore.MAGENTA + "MODIFICAR PRODUCTO".center(50," "))
    print(Fore.MAGENTA + "\t----------------------------------")

    id = int(input(Style.DIM + Fore.CYAN + "Ingrese el ID del producto: "))
    cursor.execute("SELECT * FROM Productos WHERE ID = ?",(id,))
    resultado = cursor.fetchone()

    if resultado is None:
        print(Fore.RED + "El producto no existe.")
        return
    
    print("")
    print(Fore.MAGENTA + "\t----------------------------------")
    print(Style.DIM + Fore.CYAN + "Producto encontrado:".center(50," "))
    opcion = -1

    while opcion != 0:

        printProducto(resultado)

        print(Fore.MAGENTA + "Que desea modificar?")
        print(Fore.GREEN + "1. Nombre")
        print(Fore.GREEN + "2. Descripción")
        print(Fore.GREEN + "3. Cantidad")
        print(Fore.GREEN + "4. Precio")
        print(Fore.GREEN + "5. Categoría")
        print(Fore.RED + "0. Salir")

        print("")
        opcion = int(input(Fore.CYAN + "Opción: "))
        print("")


        if opcion == 0:
            break

        elif opcion == 1:
            nuevo_nombre = input(Style.DIM + Fore.CYAN + "Ingrese el nuevo nombre: ")
            cursor.execute("UPDATE Productos SET nombre = ? WHERE ID = ?",(nuevo_nombre, resultado[0]))

        elif opcion == 2:
            nueva_descripcion = input(Style.DIM + Fore.CYAN + "Ingrese la nueva descripción: ")
            cursor.execute("UPDATE Productos SET descripcion = ? WHERE ID = ?",(nueva_descripcion, resultado[0]))

        elif opcion == 3:
            nueva_cantidad = int(input(Style.DIM + Fore.CYAN + "Ingrese la nueva cantidad: "))
            cursor.execute("UPDATE Productos SET cantidad = ? WHERE ID = ?",(nueva_cantidad, resultado[0]))

        elif opcion == 4:
            nuevo_precio = float(input(Style.DIM + Fore.CYAN + "Ingrese el nuevo precio: "))
            cursor.execute("UPDATE Productos SET precio = ? WHERE ID = ?",(nuevo_precio, resultado[0]))

        elif opcion == 5:
            nueva_categoria = input(Style.DIM + Fore.CYAN + "Ingrese la nueva categoría: ")
            cursor.execute("UPDATE Productos SET categoria = ? WHERE ID = ?",(nueva_categoria, resultado[0]))
        

        print("")
        print(Back.GREEN + "Producto actualizado correctamente")
        print("")

        cursor.execute("SELECT * FROM Productos WHERE ID = ?",(id,))
        resultado = cursor.fetchone()

    conexion.commit()
    conexion.close()


#----------------------------------------------------------------
def eliminar_producto():
    #Función para eliminar productos
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    print(Fore.MAGENTA + "\t----------------------------------")
    print(Style.BRIGHT + Fore.MAGENTA + "ELIMINAR PRODUCTO".center(50," "))
    print(Fore.MAGENTA + "\t----------------------------------")

    id = int(input(Style.DIM + Fore.CYAN + "Ingrese el ID del producto a eliminar: "))
    cursor.execute("SELECT * FROM Productos WHERE ID = ?",(id,))
    resultado = cursor.fetchone()

    if resultado is None:
        print(Fore.RED + "El producto no existe.")
        return
    
    else:
        printProducto(resultado)
        decision = int(input(Style.BRIGHT + Fore.MAGENTA + "¿Está seguro de eliminar el producto? (1.SI - 2.NO): "))

        if decision == 1:
            cursor.execute("DELETE FROM Productos WHERE ID = ?",(id,))
            conexion.commit()
            print(Back.RED + Fore.WHITE + "Producto eliminado correctamente.")

        elif decision == 2:
            print(Back.RED + Fore.WHITE + "Operación cancelada.")

        else:
            print(Fore.RED + "Opción no válida.") 
            
        conexion.close()


#----------------------------------------------------------------
def buscar_producto_por_id():
    #Función para buscar productos por ID
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    print(Fore.MAGENTA + "\t----------------------------------")
    print(Style.BRIGHT + Fore.MAGENTA + "BUSCAR PRODUCTO POR ID".center(50," "))
    print(Fore.MAGENTA + "\t----------------------------------")

    id = int(input(Style.DIM + Fore.CYAN + "Ingrese el ID del producto a buscar: "))
    cursor.execute("SELECT * FROM Productos WHERE ID = ?",(id,))
    resultado = cursor.fetchone()

    if resultado is None:
        print(Fore.RED + "El producto no existe.")
        return
    
    else:
        printProducto(resultado)
    
    conexion.close()


#----------------------------------------------------------------
def buscar_productos_por_nombre():
    #Función para buscar productos por nombre
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    print(Fore.MAGENTA + "\t----------------------------------")
    print(Style.BRIGHT + Fore.MAGENTA + "BUSQUEDA DE PRODUCTOS POR NOMBRE".center(50," "))
    print(Fore.MAGENTA + "\t----------------------------------")

    nombre = input(Style.DIM + Fore.CYAN + "Ingrese el nombre del producto a buscar: ")
    cursor.execute("SELECT * FROM Productos WHERE nombre LIKE?" , (f"%{nombre}%",))
    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print(Style.NORMAL + Fore.RED + f"No hay productos con el nombre: {nombre}.")
        return
    
    else:
        print("")
        print(Fore.MAGENTA + "\t----------------------------------")
        print(Fore.MAGENTA + f"PRODUCTOS CON EL NOMBRE: {nombre}".center(50," "))
        print(Fore.MAGENTA + "\t----------------------------------")
        print("")

        for registro in resultados:
            printProducto(registro)
        
    conexion.close()


#----------------------------------------------------------------
def buscar_productos_por_categoria():
    #Función para buscar productos por categoría
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    print(Fore.MAGENTA + "\t----------------------------------")
    print(Style.BRIGHT + Fore.MAGENTA + "BUSQUEDA DE PRODUCTOS POR CATEGORIA".center(50," "))
    print(Fore.MAGENTA + "\t----------------------------------")

    categoria = input(Style.DIM + Fore.CYAN + "Ingrese la categoría del producto a buscar: ")
    cursor.execute("SELECT * FROM Productos WHERE categoria =?" , (categoria,))
    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print(Style.NORMAL + Fore.RED + f"No hay productos con la categoría: {categoria}.")
        return
    
    else:
        print("")
        print(Fore.MAGENTA + "\t----------------------------------")
        print(Fore.MAGENTA + f"PRODUCTOS CON LA CATEGORIA: {categoria}".center(50," "))
        print(Fore.MAGENTA + "\t----------------------------------")
        print("")

        for registro in resultados:
            printProducto(registro)
        
    conexion.close()


#----------------------------------------------------------------
def reporte_bajo_stock():
    #Función para generar reporte de productos bajo stock
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    print(Fore.MAGENTA + "\t----------------------------------")
    print(Style.BRIGHT + Fore.MAGENTA + "REPORTE PRODUCTOS BAJO STOCK".center(50," "))
    print(Fore.MAGENTA + "\t----------------------------------")

    limite = int(input(Style.DIM + Fore.CYAN + "Ingrese el límite de stock a buscar:"))
    cursor.execute("SELECT * FROM Productos WHERE cantidad <= ?",(limite,))
    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print(Style.NORMAL + Fore.RED + f"No hay productos por debajo del límite de {limite} en stock.")
        return
    
    else:
        print("")
        print(Fore.MAGENTA + "\t----------------------------------")
        print(Fore.MAGENTA + "PRODUCTOS BAJO STOCK".center(50," "))
        print(Fore.MAGENTA + "\t----------------------------------")
        print("")

        for registro in resultados:
            printProducto(registro)
        
    conexion.close()




crear_tabla_productos()

opcion = menu_principal()

while opcion != 0:
    if opcion == 1:
        registrar_producto()
    elif opcion == 2:
        mostrar_productos()
    elif opcion == 3:
        actualizar_producto()
    elif opcion == 4:
        eliminar_producto()
    elif opcion == 5:
        buscar_producto_por_id()
    elif opcion == 6:
        buscar_productos_por_nombre()
    elif opcion == 7:
        buscar_productos_por_categoria()
    elif opcion == 8:
        reporte_bajo_stock()
    opcion = menu_principal()


if opcion == 0:
    print("")
    print(Fore.RED + "=====================".center(50," "))
    print(Fore.RED + "PROGRAMA FINALIZADO".center(50," "))
    print(Fore.RED + "=====================".center(50," "))
    print("")