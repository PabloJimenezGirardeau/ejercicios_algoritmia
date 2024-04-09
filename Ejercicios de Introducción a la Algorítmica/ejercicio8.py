# Función para calcular el precio de un producto con IVA incluido.
# Recibe dos argumentos: precio_sin_iva (float) y porcentaje_iva (float).
# Devuelve el precio final con el IVA aplicado.
def obtener_valores(mensaje):
    #Solicita al usuario un valor numérico válido
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor, introduce un valor positivo.")
            else:
                return valor
        except ValueError:
            print("La entrada no es válida. Por favor, introduce un número.")

def calcular_precio_con_iva():
    print("Cálculo del precio con IVA incluido:")
    precio_sin_iva = obtener_valores("Introduce el precio sin IVA: ")
    porcentaje_iva = obtener_valores("Introduce el porcentaje de IVA: ")
    precio_con_iva = precio_sin_iva + (precio_sin_iva * porcentaje_iva / 100)
    print(f"El precio con IVA incluido es: {precio_con_iva}")

def calcular_intereses_generados():
    print("\nCálculo de intereses generados por una inversión:")
    capital_inicial = obtener_valores("Introduce el capital invertido: ")
    tasa_interes_anual = obtener_valores("Introduce la tasa de interés anual (%): ")
    tiempo_meses = obtener_valores("Introduce el tiempo de la inversión en meses: ")
    intereses = capital_inicial * tasa_interes_anual * (tiempo_meses / 12) / 100
    print(f"Los intereses generados por la inversión son: {intereses}")

# Llamar a las funciones
calcular_precio_con_iva()
calcular_intereses_generados()
