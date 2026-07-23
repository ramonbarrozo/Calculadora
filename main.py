# Calculadora Simples Projeto Ramon C. P. Barrozo
from Calculadora import Calculadora

print("***Calculadora Simples***")

print("\nEscolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão \n")

calc = Calculadora()
print("Resultado : "+str(calc.operacao()))