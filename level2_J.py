# =============================================
#  EXERCICIOS - NIVEL 2 (Intermediario)
#  SOS Capacita - Introducao a Python
# =============================================
# Instrucoes:
#   - Estes exercicios combinam condicionais e lacos
#   - Pense na logica antes de escrever o codigo
#   - Faca o teste de mesa mentalmente antes de executar
#   - Execute com: python exercises/level2.py
# =============================================

# -----------------------------------------------
# EXERCICIO 1: Media e aprovacao do aluno
# -----------------------------------------------
# Peca 4 notas de um aluno (de 0 a 10).
# Calcule a media aritmetica.
# Exiba a situacao:
#   - Media >= 7.0: "Aprovado"
#   - Media >= 5.0 e < 7.0: "Recuperacao"
#   - Media < 5.0: "Reprovado"
#
# Exemplo de saida esperada:
#   Nota 1: 8
#   Nota 2: 6
#   Nota 3: 7
#   Nota 4: 9
#   Media: 7.50
#   Situacao: Aprovado
#
# Dica: Valide se cada nota esta entre 0 e 10.
#       Se nao estiver, peca novamente.
# -----------------------------------------------

# Escreva seu codigo aqui:
print("=" * 50)
print("MEDIA E APROVACAO DO ALUNO")
print("=" * 50)
var = 0
while var == 0: 
    nota1 = float(input("Digite a 1ª nota: "))
    if (nota1 <0) or (nota1 >10):
        var = 0
    else:
        var = 1
var = 0
while var == 0: 
    nota2 = float(input("Digite a 2ª nota: "))
    if (nota2 <0) or (nota2 >10):
        var = 0
    else:
        var = 1
var = 0
while var == 0: 
    nota3 = float(input("Digite a 3ª nota: "))
    if (nota3 <0) or (nota3 >10):
        var = 0
    else:
        var = 1
var = 0
while var == 0: 
    nota4 = float(input("Digite a 4ª nota: "))
    if (nota4 <0) or (nota4 >10):
        var = 0
    else:
        var = 1
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"Media: {media}")
if media < 5:
    print(f"Siuacao: Reprovado.")
elif media < 7:
    print(f"Siuacao: Recuperacao.")
else:
    print(f"Siuacao: Aprovado.")


# -----------------------------------------------
# EXERCICIO 2: Calculadora de aumento salarial
# -----------------------------------------------
# Peca o salario atual do funcionario.
# Aplique o aumento conforme a regra:
#   - Salario ate R$ 1500: aumento de 15%
#   - Salario de R$ 1500.01 a R$ 3000: aumento de 10%
#   - Salario acima de R$ 3000: aumento de 5%
#
# Exiba:
#   - Salario atual
#   - Percentual de aumento
#   - Valor do aumento
#   - Novo salario
#
# Exemplo de saida esperada:
#   Salario atual: R$ 2000.00
#   Percentual: 10%
#   Aumento: R$ 200.00
#   Novo salario: R$ 2200.00
# -----------------------------------------------

# Escreva seu codigo aqui:
print("=" * 50)
print("CALCULADORA DE AUMENTO SALARIAL")
print("=" * 50)
sal = float(input("Digite o salario atual do funcionario: "))
if sal <= 1500:
    perc = 0.15
    sal_novo = (sal * perc) + sal
elif sal <= 3000:
    perc = 0.1
    sal_novo = (sal * perc) + sal
else:
    perc = 0.05
    sal_novo = (sal * perc) + sal
aum_sal = sal * perc
print(f'''
            Salario atual: R$ {sal:.2f}
            Percentual de aumento: {perc*100}%
            Valor do aumento: R$ {aum_sal:.2f}
            Novo salario: R$ {sal_novo:.2f}
''')
# -----------------------------------------------
# EXERCICIO 3: Simulacao de login
# -----------------------------------------------
# Crie um sistema de login simples.
# O usuario correto e "admin" e a senha e "1234".
# O usuario tem no maximo 3 tentativas.
#
# A cada tentativa errada, informe quantas restam.
# Se acertar, exiba "Acesso liberado!"
# Se esgotar as tentativas, exiba "Conta bloqueada!"
#
# Exemplo de saida esperada:
#   --- Sistema de Login ---
#   Usuario: admin
#   Senha: abcd
#   Senha incorreta! Tentativas restantes: 2
#   Usuario: admin
#   Senha: 1234
#   Acesso liberado!
#
# Dica: Use um laco while com contador de tentativas.
# -----------------------------------------------

