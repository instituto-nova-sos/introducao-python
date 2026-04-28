N1 = float(input('Nota do priemiro trimestre: '))
N2 = float(input('Nota do segundo trimestre: '))
N3 = float(input('Nota do terceiro trimestre: '))
N4 = float(input('Nota do quarto trimestre: '))
media = (N1 + N2 + N3 + N4)/4
faltava = 7 - media

if media < 0:
    print(f'{media} Ah não.... não acredito nisso em negativo??? kakakakaakk o professor provavelmente tem raiva de você meu filho kkkkkkkkkk')

elif media < 1.5:
    print(f'{media} REPROVADO!!!!!!!! "Não é possivel! Você é do tipo que nunca pisou na escola se matriculou e tirou a vaga de quem precisa🤬"')

elif media < 5:
    print(f'SUA MÉDIA FOI {media} kkkkkkk REPROVADO! Parabéns você é um péssimo aluno 👏🤮 "faltar {faltava:.1f} pontos pra passar é sacanagem hein!"')

elif media < 7:
    if faltava == 1:
        print(f'{media} 🤣 Vai estudar nas férias e fazer recuperação por causa de {faltava:.1f} ponto kakakakaakka ')
    else:
        print(f'{media} 🤣 Vai estudar nas férias e fazer recuperação por causa de {faltava:.1f} pontos kakakakaakka ')

elif media > 10:
    print (f'{media} NÃO É POSSIVEL..... QUEM FOI O PROFESSOR PRA IR PRO OLHO DA RUA')

elif media == 10:
    print (f'{media}??????? Você com certeza é super dotado nem sei o que ainda esta fazendo nessa escola')

elif media > 9:
    print (f'{media} APROVADO😝🥳 PARABÉNS!!!! Você é um aluno que provavelmente senta lá na frente e puxa saco de professor 😠')

elif media > 8:
    print (f'{media} APROVADO👏 Parece que alguem se esforçou esse ano! {media} pontos é muito bom! Se continuar assim ano que vem tu melhora mais ainda!!!')

elif media >= 7:
    print (f'{media} aprovado... Éh.. Você passou cravado ná média... Não tenho muita coisa pra falar pra você 🥱')




