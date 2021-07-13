# Python | Aprendizado do Zero
### Tipos de dados
- Integer (int)  - números inteiros
- String  (str)  - texto 
- Float (float)  - números com casas decimais
- Boolean (bool) - verdadeiro ou falso

### String
- Concatenação. Utilize o símbolo (+)
	- print('Eu estou ' + 'aprendendo')
- *in* verifica se uma expressão está contida em outra e retorna um *boolean*
	- ```print('Lua' in 'Lua')```
- Métodos utéis
	- *find()* encontra um caracter ou um conjunto de caracteres e retorna a posição do primeiro caracter. ```email.find('@')```
	- *casefold()* transforma a string em letras minúsculas respeitando acentuações, diferentemente do *lower()*
	- *captalize()* transforma o primeiro caracter em letra Maiúscula.
	- *isalnum()* verifica se o texto é compoosto por letras e números. retorna um *boolean*
	- *isalpha()* verifica se o texto é composto por letras. retorna um *boolean*
	- *isnumeric()* verifica se o texto é composto por números. retorna um *boolean*
	- *replace()* encontra e substitui o texto. retorna o texto.
	- *split()* separa o texto de acordo com um delimitador. retorna um *list()*
	- *splitline()* separa o texto no *enter*. retorna um *list()*
	- *startswith()* verifica se o texto inicia com um determinado texto.
	- *endswith()* verifica se o texto finaliza com um determinado texto.
	- *strip()* remove caracteres do texto. Por padrão remove espaços em branco no inicio e final do texto.
	- *title()* transforma o primeiro caracter de cada palavra para maiúscula.
	- *upper()* transforma todo o texto em letras maiúsculas.
	- *format()*
		- *:<* Alinha o texto a esquerda na tela
		- *:>* Alinha o texto a direita na tela
		- *:^* Alinha o texto no centro na tela
		- *:+* Insere um sinal na frente do número (independentemente se positivo ou negativo)
		- *:,* Coloca a vírgula como separador de milhar
		- *:_* Coloca o underline como separador de milhar
		- *:e* Formato cientifíco
		- *:f* Número com quantidade fixa de casas decimais
		- *:x* Formato hexadecimal com letras Minúscula (geralmente utilizado em cores)
		- *:X* Formato hexadecimal com letras Maiúscula (geralmente utilizado em cores)
		- *:%* Formato percentual

### Interpolação
- Forma 1: 
```python
print("O valor R$" + variavel + " é total da compra")
```
- Forma 2:
```python
print("O valor R$ {} é total da compra".format(variavel))
```
- Forma 3:
```python
print(f"O valor R$ {variavel} é total da compra")
```

### Variável
- Uma variável é uma localização na memória RAM do computador onde vai ser armazenada temporariamente os dados que são utilizados pelo programa.
- Definir um padrão para nome de variáveis.
	- O nome da variável sempre com letras minúsculas ```nomevariavel```
	- O nome composto utilize *underline* ```nome_variavel```

### Intergindo com o usuário
- *input* => Entrada de dados de teclado.
	- ```nome = input("Qual o seu nome?")```


### Estruturas condicionais
- if => ```if condicao:```
- elif => ```elif condicao:```
- else => ```else:```

Os blocos condicionais são definidos através de identação.

```
if condicao:
	executa tudo que
	estiver dentro da
	identação
```

### Operadores de comparação
- == (igualdade)
- != (diferente)
- > (maior que)
- < (menor que)
- >= (maior ou igual à)
- <= (menor ou igual à)
- in (encontrar um texto ou caracter dentro de outro texto)
- not (verifica o contrário da comparação. Inverte o resultado)

### Operadores lógicos
- and (e)
- or (ou)

## Listas
list() vetor/matriz são a mesma coisa que array. Em Python é dinâmico e podem receber qualquer tipo de dado como valor.

