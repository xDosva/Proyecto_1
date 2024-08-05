
# Crear una lista vacía para el inventario
inventario = []

print("Bienvenido a Accesorios Jisoo empresa del Norte S.A")

# Solicitar al usuario que ingrese el nombre, la cantidad y el precio unitario del primer producto
nombre_producto = input("Ingrese el nombre del producto: ")
cantidad_producto = int(input(f"Ingrese la cantidad de unidades de {nombre_producto}: "))
precio_unitario = float(input(f"Ingrese el precio unitario de {nombre_producto}: "))


# Agregar el primer producto al inventario como una lista [nombre, cantidad, precio_unitario]
inventario.append([nombre_producto, cantidad_producto, precio_unitario])

# Mostrar el inventario actual con el primer producto
print("Inventario:")
for producto in inventario:
    print(f"{producto[0]}: {producto[1]} unidades - Precio unitario: Q{producto[2]}")

# Permitir al usuario agregar más productos al inventario
while True:
    producto_nuevo = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if producto_nuevo.lower() == 'fin':
        break
    cantidad_nueva = int(input("Ingrese la cantidad de unidades: "))
    precio_nuevo = float(input("Ingrese el precio unitario: "))
    
    # Verificar si el producto ya está en el inventario
    encontrado = False
    for producto in inventario:
        if producto[0] == producto_nuevo:
            producto[1] += cantidad_nueva
            encontrado = True
            break

    # Si el producto no estaba en el inventario, agregarlo como una lista [nombre, cantidad, precio_unitario]
    if not encontrado:
        inventario.append([producto_nuevo, cantidad_nueva, precio_nuevo])

# Mostrar el inventario actualizado 
print("\nInventario actualizado:")
for producto in inventario:
    print(f"{producto[0]}: {producto[1]} unidades - Precio unitario: Q{producto[2]}")

# Permitir al usuario vender 
while True:
    producto_vender = input("Ingrese el nombre del producto a vender (o 'fin' para terminar): ")
    if producto_vender.lower() == 'fin':
        break
    
    # Buscar el producto en el inventario
    encontrado = False
    for producto in inventario:
        if producto[0] == producto_vender:
            cantidad_vender = int(input("Ingrese la cantidad de unidades a vender: "))
            
            # Verificar si hay suficientes unidades 
            if cantidad_vender <= producto[1]:
                producto[1] -= cantidad_vender  # Actualizar la cantidad en inventario después de la venta
                print(f"Venta exitosa: {cantidad_vender} unidades de {producto_vender} vendidas.")
                encontrado = True
            else:
                print("No hay suficientes unidades")
            break

    # Si el producto no está en el inventario
    if not encontrado:
        print("El producto no está en inventario.")

# Mostrar el inventario actualizado después de las ventas
print("\nInventario actualizado")
for producto in inventario:
    print(f"{producto[0]}: {producto[1]} unidades - Precio unitario: Q{producto[2]}")

