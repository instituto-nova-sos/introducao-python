nome_correto = 'admin'
senha_correta = '1234'
tentativas = int(3)

while tentativas > 0:
    nome = input('Digite o nome de usuário: ')
    senha = input('Digite sua senha: ')
    if nome == nome_correto and senha == senha_correta:
        print(f'Bem vindo {nome}!')
        break    
    tentativas -= 1
    mensagem = f'Nome de usuário ou senha incorretos. Você só tem mais {tentativas} tentativas.' if tentativas > 0 else 'Número de tentativas esgotado. Acesso bloqueado.' 
    print(mensagem)
