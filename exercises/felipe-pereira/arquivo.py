nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

print("----- RESULTADO -----")

if idade >= 18:
    print(nome + ", você é maior de idade!")
else:
    print(nome + ", você é menor de idade!")

print("Obrigado por usar o programa!")