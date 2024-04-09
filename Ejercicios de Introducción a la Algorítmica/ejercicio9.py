def obtener_flotante(mensaje):
    #Solicita al usuario un número flotante y maneja errores de entrada.
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("La entrada no es un número válido. Por favor, intenta de nuevo.")

def calcular_media_aritmetica():
    #Calcula la media aritmética de tres números proporcionados por el usuario.
    print("Calculando la media aritmética de tres números.")
    a = obtener_flotante("Introduce el primer número: ")
    b = obtener_flotante("Introduce el segundo número: ")
    c = obtener_flotante("Introduce el tercer número: ")
    media = (a + b + c) / 3
    print(f"La media aritmética es: {media}")

def calcular_media_ponderada():
    #Calcula la media ponderada de tres números y sus pesos, proporcionados por el usuario.
    print("\nCalculando la media ponderada de tres números.")
    a = obtener_flotante("Introduce el primer número: ")
    b = obtener_flotante("Introduce el segundo número: ")
    c = obtener_flotante("Introduce el tercer número: ")
    w1 = obtener_flotante("Introduce el peso para el primer número: ")
    w2 = obtener_flotante("Introduce el peso para el segundo número: ")
    w3 = obtener_flotante("Introduce el peso para el tercer número: ")
    media_ponderada = ((a * w1) + (b * w2) + (c * w3)) / (w1 + w2 + w3)
    print(f"La media ponderada es: {media_ponderada}")

# Ejecución de las funciones para calcular la media aritmética y la media ponderada.
calcular_media_aritmetica()
calcular_media_ponderada()
