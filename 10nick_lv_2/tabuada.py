while True:
    try:
        numeros = int(input(f'Digite o número: '))
        print(F'Tabuada do número {numeros}:')
        for n in range(1, 11):
            tabuada = n * numeros
            print(f' {n} x {numeros} = {tabuada} \n')

        continuar = input("\n deseja continuar? s/n: ").strip().lower()
        if continuar != 's':
             print('Encerrando!')
             break
    except ValueError:
     print("Por favor, digite um número inteiro válido.")