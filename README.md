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
	- *min()* retorna o valor mínimo. Para utilizar função podemos utilizar a *key=lambda ...*
	- *max* retorna o valor máximo. Para utilizar função podemos utilizar a *key=lambda ...*

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

```python
if condicao:
	executa tudo que
	estiver dentro da
	identação
```

### Operadores de comparação
- == (igualdade)
- != (diferente)
- \> (maior que)
- < (menor que)
- \>= (maior ou igual à)
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

- Sintaxe sem parâmetro: *lambda: nome*
- Sintaxe com parâmetro: *lambda x: 1 + x*

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

## Função Map
*Map* é uma função que recebe 2 parâmetros, o primeiro é uma função e o segundo um iterável. Retorna um *Map Object* e pode ser convertido para uma lista.

O *map()* retorna um objeto mapeando a função para cada elemento do iterável.

- Sintaxe: **map(function, iteravel)** 

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

## Filter
O *filter()* serve para filtrar dados em uma coleção. Retorna um *filter Object* e pode ser convertido para uma lista.

Ao aplicar o *filter()* é retornado um objeto apenas os elementos filtrados de acordo com a função.

- Sintaxe: *filter(função, interável)*

**Exemplo**
```python
import statistics
dados = [2,4,9.3,7,23,0.74]

media = statistics.mean(dados)

print(f'A média é {media}')

# utilizando filter() com lambda
retorno = filter(lambda x: x > media, dados)

print(list(retorno))
```
> O **filter()** depois de utilizado é excluído da memória.

## Reduce
A função *reduce()* está disponível na biblioteca functools.

- Sintaxe: *reduce(função, interável)*

> ATENÇÃO: Utilize a função *reduce()* se realmente precisar dela. Tem casos que um *loop for* resolverá. Fonte: **Guido Van Rossum**

## All
*all()* Retorno boolean. Retorna *True* se todos os elementos do iterável são verdadeiros ou ainda está vazio.

**Exemplo**
```python
numeros = [0,1,2,3,4]
print(all(numeros)) # False, porque o 0 (zero) é False

numeros = [1,2,3,4,5]
print(all(numeros)) # True 
```

## Any
*any()* Retorno boolean. Retorna *True* se qualquer elemento do iterável for verdadeiro.

## Generators expression ou Tuple Comprehension
É muito mais performatico que os demais Comprehension.

**Exemplo**
```python
gen = (x * 2 for x in range(1000))

print(gen)

```

## Sorted
É *sorted()* utilizado para ordernar qualquer iterável. Diferentemente do *sort()* que só ordena no *list()* gerando uma nova lista ordenada. Porém o *sorted()* não altera a lista original.

- Sintaxe: 
```python
sorted([8,3,6,2,9]) # Crescente
sorted([8,3,6,2,9], reverse=True) # Decrescente
```

## Max
*max()* Retorna o valor máximo 

## Min
*min()* Retorna o valor mínimo

## Reversed
A função *reversed(iteravel)* inverte a saída de qualquer iterával, com exceção de conjuntos (*set()*) que não mantém a ordem dos elementos.

## Len
O *len(list)* Retorna o tamanho do iterável. 

## Abs
*abs(num)* Retorna o valor absoluto de um número sem o sinal.

## Sum
*sum()* Retorna o somatória de uma determinado iterável

## Round
*round()* Retorna o valor arredondado para o *n* digito de precisão após a cada decimal.
- *round(15.4)*
- *round(15.5)*
- *round(15.6)*
- *round(15.6353, 2)*    arredondamento com precisão de 2 casas decimais.
- *round(15.65567, 2)*   arredondamento com precisão de 2 casas decimais.
- *round(15.6757788, 2)* arredondamento com precisão de 2 casas decimais.

## Zip
*zip()* Cria um iterável do tipo *Zip Object*.

