import math


class Calculadora:
    def __init__(self, valor):
        self.valor = valor

    def calcular_raiz_cuadrada(self):
        if self.valor < 0:
            return "No se puede calcular la raíz cuadrada de un número negativo."
        else:
            return math.sqrt(self.valor)


# Solicitar entrada del usuario
valor = float(input("Ingresa un número para calcular su raíz cuadrada: "))

# Crear instancia de la clase con el valor ingresado
calculadora = Calculadora(valor)

# Calcular la raíz cuadrada
resultado = calculadora.calcular_raiz_cuadrada()

# Mostrar el resultado
print(f"La raíz cuadrada de {valor} es: {resultado}")
