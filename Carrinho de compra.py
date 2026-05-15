EXERCICIO 1: Carrinho de compras com desconto
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