Carro_medio_no_brasil = "100.000,50"

# Troca a vírgula por ponto para padronizar os separadores: "100.000.50"
txt = Carro_medio_no_brasil.replace(',', '.')

# .split('.') -> Cria uma lista cortando onde tem ponto. 
# Resultado: ['100', '000', '50']
limpo = txt.split('.') 

# [:-1] -> Slice (fatiamento). Pega do início ATÉ o penúltimo item.
# .join() -> Une esses itens ('100' e '000') sem nada entre eles.
# Resultado: "100000"
corte = "".join(limpo[:-1]) 

# limpo[-1] -> Índice negativo. Acessa especificamente o ÚLTIMO item da lista.
# Montamos a string final: "100000" + "." + "50"
txt = corte + "." + limpo[-1] 

print(f'Um carro no brasil custa {txt}')