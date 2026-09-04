import time

class CuentaBackend:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.saldo = saldo_inicial

    def obtener_balance(self) -> str:
        return f"[INFO] Usuario: {self.titular} | Saldo: ${self.saldo:.2f}"

    def depositar(self, monto: float) -> str:
        if monto <= 0:
            return "[ERROR] El monto a depositar debe ser mayor a cero."
        self.saldo += monto
        return f"[SUCCESS] Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}"

    def retirar(self, monto: float) -> str:
        if monto <= 0:
            return "[ERROR] El monto debe ser mayor a cero."
        if monto > self.saldo:
            return "[ERROR] Fondos insuficientes."
        
        # Ahora la resta solo se hace si pasa las validaciones de arriba
        self.saldo -= monto
        return f"[SUCCESS] Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}"


# --- MENÚ INTERACTIVO PARA LA CONSOLA ---
print("--- BIENVENIDO AL SISTEMA BANCARIO ---")
nombre = input("Ingrese su nombre para crear la cuenta: ")
while True:
    try:
        saldo_inicial = float(input("¿Con cuánto saldo desea abrir su cuenta?: $"))
        if saldo_inicial < 0:
            print("[ERROR] El saldo inicial no puede ser negativo.")
            continue
        break
    except ValueError:
        print("[ERROR] Por favor, ingrese un número válido.")

# Creamos la cuenta del usuario
cuenta_usuario = CuentaBackend(nombre, saldo_inicial)

while True:
    print("\n" + "="*30)
    print(f"  CAJERO AUTOMÁTICO - {cuenta_usuario.titular.upper()}")
    print("="*30)
    print("1. Consultar Saldo")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero")
    print("4. Salir")
    print("="*30)
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        print("\nConsultando saldo...")
        time.sleep(1)
        print(cuenta_usuario.obtener_balance())
        
    elif opcion == "2":
        try:
            monto = float(input("\nIngrese el monto a depositar: $"))
            print("Procesando depósito...")
            time.sleep(1)
            print(cuenta_usuario.depositar(monto))
        except ValueError:
            print("[ERROR] Ingrese un número válido.")
            
    elif opcion == "3":
        try:
            monto = float(input("\nIngrese el monto a retirar: $"))
            print("Verificando fondos...")
            time.sleep(1)
            print(cuenta_usuario.retirar(monto))
        except ValueError:
            print("[ERROR] Ingrese un número válido.")
            
    elif opcion == "4":
        print("\nMuchas gracias por usar nuestro sistema. ¡Hasta luego!")
        time.sleep(1)
        break
        
    else:
        print("[ERROR] Opción no válida. Intente de nuevo.")

