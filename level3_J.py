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
#
# b) validar_idade(idade)
#    - Recebe uma idade
#    - Retorna True se for valida (0 a 150), False se nao
#
# c) calcular_desconto(preco, tipo_cliente)
#    - Recebe um preco e o tipo do cliente ("vip", "regular", "novo")
#    - VIP: 20% de desconto
#    - Regular: 10% de desconto
#    - Novo: 5% de desconto
#    - Retorna o preco final (ja com desconto aplicado)
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
