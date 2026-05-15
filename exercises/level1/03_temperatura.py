# =============================================
#  NIVEL 1 - EXERCICIO 3: Conversor de temperatura
#  SOS Capacita - Introducao a Python
# =============================================
# Execute com: python exercises/level1/03_temperatura.py
# =============================================
#
# Peca ao usuario uma temperatura em Celsius.
# Converta para Fahrenheit e exiba o resultado.
#
# Formula: F = C * 9/5 + 32
#
# Exemplo de saida esperada:
#   Digite a temperatura em Celsius: 30
#   30.0°C equivale a 86.0°F
#python exercises/level1/03_temperatura.pypython exercises/level1/03_temperatura.py
# Dica: Use float() para permitir numeros decimais.
# -----------------------------------------------

# Escreva seu codigo aqui:
tempc = float(input("Digite a temperatura em ºCelsius: "))
tempF = tempc * 9/5 + 32

print(tempc,"ºC equivale a", tempF,"ºF")