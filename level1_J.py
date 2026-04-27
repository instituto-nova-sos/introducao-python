# EXERCICIO 1: Soma de dois numeros
# -----------------------------------------------
# Peca ao usuario para digitar dois numeros.
# Calcule e exiba a soma deles.
#
# Exemplo de saida esperada:
#   Digite o primeiro numero: 5
#   Digite o segundo numero: 3
#   A soma e: 8
# Dica: Lembre-se que input() retorna string.
#       Voce precisa converter para numero.
# -----------------------------------------------

# Escreva seu codigo aqui:
print("=" * 50)
print("  SOMA DE DOIS NUMEROS")
print("=" * 50)
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
result_soma = num1 + num2
print(f"A soma dos numeros é: {result_soma}")
print()

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
print("=" * 50)
print("  DESCUBRA SE O NUMERO E PAR OU IMPAR")
print("=" * 50)
num = int(input("Digite um numero: "))
if num % 2 == 0:
    print(f"O numero {num} e par.")
else:
    print(f"O numero {num} e impar.")
print()


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
print("=" * 50)
print("CONVERSOR DE TEMPERATURA")
print("=" * 50)
temp = float(input("Digite a temperatura (apenas numero): "))
tipo = input("Digite C para converter em Celsius ou F para converter em Fahrenheit: ").upper()
if tipo == "F":
    result = (temp - 32) * 5/9
    print(f"{temp}ºF equivale a {result}ºC")
elif tipo == "C":
    result = temp * 9/5 + 32
    print(f"{temp}ºC equivale a {result}ºF")
else:
    print ("Dados divergentes. Tente novamente.")
 
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
print("=" * 50)
print("CALCULADORA SIMPLES")
print("=" * 50)
num1 = float(input("Digite o primeiro num: "))
num2 = float(input("Digite o segundo num: "))
oper = input("Digite a operacao matematica desejada (+, -, *, /): ")
if oper == "+":
    result = num1 + num2
elif oper == "-":
    result = num1 - num2
elif oper == "*":
    result = num1 * num2
elif oper == "/":
    result = num1 / num2
else:
    print("Operacao matematica invalida.")
print(f"Calculo: {num1} {oper} {num2} = {result}")



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
print("=" * 50)
print("CLASSIFICACAO POR FAIXA ETARIA")
print("=" * 50)
idade = int(input("Digite sua idade: "))
if idade < 0:
    print("Idade invalida.")
elif idade < 13:
    print(f"Classificacao: Crianca")
elif idade < 18:
    print(f"Classificacao: Adolescente")
elif idade < 60:
    print(f"Classificacao: Adulto")
else:
    print(f"Classificacao: Idoso")

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
print("=" * 50)
print("VERIFICAR TRIANGULO")
print("=" * 50)
l1 = float(input("Digite o tamanho do lado 1:"))
l2 = float(input("Digite o tamanho do lado 2:"))
l3 = float(input("Digite o tamanho do lado 3:"))
if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print("Os lados formam um triangulo valido.")
else:
    print("Os lados NAO formam um triangulo.")