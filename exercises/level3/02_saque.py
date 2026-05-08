# =============================================
#  NIVEL 3 - EXERCICIO 2: Validacao de saque bancario
#  SOS Capacita - Introducao a Python
# =============================================
# Execute com: python exercises/level3/02_saque.py
# =============================================
#
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