**Exemplos**
```python
prova1 = [9.7, 6.7, 7.8]
prova2 = [5.5, 7.2, 6.8]
alunos = ['Maria', 'Roger', 'Joaquina']

media_final = zip(alunos, map(lambda: nota: max(nota), zip(prova1, prova2)))

print(dict(media_final))

# MODULARIZANDO A FUNÇÃO
# Primeiro: list(zip(prova1, prova2)) # output: [(9.7, 5.5),(6.7, 7.2),(7.8, 6.8)]
# Segundo : list(map(lambda nota: max(nota), [(9.7, 5.5),(6.7, 7.2),(7.8, 6.8)])) # output: [9.7, 7.2, 7.8]
# Terceiro: dict(zip(alunos, [9.7, 7.2, 7.8])) # output: {'Maria': 9.7, 'Roger': 7.2, 'Joaquina': 6.8} 
```


### Benchmark -> Avaliando o desempenho computacional de cada Comprehension

```python
from sys import getsizeof

list_comp = getsizeof([x * 2 for x in range(1000)])
print(f'Tamanho da memória alocada: {list_comp} bytes')

set_comp = getsizeof({x * 2 for x in range(1000)})
print(f'Tamanho da memória alocada: {set_comp} bytes')

dict_comp = getsizeof({x: x * 2 for x in range(1000)})
print(f'Tamanho da memória alocada: {dict_comp} bytes')

get_comp = getsizeof((x * 2 for x in range(1000)))
print(f'Tamanho da memória alocada: {get_comp} bytes')

```

# Tratamento de Exceções
Métodos úteis:
- *try e except*
	- *try* tenta executar e caso ocorra um erro entra no *except* e aqui 
	podemos tratar o erro exibindo uma mensagem personalizada para o usuário.
- *try, except e else*
	- *try* tenta executar e caso ocorra um erro entra no *except* e caso 
	contrário entra no *else* para executar outra instrução.
- *try, except, else e finally*

**Exemplos**
```python
### try e except
# vai tentar executar uma função que não existe. Isso gera o erro de NameError
# porque a função não foi definida. mas o erro não será exibido porque ao 
# utilizar o except informamos ao python o pass para não fazer nada.
# tratamos de forma genérica.
try:
	tente()
except:
	pass


# Vamos enviar uma mensagem de erro personalizada.
try:
	tentar()
except:
	print("Ops! Algo de errado aconteceu e o sistema não executou como" + 
		"esperado informe o Administrador do Sistema")


# Além de informar ao usuário uma mensagem vamos exibir o erro, nesse caso
#  temos que saber o tipo de erro é de NameError
try:
	tentar()
except NameError as erro:
	print("Ops! Algo de errado aconteceu e o sistema não executou como "+
		"esperado informe o Administrador do Sistema")
	print(f"Erro: {erro}")


### try, except e else
# Tratando entrada do usuário. Nesse exemplo esperamos que ele digite
#  apenas números.
# Caso 1: Entrada correta, valor digitado 15
# Nesse caso o sistema vai executar normalmente e imprimir a mensagem 
# que está fora do tratamento.
try:
	num = int(input("Entre com o valor do desconto"))
except ValueError as erro:
	print("Ops! Entrada inválida, digite apenas numéros")

print(f"O valor informando é de: {num}")

# Caso 2: Entrada incorreta, valor digitado gentalha
# Nesse caso vai cair na exceção e imprimir a mensagem de erro MAS também 
# vai gerar um erro no print de fora do bloco porque não inicializamos a 
# variável num que recebe o valor dentro do try. E para tratar isso precisamos
#  utilizar o else no caso 3.
try:
	num = int(input("Entre com o valor do desconto"))
except ValueError as erro:
	print("Ops! Entrada inválida, digite apenas numéros")

print(f"O valor informando é de: {num}")

# Caso 3: 
# Entrada correta vai para o else
# Entrada incorreta vai para o except
try:
	num = int(input("Entre com o valor do desconto"))
except ValueError as erro:
	print("Ops! Entrada inválida, digite apenas numéros")
else
	print(f"O valor informando é de: {num}")


### try, except, else e finally
# Caso 1:
# A instrução finally sempre será executa, independentemente se entrar no 
# except ou no else
try:
	num = int(input("Entre com o valor do desconto"))
except ValueError as erro:
	print("Ops! Entrada inválida, digite apenas numéros")
else
	print(f"O valor informando é de: {num}")
finally:
	print("Sempre será executado.")

```

