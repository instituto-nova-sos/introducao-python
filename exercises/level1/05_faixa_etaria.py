# =============================================
#  NIVEL 1 - EXERCICIO 5: Classificacao por faixa etaria
#  SOS Capacita - Introducao a Python
# =============================================
# Execute com: python exercises/level1/05_faixa_etaria.py
# =============================================
#
# Peca a idade do usuario e classifique:
#   - 0 a 12: Crianca
#   - 13 a 17: Adolescente
#   - 18 a 59: Adulto
#   - 60 ou mais: Idoso
#
# Se a idade for negativa, exiba "Idade invalida".
#
# Exemplo de saida esperada:
#   Digite sua idade: 25
#   Classificacao: Adulto
# -----------------------------------------------

# Escreva seu codigo aqui:
idade= float(input('digite sua idade: '))
if  idade <= 0: 
    print("É sério cara? quer atenção?😡")

elif  0 < idade <= 12:
    print("Você ê ainda é um(a) pivéte👶")

elif 12 < idade <= 17:
    print("você é um aborrecente😤")

elif 17 < idade <= 29:
    print("Você é um jovem adulto que está começando a crescer na vida😯")

elif 29 < idade <= 59:
    print("Você é um adulto com muitas experiências e hitórias pra contar🤩")

elif 59 < idade <= 110:
    print("Você é um idoso um velha guarda 🔥")

elif 110 < idade:
    print("Valeu Noé! 😑👍")