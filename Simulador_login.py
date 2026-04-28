usuario_correto = "admin"
senha_correta = "1234"
MAX_TENTATIVAS = 3

while tentativas < MAX_TENTATIVAS
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    if nome == usuario_correto and senha == senha_correta:
        print(f'Bem vindo {nome}! ')
    break
    else:
        tentativas += 1






