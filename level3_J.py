# =============================================
#  EXERCICIOS - NIVEL 3 (Problemas Reais + Funcoes)
#  SOS Capacita - Introducao a Python
# =============================================
# Instrucoes:
#   - Estes exercicios simulam problemas reais
#   - TODOS devem ser resolvidos usando FUNCOES
#   - Pense como um desenvolvedor profissional:
#     * Nomes claros para variaveis e funcoes
#     * Codigo organizado e legivel
#     * Tratamento de erros quando necessario
#   - Execute com: python exercises/level3.py
# =============================================


# -----------------------------------------------
# EXERCICIO 1: Carrinho de compras com desconto
# -----------------------------------------------
# Crie um sistema de carrinho de compras.
#
# O usuario pode adicionar produtos (nome e preco).
# Quando terminar, o sistema calcula o total.
# Regras de desconto sobre o total:
#   - Total >= R$ 500: 15% de desconto
#   - Total >= R$ 200: 10% de desconto
#   - Total < R$ 200: sem desconto
#
# Funcoes que voce DEVE criar:
#   - calcular_desconto(total) -> retorna o valor do desconto
#   - exibir_resumo(produtos, total, desconto) -> mostra o resumo
#
# Exemplo de saida esperada:
#   --- Carrinho de Compras ---
#   Nome do produto (ou 'fim' para encerrar): Camiseta
#   Preco: 89.90
#   Nome do produto (ou 'fim' para encerrar): Calca
#   Preco: 159.90
#   Nome do produto (ou 'fim' para encerrar): Tenis
#   Preco: 299.90
#   Nome do produto (ou 'fim' para encerrar): fim
#
#   === RESUMO DA COMPRA ===
#   Camiseta - R$ 89.90
#   Calca - R$ 159.90
#   Tenis - R$ 299.90
#   -------------------------
#   Subtotal: R$ 549.70
#   Desconto (15%): R$ 82.46
#   Total: R$ 467.25
#
# Dica: Use uma lista para guardar os produtos.
#       Cada produto pode ser uma tupla: (nome, preco)
#       Exemplo: produtos = [("Camiseta", 89.90)]
# -----------------------------------------------

# Escreva seu codigo aqui:
print("=" * 50)
print("CARRINHO DE COMPRAS COM DESCONTO")
print("=" * 50)

# funcao para add produtos
produtos = []
def validar_cadastro():
    while True:    
        nome_prod = input("Nome Produto (Digite fim para encerrar):  ").upper()
        if nome_prod == "FIM":
            break
        else: 
            while True:    
                try:
                    preco_prod = float(input("Preço Produto: R$ "))
                    break
                except ValueError:
                    print("Erro: Digite um preço válido.")
                    continue
        produtos.append({"nome_prod": nome_prod, "preco_prod": preco_prod})

# funcao para calcular o desconto
def calcular_subtotal():
    subtotal = 0
    for produto in produtos:
        subtotal += produto['preco_prod']
    return subtotal

# funcao para calcular o desconto
def calculo_desconto (subtotal):
    if subtotal >= 500: 
        perc_desconto = 0.15
    elif subtotal >= 200:
        perc_desconto = 0.10
    else:
        perc_desconto = 0
    return perc_desconto

# funcao exibir resumo de compra
def exibir_resumo(subtotal, perc_desconto, total):
    print("------------------------")
    print("RESUMO DA COMPRA")
    for produto in produtos:
        print(f"{produto["nome_prod"]} - R$ {produto["preco_prod"]:.2f}")
    
    print("----------------------") 
    print(f"Subtotal: R$ {subtotal:.2f}")        
    print(f"Desconto({perc_desconto*100:.0f}%: R$ {subtotal*perc_desconto:.2f})")
    print(f"Total: R$ {total:.2f}")

# execucao do programa
validar_cadastro()
subtotal = calcular_subtotal()
perc_desconto = calculo_desconto(subtotal)
total = subtotal - (subtotal*perc_desconto)
exibir_resumo(subtotal, perc_desconto, total)


