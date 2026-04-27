# =============================================
#  NIVEL 3 - EXERCICIO 3: Validacao de entrada com laco
#  SOS Capacita - Introducao a Python
# =============================================
# Execute com: python exercises/level3/03_cadastro.py
# =============================================
#
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
