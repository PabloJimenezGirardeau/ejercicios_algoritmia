def obtener_valor_positivo(mensaje, es_entero=False):
    #Solicita al usuario un valor numérico válido
    while True:
        try:
            valor = input(mensaje)
            valor = int(valor) if es_entero else float(valor)
            if valor > 0:
                return valor
            else:
                print("Por favor, introduce un valor positivo.")
        except ValueError:
            print("La entrada no es válida. Por favor, introduce un número.")

def calcular_pago_horas_extra(salario_mensual, horas_extra):
    """
    Calcula el pago por horas extra basándose en el salario mensual y la cantidad de horas extra trabajadas.
    
    Parámetros:
    salario_mensual (float): El salario bruto mensual del empleado.
    horas_extra (int): Total de horas extra trabajadas en el mes.
    
    Retorna:
    float: Total a pagar por las horas extra.
    """
    
    # Calcular la tarifa por hora normal.
    horas_normales_mes = 35 * 4  # 35 horas por semana, 4 semanas al mes
    tarifa_hora_normal = salario_mensual / horas_normales_mes
    
    # Inicializar el total a pagar por horas extra.
    pago_horas_extra = 0
    
    # Determinar horas a 125% y 150%
    horas_a_125 = min(horas_extra, 8)  # Las primeras 8 horas extra se pagan a 125%
    horas_a_150 = max(horas_extra - 8, 0)  # Las horas extra después de las primeras 8 se pagan a 150%
    
    # Añadir al total el pago por las horas a 125%.
    pago_horas_extra += horas_a_125 * tarifa_hora_normal * 1.25
    
    # Añadir al total el pago por las horas a 150%.
    pago_horas_extra += horas_a_150 * tarifa_hora_normal * 1.50
    
    return pago_horas_extra

# Ejemplo de uso con control de excepciones y validación de entrada:
salario_mensual = obtener_valor_positivo("Introduce el salario mensual bruto del empleado: ")
horas_extra = obtener_valor_positivo("Introduce el total de horas extra trabajadas en el mes: ", es_entero=True)
total_pago_horas_extra = calcular_pago_horas_extra(salario_mensual, horas_extra)
print(f"Total a pagar por horas extra: {total_pago_horas_extra}")
