def division (a, b):
    """
    Esta función divide dos números y retorna el resultado.
    
    Args:
        a (int/float): Primer número
        b (int/float): Segundo número
    
    Returns:
        int/float: La división de a y b.
    """
    if b == 0:
        return "No se puede dividir por cero."
    else:
        return a/b