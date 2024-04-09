class CUENTA:
    def __init__(self, titular, saldo_inicial=0, limite_descubierto=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.limite_descubierto = limite_descubierto
    
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito realizado: {monto}. Saldo actual: {self.saldo}")
        else:
            print("El monto a depositar debe ser positivo.")
    
    def retirar(self, monto):
        if monto <= self.saldo + self.limite_descubierto:
            self.saldo -= monto
            print(f"Retiro realizado: {monto}. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes para completar el retiro.")

def obtener_valor_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("Por favor, introduce un valor positivo.")
        except ValueError:
            print("La entrada no es válida. Por favor, introduce un número.")

def obtener_accion_usuario():
    while True:
        accion = input("¿Deseas depositar o retirar dinero? (depositar/retirar): ").lower()
        if accion in ["depositar", "retirar"]:
            return accion
        else:
            print("Por favor, escribe 'depositar' o 'retirar' para seleccionar tu acción.")

# Creación de la cuenta
titular = input("Introduce el nombre del titular de la cuenta: ")
saldo_inicial = obtener_valor_positivo("Introduce el saldo inicial de la cuenta: ")
limite_descubierto = obtener_valor_positivo("Introduce el límite de descubierto autorizado: ")
cuenta_usuario = CUENTA(titular, saldo_inicial, limite_descubierto)

# Elección de la acción
accion_usuario = obtener_accion_usuario()
monto = obtener_valor_positivo("Introduce el monto: ")

if accion_usuario == "depositar":
    cuenta_usuario.depositar(monto)
elif accion_usuario == "retirar":
    cuenta_usuario.retirar(monto)

# Mostrar el saldo final
print(f"Saldo final en la cuenta de {cuenta_usuario.titular}: {cuenta_usuario.saldo}")