# -----------------------------------------------
# EXERCICIO 2: Validacao de saque bancario
# -----------------------------------------------
# Simule um sistema de saque em caixa eletronico.
#
# O usuario tem um saldo inicial de R$ 1000.00.
# Ele pode fazer saques ate digitar 0 para sair.
#
# Regras:
#   - Valor do saque deve ser positivo
#   - Valor do saque nao pode ser maior que o saldo
#   - Cada saque tem uma taxa de R$ 2.50
#   - A taxa tambem e descontada do saldo
#   - Exibir saldo atualizado apos cada operacao
#
# Funcoes que voce DEVE criar:
#   - validar_saque(valor, saldo) -> retorna True/False
#   - realizar_saque(valor, saldo, taxa) -> retorna novo saldo
#   - exibir_saldo(saldo) -> mostra o saldo formatado
#
# Exemplo de saida esperada:
#   === CAIXA ELETRONICO ===
#   Saldo atual: R$ 1000.00
#   Valor do saque (0 para sair): 200
#   Saque de R$ 200.00 realizado! Taxa: R$ 2.50
#   Saldo atual: R$ 797.50
#   Valor do saque (0 para sair): 900
#   Saldo insuficiente!
#   Valor do saque (0 para sair): 0
#   Obrigado por usar nosso caixa!
#   Saldo final: R$ 797.50
# -----------------------------------------------

# Escreva seu codigo aqui:
# funcao para exibir o saldo
def exibir_saldo (saldo):
    print(f"Saldo atual: R$ {saldo:.2f}")

# funcao para validar saque
def validar_saque (valor, saldo):
    if valor <= 0:
        print("O valor do saque deve ser positivo.")
        return False
    elif valor + taxa > saldo:
        print (f"Saldo insuficiente.")
        return False
    return True

# funcao para realizar saque
def realizar_saque (valor, saldo, taxa):
    print(f"Saque de R$ {valor:.2f} realizado! Tarifa bancária: R$ {taxa:.2f}")
    saldo = saldo - (valor + taxa)
    return saldo

# execucao do programa
print("=" * 50)
print("CAIXA ELETRONICO")
print("=" * 50)
saldo = 1000
taxa = 2.5
while True:
    exibir_saldo(saldo)
    try:
        valor = float(input("Valor do saque (0 para sair): "))
    except ValueError:
        print(f"Erro: Digite um número válido.")
        continue
    if valor == 0:
        print(f"Obrigado por usar nosso caixa!")
        break
    if validar_saque(valor, saldo):
        saldo = realizar_saque(valor, saldo, taxa)
print(f"Saldo final: R$ {saldo:.2f}")

# -----------------------------------------------
# EXERCICIO 3: Validacao de entrada com laco
# -----------------------------------------------
# Crie um programa que peca dados de cadastro:
#   - Nome (nao pode ser vazio)
#   - Idade (deve ser entre 0 e 150)
#   - Email (deve conter "@")
#   - Salario (deve ser positivo)
#
# Para CADA campo, se o usuario digitar algo invalido,
# o programa deve pedir novamente ate receber um valor
# valido. Use try/except onde necessario.
#
# Funcoes que voce DEVE criar:
#   - ler_nome() -> retorna nome valido
#   - ler_idade() -> retorna idade valida (int)
#   - ler_email() -> retorna email valido
#   - ler_salario() -> retorna salario valido (float)
#   - exibir_cadastro(nome, idade, email, salario) -> mostra dados
#
# Exemplo de saida esperada:
#   --- CADASTRO ---
#   Nome:
#   Erro: nome nao pode ser vazio!
#   Nome: Joao
#   Idade: -5
#   Erro: idade deve ser entre 0 e 150!
#   Idade: abc
#   Erro: digite um numero valido!
#   Idade: 25
#   Email: joao.email
#   Erro: email deve conter @!
#   Email: joao@email.com
#   Salario: -100
#   Erro: salario deve ser positivo!
#   Salario: 3000
#
#   === DADOS DO CADASTRO ===
#   Nome: Joao
#   Idade: 25
#   Email: joao@email.com
#   Salario: R$ 3000.00
# -----------------------------------------------

