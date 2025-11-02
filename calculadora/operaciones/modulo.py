def modulo (a, b):
    """
    Esta función devuelve el resto de una división.
    
    Args:
        a (int/float): Primer número
        b (int/float): Segundo número
    
    Returns:
        int/float: El resto de a y b
    """
    if b == 0:
        return "No se puede dividir por cero."
    else: 
        return a%b