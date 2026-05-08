# =============================================
#  EXERCICIOS - NIVEL 1 (Basico)
#  SOS Capacita - Introducao a Python
# =============================================
# Instrucoes:
#   - Leia cada exercicio com atencao
#   - Escreva seu codigo logo abaixo de cada enunciado
#   - Execute o arquivo com: python exercises/level1.py
#   - Teste com diferentes valores para garantir que funciona
#
# Dica: Comece pelo exercicio 1 e va em ordem.
#       Cada exercicio usa o que voce aprendeu nos anteriores.
# =============================================


# -----------------------------------------------
# EXERCICIO 1: Soma de dois numeros
# -----------------------------------------------
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

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um segundo número: '))
print(f"O resultado da soma desses dois números é: {numero1 + numero2}")

# -----------------------------------------------
# EXERCICIO 2: Par ou impar
# -----------------------------------------------
# Peca ao usuario para digitar um numero inteiro.
# Diga se o numero e par ou impar.
#
# Exemplo de saida esperada:
#   Digite um numero: 7
#   O numero 7 e impar.
#
# Dica: Use o operador % (modulo).
#       Se numero % 2 == 0, o numero e par.
# -----------------------------------------------

# Escreva seu codigo aqui:

numero = int(input('Digite um número para saber se esse é ímpar ou par: '))

if numero % 2 == 0:
    parimpar = "par"
else: parimpar = "ímpar"
print(f"O número digitado é {parimpar}")

# -----------------------------------------------
# EXERCICIO 3: Conversor de temperatura
# -----------------------------------------------
# Peca ao usuario uma temperatura em Celsius.
# Converta para Fahrenheit e exiba o resultado.
#
# Formula: F = C * 9/5 + 32
#
# Exemplo de saida esperada:
#   Digite a temperatura em Celsius: 30
#   30.0°C equivale a 86.0°F
#
# Dica: Use float() para permitir numeros decimais.
# -----------------------------------------------

# Escreva seu codigo aqui:
temperatura = float(input('Digite a temperatura a ser convertida: '))
temperatura_final = (temperatura)*9/5 + 32
print(f"A temperatura convertida para graus Fahrenheit é: {temperatura_final}")
# -----------------------------------------------
# EXERCICIO 4: Calculadora simples
# -----------------------------------------------
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
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação desejada (+, -, *, /): ')

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    resultado = numero1 / numero2
print("O resultado da operação é: ", resultado)
# -----------------------------------------------
# EXERCICIO 5: Classificacao por faixa etaria
# -----------------------------------------------
# Peca a idade do usuario e classifique:
#   - 0 a 12: Crianca
#   - 13 a 17: Adolescente
#   - 18 a 59: Adulto
#   - 60 ou mais: Idoso
#
# Se a idade for negativa, exiba "Idade invalida".
#
# Exemplo de saida esperada:
#   Digite sua idade: 25
#   Classificacao: Adulto
# -----------------------------------------------

# Escreva seu codigo aqui:
idade = int(input("Digite a sua idade: "))
if 0 < idade < 12:
    usuario = 'criança'
elif 13 < idade < 17:
    usuario = 'adolescente'
elif 18 < idade < 59:
    usuario = 'adulto'
elif 60 < idade:
    usuario = 'idoso'
elif idade < 0:
    usuario = 'idade inválida'
print("Você é: ", usuario)

# -----------------------------------------------
# EXERCICIO 6: Verificar triangulo
# -----------------------------------------------
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

lado1 = float(input('Digite um dos lados do triângulo: '))
lado2 = float(input('Digite outro lado do triângulo: '))
lado3 = float(input('Digite o último lado do triângulo: '))

if lado3 < lado1 + lado2:
    print("Os lados formam um triângulo váilido!")
else:
    print("Os lados NÃO formam um triângulo válido!")