# Escreva seu codigo aqui:
print("=" * 50)
print("SIMULACAO DE LOGIN")
print("=" * 50)
usuario_adm = "admin"
senha_adm = "1234"
usuario_cli = input("Usuario: ")
senha_cli = input("Senha: ")
var = 3
if (usuario_cli == usuario_adm) and (senha_adm == senha_cli):
    print(f"Acesso liberado!")
    var = 0
else:
    while var > 1:
        var= var - 1
        print(f"Dados incorretos. Tentativa(s) restante(s): {var}")
        usuario_cli = input("Usuario: ")
        senha_cli = input("Senha: ")
        if (usuario_adm == usuario_cli) and (senha_adm == senha_cli):
            print(f"Acesso liberado!")
            var = 0
    if var == 1:
        print(f"Acesso bloqueado!")          


# -----------------------------------------------
# EXERCICIO 4: Tabuada completa
# -----------------------------------------------
# Peca um numero ao usuario.
# Exiba a tabuada desse numero de 1 a 10.
# Depois, pergunte se ele quer ver outra tabuada.
# Se sim, repita. Se nao, encerre.
#
# Exemplo de saida esperada:
#   Qual numero? 5
#   5 x 1 = 5
#   5 x 2 = 10
#   ...
#   5 x 10 = 50
#   Ver outra tabuada? (s/n): s
#   Qual numero? 3
#   3 x 1 = 3
#   ...
# -----------------------------------------------

# Escreva seu codigo aqui:
print("=" * 50)
print("TABUADA COMPLETA")
print("=" * 50)
num1 = int(input("Digite o numero que deseja calcular a tabuada: "))
num2 = 0
while num2 < 11:
    print(f"{num1} * {num2} = {num1 * num2}")
    num2 = num2 + 1
repeat = (input("Ver outra tabuada? (s/n): ")).upper()
while repeat == "S":
    num1 = int(input("Digite o numero que deseja calcular a tabuada: "))
    num2 = 0
    while num2 < 11:
        print(f"{num1} * {num2} = {num1 * num2}")
        num2 = num2 + 1
    repeat = (input("Ver outra tabuada? (s/n): ")).upper()    
print("Obrigado!")


# -----------------------------------------------
# EXERCICIO 5: Contador de pares e impares
# -----------------------------------------------
# Peca ao usuario para digitar 10 numeros inteiros.
# Ao final, exiba:
#   - Quantos eram pares
#   - Quantos eram impares
#   - A soma dos pares
#   - A soma dos impares
#
# Exemplo de saida esperada:
#   Digite o numero 1: 4
#   Digite o numero 2: 7
#   ...
#   Pares: 6 | Soma dos pares: 30
#   Impares: 4 | Soma dos impares: 25
# -----------------------------------------------

# Escreva seu codigo aqui:
print("=" * 50)
print("CONTADOR DE PARES E IMPARES")
print("=" * 50)
lista_par = 0
lista_impar = 0
soma_par = 0
soma_impar = 0
for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    if num % 2 == 0:
        lista_par += 1
        soma_par += num
    else:
        lista_impar += 1
        soma_impar += num
print(f'''
        Pares: {lista_par} | Soma dos pares: {soma_par}
        Impares: {lista_impar} | Soma dos impares: {soma_impar}
''')


# -----------------------------------------------
# EXERCICIO 6: Fatorial
# -----------------------------------------------
# Peca um numero inteiro positivo ao usuario.
# Calcule o fatorial desse numero usando um laco.
#
# Fatorial de N = N * (N-1) * (N-2) * ... * 1
# Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
# Caso especial: 0! = 1
#
# Exemplo de saida esperada:
#   Digite um numero: 5
#   O fatorial de 5 e: 120
#
# Dica: NAO use a funcao math.factorial().
#       O objetivo e praticar lacos.
# -----------------------------------------------

# Escreva seu codigo aqui:


# -----------------------------------------------
# EXERCICIO 7: Sequencia de Fibonacci
# -----------------------------------------------
# Peca ao usuario quantos termos da sequencia de
# Fibonacci ele quer ver.
# Exiba a sequencia.
#
# Fibonacci: cada numero e a soma dos dois anteriores.
# Comeca com 0 e 1:
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Exemplo de saida esperada:
#   Quantos termos? 8
#   0 1 1 2 3 5 8 13
#
# Dica: Use duas variaveis para guardar os dois
#       numeros anteriores.
# -----------------------------------------------

# Escreva seu codigo aqui:
print("=" * 50)
atual = 1
ant = 0
i = 0
lista_num = []
num = int(input("Informe qual o número de sequência Fibonacci deseja que seja calculada? "))
while i < num:
    result = ant + atual
    ant = atual
    atual = result
    i += 1
    lista_num.append(result)
print(f"{lista_num}")