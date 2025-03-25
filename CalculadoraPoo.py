class calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.operacion = ""
        self.resultado = 0

    def sumar(self):
        self.operacion = "suma"
        self.resultado = self.a + self.b
        return self.mostrar_resultado()
    def restar(self):
        self.operacion = "resta"
        self.resultado = self.a - self.b
        return self.mostrar_resultado()
    def multiplicar(self):
        self.operacion = "multiplicacion"
        self.resultado = self.a * self.b
        return self.mostrar_resultado()
    def dividir(self):
        self.operacion = "division"
        self.resultado = self.a / self.b
        return self.mostrar_resultado()
    def mostrar_resultado(self):
        return f"tu resultado de la operacion {self.operacion} es:  {self.resultado}"

calculadora = calculadora(5, 2)
print(calculadora.sumar())
print(calculadora.restar())
print(calculadora.multiplicar())
print(calculadora.dividir())