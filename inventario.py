import csv

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad):
        if nombre in self.productos:
            print(f"El producto '{nombre}' ya existe en el inventario.")
        else:
            self.productos[nombre] = cantidad
            print(f"Producto '{nombre}' agregado al inventario con cantidad {cantidad}.")

    def actualizar_cantidad(self, nombre, nueva_cantidad):
        if nombre in self.productos:
            self.productos[nombre] = nueva_cantidad
            print(f"Cantidad del producto '{nombre}' actualizada a {nueva_cantidad}.")
        else:
            print(f"El producto '{nombre}' no existe en el inventario.")

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            print(f"Producto '{nombre}' eliminado del inventario.")
        else:
            print(f"El producto '{nombre}' no existe en el inventario.")

    def mostrar_inventario(self):
        print("Inventario:")
        for nombre, cantidad in sorted(self.productos.items()):
            print(f"{nombre}: {cantidad}")

    def guardar_inventario(self, archivo):
        with open(archivo, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Producto', 'Cantidad'])
            for nombre, cantidad in self.productos.items():
                writer.writerow([nombre, cantidad])

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.productos[row['Producto']] = int(row['Cantidad'])
        except FileNotFoundError:
            print("El archivo no existe. Se creará un nuevo inventario.")

# Ejemplo de uso
inventario = Inventario()

# Cargar inventario desde un archivo existente o crear uno nuevo si no existe
inventario.cargar_inventario('inventario.csv')

while True:
    accion = input("¿Qué acción desea realizar?\n"
                   "1. Agregar un producto al inventario\n"
                   "2. Actualizar la cantidad de un producto en el inventario\n"
                   "3. Eliminar un producto del inventario\n"
                   "4. Mostrar inventario ordenado alfabéticamente\n"
                   "5. Guardar inventario en archivo CSV\n"
                   "6. Salir\n")

    if accion == '1':
        nombre = input("Ingrese el nombre del producto a agregar: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        inventario.agregar_producto(nombre, cantidad)
    elif accion == '2':
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        inventario.actualizar_cantidad(nombre, nueva_cantidad)
    elif accion == '3':
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        inventario.eliminar_producto(nombre)
    elif accion == '4':
        inventario.mostrar_inventario()
    elif accion == '5':
        inventario.guardar_inventario('inventario.csv')
    elif accion == '6':
        break
    else:
        print("Acción no válida. Por favor ingrese un número válido.")

print("¡Gracias por usar el sistema de control de inventario!")
