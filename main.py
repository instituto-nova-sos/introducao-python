# =============================================
#  SOS Capacita - Introducao a Python
#  Arquivo principal de demonstracao
# =============================================
# Este arquivo mostra exemplos praticos de tudo
# que foi ensinado na aula. Execute com:
#   python main.py

# --- 1. VARIAVEIS E TIPOS DE DADOS ---

print("=" * 50)
print("  DEMONSTRACAO - VARIAVEIS E TIPOS")
print("=" * 50)

# Tipos basicos
nome = "Maria Silva"          # str  - texto
idade = 28                    # int  - numero inteiro
salario = 3500.50             # float - numero decimal
esta_ativa = True             # bool - verdadeiro ou falso

print(f"Nome: {nome} (tipo: {type(nome).__name__})")
print(f"Idade: {idade} (tipo: {type(idade).__name__})")
print(f"Salario: R$ {salario:.2f} (tipo: {type(salario).__name__})")
print(f"Ativa: {esta_ativa} (tipo: {type(esta_ativa).__name__})")
print()


# --- 2. ENTRADA E SAIDA ---

print("=" * 50)
print("  DEMONSTRACAO - ENTRADA E SAIDA")
print("=" * 50)

nome_usuario = input("Digite seu nome: ")
print(f"Ola, {nome_usuario}! Bem-vindo ao curso de Python.")
print()


# --- 3. CONVERSAO DE TIPOS ---

print("=" * 50)
print("  DEMONSTRACAO - CONVERSAO DE TIPOS")
print("=" * 50)

idade_texto = input("Digite sua idade: ")
print(f"Antes da conversao: '{idade_texto}' (tipo: {type(idade_texto).__name__})")

idade_numero = int(idade_texto)
print(f"Depois da conversao: {idade_numero} (tipo: {type(idade_numero).__name__})")

ano_nascimento = 2026 - idade_numero
print(f"Voce nasceu aproximadamente em {ano_nascimento}.")
print()


# --- 4. CONDICIONAIS ---

print("=" * 50)
print("  DEMONSTRACAO - CONDICIONAIS")
print("=" * 50)

valor_compra = float(input("Digite o valor da compra: R$ "))

# Regras de desconto
DESCONTO_ALTO = 0.15       # 15% para compras acima de R$ 500
DESCONTO_MEDIO = 0.10      # 10% para compras acima de R$ 200
DESCONTO_NENHUM = 0.0

if valor_compra >= 500:
    taxa_desconto = DESCONTO_ALTO
    print("Voce ganhou 15% de desconto!")
elif valor_compra >= 200:
    taxa_desconto = DESCONTO_MEDIO
    print("Voce ganhou 10% de desconto!")
else:
    taxa_desconto = DESCONTO_NENHUM
    print("Sem desconto para esta compra.")

valor_desconto = valor_compra * taxa_desconto
valor_final = valor_compra - valor_desconto
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
print()


# --- 5. LACOS DE REPETICAO ---

print("=" * 50)
print("  DEMONSTRACAO - LACOS DE REPETICAO")
print("=" * 50)

# Laco for: tabuada
numero = int(input("Digite um numero para ver a tabuada: "))
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"  {numero} x {i} = {resultado}")

# Laco while: adivinhar numero
print("\n--- Jogo: Adivinhe o numero ---")
numero_secreto = 7
tentativas = 0
MAX_TENTATIVAS = 3

while tentativas < MAX_TENTATIVAS:
    palpite = int(input(f"Tentativa {tentativas + 1}/{MAX_TENTATIVAS} - Chute um numero de 1 a 10: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabens! Voce acertou em {tentativas} tentativa(s)!")
        break
    elif palpite < numero_secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")
else:
    # Este bloco executa se o while terminar sem break
    print(f"Suas tentativas acabaram! O numero era {numero_secreto}.")
print()


# --- 6. FUNCOES ---

print("=" * 50)
print("  DEMONSTRACAO - FUNCOES")
print("=" * 50)


def calcular_imposto(salario, taxa=0.10):
    """Calcula o valor do imposto sobre o salario."""
    return salario * taxa


def calcular_salario_liquido(salario_bruto):
    """Calcula o salario liquido apos descontos."""
    imposto = calcular_imposto(salario_bruto)
    inss = salario_bruto * 0.08  # 8% de INSS (simplificado)
    liquido = salario_bruto - imposto - inss
    return liquido


def exibir_contracheque(nome, salario_bruto):
    """Exibe um contracheque simplificado."""
    imposto = calcular_imposto(salario_bruto)
    inss = salario_bruto * 0.08
    liquido = calcular_salario_liquido(salario_bruto)

    print("\n--- CONTRACHEQUE ---")
    print(f"Funcionario: {nome}")
    print(f"Salario bruto:  R$ {salario_bruto:.2f}")
    print(f"Imposto (10%):  R$ {imposto:.2f}")
    print(f"INSS (8%):      R$ {inss:.2f}")
    print(f"Salario liquido: R$ {liquido:.2f}")
    print("--------------------")


# Usando as funcoes
nome_func = input("Nome do funcionario: ")
salario_func = float(input("Salario bruto: R$ "))
exibir_contracheque(nome_func, salario_func)
print()


# --- 7. TRATAMENTO DE ERROS ---

print("=" * 50)
print("  DEMONSTRACAO - TRATAMENTO DE ERROS")
print("=" * 50)


def ler_numero_seguro(mensagem):
    """Le um numero do usuario, repetindo ate receber um valor valido."""
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Erro: por favor, digite um numero valido!")


print("Tente digitar uma letra para ver o tratamento de erro:")
numero_seguro = ler_numero_seguro("Digite um numero qualquer: ")
print(f"Voce digitou: {numero_seguro}")
print()


# --- ENCERRAMENTO ---

print("=" * 50)
print("  FIM DA DEMONSTRACAO")
print("  Agora faca os exercicios na pasta exercises/")
print("  e o projeto na pasta project/")
print("=" * 50)