Métodos úteis:
- *list.index('item')* -> encontre o índice de um item na lista.
- *list.append('novo_item')* -> adiciona um elemento no final da lista.
- *list.pop()* -> remove o útlimo elemento da lista.
- *list.pop(indice)* -> remove o elemento através de um determinado índice e retorna-o.
- *list.remove('nome_item')*
- *list.extend(list2)* -> Merge (juntando ou mesclando) listas.
- *list.sort()* -> Ordenação padrão crescente. Para ordenar descrescente passar o parâmentro *reverse=True* ```list.sort(reverse=True)``` 
- *len(list)* -> retorna o tamanho da lista
- *min(list)* -> retorna o menor valor em uma lista. Utilizado em uma lista numerica.
- *max(list)* -> retorna o maior valor em uma lista. Utilizado em uma lista numerica.
- *sum(list)* -> retorna a soma do valores de uma lista. Utilizado em uma lista numerica.
- *list.copy() ou list[:]* -> copia uma lista em outro endereço da memória.
- *Nested list* -> uma lista de listas ou Matriz.
- *extend(list)* -> adiciona elementos na lista.

## Estrutura de repetição
#### for
O for percorre uma lista e cada loop retorna o valor do item.
```
for i in list:
	print(i)
```
- **Enumerate** permite acesso ao índice e ao valor.
```
for indice, item in enumerate(list):
	print("O id {} pertence ao {}".format(indice, item))
```

#### while
loop muito útil para repetir um código indeterminadamente enquanto a condição for verdadeira.
```
produtos = []
while True:
	
	produto = input("Informe o nome do produto: ")
	if not produto:
		break
	produtos.append(produto)

print(produtos)
```

## Tuplas -> tuple()
tuple() -> elementos devem ser separados por vírgula dentro de parenteses ().
- É mais eficiente que as listas
- É imutável
- Acessos aos elementos
```
tupla = ('Fulano', 'de tal', '20-10-2000')
#  por colchetes []
tupla[0]
# Desempacotamento
nome, sobrenome, data_nasc = tupla
```

## Dicionário
dict() -> chave:valor separados por vírgula dentro de chaves {}.
- Chaves são únicas. Caso utilize repetidas o valor será atualizado.
- Acessar elementos no dict() 
	- Forma 1: Utilizamos a chave. ```dicionario['chave']``` dessa forma se a chave não existir retorna um KeyError.
	- Forma 2: via *get()* ```dicionario.get('chave')``` dessa forma se a chave não existir retorna None. Uso recomendado.
- Adicionar elementos no dict() 
	- Forma 1: ```dicionario['chave'] = valor```
	- Forma 2: via *update({})* ```dic1.update({'nova_chave': 'novo_valor'})```. Uso recomendado.
- Remover elementos do dict()
	- Forma 1: ```del dicionario['chave']```
	- Forma 2: ```dicionario.pop('chave')``` retorna o valor removido.
- Limpar o dicionário ```dicionario.clear()```

**Métodos úteis de *dict()***

-	*items()* ```dicionario.items()``` retorna uma lista[] de tuplas().
- *keys()* ```dicionario.keys()``` 
- *values()* ```dicionario.values()```
- *fromkeys()* ```dicionario = dict.fromkeys(list, 0)``` Cria um dicionário com valor padrão 0.
- *zip()* mescla lista e tranforma em tupla

> items(), lembre-se de unpackage.

#### Transformando dict() em list()
```
dicionario = {'notebook asus': 3000, 'notebook acer': 2500, 'notebook samsung': 2800}
dict_chaves = dicionario.keys()
dict_values = dicionario.values()
print(dict_chaves)
print(dict_values)
# Convertendo para list()
list_chaves = list(dict_chaves)
list_values = list(dict_values)
print(list_chaves)
print(list_values)
```

#### Transformando list() ou tuple() em dict()
- Se tiver uma lista utilize o método *fromkeys()* ```dicionario = dict.fromkeys(lista1, 0)```
- Se tiver duas lista utilize o método *tupla = zip(lista1, lista2)* ```dicionario = dict(tupla)```

## Conjunto - set()
Um conjunto de dados apenas com valores e não duplicados. ```conjunto = {'arroz', 'feijão', 'farinha'}```
- Transformando lista em conjunto ```conversao = set(lista)``` assim removemos valores duplicados.

