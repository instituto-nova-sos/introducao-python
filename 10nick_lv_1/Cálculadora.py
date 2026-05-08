       
n1 = float(input('Digite um número: '))
conta = input('digite a operação (+,-,/,*): ')
n2 = float(input('Digite outro número: '))

if conta == "+":
    conta = n1 + n2
    print(f' =  {conta}')

elif conta == "-":
    conta = n1 - n2
    print(f' =  {conta}')

elif conta == "/":
    if n2 !=0:
        conta = n1 / n2
        print(f' = {conta}')
    else: 
        print("Tá dividindo por 0?? quer queimar o PC seu maluco?")

elif conta == "*":
    conta = n1 * n2
    print(f' =  {conta}')

elif conta == "x":
    conta = n1 * n2
    print(f' =  {conta}')