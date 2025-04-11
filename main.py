
# Importamos la clase
from CalculadoraPoo import calculadora
from factorial_poo import calculadoraFactorial

# Creamos una instancia de la clase
calculadora = calculadora()
print(calculadora.sumar(5, 3))
print(calculadora.restar(5, 3))
print(calculadora.multiplicar(5, 3))
print(calculadora.dividir(5, 3))

factorial = calculadoraFactorial(5)
print(factorial.factorial())
