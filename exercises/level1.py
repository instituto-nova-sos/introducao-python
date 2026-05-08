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
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1+n2
print("A soma dos números acima é: " ,soma)
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
nint = int(input("Digite um número inteiro:"))
if nint % 2 == 0:
    print("O número ",nint," digitado é par")
else:
    print("O número ",nint," digitado é impar")

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
celsius = float(input("Escreva uma temperatura em Celsius"))
fahrenheit = celsius * 9/5 + 32
print ("Sua temperatura convertida de Celsius para Fahnheit é ",fahrenheit)

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
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operacao = input("Qual operação você deseja realizar entre +(soma), -(subtração), *(multiplicação ou /(divisão)?")
if operacao == "+":
    print ("A soma dos números escolhidos é ",n1+n2)
elif operacao == "-":
    print ("A subtração dos números escolhidos é ",n1-n2)
elif operacao == "*":
    print ("A multiplicação dos números escolhidos é ",n1*n2)
elif operacao == "/":
    if % 2 == 0:
        print ("A divisão dos números escolhidos é ",n1/n2)
    else:    
        print ("A divisão dos números resulta em zero")
else:
    print ("Operação inválida")
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
idade = int(input("Qual a sua idade? "))
if 0 <= idade <= 12:
    print ("Com ",idade," anos você é uma criança")
elif 13 <= idade <= 17:
    print ("Com ",idade," anos você é um adolescente")
elif 18 <= idade <= 59:
    print ("Com ",idade," anos você é um adulto")
elif idade >= 60:
    print ("Com",idade," anos você é um idoso")
else:
    print ("Idade inválida")
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
n1 = int(input("Digite o lado direito do triangulo: "))
n2 = int(input("Digite o lado esquerdo do triangulo: "))
n3 = int(input("Digite a base do triangulo: "))
if n1+n2 > n3:
    print ("Os lados formam um triangulo valido!")
elif n1+n2 < n3:
    print ("Os lados não formam um triangulo valido!")
elif n1+n3 > n2:
    print ("Os lados formam um triangulo valido!")
elif n1+n3 < n2:
    print ("Os lados não formam um triangulo valido!")