# Escreva seu codigo aqui:
# funcao ler nome (nao pode ser vazio)
def ler_nome():
    while True:
        nome = input("Digite o nome: ")
        if nome == "":
            print(f"Erro: nome nao pode ser vazio!")  
            continue          
        return nome

# funcao ler idade (deve ser entre 0 e 150 e inteiro)
def ler_idade():
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade < 0 or idade > 150:
                print(f"Erro: Digite um numero valido (0 a 150)")  
                continue          
        except ValueError:
            return True
        return idade

# funcao ler_email (deve conter "@")
def ler_email():
    while True:
        email = input("Digite o email: ")
        if not "@" in email:
            print(f"Erro: o email deve conter @!")  
            continue          
        return email
    
# funcao ler_salario  (deve ser positivo e float)
def ler_salario():
    while True:
        try:
            salario = float(input("Digite o salario: "))
            if salario < 1:
                print(f"Erro: salario deve ser positivo")  
                continue          
        except ValueError:
            return True
        return salario

# funcao exibir_cadastro (nome, idade, email, salario)
print("=" * 50)
print("CADASTRO")
print("=" * 50)
nome_cadastro = ler_nome()
idade_cadastro = ler_idade()
email_cadastro = ler_email()
salario_cadastro = ler_salario()

# execucao do programa
print("=" * 50)
print("DADOS DO CADASTRO")
print("=" * 50)
print(f"Nome: {nome_cadastro}")
print(f"Idade: {idade_cadastro}")
print(f"Email: {email_cadastro}")
print(f"Salario: R$ {salario_cadastro}")

# -----------------------------------------------
# EXERCICIO 4: Desafio de funcoes
# -----------------------------------------------
# Crie as seguintes funcoes reutilizaveis e teste
# cada uma delas com pelo menos 2 chamadas diferentes.
#
# a) calcular_imposto(valor, taxa)
#    - Recebe um valor e uma taxa (ex: 0.10 para 10%)
#    - Retorna o valor do imposto
#    - Se a taxa nao for informada, usar 10% como padrao

def calcular_imposto():
    valor = float(input("Digite o valor: R$ "))
    taxa = input("Digite a taxa(ex:0.10 para 10%):")
    if taxa == "":
        imposto = valor * 0.1    
    else:
        taxa = float(taxa)
        imposto = valor * taxa
    return imposto

imposto_calculado = calcular_imposto()
print(f"O imposto sob o valor é: R$ {imposto_calculado}")

# b) validar_idade(idade)
#    - Recebe uma idade
#    - Retorna True se for valida (0 a 150), False se nao

def validar_idade():
    print("-------------------------")
    idade = int(input(("Digite a idade: ")))
    if idade < 0 or idade > 150:
        print("False")
    else:
        print("True")

calculo_idade = validar_idade()

# c) calcular_desconto(preco, tipo_cliente)
#    - Recebe um preco e o tipo do cliente ("vip", "regular", "novo")
#    - VIP: 20% de desconto
#    - Regular: 10% de desconto
#    - Novo: 5% de desconto
#    - Retorna o preco final (ja com desconto aplicado)

def calcular_desconto():
    preco = float(input(("Digite o preco: R$ ")))
    cliente = input("Tipo de cliente(VIP, Regular ou Novo): ").lower()
    if cliente == "vip":
        valor = preco * 0.20
    elif cliente == "regular":
        valor = preco * 0.10
    elif cliente == "novo":
        valor = preco * 0.5
    return valor

valor_final = calcular_desconto()
print(f"O valor final do produto é: {valor_final:.2f}")


#
# d) gerar_relatorio(nome, valores)
#    - Recebe o nome de um funcionario e uma lista de valores
#    - Calcula: total, media, maior valor, menor valor
#    - Exibe um relatorio formatado


#
# Exemplo de uso:
#   print(calcular_imposto(1000))           # 100.0
#   print(calcular_imposto(1000, 0.15))     # 150.0
#   print(validar_idade(25))                 # True
#   print(validar_idade(-5))                 # False
#   print(calcular_desconto(100, "vip"))     # 80.0
#   gerar_relatorio("Ana", [1500, 2000, 1800, 2200])
# -----------------------------------------------

# Escreva seu codigo aqui:
