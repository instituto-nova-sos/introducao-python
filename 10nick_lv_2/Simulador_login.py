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
            print(f'Senha incorreta ou usuário Você só tem mais {tentativas} tentativas' )
        else:
            print('Usuário bloqueado no dispositivo!' )
           