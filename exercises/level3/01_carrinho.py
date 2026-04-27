# =============================================
#  NIVEL 3 - EXERCICIO 1: Carrinho de compras com desconto
#  SOS Capacita - Introducao a Python
# =============================================
# Execute com: python exercises/level3/01_carrinho.py
# =============================================
#
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

# funcao para calcular o desconto com base no total da compra
def calcular_desconto(total):
    """Calcula o valor do desconto com base no total da compra."""
    if total >= 500:
        return total * 0.15
    elif total >= 200:
        return total * 0.10
    else:
        return 0.0

# funcao para exibir o resumo da compra
def exibir_resumo(produtos, total, desconto):
    """Exibe o resumo da compra, incluindo produtos, subtotal, desconto e total."""
    print("\n=== RESUMO DA COMPRA ===")
    for nome, preco in produtos:
        print(f"{nome} - R$ {preco:.2f}")
    print("-" * 25)
    print(f"Subtotal: R$ {total:.2f}")
    print(f"Desconto ({desconto/total*100:.0f}%): R$ {desconto:.2f}")
    print(f"Total: R$ {total - desconto:.2f}")

# inicio do programa
print("=" * 50)
print("  SISTEMA DE CARRINHO DE COMPRAS")
print("=" * 50)

# inicializacao da lista de produtos - carrinho, onde cada produto e uma tupla (nome, preco)
carrinho = []

# loop para adicionar produtos ao carrinho
while True:
    nome = input("Nome do produto (ou 'fim' para encerrar): ")
    if nome.lower() == 'fim':
        break
    try:
        preco = float(input("Preco: "))
        if preco < 0:
            print("Preco nao pode ser negativo. Tente novamente.")
            continue # nao adiciona produtos com preco negativo, volta para o inicio do loop
        carrinho.append((nome, preco)) # adiciona o produto como uma tupla (nome, preco) na lista do carrinho
    except ValueError:
        print("Preco invalido. Digite um numero. Tente novamente.")

# calcula o total da compra somando os precos dos produtos no carrinho
# usando uma funcao do Python chamada `sum` junto com uma expressao geradora para iterar sobre os produtos e somar os precos
total_compra = sum(preco for _, preco in carrinho)

# calcula o desconto com base no total da compra usando a funcao `calcular_desconto`
total_descontos = calcular_desconto(total_compra)

# exibe o resumo da compra, passando a lista de produtos, o total e o desconto para a funcao `exibir_resumo`
exibir_resumo(carrinho, total_compra, total_descontos)