**Tratamento de vários erros possíveis**
- Para tratar vários erros possíveis utilize uma tupla.
```python
# Divisão que pode gerar erro nos casos de divisão por zero ou usuário inserir
# letras ao invés de números.

def divisao(a, b):
	try:
		return int(a) / int(b)
	except (ValueError, ZeroDivisionError, TypeError):
		return "Ops! Verifique os Dividendo e o Divisor"

num1 = input("Dividendo")
num2 = input("Divisor")

divisao(num1, num2)
```

> O finally poderia ser usado para fechar uma conexão com o banco de dados
 independentemente do que ocorra com a tentativa de conexão, Se sucesso ou insucesso.

# Módulos
Em Python módulos são arquivos python (.py). Em um módulo existem várias funções
disponíveis.

#### Importando módulos
Existe duas formas de importar os módulos:
- Forma 1: Importar o módulo completo, ou seja, todas as funções, atributos,
 propriedades ou classes pertecentes ao módulo. Isso ficará alocado em memória.
 **(Não recomendado)**
	- *import nome_do_modulo*
- Forma 2: Importar apenas a função à utlizar **(recomendado)**
	- *from nome_modulo import nome_funcao*

> Importante para saber quais funções tem no módulo utilize o *dir()*

**Exemplos**
```python
# importando o Módulo random disponibilizará todos as funções
# 
import random

# para saber quais funções estão disponíveis nesse Módulo basta consultar a
# documentação dir(random).
dir(random)

# Nesse caso identificamos que o módulo random tem a função random para saber o
# que essa função faz podemos utilizar o help(random.random)

help(random.random)

print(random.random())

# Importando apenas a função uniform() do Módulo random
# A função uniform() gera números pré-estabelecido entre valores determinados
from random import uniform

for i in range(10):
	print(uniform(3,7))


# Função randint() -> gera números inteiros entre um determinado intervalo
from random import randint

for i in range(6):
	# Números para o sorteio da Mega-sena do 1 ao 60
	# o parâmentro end=', ' é um separador para a saída
	print(randint(1, 61, end=', '))

# Função choice()  -> retorna um valor aleatório de um determinado iterável.
from random import choice 
jogadas = [('pedra', 1), ('papel', 2), ('tesoura', 3)]
print(choice(jogadas))

# Função shuffle -> mistura a ordem dos elementos aleatoriamente
from random import shuffle
cartas = ['A', '2', '3', '4', '5', '6', '7', 'Q', 'J', 'K']
print(cartas)
shuffle(cartas)
print(cartas)

# Importando todo o módulo sem precisar passar o nome do Módulo
from random import *

print(uniform(1, 10))
```

