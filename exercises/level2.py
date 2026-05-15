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
N1 = float(input('Nota do priemiro trimestre: '))
N2 = float(input('Nota do segundo trimestre: '))
N3 = float(input('Nota do terceiro trimestre: '))
N4 = float(input('Nota do quarto trimestre: '))
media = (N1 + N2 + N3 + N4)/4
faltava = 7 - media

if media < 0:
    print(f'{media} Ah não.... não acredito nisso em negativo??? kakakakaakk o professor provavelmente tem raiva de você meu filho kkkkkkkkkk')

elif media < 1.5:
    print(f'{media} REPROVADO!!!!!!!! "Não é possivel! Você é do tipo que nunca pisou na escola se matriculou e tirou a vaga de quem precisa🤬"')

elif media < 5:
    print(f'SUA MÉDIA FOI {media} kkkkkkk REPROVADO! Parabéns você é um péssimo aluno 👏🤮 "faltar {faltava:.1f} pontos pra passar é sacanagem hein!"')

elif media < 7:
    if faltava == 1:
        print(f'{media} 🤣 Vai estudar nas férias e fazer recuperação por causa de {faltava:.1f} ponto kakakakaakka ')
    else:
        print(f'{media} 🤣 Vai estudar nas férias e fazer recuperação por causa de {faltava:.1f} pontos kakakakaakka ')

elif media > 10:
    print (f'{media} NÃO É POSSIVEL..... QUEM FOI O PROFESSOR PRA IR PRO OLHO DA RUA')

elif media == 10:
    print (f'{media}??????? Você com certeza é super dotado nem sei o que ainda esta fazendo nessa escola')

elif media > 9:
    print (f'{media} APROVADO😝🥳 PARABÉNS!!!! Você é um aluno que provavelmente senta lá na frente e puxa saco de professor 😠')

elif media > 8:
    print (f'{media} APROVADO👏 Parece que alguem se esforçou esse ano! {media} pontos é muito bom! Se continuar assim ano que vem tu melhora mais ainda!!!')

elif media >= 7:
    print (f'{media} aprovado... Éh.. Você passou cravado ná média... Não tenho muita coisa pra falar pra você 🥱')










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
entrada = (input('Digite o seu salário atual por favor: '))

#Limpesa----------------------------------------------------------------------------
txt = entrada.replace('R$', '').replace('$','').replace('reais', '').strip()

if ',' in txt: #Se existe , no texto
    if txt.count (',') > 1: #se o jegue escreveu com 2 , ex: 1,500,50
       partes = txt.split(',')
       corte_final= "".join(partes[:-1])
       txt = corte_final + "." + partes[-1] #AQUI não utilizamos os (:) se não ele nos tráz a lista e não o número
    
    else: #se escreveu do jeito Br    1.500,50 ele vai apagar o ".": 1500,50 e substituir o "," por um "." 1500.50
        txt = txt.replace('.', '')
        txt = txt.replace (',','.')


else: #Se o usuário escreveu o número com 2 pontos ex: 1.500.00
    if txt.count ('.') > 1:  #Aqui detectamos que existem 2 pontos no input
        partes = txt.split('.') #txt.split('.') determinamos qwue onde tem um . ele deve cortar e guardar os valores. ex: 1.500.50 Ele irá gaurdar como (1, 500, 50)
        corte_final= "".join(partes[:-1]) #Aqui ele guarda o ultimo numero da lista como eram (1, 500, 50) ele vai isolar o (50)
        txt = corte_final + "." + partes[-1] #Aqui fazemos a conta partes (1, 500) vai ficar 1500 + o "." + o 50 ficando assim 1500.50 um perfeito float
    
    elif txt.count ('.') == 1: #Se o usuário colocar 1.500 normalmente ele leria como 1 real e 50 centavos 
        txt = txt.replace('.','') #Como aqui eu removi o ponto de 1.500  ele ficou 1500

#IFs e Elifs-------------------------------------------------------------------------
salario_atual = float(txt) #Aqui definimos que a entrada que virou txt é um float
if salario_atual <= 1500.00:
    porcentagem  = 15

elif 1500.00 < salario_atual < 3000.00:
    porcentagem  = 10

else:
    porcentagem  = 5

#Fórmula-----------------------------------------------------------------------------

aumento = (salario_atual * porcentagem) / 100 
novo_salário = salario_atual + aumento

#Output------------------------------------------------------------------------------

print(f"""
      RELATÓRIO SALARIAL:
      ----------------------------------------
      Salario atual:     R${salario_atual:.2f}
      Porcentual:        {porcentagem}%
      Aumento:           R${aumento:.2f}
      Novo salário:      R${novo_salário:.2f}
    -------------------------------------------
 """)

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
nome_correto = 'admin'
senha_correta = '1234'
tentativas = int(3)

while tentativas > 0:
    nome = input('Digite o nome de usuário: ')
    senha = input('Digite sua senha: ')
    if nome == nome_correto and senha == senha_correta:
        print(f'Bem vindo {nome}!')
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f'Senha incorreta Você só tem mais {tentativas} tentativas' )
        else:
            print('Usuário bloqueado no dispositivo!' )
            break 


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

while True:
    try:
        numeros = int(input(f'Digite o número: '))
        print(F'Tabuada do número {numeros}:')
        for n in range(1, 11):
            tabuada = n * numeros
            print(f' {n} x {numeros} = {tabuada} \n')

        continuar = input("\n deseja continuar? s/n: ").strip().lower()
        if continuar != 's':
             print('Encerrando!')
             break
    except ValueError:
     print("Por favor, digite um número inteiro válido.")


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

todos = []
par = []
impar = []

for i in range(1, 11):
    while True:
        entrada = input(f'Digite o {i}° número: ').strip() 

        if entrada.replace('-', '', 1).isdigit() and entrada != "":
            num = int(entrada)
            break 
        else:
            print(f" ATENÇÃO: '{entrada}' NÃO É UM NÚMERO VÁLIDO!")
    todos.append(num)

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"""
----------
Lista completa: {todos}

PARES ({len(par)} números): {par}
Soma dos pares: {sum(par)}

ÍMPARES ({len(impar)} números): {impar}
Soma dos ímpares: {sum(impar)}
------------------------------------------
""")


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
# EXERCICIO 7: Sequencia de Fibonacci--
# ---------------------------------------------
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
