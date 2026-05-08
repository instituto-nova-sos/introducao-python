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
primeiro_número = int(input('Digite o primeiro número: '))
segundo_número = int(input('Digite o segundo número: '))
Soma= primeiro_número + segundo_número
print: ('A soma é:  {soma}')

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

número = int(input('Digite um número: '))
if número % 2 == 0:
    print(' {número} é um número par')
else:
     print(' {número} é um número ímpar')
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
C = float(input('Digite a temperatura em Celsius: '))
F = C * 9/5 + 32
print(f' {C} °C equivale a {F} °F')     

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
n1 = float(input('Digite um número: '))
conta = input('digite a operação (+,-,/,*): ')
n2 = float(input('Digite outro número: '))

if conta == "+":
    conta = n1 + n2
    print(f' =  {conta}')

elif conta == "-":
    conta = n1 - n2
    print(f' =  {conta}')

elif conta == "/":
    if n2 !=0:
        conta = n1 / n2
        print(f' = {conta}')
    else: 
        print("Tá dividindo por 0?? quer queimar o PC seu maluco?")

elif conta == "*":
    conta = n1 * n2
    print(f' =  {conta}')

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
idade= float(input('digite sua idade: '))
if  idade <= 0: 
    print("É sério cara? quer atenção?😡")

elif  0 < idade <= 12:
    print("Você ê ainda é um(a) pivéte👶")

elif 12 < idade <= 17:
    print("você é um aborrecente😤")

elif 17 < idade <= 29:
    print("Você é um jovem adulto que está começando a crescer na vida😯")

elif 29 < idade <= 59:
    print("Você é´um adulto com muitas experiências e hitórias pra contar🤩")

elif 59 < idade <= 110:
    print("Você é um idoso um velha guarda 🔥")

elif 110 < idade:
    print("Valeu Noé! 😑👍")

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
l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

if (l1 + l2 > l3) and (l2 + l3 > l1) and (l3 + l1 > l2):
    S = (l1 + l2 + l3) / 2
    A = (S * (S - l1) * (S - l2) * (S - l3)) ** 0.5                  

    print(f'✅ É um triângulo válido! Com uma área de {A:.2f}m²')

else:
    print(f"❌ Error. Desculpe amigo mas esse triângulo é inválido! {l1} x {l2} x {l3}  não dá né? ")