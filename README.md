# Introducao a Python - SOS Capacita

## De Algoritmos para Codigo Real

---

## 1. Visao Geral da Aula

### Objetivo

Nesta aula, voce vai dar o salto mais importante da sua jornada como desenvolvedor: **sair do pseudocodigo e escrever codigo real que o computador executa**.

Tudo o que voce aprendeu ate agora - variaveis, condicionais, lacos de repeticao, logica - continua valendo. A diferenca e que agora voce vai escrever em uma linguagem que o computador entende de verdade.

### Por que Python?

Python e uma das linguagens mais usadas no mundo. Ela aparece em:

- **Backend web** - sistemas como Instagram, Spotify e Netflix usam Python
- **Ciencia de dados** - analise de dados, graficos, relatorios
- **Inteligencia artificial** - a maioria dos modelos de IA e treinada com Python
- **Automacao** - scripts que automatizam tarefas repetitivas
- **Financas** - analise de mercado, controle financeiro

Empresas contratam desenvolvedores Python para cargos junior com frequencia. E uma linguagem excelente para comecar porque sua sintaxe e limpa e legivel - quase como pseudocodigo.

### Conexao com o que voce ja sabe

| Portugol (pseudocodigo)         | Python                        |
|--------------------------------|-------------------------------|
| `escreva("Ola")`              | `print("Ola")`               |
| `leia(nome)`                  | `nome = input("Nome: ")`     |
| `se (idade >= 18) entao`      | `if idade >= 18:`             |
| `enquanto (x < 10) faca`      | `while x < 10:`              |
| `para i de 1 ate 10 faca`     | `for i in range(1, 11):`     |
| `funcao soma(a, b)`           | `def soma(a, b):`            |

Perceba: a logica e a mesma. O que muda e a forma de escrever.

---

## 2. Como o Codigo Realmente Funciona

### Do arquivo ate a execucao

Quando voce escreve um arquivo chamado `main.py`, voce esta criando um **arquivo de texto** com instrucoes. Esse arquivo nao faz nada sozinho.

Para o computador executar essas instrucoes, voce precisa do **interpretador Python**. O processo e:

```
Voce escreve o codigo (main.py)
        |
        v
O interpretador Python le o arquivo linha por linha
        |
        v
Cada linha e traduzida e executada imediatamente
        |
        v
O resultado aparece no terminal
```

Para executar, voce abre o terminal e digita:

```bash
python main.py
```

### Tipos de erro

Existem dois tipos de erro que voce vai encontrar:

**Erro de execucao (runtime error)** - o programa quebra no meio da execucao:

```python
# Isso vai dar erro porque voce nao pode dividir por zero
resultado = 10 / 0
```

**Erro de logica** - o programa roda sem quebrar, mas o resultado esta errado:

```python
# Queremos calcular 10% de desconto, mas a conta esta errada
preco = 100
desconto = preco * 10  # Errado! Deveria ser preco * 0.10
# O programa roda, mas o desconto fica 1000 em vez de 10
```

O erro de logica e o mais perigoso porque o programa nao avisa que esta errado. Por isso, **testar mentalmente** (teste de mesa) e tao importante.

---

## 3. Variaveis e Tipos de Dados

### O que e uma variavel?

Uma variavel e um **nome que aponta para um valor na memoria do computador**.

Imagine que a memoria do computador e um grande armario com gavetas. Quando voce cria uma variavel, voce esta colocando uma etiqueta em uma gaveta e guardando um valor dentro dela.

```python
idade = 25
nome = "Maria"
salario = 3500.50
ativo = True
```

### Tipos de dados fundamentais

| Tipo    | O que guarda         | Exemplo              |
|---------|---------------------|----------------------|
| `int`   | Numeros inteiros     | `42`, `-3`, `0`      |
| `float` | Numeros decimais     | `3.14`, `-0.5`       |
| `str`   | Texto (strings)      | `"Ola"`, `"Python"`  |
| `bool`  | Verdadeiro ou falso  | `True`, `False`      |

### Tipagem dinamica

Em Python, voce **nao precisa declarar o tipo** da variavel. O Python descobre sozinho:

