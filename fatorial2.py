while True:
    n = input('Digite um número: ')
    try:
        int(n)
        if n < 0:
            print("Não existe fatorial de número negativo!")
            continue
        else:
            fatorial = 1
            for i in range(n, 0, -1):
                fatorial *= i  
                
                if i == 1:
                    print(f"{i} = ", end="")
                else:
                    print(f"{i} x ", end="")
            print (f'{fatorial}')
        break
            

    except ValueError:
        print('digite um número válido por favor! ')