### Módulos built-in
São Módulos integrados que já vem instalados no Python (https://docs.python.org/3/py-modindex.html)


### Módulos externos
Para instalar módulos externos criados pela comunidade utilizamos o PIP.

Os módulos estão disponíveis (https://pypi.org)


# Pacotes
É um diretório que contém vários Módulos, ou seja, arquivos Python (.py)

**OBS:** Nas versões 2.x do Python para utilizar os módulos é obrigatório existir 
um arquivo *Dunder __init__.py*. Nas versões 3.x não é obrigatório, mas é utilizado 
para manter a compatibilidade.

Para utilizar os pacotes podemos importa-los da mesma maneira que fizemos 
com os módulos.

```python
# Lembre-se que os pacotes são diretórios
from diretorio1 import funcao1

print(funcao1())


# Se dentro do pacote existe outros pacotes, ou seja, sub-diretórios
from diretorio1.subdiretorio import funcao2

print(funcao2())
```

# Dunder Main e Name
*Dunder* significa Doble Under

*__main__* é o arquivo principal o que será executado

*__name__* é o nome do arquivo que está sendo importado.

A partir da execução de um arquivo Python diretamente na linha de comando, 
o python internamente atribui o valor de *__main__* na variável *__name__* em 
indicando que é um módulo de execução.

O que está dentro do *__name__ ou __main__* só será exeutado se o próprio 
arquivo for executado.

**Exemplo para compreensão**
```python
# Considere o Módulo com o nome primeiro.py
# Esse arquivo se for importado executará o print() implicitamente
def funcao1():
	return "Função 1"

print(funcao1())

# Para evitar chamada implicitas utilizamos o Dunder __name__
def funcao1():
	return "Função 1"

if __name__ == '__main__':
	print(funcao1())
```

# Files
Para ler ou escrever dados em um arquivo do sistema operacional o script
precisa de ter permissão.

#### Lendo os arquivos
Para leitura de arquivos em Python utilizamos a função nativa *open()* que 
retorna um objeto *io.TextIOWrapper*

Para exibir informações do arquivo basta dar um *print* na saída.
```python
# Abrindo um arquivo e obtendo informações.
arquivo = open('edital.pdf')
print(arquivo)
# output: <_io.TextIOWrapper name='PDF/edital.pdf' mode='r' encoding='UTF-8'>
print(type(arquivo))
# output: <class '_io.TextIOWrapper'>

# Para ler o conteúdo do arquivo utiliza-se read()
print(arquivo.read())
arquivo.close()
```
> O Mode r (read) é o padrão da função open()

#### Escrevendo em arquivos
```python
# O Mode w (write) nos permite escreve no arquivo até que o mesmo seja fechado
# como o uso do with envolvemos em um bloco e portanto ao sair ele fechará
# automáticamento.
with open('novo.txt', 'w') as arquivo:
	arquivo.write("Escrevendo em um arquivo")
	arquivo.write("Continuamos a escrever no arquivo")
	arquivo.write("Vamos finalizar aqui.")

# Escrevendo a partir de interação do usuaário
with open('frutas.txt', 'w') as frutas:
	print("Para encerrar o sistema escreva sair")
	while True:
		fruta = input("Informe o nome de uma fruta")
		if fruta == 'sair':
			break
		frutas.write(fruta)
```

> O Mode w (write) na função *open()* se chamado ele sobreescreve o conteúdo 
do arquivo. Se o arquivo não existir ele criará. 

> **IMPORTANTE: Forma Pythônica** O uso do bloco *with* garante que o arquivo será fechado
imediatamento quando o bloco finalizar.

### Mode para abrir arquivos
- **r** Abre para leitura open('arquivo.txt')
- **w** Abre para escrita *open('arquivo.txt', 'w')* Essa operação sobreescre o
conteúdo do arquivo.
- **a** Abre para escrita como *append* open('arquivo.txt', 'a'). Adiciona no
final do arquivo.
- **+** Abre o arquivo para escrita e leitura. Modo de atualização. Tem que 
combinar com outro modo *open('arquivo.txt', 'a+')*

## StringIO
Utilizado para ler e criar arquivos na mémoria. é necessário importa-lo
do pacote *io*

```python
from io import StringIO

arquivo = StringIO("aqui vai o texto")
arquivo.read()
arquivo.write("adicionado novo texto")
arquivo.seek(0)
arquivo.read()
```

## Seek e Cursor
*seek()* é a função que movimenta o cursor no arquivo. Essa função recebe um
parâmentro que indica onde queremos posicionar o cursor quando ele atige o 
final do arquivo.

```python
arquivo.open('PDF/edital.txt')
arquivo.read()
arquvo.seek(0) # posiciona o cursor no inicio do arquivo
arquivo.read()
print(arquivo.closed) # False (arquivo ainda aberto)
arquivo.close()
print(arquivo.closed) # True (Arquivo fechado)

# with -> bloco que utilizado para trabalhar com recurso e fecha-los após o uso.
with open('PDF/edital.pf') as arquivo:
	print(arquivo.readlines())

# a partir daqui o arquivo não existe mais porque a conexão já foi fechada.

```

- *read()* retorna todas as linhas/páginas do arquivo.
	- *read(50)* podemos retornar uma determinada quantidade de caracteres.
- *readline()* retornar uma linha do arquivo.
- *readlines()* retorna todas as linhas do arquivo em um *list()*
- *close()* fecha o arquivo.
- *closed* verifica se o arquivo está aberto ou fechado. Retorna um *boolean*.
- *with* Forma Pythônica. É um bloco utilizado para trabalhar com o arquivo e após sair do bloco
o mesmo é fechado.

> Ao abrir um arquivo com *open()* é criada um conexão entre o arquivo
e o disco. Essa conexão é chamada de *streaming* é sempre recomendado
fechar essa conexão depois de trabalhar com o arquivo.

# Sistemas de arquivos
Para manipulação de arquivos no Python é necessário importar o módulo *os*.

```python
import os
# getcwd() -> retorna o caminho absoluto.
os.getcwd()

# chdir() -> Alterando o diretório
os.chdir('..')

# name() -> retorna o sistema de arquivo do sistema operacional
os.name()

# uname() -> Detalhes do sistema operaciona
os.uname() 

# path.join() -> Junta os diretórios separando as barras de acordo
# o sistema operacional
os.path.join()

# listdir() -> lista o conteúdo de um diretório
os.listdir()

# scandir() -> consultar

# verificar se o diretorio ou arquivo existe
os.path.exists('arquivo.txt')
os.path.exists('diretorio')

# Criar arquivos em branco
os.mknod('arquivo-teste.txt')

# Criar diretório, mkdir cria apenas um diretório
os.mkdir('teste')

# Criar árvore de diretorios
os.makedirs('teste/teste1/teste2/teste3')

# Criar árvore de diretórios checando se já existe.
os.makedirs('teste/teste1/teste2', exist_ok=True)

# Renomer arquivos ou diretórios
os.rename('teste1', 'teste4') # Diretorios
os.rename('arquivo.txt', 'novo_arquivo.txt') # Arquivos

# Remover arquivos
os.remove('arquivo.txt')

# Remover diretórios -> Remove diretorio vazio
os.rmdir('teste1')

# Remover árvore de diretórios -> Remove diretorios vazios
os.removedirs('teste1/teste/2/teste3')

# Criando diretórios temporários
import filetemp
with filetemp.TemporaryDirectory() as tmp:
	print(f'Foi criado um diretório temporario em {tmp}')
	with open(os.path.join(tmp, 'arquivo_temp.txt'), 'w') as arquivo:
		arquivo.write("Foi criado um arquivo temporário")
	input() # Usado apenas para segurar o terminal e podermos validar que foi criado.

# Criando um arquivo temporário -> Em arquivos temporários só conseguimos escrever
# bits
import filetemp
with file.TemporaryFile() as tmp:
	tmp.write(b'Teste de escrita') # O b representa o Mode bits
	tmp.seek(0)
	print(tmp.read())



```

# Python Debugger
Deve-se importar a biblioteca pdb *import pdb*

#### Lista de comandos básicos
- l -> lista o código
- n -> vai para próxima linha
- p -> imprime variável
- c -> continua a execução

**Nas versões anteriores ao 3.7** utilizar o *set_trace()* e importar o python debugger
O ponto para debugar o código deve-se utilizar o *set_trace()* antes da linha 
depois utilizar os comandos básicos para interagir com o python debugger.

**Nas versões posterior ao 3.7** Não é necessário importar a biblioteca, basta 
chamar a função *built-in, brackpoint()* 

# Algumas Bibliotecas utilizadas
- math -> Funções matemáticas
- statistics -> Esse módulo fornece funções para o cálculo de estatísticas 
matemáticas de dados numéricos
- functools
- sys
	- getsizeof('TExto') - Retorna o tamanho em bytes alocado na mémoria de um determinado parâmetro.

# Iterator e Iterables
- *Iterator* é um objeto que pode ser iterável e que retornar uma elemento por
 vez quando a função *next()* for chamada.
 - *Iterable* um objeto que retorna um *iterator* quando a função *iter()* é chamada.

**Exemplo**
```python
nome = 'Nome' # É um iterable mas não é iterator
numeros = [1,2,3,4,5,6] # É um iterable mas não é iterator

print(next(nome)) # Aqui é um iterable.
# Lembre-se que um objeto iterator tem a função next()
# nesse exemplo vemos que a variável nome é uma str
# TypeError: 'str' object is not an iterator

print(next(numeros)) 
# TypeError: 'list' object is not an iterator

# Mas podemos transformar essas variáveis em iterator através da função iter()
# Posteriormente acessar os elementos com a função next()
nome = iter(nome)
type(nome)
print(next(nome))

numeros = iter(numeros)
type(numeros)
print(numeros)
```

# Orientação objeto - Python
É o paradigma de programação que utiliza mapeamento de objetos do mundo real 
para modelos computacionais.

#### Principais elementos de POO
- Classe: Modelo do objeto do mundo real sendo representado computacionalmente.
- Atributos: Características do objeto
- Métodos: Comportamento do objeto (funções)
- Construtor: Método especial utilizado para criar os objetos.
- Objeto: Instância da class. Tipo de dado complexo.

Em Python atributos são declarados dentro do construtor.

Sintaxe: construtor padrão 
```python
def __init__(self):
```

> *self* é o próprio objeto da classe ou referência de instância.

### Atributos


### Métodos (funções)
Representam o comportamento do objeto, ou seja, as funções que ele pode 
realizar no sistema.

O nome dos métodos devem ser escrito com letras minúsculas se for composto
deve-se separar por underline.

#### Método de Instância
São os métodos que precisamos de uma instância para ter acesso.

```python

class Pessoa:

	def __init__(self, nome, sobrenome):
		self.__nome = nome # atributo privado representado por __
		self.__sobrenome = sobrenome


	# Método de Instância, necessitam da instância para ser acessados
	def saudacao(self):
		return f"Seja bem vindo, {self.__nome} {self.__sobrenome}"


p1 = Pessoa('Nome', 'Sobrenome')

p1.saudacao()
```

#### Métodos de Classe
São conhecido como métodos estáticos em outras linguagens, mas a diferença
é principalmente por ter o decorador *@classmethod* e o parâmetro *cls*

```python
class Pessoa:

	contador = 0

	@classmethod # Decorador de classe
	def contador_de_usuarios(cls):
		print(f'Temos {cls.contador} online')

	def __init__(self, nome, sobrenome):
		self.__nome = nome # atributo privado representado por __
		self.__sobrenome = sobrenome


	# Método de Instância, necessitam da instância para ser acessados
	def saudacao(self):
		return f"Seja bem vindo, {self.__nome} {self.__sobrenome}"


p1 = Pessoa('Nome', 'Sobrenome')

p1.saudacao()

```

#### Método Estático
Método estático é acompanhado do decorador *@staticmethod*
```python

class Pessoa:

	contador = 0

	@staticmethod
	def definicao():
		return Pessoa.contador + 1

Pessoa.definicao()
```

#### Herança (Inheritance)
A idéia de herança é reaproveitamento de código e também a possibilidade de
extender as classes.

A Herança nos permite extender atributos e métodos.

Para entender melhor o uso de herança usaremos como exemplo duas entidades 
com mesmos atributos e métodos.
```python

# Classe cliente
class Cliente:
	def __init__(self, nome, sobrenome, cpf, salario):
		self.__nome = nome
		self.__sobrenome = sobrenome
		self.__cpf = cpf
		self.__salario = salario

	def nome_completo(self):
		return f'{self.__nome} {self.__sobrenome}'

# Classe Funcionario
class Funcionario:
	def __init__(self, nome, sobrenome, cpf, matricula):
		self.__nome = nome
		self.__sobrenome = sobrenome
		self.__cpf = cpf
		self.__matricula = matricula

	def nome_completo(self):
		return f'{self.__nome} {self.__sobrenome}'

# Perceba que essas duas Entidades tem atributos e método iguais
# Agora temos que responder a pergunta abaixo
## Existe alguma entidade genérica suficiente para encapsular os atributos 
## e métodos comuns em outras entidades?
### Nesse exemplo, Sim. Ambas as Classes tem atributos de uma Pessoa.

# Refatorando as classes e aplicando herança
class Pessoa:
	def __init__(self, nome, sobrenome, cpf):
		self.__nome = nome
		self.__sobrenome = sobrenome
		self.__cpf = cpf

	def nome_completo(self):
		return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
	def __init__(self, nome, sobrenome, cpf, salario):
		super().__init__(nome, sobrenome, cpf)
		self.__salario = salario


class Funcionario(Pessoa):
	def __init__(self, nome, sobrenome, cpf, matricula):
		super().__init__(nome, sobrenome, cpf)
		# ou
		# Animal.__init__(self, nome, sobrenome, cpf)
		self.__matricula = matricula

	# sobreescrita de método

	def nome_completo(self):
		return f'{self._Pessoa__nome} {self._Pessoa__sobrenome} o número de sua matricula é {self.__matricula}'

```

> Para usar herança é importante responder a essa pergunta: 
> Existe alguma entidade genérica suficiente para encapsular os atributos 
> e métodos comuns em outras entidades?

#### Propriedades (Getters e Setters)
No Python utiliza-se **Decoradores (Decorators)** para *getters* e *setters*
```python

# Refatorando a Classe Pessoa

class Pessoa:
	def __init__(self, nome, sobrenome, cpf):
		self._nome = nome
		self._sobrenome = sobrenome
		self._cpf = cpf


	# Uso de decoradores para getters
	@property
	def nome(self):
		return self._nome
	
	# Uso de decoradores para setters
	@nome.setter
	def nome(self, nome):
		self._nome = nome


p1 = Pessoa('Fabio', 'Ribeiro', '123.456.789-00')

print(p1.nome) # get nome
p1.nome = 'João'
print(p1.nome) # get nome
```

#### Herança Multipla
É a possibilidade herdar atributos e métodos de multiplas classes herdadas. 
Existe a forma a Herança direta e a Herança indireta (Multiderivação).

- Herança Direta: é aquela em que a herança é direta na classe.
```python
# Classe pai
class Animal:

	def __init__(self, nome):
		self.__nome = nome

	def cumprimentar(self):
		return f'Eu sou {self.__nome}'

# Herança Direta
class Aquatico(Animal):

	def __init__(self, nome):
		super().__init__(nome)

	def cumprimentar(self):
		return f'Eu sou {self._Animal__nome} do Mar!'

# Herança Direta
class Terrestre(Animal):

	def __init__(self, nome):
		super().__init__(nome)

	def cumprimentar(self):
		return f'Eu sou {self._Animal__nome} da Terra!'

# Multipla Herança
# Herança Direta para as Classes Terrestre e Aquatico
# Herança indireta da Classe Animal
# Isso é conhecido como MRO, explicação abaixo
class Pinguim(Terrestre, Aquatico):

	def __init__(self, nome):
		super().__init__(nome)


baleia = Animal('Wally')
print(baleia.cumprimentar())

cachorro = Terrestre('Belinha')
print(cachorro.cumprimentar())

pinguim = Pinguim('Tux')
print(pinguim.cumprimentar())
```

- Herança Indireta: é aquela em que a herança é Indireta onde a classe filha recebe
 os atribuitos e métodos da classe pai de outra classe herdada (Multiderivação).

> Para determinar se um objeto pertence a uma determinada instância, utilizar o 
método *isinstance(objeto, instancia)*

#### Method Resolution Order (Resolução de Ordem de Métodos)
É a ordem de execução dos métodos, ou seja, qual será executado primeiro

Três formas de verificar a ordem de execução dos métodos:
- Via propriedade: *Pinguim.__mro__*
- Via método: *Pinguim.mro()*
- Via help: *help(Pinguim)*

```python
# utilize o exemplo acima para analisar a saída
# assim pode verificar a ordem que o pythom vai resolve
# O MRO basicamente resolve métodos com mesmo nome em todos atribuitos
# propriedades e métodos herdados.
from mro import Pinguim

Pinguim.__mro__
Pinguim.mro()
help(Pinguim)
```

#### Polimorfismo (Muitas formas)
O polimorfismo pode ser identificado através do override (sobreescrita)

Exemplo:
```python

class Animal:
	
	def __init__(self, nome):
		self.__nome = nome

	def comer(self):
		print(f'O {self.__nome} está comendo')
		
	def falar(self):
		raise NotImplementedError('Método não acessível na classe pai, implemente-a na classe filha')


class Gato(Animal):
	def __init__(self, nome):
		super().__init__(nome)

	def falar(self):
		print(f'O {self._Animal__nome} está miando... miau miau')


class Cachorro(Animal):
	def __init__(self, nome):
		super().__init__(nome)


felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
# aqui gera a exceção
pluto.falar()

```


#### Métodos Mágicos