```python
x = 10        # Python sabe que e int
x = "texto"   # Agora x e str - Python aceita isso sem problema
```

Isso e chamado de **tipagem dinamica**. E pratico, mas exige atencao: voce precisa saber qual tipo esta em cada variavel para evitar erros.

```python
idade = "25"       # Isso e uma STRING, nao um numero!
resultado = idade + 5  # ERRO! Nao pode somar string com numero
```

### Verificando o tipo

Use `type()` para descobrir o tipo de uma variavel:

```python
salario = 3500.50
print(type(salario))  # <class 'float'>
```

### Exemplos do mundo real

```python
# Cadastro de funcionario
nome_funcionario = "Carlos Silva"
idade_funcionario = 28
salario_base = 2800.00
esta_ativo = True

# Produto em loja
nome_produto = "Notebook Dell"
preco_produto = 4299.90
quantidade_estoque = 15
disponivel = True
```

---

## 4. Entrada e Saida de Dados

### Saida com print()

O `print()` mostra informacoes na tela (terminal):

```python
print("Bem-vindo ao sistema!")
print("O resultado e:", 42)
```

Voce pode formatar a saida usando **f-strings** (o jeito moderno):

```python
nome = "Ana"
idade = 22
print(f"Nome: {nome}, Idade: {idade}")
# Saida: Nome: Ana, Idade: 22
```

### Entrada com input()

O `input()` **sempre retorna uma string**. Isso e muito importante:

```python
nome = input("Digite seu nome: ")  # Retorna string - ok para nome

idade = input("Digite sua idade: ")  # Retorna string - CUIDADO!
# Se voce digitar 25, a variavel 'idade' contem "25" (texto), nao 25 (numero)
```

### Conversao de tipos

Para trabalhar com numeros vindos do `input()`, voce precisa converter:

```python
idade = int(input("Digite sua idade: "))       # Converte para inteiro
salario = float(input("Digite seu salario: "))  # Converte para decimal
```

**Cuidado:** se o usuario digitar algo que nao e numero, o programa quebra:

```python
idade = int(input("Digite sua idade: "))
# Se o usuario digitar "abc", da erro: ValueError
```

Mais adiante, voce vai aprender a tratar isso com `try/except`.

---

## 5. Estruturas Condicionais (if / elif / else)

### Tomando decisoes no codigo

Toda aplicacao real precisa tomar decisoes. Um sistema de banco decide se aprova um emprestimo. Um site decide se o usuario pode acessar uma pagina. Um caixa decide se aplica desconto.

### Sintaxe

```python
if condicao:
    # codigo executado se a condicao for verdadeira
elif outra_condicao:
    # codigo executado se a primeira for falsa e esta for verdadeira
else:
    # codigo executado se nenhuma condicao anterior for verdadeira
```

**Importante:** em Python, a indentacao (espacos no inicio da linha) define o bloco de codigo. Use **4 espacos** (ou Tab) de forma consistente.

### Operadores de comparacao

| Operador | Significado       | Exemplo        |
|----------|------------------|----------------|
| `==`     | Igual a           | `x == 10`      |
| `!=`     | Diferente de      | `x != 10`      |
| `>`      | Maior que         | `x > 10`       |
| `<`      | Menor que         | `x < 10`       |
| `>=`     | Maior ou igual    | `x >= 10`      |
| `<=`     | Menor ou igual    | `x <= 10`      |

### Operadores logicos

| Operador | Significado                          |
|----------|--------------------------------------|
| `and`    | Verdadeiro se AMBOS forem verdadeiros|
| `or`     | Verdadeiro se PELO MENOS UM for      |
| `not`    | Inverte o valor logico               |

### Exemplo 1: Validacao de idade

```python
idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade invalida!")
elif idade < 18:
    print("Voce e menor de idade.")
elif idade < 60:
    print("Voce e adulto.")
else:
    print("Voce e idoso.")
```

