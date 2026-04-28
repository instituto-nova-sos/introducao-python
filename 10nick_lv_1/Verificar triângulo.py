l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

if (l1 + l2 > l3) and (l2 + l3 > l1) and (l3 + l1 > l2): #Saber se o triângulo é valido pra não cair em um tringulo de 2 x 2 x 100
    S = (l1 + l2 + l3) / 2 #Formula do semiperímetro
    A = (S * (S - l1) * (S - l2) * (S - l3)) ** 0.5   #Formula HERON  pra descobrir a área do triângulo        

    print(f'✅ É um triângulo válido! Com uma área de {A:.2f}m²')

else:
    print(f"❌ Error. Desculpe amigo mas esse triângulo é inválido! {l1} x {l2} x {l3}  não dá né? ")