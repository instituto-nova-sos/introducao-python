# =============================================
#  MINI PROJETO: Sistema de Controle Financeiro
#  SOS Capacita - Introducao a Python
# =============================================
# Este projeto une todos os conceitos da aula:
#   - Variaveis e tipos de dados
#   - Entrada e saida (input/print)
#   - Condicionais (if/elif/else)
#   - Lacos de repeticao (while)
#   - Funcoes (def)
#   - Tratamento de erros (try/except)
#
# Funcionalidades:
#   1. Adicionar receita (entrada de dinheiro)
#   2. Adicionar despesa (saida de dinheiro)
#   3. Consultar saldo atual
#   4. Ver extrato completo
#   5. Sair do sistema
#
# Execute com: python project/financial_system.py
# =============================================


# --- FUNCOES DO SISTEMA ---

def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\n" + "=" * 40)
    print("  SISTEMA DE CONTROLE FINANCEIRO")
    print("=" * 40)
    print("  [1] Adicionar receita")
    print("  [2] Adicionar despesa")
    print("  [3] Consultar saldo")
    print("  [4] Ver extrato")
    print("  [5] Sair")
    print("=" * 40)


def ler_valor(mensagem):
    """Le um valor numerico positivo do usuario.
    Repete ate receber um valor valido.
    """
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Erro: o valor deve ser maior que zero!")
                continue
            return valor
        except ValueError:
            print("Erro: digite um numero valido!")


def ler_opcao():
    """Le a opcao do menu escolhida pelo usuario."""
    while True:
        try:
            opcao = int(input("\nEscolha uma opcao: "))
            if opcao < 1 or opcao > 5:
                print("Erro: escolha uma opcao de 1 a 5!")
                continue
            return opcao
        except ValueError:
            print("Erro: digite um numero de 1 a 5!")


def adicionar_receita(transacoes):
    """Adiciona uma receita (entrada de dinheiro) ao registro.

    Parametros:
        transacoes: lista onde cada item e uma tupla (tipo, descricao, valor)

    Retorna:
        O valor da receita adicionada.
    """
    print("\n--- Nova Receita ---")
    descricao = input("Descricao (ex: Salario, Freelance): ")
    valor = ler_valor("Valor: R$ ")

    # Guarda a transacao como uma tupla: (tipo, descricao, valor)
    transacoes.append(("receita", descricao, valor))
    print(f"Receita de R$ {valor:.2f} adicionada com sucesso!")
    return valor


def adicionar_despesa(transacoes):
    """Adiciona uma despesa (saida de dinheiro) ao registro.

    Parametros:
        transacoes: lista onde cada item e uma tupla (tipo, descricao, valor)

    Retorna:
        O valor da despesa adicionada.
    """
    print("\n--- Nova Despesa ---")
    descricao = input("Descricao (ex: Aluguel, Mercado): ")
    valor = ler_valor("Valor: R$ ")

    transacoes.append(("despesa", descricao, valor))
    print(f"Despesa de R$ {valor:.2f} adicionada com sucesso!")
    return valor


def calcular_saldo(transacoes):
    """Calcula o saldo atual baseado em todas as transacoes.

    Soma todas as receitas e subtrai todas as despesas.

    Parametros:
        transacoes: lista de tuplas (tipo, descricao, valor)

    Retorna:
        O saldo atual (float).
    """
    saldo = 0.0
    for tipo, descricao, valor in transacoes:
        if tipo == "receita":
            saldo += valor
        else:
            saldo -= valor
    return saldo


def exibir_saldo(transacoes):
    """Mostra o saldo atual formatado na tela."""
    saldo = calcular_saldo(transacoes)

    print("\n--- Saldo Atual ---")
    if saldo >= 0:
        print(f"  R$ {saldo:.2f}")
        if saldo == 0:
            print("  Seu saldo esta zerado.")
        else:
            print("  Voce esta no positivo!")
    else:
        print(f"  R$ {saldo:.2f}")
        print("  ATENCAO: voce esta no vermelho!")


def exibir_extrato(transacoes):
    """Mostra o extrato completo de todas as transacoes."""
    print("\n" + "=" * 45)
    print("  EXTRATO COMPLETO")
    print("=" * 45)

    if not transacoes:
        print("  Nenhuma transacao registrada.")
        print("=" * 45)
        return

    total_receitas = 0.0
    total_despesas = 0.0

    for i, (tipo, descricao, valor) in enumerate(transacoes, 1):
        if tipo == "receita":
            simbolo = "+"
            total_receitas += valor
        else:
            simbolo = "-"
            total_despesas += valor

        print(f"  {i:02d}. [{simbolo}] {descricao:<20} R$ {valor:>10.2f}")

    saldo = total_receitas - total_despesas

    print("-" * 45)
    print(f"  Total receitas:  R$ {total_receitas:>10.2f}")
    print(f"  Total despesas:  R$ {total_despesas:>10.2f}")
    print(f"  Saldo:           R$ {saldo:>10.2f}")
    print("=" * 45)


# --- FUNCAO PRINCIPAL ---

def main():
    """Funcao principal que controla o fluxo do sistema.

    Essa funcao contem o laco principal do programa.
    Ela exibe o menu, le a opcao do usuario e chama
    a funcao correspondente. O laco repete ate o usuario
    escolher a opcao 5 (sair).
    """
    # Lista que armazena todas as transacoes do usuario
    # Cada transacao e uma tupla: (tipo, descricao, valor)
    transacoes = []

    print("\nBem-vindo ao Sistema de Controle Financeiro!")
    print("Use este sistema para acompanhar suas receitas e despesas.")

    # Laco principal - repete ate o usuario escolher sair
    while True:
        exibir_menu()
        opcao = ler_opcao()

        if opcao == 1:
            adicionar_receita(transacoes)

        elif opcao == 2:
            adicionar_despesa(transacoes)

        elif opcao == 3:
            exibir_saldo(transacoes)

        elif opcao == 4:
            exibir_extrato(transacoes)

        elif opcao == 5:
            # Antes de sair, mostra o extrato final
            if transacoes:
                print("\n--- Extrato final ---")
                exibir_extrato(transacoes)
            print("\nObrigado por usar o Sistema Financeiro!")
            print("Ate a proxima!")
            break  # Sai do laco while, encerrando o programa


# --- PONTO DE ENTRADA ---
# Este bloco so executa quando o arquivo e rodado diretamente.
# Se este arquivo fosse importado por outro, o bloco nao executaria.
if __name__ == "__main__":
    main()