**Teste de mesa** - simulando a execucao com idade = 25:
1. `idade` recebe 25
2. `idade < 0`? 25 < 0? **Falso** - pula
3. `idade < 18`? 25 < 18? **Falso** - pula
4. `idade < 60`? 25 < 60? **Verdadeiro** - entra aqui
5. Imprime: "Voce e adulto."

### Exemplo 2: Sistema de login simples

```python
usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Usuario: ")
senha = input("Senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login realizado com sucesso!")
else:
    print("Usuario ou senha incorretos.")
```

### Exemplo 3: Calculo de desconto

```python
valor_compra = float(input("Valor da compra: R$ "))

if valor_compra >= 500:
    desconto = 0.15  # 15% de desconto
elif valor_compra >= 200:
    desconto = 0.10  # 10% de desconto
else:
    desconto = 0.0   # Sem desconto

valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
```

### Erro comum: confundir `=` com `==`

```python
# ERRADO - isso atribui valor, nao compara
if x = 10:

# CORRETO - isso compara
if x == 10:
```

---

## 6. Lacos de Repeticao (for / while)

### Por que precisamos de lacos?

Imagine que voce precisa imprimir os numeros de 1 a 100. Sem lacos, voce precisaria de 100 linhas de `print()`. Com um laco, voce resolve em 2 linhas.

No Portugol, voce ja usou `para` e `enquanto`. Agora vamos ver como funciona em Python.

### Laco for - quando voce sabe quantas vezes repetir

```python
# Imprimir numeros de 1 a 10
for i in range(1, 11):
    print(i)
```

**Entendendo o `range()`:**

| Chamada           | Gera                    |
|-------------------|------------------------|
| `range(5)`        | 0, 1, 2, 3, 4          |
| `range(1, 6)`     | 1, 2, 3, 4, 5          |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8          |

**Atencao:** o ultimo numero **nao** e incluido. `range(1, 11)` vai de 1 ate 10.

### Laco while - quando voce nao sabe quantas vezes vai repetir

```python
# Pedir senha ate o usuario acertar
senha_correta = "1234"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")

print("Acesso liberado!")
```

### Quando usar cada um?

| Situacao                                    | Use        |
|--------------------------------------------|------------|
| Repetir um numero fixo de vezes            | `for`      |
| Percorrer uma lista de itens               | `for`      |
| Repetir ate uma condicao mudar             | `while`    |
| Validar entrada do usuario                 | `while`    |

### Exemplo: Somatorio

```python
# Somar todos os numeros de 1 a 100
soma = 0
for i in range(1, 101):
    soma = soma + i

print(f"A soma de 1 a 100 e: {soma}")
```

**Teste de mesa** (primeiras iteracoes):

| Iteracao | `i` | `soma` antes | `soma` depois |
|----------|-----|-------------|--------------|
| 1        | 1   | 0           | 1            |
| 2        | 2   | 1           | 3            |
| 3        | 3   | 3           | 6            |
| 4        | 4   | 6           | 10           |
| ...      | ... | ...         | ...          |

### PERIGO: Laco infinito

Um laco infinito acontece quando a condicao do `while` **nunca se torna falsa**:

```python
# LACO INFINITO - o programa nunca para!
x = 1
while x > 0:
    print(x)
    x = x + 1  # x so aumenta, nunca fica <= 0
```

**Como evitar:**
1. Sempre garanta que a condicao do `while` vai mudar em algum momento
2. Use `break` para sair de um laco quando necessario
3. Teste mentalmente: "essa condicao vai ser falsa em algum momento?"

### Comandos uteis dentro de lacos

```python
# break - sai do laco imediatamente
for i in range(1, 100):
    if i == 5:
        break  # Para quando i chega em 5
    print(i)
# Imprime: 1, 2, 3, 4

# continue - pula para a proxima iteracao
for i in range(1, 6):
    if i == 3:
        continue  # Pula o 3
    print(i)
# Imprime: 1, 2, 4, 5
```

---

## 7. Funcoes

### Por que funcoes sao essenciais?

Imagine que voce precisa calcular desconto em 10 lugares diferentes do seu programa. Sem funcoes, voce copiaria o mesmo codigo 10 vezes. Se a regra de desconto mudar, voce precisaria alterar 10 trechos.

