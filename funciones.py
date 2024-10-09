import math

# Función incorrecta para calcular el tamaño de la muestra
def calcular_muestra_incorrecta(N, Z, p, e):
    """
    Función incorrecta que tiene errores en los cálculos del tamaño de muestra.
    N: Tamaño de la población
    Z: Valor Z correspondiente al nivel de confianza
    p: Proporción esperada de la población
    e: Margen de error
    """
    print("Cálculo incorrecto del tamaño de muestra")
    
    # Fórmula errada (mal uso del término N y confusión en la ecuación)
    n0 = (Z**2 * p * (1 - p)) / (e**2 * N)
    n = n0 / (1 + ((n0 - 1) / (N + 50)))  # Error en la fórmula
    
    return math.ceil(n)  # Redondeo hacia arriba

# Función correcta para calcular el tamaño de la muestra
def calcular_muestra_correcta(N, Z, p, e):
    """
    Calcula correctamente el tamaño de muestra usando la fórmula de Cochran ajustada para poblaciones finitas.
    N: Tamaño de la población
    Z: Valor Z correspondiente al nivel de confianza
    p: Proporción esperada de la población
    e: Margen de error
    """
    print("Cálculo correcto del tamaño de muestra")
    
    # Cálculo inicial (muestra infinita)
    n0 = (Z**2 * p * (1 - p)) / (e**2)
    
    # Ajuste para población finita
    n = n0 / (1 + ((n0 - 1) / N))
    
    return math.ceil(n)  # Redondeo hacia arriba

# Función para calcular la población
def calcular_poblacion(tasa_crecimiento_anual, poblacion_inicial, anos):
    """
    Calcula el tamaño de la población después de un número de años dado un crecimiento exponencial.
    tasa_crecimiento_anual: Tasa de crecimiento anual (en porcentaje)
    poblacion_inicial: Población inicial
    anos: Número de años de crecimiento
    """
    print("Cálculo de la población")
    
    # Conversión de porcentaje a decimal
    tasa_crecimiento_anual = tasa_crecimiento_anual / 100
    
    # Cálculo de la población futura usando la fórmula de crecimiento exponencial
    poblacion_futura = poblacion_inicial * ((1 + tasa_crecimiento_anual) ** anos)
    
    return math.ceil(poblacion_futura)  # Redondeo hacia arriba


# Ejemplo de uso
if __name__ == "__main__":
    # Parámetros comunes
    Z = 1.96  # 95% nivel de confianza
    p = 0.5   # Proporción esperada
    e = 0.05  # Margen de error (5%)
    
    # Solicitar el tamaño de la población al usuario
    N = int(input("Introduce el tamaño de la población: "))
    
    # Cálculo incorrecto del tamaño de muestra
    muestra_incorrecta = calcular_muestra_incorrecta(N, Z, p, e)
    print(f"Tamaño de muestra incorrecta: {muestra_incorrecta}")
    
    # Cálculo correcto del tamaño de muestra
    muestra_correcta = calcular_muestra_correcta(N, Z, p, e)
    print(f"Tamaño de muestra correcta: {muestra_correcta}")
    
    # Cálculo de la población con un 2% de tasa de crecimiento anual durante 10 años
    poblacion_futura = calcular_poblacion(2, N, 10)
    print(f"Tamaño de la población en 10 años: {poblacion_futura}")