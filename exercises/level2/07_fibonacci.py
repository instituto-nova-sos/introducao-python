# =============================================
#  NIVEL 2 - EXERCICIO 7: Sequencia de Fibonacci
#  SOS Capacita - Introducao a Python
# =============================================
# Execute com: python exercises/level2/07_fibonacci.py
# =============================================
#
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

while True:
    termos = input('Digite um número: ')
    fibonacci = [0,1]
    try:
        termos = int(termos)

        if termos <= 0:
            print('Por favor digite um número positivo! ➕')
            continue
        elif termos > 200:
            print(f"print(f'⚠️ Limite excedido! {termos} é muito grande. Digite até 200 se não seu PC vai virar uma churrasqueira elétrica! 💣\n')")
            continue
        elif termos == 1:
            print('Sequência gerada: [0]')
            break
        elif termos == 2:
            print(f"Sequência gerada: {fibonacci}")
            break
        else:
            for i in range(termos -2):
                proximo_numero = fibonacci[-1] + fibonacci[-2]
                fibonacci.append(proximo_numero)
            print(f'Sequência gerada: {fibonacci}')
        break
    except ValueError:
        print(f'Tu vai calcular Fibonacci com "{termos}"? 🤬')