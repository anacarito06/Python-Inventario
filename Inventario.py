from itertools import product
from unittest.mock import InvalidSpecError


class producto:

    def __init__(self,nombre,cantidad,precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

def mostrar_menu():
    print("Sistema de inventario")
    print("1. Agregar Producto")
    print("2. Mostrar Productos")
    print("3. Buscar Producto")
    print("4. Actualizar Cantidad")
    print("5. Eliminar Producto")
    print("6. Salir")

Inventario = []

while True:
    mostrar_menu()
    opcion = input("Elige una opcion:  ")

    if opcion == "6":
        print("Saliendo del programa")
        break

    if opcion == "1":
        nombre = input("Ingresa el nombre del producto ")
        try:
            cantidad = int(input("Ingrese la cantidad "))
            precio = float(input("Ingrese el precio "))
            producto = producto(nombre,cantidad,precio)
            Inventario.append(producto)
            print("producto agregado ")
        except ValueError:
            print("Error: Entrada no valida")

    elif opcion == "2":
        for p in Inventario:
            print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")

    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a buscar ")
        encontrado = False
        for p in Inventario:
            if p.nombre == nombre:
                print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
                encontrado = True
                break
            if not encontrado:
                print("Producto no encontrado ")

    elif opcion == "4":
        nombre = input("Ingrese el nombre del producto a actualizar")
        try:
            nueva_cantidad = int(input("Ingrese la nueva cantidad"))
            for p in Inventario:
                if p.nombre == nombre:
                    p.cantidad = cantidad
                    print("Cantidad actualizada")
                    break
        except ValueError:
            print("Error: entrada no valida")
            
    elif opcion == "5":
        nombre = input("Ingrese el producto a eliminar: ")
        for p in Inventario:
            if p.producto == producto:
                Inventario.remove(p)
                print("Producto eliminado")
                break
    else:
        print("Opcion no valido. Intentalo de nuevo")