## Range()
- range(tamanho) -> definimos o valor fim pelo tamanho.
- range(inicio, fim) -> definimos o valor de inicio e fim
- range(inicio, fim, passo) -> definimos o vlaor de inicio, fim e de quanto em quantos passos deve pular.


## Iterable
São estrutura de dados que podemos percorrer seus elementos.
- string
- list()
- tuple()
- dict()
- range()
- set()


## funções
Funções em Python são definidas a partir da palavra reservada *def* seguido no nome da função e dois pontos (:)
```def nome_funcao():```
- Retorno de dados nas funções
	- Para retornar dados utilizamos a palavra reservada *return*
- Variáveis dentro do bloco da função só podem ser acessadas dentro do escopo da função.
- Parâmetro nas funções ```def nome_completo(nome, sobrenome)```
- Parâmetro pré-definido ```def nome_completo(nome, sobrenome = "Não informado")```


## Argumentos indefinidos
- *\*args* Position Arguments - n argumentos do tipo tupla.
```
def nome_completo(*args): #definição
	nome = args['nome']
	sobrenome = args['sobrenome']
	idade = args['idade']

print(nome_completo('João', 'Santos', 34))
```
- *\*\*kwargs* Keyword Arguments - n argumentos do tipo dicionário.
```
def nome_completo(**kwargs):
	nome = kwargs['nome']
	sobrenome = kwargs['sobrenome']
	idade = kwargs['idade']

print(nome_completo(nome='João', sobrenome='Santos', idade=34))
```

#### Ordem dos argumentos nos parâmetros
```
def nome_completo(var1, var2, *args, nome="Não informado", **kwargs)
```

# Docstring
Descreve o que a função deve fazer. Além disso os seus parâmentros.
**Exemplo**
```
def nome_completo(nome, sobrenome, idade):
'''
Retorna o nome e sobrenome e idade

Parameters:
nome (str)
sobrenome (str)
idade (int)
Returns:
Retorna o nome completo e idade
'''
nome_completo = nome + " " + sobrenome
return nome_completo, idade
```

# Annotation
Descreve ou informa o tipo de dado dos argumentos e o tipo de dado do retorno
**Exemplo**
```
def nome_completo(nome: str, sobrenome: str, idade: int) -> str:
nome_completo = nome + " " + sobrenome
return nome_completo, idade
```

## Módulos
Para utlizar módulos é necessário fazer o *import*. Entenda módulo como um objeto ou uma *Class* de um arquivo.
- Importando todos os módulos de um objeto.
```
import webbrowser
```
- Importantdo partes especificas de um módulos.
```
from nome_modulo import funcao1, funcao2 ...
```

### Módulos úteis
- time
	- gmtime()
- datetime

### Módulos de gráficos
- *Matplotlib*
```python
import Matplotlib as plt
```
	- plt.plot(eixo_x, eixo_y, tipo_de_grafico)
	- plt.xlabel(rótulo do eixo x)
	- plt.ylabel(rótulo do eixo y)
	- plt.axis([min_eixo_x, max_eixo_x, min_eixo_y, max_eixo_y])
	- plt.show() -> Exibe o gráfico

### Módulo Numpy
O pacote fundamental para computação científica.
```python
import numpy as np
```


## Instalar ou desinstalar módulos ou pacotes
Utilizamos PIP para instalar pacotes ou módulos. PIP é o gerenciador de pactes do Python.
```python
pip install keyboard   # instalar
pip uninstall keyboard # desinstalar

```
## List Comprehension
List Comprehension é um método pythonico para inteirar em lista com maior performance.
**Exemplo de iteração padrão**
```python
precos = [100, 150, 450, 6000]
produtos = ['camisa', 'blusa', 'Fire Tv stick', 'iPhone']

# Aplicar 30% de imposto sobre o preço de cada produto
imposto = []
for preco in precos:
	imposto.append(preco * 0.3)

```
**Exemplo com List Comprehension**
```python
precos = [100, 150, 450, 6000]
produtos = ['camisa', 'blusa', 'Fire Tv stick', 'iPhone']

# Aplicar 30% de imposto sobre o preço de cada produto
imposto = [preco * 0.3 for preco in precos]
```

