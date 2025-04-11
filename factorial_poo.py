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
        
