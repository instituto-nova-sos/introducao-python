# =============================================
#  NIVEL 2 - EXERCICIO 3: Simulacao de login
#  SOS Capacita - Introducao a Python
# =============================================
# Execute com: python exercises/level2/03_login.py
# =============================================
#
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
            print(f'Senha ou usuário incorreta! Você só tem mais {tentativas} tentativas' )
        else:
            print('Usuário bloqueado no dispositivo!' )
           