Com funcoes, voce escreve a logica **uma vez** e usa onde precisar. Se a regra mudar, altera em **um lugar so**.

Isso se chama **reutilizacao de codigo** e e um dos principios mais importantes da programacao profissional.

### Sintaxe basica

```python
def nome_da_funcao(parametro1, parametro2):
    # codigo da funcao
    return resultado
```

### Exemplo 1: Funcao simples

```python
def calcular_desconto(preco, percentual):
    """Calcula o valor do desconto sobre um preco."""
    valor_desconto = preco * (percentual / 100)
    return valor_desconto

# Usando a funcao
desconto = calcular_desconto(200, 10)
print(f"Desconto: R$ {desconto:.2f}")  # Desconto: R$ 20.00
```

### Exemplo 2: Funcao com validacao

```python
def validar_idade(idade):
    """Verifica se a idade e valida para cadastro."""
    if idade < 0 or idade > 150:
        return False
    return True

# Usando a funcao
idade_digitada = int(input("Idade: "))
if validar_idade(idade_digitada):
    print("Idade valida!")
else:
    print("Idade invalida!")
```

### Exemplo 3: Funcao sem retorno

Nem toda funcao precisa retornar um valor. Algumas apenas executam uma acao:

```python
def exibir_cabecalho(titulo):
    """Exibe um cabecalho formatado."""
    print("=" * 40)
    print(f"  {titulo}")
    print("=" * 40)

exibir_cabecalho("SISTEMA FINANCEIRO")
```

### Parametros com valor padrao

```python
def calcular_imposto(valor, taxa=0.10):
    """Calcula imposto. Taxa padrao: 10%."""
    return valor * taxa

# Usando taxa padrao (10%)
imposto1 = calcular_imposto(1000)       # 100.0

# Usando taxa personalizada (15%)
imposto2 = calcular_imposto(1000, 0.15)  # 150.0
```

### Principios de boas funcoes

1. **Uma funcao deve fazer UMA coisa** - se ela faz muitas coisas, divida em funcoes menores
2. **Nome claro** - o nome deve dizer o que ela faz: `calcular_desconto`, `validar_email`
3. **Poucas linhas** - funcoes muito longas sao dificeis de entender e manter
4. **Parametros claros** - nomes de parametros devem ser descritivos

---

## 8. Tratamento de Erros (Introducao)

### Por que tratar erros?

Em um ambiente profissional, **o sistema nao pode simplesmente quebrar**. Imagine um caixa eletronico que trava porque alguem digitou uma letra em vez de numero. Isso e inaceitavel.

O tratamento de erros permite que o programa **lide com situacoes inesperadas** sem parar de funcionar.

### try / except

```python
try:
    # Codigo que pode dar erro
    idade = int(input("Digite sua idade: "))
    print(f"Sua idade e {idade}")
except ValueError:
    # Codigo executado se o erro acontecer
    print("Erro: digite um numero valido!")
```

### Exemplo pratico: entrada segura

```python
def ler_numero(mensagem):
    """Le um numero do usuario, repetindo ate receber um valor valido."""
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Erro: digite um numero valido!")

# Agora essa funcao NUNCA vai quebrar o programa
salario = ler_numero("Digite seu salario: ")
print(f"Salario informado: R$ {salario:.2f}")
```

### Quando usar try/except

- Ao receber dados do usuario (input)
- Ao ler arquivos
- Ao fazer calculos que podem falhar (divisao por zero)
- Em qualquer ponto onde dados externos entram no sistema

---

## 9. Boas Praticas (Nivel Iniciante Profissional)

### 1. Nomes de variaveis claros

```python
# RUIM - ninguem sabe o que e x, y, z
x = 2500
y = x * 0.1
z = x - y

# BOM - qualquer pessoa entende o codigo
salario_bruto = 2500
imposto = salario_bruto * 0.1
salario_liquido = salario_bruto - imposto
```

### 2. Evite numeros magicos

Numeros magicos sao valores numericos soltos no codigo sem explicacao:

