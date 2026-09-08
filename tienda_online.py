import time

class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float, stock: int):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad: int) -> bool:
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False

    def __str__(self) -> str:
        return f"ID: {self.id_producto} | {self.nombre:<18} | Precio: ${self.precio:.2f} | Stock: {self.stock}"


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto: Producto, cantidad: int):
        for item in self.items:
            if item["producto"].id_producto == producto.id_producto:
                item["cantidad"] += cantidad
                return
        self.items.append({"producto": producto, "cantidad": cantidad})

    def calcular_total(self) -> float:
        total = 0.0
        for item in self.items:
            total += item["producto"].precio * item["cantidad"]
        return total

    def mostrar_carrito(self):
        if not self.items:
            print("[CARRITO] Tu carrito está vacío.")
            return
        print("\n--- 🛒 TU CARRITO DE COMPRAS ---")
        for item in self.items:
            p = item["producto"]
            cant = item["cantidad"]
            subtotal = p.precio * cant
            print(f"• {p.nombre:<18} x{cant:<3} | Subtotal: ${subtotal:.2f}")
        print(f"Total acumulado: ${self.calcular_total():.2f}\n")


class Usuario:
    def __init__(self, nombre: str, saldo_inicial: float):
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.carrito = Carrito()

    def __str__(self) -> str:
        return f"Cliente: {self.nombre} | Saldo Disponible: ${self.saldo:.2f}"


class Tienda:
    def __init__(self, nombre_tienda: str):
        self.nombre_tienda = nombre_tienda
        self.inventario = {}

    def registrar_producto(self, producto: Producto):
        self.inventario[producto.id_producto] = producto

    def mostrar_catalogo(self):
        print(f"\n--- 🏪 CATÁLOGO DE {self.nombre_tienda.upper()} ---")
        for producto in self.inventario.values():
            print(producto)
        print("-" * 50)


class Cajero:
    def __init__(self, nombre_cajero: str):
        self.nombre_cajero = nombre_cajero

    def procesar_compra(self, usuario: Usuario) -> bool:
        total = usuario.carrito.calcular_total()
        
        print(f"\n[CAJERO {self.nombre_cajero}] Iniciando proceso de cobro...")
        time.sleep(1.2)
        
        if total == 0:
            print("[MISTAKE] No tienes artículos en el carrito para pagar.")
            return False

        print(f"Total a pagar: ${total:.2f} | Tu saldo: ${usuario.saldo:.2f}")
        time.sleep(1)

        if usuario.saldo >= total:
            usuario.saldo -= total
            
            print("\n==========================================")
            print(f"         FACTURA DIGITAL - {usuario.nombre.upper()}  ")
            print("==========================================")
            time.sleep(0.5)
            for item in usuario.carrito.items:
                p = item["producto"]
                c = item["cantidad"]
                print(f"{p.nombre:<20} x{c:<3}   ${(p.precio * c):.2f}")
                time.sleep(0.3)
            print("------------------------------------------")
            print(f"TOTAL PAGADO:                       ${total:.2f}")
            print(f"NUEVO SALDO:                        ${usuario.saldo:.2f}")
            print("==========================================")
            print(f"[SUCCESS] ¡Compra procesada por {self.nombre_cajero}! Gracias por su compra.\n")
            
            usuario.carrito.items = []
            return True
        else:
            print(f"[MISTAKE] Fondos insuficientes. Te faltan ${(total - usuario.saldo):.2f}")
            return False


# ==========================================
#        SIMULACIÓN DE LA INTERFAZ
# ==========================================

tienda = Tienda("Supermercado Programación")
tienda.registrar_producto(Producto(1, "Leche Entera 1L", 2.50, 20))
tienda.registrar_producto(Producto(2, "Cereal de Chocolate", 4.80, 15))
tienda.registrar_producto(Producto(3, "Papitas Fritas XL", 3.20, 30))
tienda.registrar_producto(Producto(4, "Gaseosa 2L", 1.99, 50))

cajero_turno = Cajero("Carlos")

print("--- BIENVENIDO AL COMERCIO DIGITAL ---")
nombre_cliente = input("Por favor, ingrese su nombre: ")

intentos_saldo = 0
while intentos_saldo < 3:
    try:
        saldo_inicial = float(input(f"Hola {nombre_cliente}, ¿con cuánto dinero virtual entrarás a la tienda?: $"))
        if saldo_inicial < 0:
            print("[ERROR] El saldo no puede ser negativo.")
            intentos_saldo += 1
            print(f"Te quedan {3 - intentos_saldo} intentos.")
            continue
        break
    except ValueError:
        intentos_saldo += 1
        print(f"[ERROR] Entrada inválida. Escribe un número válido. Te quedan {3 - intentos_saldo} intentos.")
        
if intentos_saldo == 3:
    print("\n[SISTEMA DE SEGURIDAD] Demasiados intentos fallidos. Cerrando conexión...")
    time.sleep(2)
    exit()

usuario_activo = Usuario(nombre_cliente, saldo_inicial)
print("\n[SISTEMA] Cargando interfaz de usuario...")
time.sleep(1.5)

while True:
    print("\n" + "="*40)
    print(f"      {tienda.nombre_tienda.upper()} ")
    print("==========================================")
    print("1. Ver catálogo de productos")
    print("2. Agregar producto al carrito")
    print("3. Ver carrito de compras")
    print("4. Ir a la Caja (Pagar)")
    print("5. Salir del supermercado digital")
    print("==========================================")
    
    opcion = input("Seleccione una opción (1-5): ")
    
    if opcion == "1":
        print("\n[PROCESANDO] Abriendo catálogo...")
        time.sleep(0.8)
        tienda.mostrar_catalogo()
        
    elif opcion == "2":
        tienda.mostrar_catalogo()
        
        try:
            id_elegido = int(input("Ingrese el ID del producto que desea: "))
        except ValueError:
            print("[ERROR] El ID debe ser un número entero.")
            continue
            
        if id_elegido not in tienda.inventario:
            print("[ERROR] Ese ID de producto no existe en nuestra tienda.")
            continue
            
        producto_seleccionado = tienda.inventario[id_elegido]
        
        try:
            cantidad_deseada = int(input(f"¿Cuántas unidades de '{producto_seleccionado.nombre}' quiere?: "))
            if cantidad_deseada <= 0:
                print("[ERROR] La cantidad debe ser mayor a cero.")
                continue
        except ValueError:
            print("[ERROR] La cantidad debe ser un número entero.")
            continue
            
        print("\n[PROCESANDO] Verificando existencias en bodega...")
        time.sleep(1)
        
        if producto_seleccionado.reducir_stock(cantidad_deseada):
            usuario_activo.carrito.agregar_producto(producto_seleccionado, cantidad_deseada)
            print(f"[SUCCESS] Agregado: {cantidad_deseada}x {producto_seleccionado.nombre} al carrito.")
        else:
            print(f"[MISTAKE] No hay suficiente stock. Disponibles actualmente: {producto_seleccionado.stock}")
            
    elif opcion == "3":
        print("\n[PROCESANDO] Abriendo su carrito...")
        time.sleep(0.8)
        usuario_activo.carrito.mostrar_carrito()
        print(usuario_activo)
        
    elif opcion == "4":
        cajero_turno.procesar_compra(usuario_activo)
        
    elif opcion == "5":
        print(f"\n[SISTEMA] Gracias por visitar {tienda.nombre_tienda}. Saliendo...")
        time.sleep(1.5)
        break
        
    else:
        print("[ERROR] Opción no válida. Seleccione un número del 1 al 5.")
        time.sleep(1)
  
   
