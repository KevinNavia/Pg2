#practica 1 
'''
En esta práctica se implementa una calculadora en Python que permite realizar
 operaciones aritméticas básicas como suma, resta, multiplicación y división.
 
 Del mismo modo, se implementa una calculadora de factorial que aplica principios
 de herencia y polimorfismo.

'''
1. CLONAR EL REPOSITORIO 
''' bash
git clone https://github.com/KevinNavia/Pg2.git
cd pg2
'''
2.CREAR UN ENTORNO VIRTUAL
'''bash
python -m venv env
 ```
 
3. Activar el entorno virtual:
 
 - En Windows:
 
 ```bash
 .\env\Scripts\activate
 ```
 
 - En Linux o Mac:
 
 ```bash
 source env/bin/activate
 ```
 
 4. Ejecutar el script:
 
 ```bash
 python calculadora_poo.py
 python factorial_poo.py
 python main.py
 ```
 
 5. Desactivar el entorno virtual:
 
 ```bash
 deactivate
 ```
 
 ## Implementacion Calculadora Estandar
 
 Este módulo implementa una calculadora estándar que permite realizar operaciones
 aritméticas básicas como suma, resta, multiplicación y división. El modo de
 funcionamiento es el siguiente:
 
 ```python
 class calculadora:
    def __init__(self):
        self.operacion = ""
        self.resultado = 0

    def sumar(self, a, b):
        self.operacion = "suma"
        self.resultado = a + b
        return self.mostrar_resultado(a, b)
    def restar(self, a, b):
        self.operacion = "resta"
        self.resultado = a - b
        return self.mostrar_resultado(a, b)
    def multiplicar(self, a, b):
        self.operacion = "multiplicacion"
        self.resultado = a * b
        return self.mostrar_resultado(a, b)
    def dividir(self, a, b):
        self.operacion = "division"
        self.resultado = a / b
        return self.mostrar_resultado(a, b)
    def mostrar_resultado(self, a, b):
        return f"tu resultado de la operacion {self.operacion} entre {a} y {b} es:  {self.resultado}"
 ```
 
 ## Implementacion Calculadora Factorial
 
 Este módulo implementa una calculadora factorial que hereda de la clase
 Calculadora. Permite calcular el factorial de un número entero positivo. El modo
 de funcionamiento es el siguiente:
 
 ```python
from CalculadoraPoo import calculadora
class calculadoraFactorial(calculadora):
    def __init__(self, numero):
        self.numero = numero
        super().__init__()
        self.resultado = 1
        
    def factorial(self):
        cont = 1
        while self.numero >= cont :
            self.resultado *= cont
            cont += 1
        return self.mostrar_resultado()
    
    def mostrar_resultado(self):
        return f"el resultado del factorial de {self.numero} es: {self.resultado}"
 ```
## Este metodo implementa una calculadora Factorial 
En este modulo creamos la base de una factorial para hacer la Subsigientes pruebas 
Su modo de funcionamiento es el siguiente:
```python
n=input("introducir el numero :   ")
fac=1
cont=1
while n>0:
    fac=fac*cont
    cont += 1
print("El factorial es",cont)
```
## En este modulo implementamos un Main 
En este modulo implementamos todos los modulos aprendidos en el cual ejecutamos todos en uno pero con
progamacion Dirigida a Objetos , la cual imprime el resultado de todos los modulos.
Su funcionamiento es el siguiente :
```python
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
```
^^^^