- Filtrando List Comprehension com if
**Exemplo**
```python
meta = 1000
precos = [100, 150, 450, 6000]
produtos = ['camisa', 'blusa', 'Fire Tv stick', 'iPhone']

lista = [produto for i, produto in enumerate(produtos) if preco[i] > meta]

```

- Filtrando List Comprehension com if e else
Para esse tipo de condição, aplicamos a condição antes do for
**Exemplo**
```python
vendedores = {'Maria': 1500, 'José': 800, 'Pedro': 1100, 'Patricia': 990}
meta = 1000
bonus = 0.1

venderes_bateram_a_meta = [vendedores[item] * bonus if vendedores[item] > meta else 0 for item in vendedores]
```

## Função Map
- sintaxe: map(function, iterable)
```python
produtos = [7000, 11340, 4699, 2999]

def prod(produto):
	return produto * 0.1

nova_lista = list(map(prod, produtos))

print(nova_lista)
```
- O retorno é um objeto e pode ser transformado em *list()*

## sort() ou sorted() -> Ordenação
*sort()* altera a lista original
```python
produtos = ['iPhone', 'Maça', 'alaska', 'Opera', 'firefox']
produtos.sort() # O padrão de ordenação é a tabela ASC
# Para ignorar a ordenação padrão utlizamos o parâmetro key do próprio sort(key=str.casefold) 
produtos.sort(key=str.casefold)
# Se fosse uma função que eu implementei não precisaria informar que pertence ao str
produtos.sort(key=minha_funcao)

# Ordem decrescente
produtos.sort(reverse=True)
```
*sorted()* cria uma nova lista.
```python
nova_lista = sorted(produtos)
```

## Lambda Expression -> Expressões Lambda
São funções anônimas (sem nome) que tem uma linha de código e é atribuída a uma variável através da palavra reservada *lambda*.

**Exemplo de função normal**
```python
def quadrado(num):
	return num ** 2

print(quadrado(3))
```
**Exemplo com lambda**
```python

calcula_quadrado = lambda num: num ** 2

print(calcula_quadrado(5))
```
**Exemplo em um caso real** aplicar 30% de acréscimo em todos os produtos.
```python
produtos = {'iPhone': 7000, 'iMac': 11340, 'iPad': 4699, 'iPod': 2999}

valores_atualizados = list(map(lambda preco: preco * 1.3, produtos))
print(valores_atualizados)
```

## Filter
Filtra um *iterable* e retorna todos os itens onde a função for True.
- sintaxe: filter(function, iterable)
```python
produtos = {'iPhone': 7000, 'iMac': 11340, 'iPad': 4699, 'iPod': 2999}
filtrar_produto_acima5000 = dict(list(filter(lambda item: item[1] > 5000, produtos.items())))

print(filtrar_produto_acima5000)
```
- O retorno é um object filter e transformo em *list()* e depois em *dict()*

## Collections
- *Counter* Podemos utilizar para exibir o top 10 produtos por exemplo, utilizando a função most_common(10)

## Tratamento de Exceções
Métodos úteis:
- *try* tenta executar e *except* faz outra coisa.
- *raise Exception()* ou *raise ValueError()* ou *raise ZeroDivisionError()*
```python
try:
	Tenta executar um código
except:
	Deu um erro inesperado e aqui podemos retornar o erro ou uma mensagem.
	raise ValueError("O @ não foi informado")
else:
	se a execução no try for bem sucedida executa o código que está aqui
finally:
	Independetemente o que acontecer ele será executado

```


## Métodos reservados do Python
- Cria uma lista a partir do texto, quebrando-o no espaço em branco.
```python
texto.split(', ')

```
- Join separa o texto com delimitador definido.
```python
';'.join(list)

```
- Exibe o tipo de dado de uma variável
```python
type(variavel)

```
- Utilizamos quanto não queremos codificar nenhuma instrução para um bloco obrigatório.
```python
pass

```
	- Exemplo:
		```python
			try:
				list.remove('chaveiro')
			except:
				pass
		
		```

> acima o ***except*** é obrigatório, mas como não queremos implementar instruções utilizamos a palavra reservada *pass* para continar o *script*.