```python
# RUIM - o que e 0.15? Por que 500?
if valor > 500:
    desconto = valor * 0.15

# BOM - fica claro o que cada valor representa
VALOR_MINIMO_DESCONTO = 500
TAXA_DESCONTO = 0.15

if valor > VALOR_MINIMO_DESCONTO:
    desconto = valor * TAXA_DESCONTO
```

Constantes em Python sao escritas em **LETRAS_MAIUSCULAS** por convencao.

### 3. Legibilidade

```python
# RUIM - tudo apertado, dificil de ler
if(a>b and c<d or e==f):resultado=a*b-c

# BOM - espacos e organizacao
if (a > b and c < d) or e == f:
    resultado = a * b - c
```

### 4. Funcoes pequenas

Se sua funcao tem mais de 20 linhas, provavelmente ela esta fazendo coisas demais. Divida em funcoes menores.

### 5. Comentarios uteis

```python
# RUIM - o comentario repete o que o codigo ja diz
x = x + 1  # Soma 1 a x

# BOM - o comentario explica o PORQUE
tentativas = tentativas + 1  # Conta tentativas para limitar a 3
```

---

## 10. Teste de Mesa - Simulando a Execucao

O teste de mesa e uma tecnica onde voce **simula a execucao do programa manualmente**, anotando o valor de cada variavel a cada passo.

### Exemplo

```python
def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma = soma + nota
    media = soma / len(notas)
    return media

resultado = calcular_media([7, 8, 6])
```

**Teste de mesa:**

| Passo | Instrucao              | `soma` | `nota` | `media` |
|-------|------------------------|--------|--------|---------|
| 1     | `soma = 0`             | 0      | -      | -       |
| 2     | `nota = 7`, soma += 7  | 7      | 7      | -       |
| 3     | `nota = 8`, soma += 8  | 15     | 8      | -       |
| 4     | `nota = 6`, soma += 6  | 21     | 6      | -       |
| 5     | `media = 21 / 3`       | 21     | 6      | 7.0     |
| 6     | `return 7.0`           | -      | -      | 7.0     |

Essa tecnica ajuda voce a **encontrar erros de logica** antes mesmo de rodar o programa.

---

## Exercicios

Os exercicios estao organizados em niveis progressivos na pasta `exercises/`.
Cada exercicio fica em seu proprio arquivo, dentro da pasta do nivel correspondente:

- **`exercises/level1/`** - Exercicios basicos (variaveis, entrada/saida, condicionais simples)
- **`exercises/level2/`** - Exercicios intermediarios (condicionais compostas, lacos, logica)
- **`exercises/level3/`** - Problemas do mundo real (validacao, carrinho de compras, sistema bancario)

Os arquivos sao numerados (`01_soma.py`, `02_par_impar.py`, ...). Comece pelo
exercicio 01 de cada nivel e siga em ordem. Execute um exercicio com:

```bash
python exercises/level1/01_soma.py
```

Na pasta `exercises/level3/`, voce tambem encontrara um desafio de funcoes
(`04_funcoes.py`).

---

## Mini Projeto: Sistema de Controle Financeiro

O arquivo `project/financial_system.py` contem um projeto completo que une tudo que voce aprendeu:

- Variaveis e tipos de dados
- Entrada e saida
- Condicionais
- Lacos de repeticao
- Funcoes
- Tratamento de erros

O sistema permite:
- Adicionar receitas (entradas de dinheiro)
- Adicionar despesas (saidas de dinheiro)
- Consultar o saldo atual
- Ver o extrato completo

Estude o codigo, entenda cada funcao, e tente modificar para adicionar novas funcionalidades.

---

## Proximo Passo

Depois de dominar este conteudo, voce estara pronto para:

- **Listas e dicionarios** - estruturas de dados mais poderosas
- **Manipulacao de arquivos** - salvar e ler dados de arquivos
- **Modulos e bibliotecas** - usar codigo feito por outras pessoas
- **Orientacao a objetos** - organizar codigo em classes

Lembre-se: **programar e resolver problemas**. A linguagem e apenas a ferramenta. A logica que voce ja aprendeu e o que realmente importa.
