# =============================================
#  NIVEL 1 - EXERCICIO 1: Soma de dois numeros
#  SOS Capacita - Introducao a Python
# =============================================
# Execute com: python exercises/level1/01_soma.py
# =============================================
#
# Peca ao usuario para digitar dois numeros.
# Calcule e exiba a soma deles.
#
# Exemplo de saida esperada:
#   Digite o primeiro numero: 5
#   Digite o segundo numero: 3
#   A soma e: 8
#
# Dica: Lembre-se que input() retorna string.
#       Voce precisa converter para numero.
# -----------------------------------------------

# Escreva seu codigo aqui:
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

soma = numero1 + numero2

print("A soma e:", soma)