# 🚀 Mis Sistemas de Programación Orientada a Objetos (POO)

## 🛒 1. Simulador de Tienda Online (`tienda_online.py`)
Un sistema completo y robusto de **224 líneas** que emula el flujo interactivo de un comercio electrónico a través de una interfaz de consola, conectando de forma lógica múltiples objetos y controles de flujo.

### 🧩 Arquitectura de Clases y Métodos:
* **Clase Producto:** Modela los artículos con código único (`id_producto`), nombre, precio y stock. Cuenta con el método `reducir_stock` para descontar artículos vendidos y formato estético mediante `__str__`.
* **Clase Carrito:** Almacena temporalmente los productos seleccionados y sus cantidades. Incluye métodos para `agregar_producto`, `calcular_total` de la compra y `mostrar_carrito` con subtotales por artículo.
* **Clase Usuario:** Administra el perfil del comprador con su nombre, saldo inicial disponible y la vinculación de su propia instancia de `Carrito`.
* **Clase Tienda:** Centraliza el catálogo del negocio mediante un diccionario de inventario. Posee métodos para `registrar_producto` y `mostrar_catalogo` formateando el nombre del comercio en mayúsculas (`.upper()`).
* **Clase Cajero:** Gestiona la fase de pago. Valida si el carrito tiene elementos, genera una **Factura Digital** detallada, descuenta el saldo al usuario, vacía el carrito tras el éxito y calcula cuánto dinero le falta al cliente si sus fondos son insuficientes.

### 🛡️ Sistemas de Control y Seguridad Implementados:
* **Validación contra Datos Inválidos:** Uso estratégico de bloques `intentar/excepto` (Try/Except) para interceptar `Error de valor` (ValueError) y evitar que el programa se rompa si el usuario introduce texto en opciones numéricas.
* **Control de Saldo Inicial:** Bucle de seguridad limitado a un máximo de **3 intentos** para ingresar el dinero virtual; si se agotan los intentos o se introduce un saldo negativo, el sistema bloquea el acceso por seguridad.
* **Gestión de Stock en Tiempo Real:** El menú interactivo verifica dinámicamente si la tienda cuenta con existencias suficientes en bodega antes de autorizar la adición de un artículo al carrito.

---

## 🏦 2. Simulador de Cuenta Bancaria (`main.py`)
Un programa interactivo previo que recrea las operaciones esenciales de una banca personal, aplicando encapsulamiento lógico para depósitos, retiros y validaciones de seguridad de fondos.

---

## 🛠️ Tecnologías y Entorno de Desarrollo
* **Lenguaje:** Python 3 (Estructurado en entorno con palabras clave adaptadas al Español).
* **Entorno de Trabajo:** IDE Móvil (Desarrollo nativo y estructuración 100% táctil).
