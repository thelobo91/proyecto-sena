class Producto:
    def __init__(self, nombre, stock):
        self.__nombre = nombre
        self.__stock = stock

    def obtener_info(self):
        return f"Producto: {self.__nombre} | Stock actual: {self.__stock}"

    def aumentar_stock(self, cantidad):
        if cantidad > 0:
            self.__stock += cantidad
        else:
            print("Error: La cantidad debe ser positiva.")

    def disminuir_stock(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.__stock:
                self.__stock -= cantidad
            else:
                print("Error: No hay suficiente stock disponible.")
        else:
            print("Error: La cantidad debe ser positiva.")


# Programa principal
nombre_producto = input("Ingrese el nombre del producto: ")
stock_inicial = int(input("Ingrese el stock inicial: "))

producto1 = Producto(nombre_producto, stock_inicial)

print(producto1.obtener_info())

aumento = int(input("Cantidad para aumentar stock: "))
producto1.aumentar_stock(aumento)

disminucion = int(input("Cantidad para disminuir stock: "))
producto1.disminuir_stock(disminucion)

print("Estado final del inventario:")
print(producto1.obtener_info())
        