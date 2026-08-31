import time

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial 
        
    def mostrar_balance(self):
        return f"Usuario: {self.titular} | Saldo disponible: ${self.saldo} \n"
        
    def depositar(self, monto):
        print(f"📡Conectando al servidor... procesando depósito de ${monto}")
        time.sleep(2)
        self.saldo = self.saldo + monto
        return "✅ Depósito exitoso y reflejado en el sistema \n"

    def retirar(self, monto):
        print(f"📡Conectando al servidor... Procesando retiro de ${monto}")
        time.sleep(2)
        if monto > self.saldo:
            return "❌Error fondos insuficientes en la cuenta... \n"
           
        else:
            self.saldo = self.saldo - monto
            return f"✅Retiro exitoso, Se retiro ${monto}"        
        
cuenta_juan = CuentaBancaria("juan_backend",  500)

print(cuenta_juan.mostrar_balance())
print(cuenta_juan.depositar(300))
print(cuenta_juan.mostrar_balance())

print(cuenta_juan.retirar(1000))
print(cuenta_juan.retirar(300))
print(cuenta_juan.mostrar_balance())
        
   
