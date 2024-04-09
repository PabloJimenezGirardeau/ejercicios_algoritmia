def obtener_lado(mensaje):
    #Solicita al usuario un valor numérico positivo
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Por favor, introduce un valor positivo.")
        except ValueError:
            print("La entrada no es válida. Por favor, introduce un número.")

def calcular_area_triangulo():
    """
    Calcula el área de un triángulo a partir de la base y la altura proporcionadas por el usuario,
    asegurando que sean valores positivos. Después de calcular el área, plantea una pregunta sobre
    su aplicabilidad a triángulos rectángulos y proporciona la respuesta.
    """
    base = obtener_lado("Introduce la longitud de la base del triángulo (valor positivo): ")
    altura = obtener_lado("Introduce la altura del triángulo (valor positivo): ")
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")

    # Plantea la pregunta y proporciona la respuesta
    print("\n¿Se puede utilizar este algoritmo para un triángulo rectángulo si se dan las medidas de sus dos lados perpendiculares?")
    respuesta = "\n ==> Sí, este algoritmo se puede utilizar perfectamente para calcular el área de un triángulo rectángulo. En un triángulo rectángulo, los dos lados que forman el ángulo recto pueden considerarse como la base y la altura."
    print(respuesta)

# Llamar a la función para calcular el área del triángulo y responder a la pregunta.
calcular_area_triangulo()

