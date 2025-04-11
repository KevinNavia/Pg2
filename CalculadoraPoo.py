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