## Informações e dicas
- Podemos utilizar o *pass* em trechos que possa gerar erro ou que sejá obrigatório a implementação e não queremos codificar regras de negócio.
- zip() junta duas lista em uma única *zip(precos, produtos)*


# Pandas
É um módulo para Análise de Dados. Excelente para grandes volumes de dados.
## Leitura de arquivos
### CSV
- dataframe -> E uma tipo de tabela.
- Para acessar as colunas acessamos como dicionário, passando a chave.
- Para acessar as linhas acessmos como listas, passando o índice.
- *dataframe.info()*

**Importando arquivos**
```python
import pandas as pd

dataframe_vendas = pd.read_csv(r'nome_arquivo.csv', sep=';') # separador padrão é vírgula
dataframe_clientes = pd.read_csv(r'nome_arquivo.csv', sep=';')
dataframe_lojas = pd.read_csv(r'nome_arquivo.csv', sep=';')
# Para exibir
display(dataframe_vendas)
display(dataframe_clientes)
display(dataframe_lojas)
```

- Removendo Colunas de um *dataframe*
	- *drop()* parâmetro *axis=1*
```python
dataframe_nome.drop(['chave_coluna1', 'chave_coluna2', 'chave_coluna3'], axis=1)

```
- Removendo Linhas de um *dataframs*
	- *drop()* por padrão remove linhas, mas por parâmentro é o *axis=0*
```python
dataframe_nome.drop([0:10]) #remove as linha 0 até 10 exclusive.
```

- Selecionando as colunas necessárias no *dataframe*
```python
dataframe_vendas = dataframe_vendas[['id_produto', 'nome_produto']]
dataframe_clientes = dataframe_clientes[['id_cliente', 'email']]
dataframe_lojas = dataframe_lojas[['id_loja', 'nome_loja']]
```

- Unificando (juntando) *dataframe* 
	- *merge()*
Importante para aplicar o *merge()* as colunas devem ter o mesmo nome nos *dataframes*. Se necessário renomeio o nome da coluna do *dataframe*
```python
novo_dataframe = dataframe_clientes.merge(dataframe_vendas, on='id_produto')
```

- Renomeando colunas
	- *rename(coluna={'de':'para'})*
```python
dataframe_clientes = dataframe_clientes.rename(columns={'emial': 'Email do cliente'})

```

- Agrupar dados no dataframe
	- *groupby('coluna')*
```python

dataframe_vendas_loja  = dataframe_vendas.groupby('nome_coluna').sum()
```

- Ordernar um dataframe
	- *sort_values('coluna')*
```python
dataframe_vendas.sort_values('coluna')

# ordem decrescente
dataframe_vendas.sort_values('coluna', ascending=False)

```

> Analise idmax() e idmin()
> Problemas com charset podem ser resovidos com parâmetro *encoding='utf-8' ou encoding='iso-8859-1*

# Expressões Lambdas
Expressões Lambdas ou Lambdas são funções anônimas.Para criar funções lambdas utilizamos a palavra reservada *lambda*

```python
# um uso de lambda, não convencional

calc = lambda x: 3 * x

# chamada
calc(4)
```

Expressões *lambdas* com multiplos parâmetros
```python
nome_completo = lambda nome, sobrenome: "Olá "+ nome.strip().title() +" "+sobrenome.strip().title()
```

Exemplo mais útil para expressões lambdas
```python
# f(x) função quadratica
def funcao_quadratica(a,b,c):
    return lambda x: a * x ** 2 + b * x + c

solucao = funcao_quadratica(3, 4, 2)

solucao(2)
# 3 * 2**2 + 4 * 2 + 2
# 3 * 4 + 8 + 2
# 12 + 10
# 22
```

# Função Map
*Map* é uma função que recebe 2 parâmetros, o primeiro é uma função e o segundo um iterável. **map(function, iteravel)** retorna um *Map Object*
```python
import math

def area(raio):
    return math.pi * raio ** 2


raios = [14,3,0.4, 8.4]

areas = map(area, raio)

```
Agora a operação acima usando **lambda**
```python
print(list(map(lambda r: math.pi * r ** 2, raios)))
```

> O **map()** depois de utilizado é excluído da memória.