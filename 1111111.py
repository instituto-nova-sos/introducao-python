entrada = (input('Digite o seu salário atual por favor: '))

#Limpesa----------------------------------------------------------------------------
txt = entrada.replace('R$', '').replace('$','').replace('reais', '').strip()

if ',' in txt: #Se existe , no texto
    if txt.count (',') > 1: #se o jegue escreveu com 2 , ex: 1,500,50
       partes = txt.split(',')
       corte_final= "".join(partes[:-1])
       txt = corte_final + "." + partes[-1] #AQUI não utilizamos os (:) se não ele nos tráz a lista e não o número
    
    else: #se escreveu do jeito Br    1.500,50 ele vai apagar o ".": 1500,50 e substituir o "," por um "." 1500.50
        txt = txt.replace('.', '')
        txt = txt.replace (',','.')


else: #Se o usuário escreveu o número com 2 pontos ex: 1.500.00
    if txt.count ('.') > 1:  #Aqui detectamos que existem 2 pontos no input
        partes = txt.split('.') #txt.split('.') determinamos qwue onde tem um . ele deve cortar e guardar os valores. ex: 1.500.50 Ele irá gaurdar como (1, 500, 50)
        corte_final= "".join(partes[:-1]) #Aqui ele guarda o ultimo numero da lista como eram (1, 500, 50) ele vai isolar o (50)
        txt = corte_final + "." + partes[-1] #Aqui fazemos a conta partes (1, 500) vai ficar 1500 + o "." + o 50 ficando assim 1500.50 um perfeito float
    
    elif txt.count ('.') == 1: #Se o usuário colocar 1.500 normalmente ele leria como 1 real e 50 centavos 
        txt = txt.replace('.','') #Como aqui eu removi o ponto de 1.500  ele ficou 1500

#IFs e Elifs-------------------------------------------------------------------------
salario_atual = float(txt) #Aqui definimos que a entrada que virou txt é um float
if salario_atual <= 1500.00:
    porcentagem  = 15

elif 1500.00 < salario_atual < 3000.00:
    porcentagem  = 10

else:
    porcentagem  = 5

#Fórmula-----------------------------------------------------------------------------

aumento = (salario_atual * porcentagem) / 100 
novo_salário = salario_atual + aumento

#Output------------------------------------------------------------------------------

print(f"""
      RELATÓRIO SALARIAL:
      ----------------------------------------
      Salario atual:     R${salario_atual:.2f}
      Porcentual:        {porcentagem}%
      Aumento:           R${aumento:.2f}
      Novo salário:      R${novo_salário:.2f}
    -------------------------------------------
 """)
