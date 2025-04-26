def validar_run(run):
    """Valida que el RUN tenga exactamente 8 dígitos numéricos"""
    return len(run) == 8 and run.isdigit()

def calcular_suma_ponderada(run):
    """Calcula la suma ponderada de los dígitos del RUN"""
    factores = [2, 3, 4, 5, 6, 7, 2, 3]
    suma = 0
    for i in range(8):
        digito = int(run[7 - i])  # Leer de derecha a izquierda
        suma += digito * factores[i]
    return suma

def formatear_dv(dv_crudo):
    """Formatea el dígito verificador según reglas especiales"""
    if dv_crudo == 10:
        return "K"
    elif dv_crudo == 11:
        return 0
    return dv_crudo

def calcular_digito_verificador(run):
    """Función principal de cálculo: recibe el RUN y retorna el DV"""
    if not validar_run(run):
        return None  # Indica error de formato
    
    suma = calcular_suma_ponderada(run)
    resto = suma % 11
    dv_crudo = 11 - resto
    return formatear_dv(dv_crudo)