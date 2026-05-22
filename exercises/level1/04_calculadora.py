# =============================================
#  NIVEL 1 - EXERCICIO 4: Calculadora simples
#  SOS Capacita - Introducao a Python
# =============================================
# Execute com: python exercises/level1/04_calculadora.py
# =============================================
#
# Peca dois numeros e uma operacao (+, -, *, /).
# Realize a operacao e exiba o resultado.
#
# Exemplo de saida esperada:
#   Primeiro numero: 10
#   Segundo numero: 3
#   Operacao (+, -, *, /): *
#   10.0 * 3.0 = 30.0
#
# Dica: Use if/elif/else para verificar a operacao.
#       Cuidado com divisao por zero!
# -----------------------------------------------

# Escreva seu codigo aqui:
numero1= float(input("digite o primeiro numero:"))
numero2= float(input("digite o segundo numero:"))
operacao = input("digite a operacao(+, -, *, /,):")
if operacao == "+":
    soma = (numero1 +  numero2)
    print(" o resultado e: ",soma)
elif operacao == "-":
    subtracao = (numero1 - numero2)
    print("o resultado e:", subtracao)
elif operacao == "*":
    multiplicacao = (numero1 * numero2)
    print("o resultado e:", multiplicacao)
else:
    divisao = (numero1 / numero2)
    print("o resultado e:", divisao)






#fahrenheit = celsius * 9/5 + 32
#print(celsius, "°C equivale a", Fahrenheit, "°f")













