todos = []
par = []
impar = []

for i in range(1, 11):
    while True:
        entrada = input(f'Digite o {i}° número: ').strip() 

        if entrada.replace('-', '', 1).isdigit() and entrada != "":
            num = int(entrada)
            break 
        else:
            print(f" ATENÇÃO: '{entrada}' NÃO É UM NÚMERO VÁLIDO!")
    todos.append(num)

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"""
------------------------------------------
Lista completa: {todos}

------------------------------------------

PARES ({len(par)} números): {par}
Soma dos pares: {sum(par)}

------------------------------------------

ÍMPARES ({len(impar)} números): {impar}
Soma dos ímpares: {sum(impar)}
------------------------------------------
""")