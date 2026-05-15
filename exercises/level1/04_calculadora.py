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
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Qual operacao deseja? (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2

elif operacao == "-":
    resultado = numero1 - numero2

elif operacao == "*":
    resultado = numero1 * numero2

elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Erro: divisao por zero")
        resultado = None

else:
    print("Operacao invalida")
    resultado = None

if resultado != None:
    print(numero1, operacao, numero2, "=", resultado)