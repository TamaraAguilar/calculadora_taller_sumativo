from operaciones.suma import suma
from operaciones.resta import resta
from operaciones.multiplicacion import multiplicacion
from operaciones.division import division
from operaciones.modulo import modulo
from operaciones.exponente import exponente


def main():
    """
    Función principal que solicita dos números al usuario y realiza operaciones matemáticas 
    (suma, resta, multiplicación, división, potencia, y módulo)
    """

    # Obtener números
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    # Realizar operaciones matemáticas
    print("########################################################")
    print(f"Suma: { suma(a, b)}")
    print(f"Resta: { resta(a, b)}")
    print(f"Multiplicación: { multiplicacion(a, b)}")
    print(f"División: { division(a, b)}")
    print(f"Módulo: { modulo(a, b)}")
    print(f"Exponente: { exponente(a, b)}")

# Llamar a la función principal
if __name__ == "__main__":
    main()
