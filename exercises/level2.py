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

def obter_nota_valida(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Digite um valor de 0 a 10.")
        except ValueError:
            print("Entrada inválida. Digite apenas números")

n1 = obter_nota_valida("Digite sua primeira nota: ")
n2 = obter_nota_valida("Digite sua segunda nota: ")
n3 = obter_nota_valida("Digite sua terceira nota: ")
n4 = obter_nota_valida("Digite sua quarta nota: ")

média = (n1 + n2 + n3 + n4)/4

if média >= 7:
    print(f"Parabéns! Você foi aprovado com nota", média)
elif média >= 5 and média <= 6.9:
    print(f"Ainda há esperança! Você está de recuperação com nota", média)
else:
    print(f"Que pena, você foi reprovado com nota", média)

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

#while True:
#    try:
#        salario = float(input("Digite o seu salário: "))
#        break 
#    except ValueError:
#            print("Formato inválido. Por favor, digite o seu salário em forma numérica")

#if salario >= 0 and salario <= 1500:
#    salario_atual = salario * 1.15
#elif salario >= 1500.01 and salario <= 3000:
#    salario_atual = salario * 1.1
#else: salario_atual = salario * 1.05

#print(f"Salario atual: ", salario)
#print(f"A porcentagem de aumento foi:", ((salario_atual/salario) - 1)*100, "%")
#print(f"O aumento foi de:", salario_atual - salario)
#print(f"O seu novo salário é: ", salario_atual)



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

#usuario_ok = "admin"
#senha_ok = "1234"

#for i in range(3):
#    login = input("Digite o login: ")
#    senha = input("Digite a senha: ")

#    if login == usuario_ok and senha == senha_ok:
#        print("Usuário e senha corretos. Redirecionando...")
#        break
#    else:
#        print(f"Dados incorretos. Tentativa {i + 1} de 3")
#else: 
#    print("Você excedeu o número de tentativas. Acesso bloquado.")
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

def tabuada():
    while True:
        try:
            numero = int(input("Digite o número que você quer saber a tabuada: "))
            for i in range(1, 11):
                resultado = numero * i
                print(f"{numero} * {i} = {resultado}")
        

            novamente = input("Deseja saber outro número? (sim/nao) ")
            if novamente != 'sim':
                print("Operação finalizada.")
                break

        except ValueError:
            print("Formato inválido. por favor, digite um número inteiro.")



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
