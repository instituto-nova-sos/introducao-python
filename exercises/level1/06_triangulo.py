# =============================================
#  NIVEL 1 - EXERCICIO 6: Verificar triangulo
#  SOS Capacita - Introducao a Python
# =============================================
# Execute com: python exercises/level1/06_triangulo.py
# =============================================
#
# Peca tres valores que representam lados de um triangulo.
# Verifique se eles podem formar um triangulo valido.
#
# Regra: A soma de dois lados deve ser MAIOR que o terceiro lado.
#        (para todos os tres pares)
#
# Exemplo de saida esperada:
#   Lado 1: 3
#   Lado 2: 4
#   Lado 3: 5
#   Os lados formam um triangulo valido!
#
#   Lado 1: 1
#   Lado 2: 2
#   Lado 3: 10
#   Os lados NAO formam um triangulo.
# -----------------------------------------------

# Escreva seu codigo aqui:
lado1 = float(input("Digite a medida do lado 1: "))
lado2 = float(input("Digite a medida do lado 2: "))
lado3 = float(input("Digite a medida do lado 3: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os lados formam um triângulo válido!")

else:
    print("Os lados NÃO formam um triângulo.")
    