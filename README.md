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



### Variável
- Uma variável é uma localização na memória RAM do computador onde vai ser armazenada temporariamente os dados que são utilizados pelo programa.
- Definir um padrão para nome de variáveis.
	- O nome da variável sempre com letras minúsculas ```nomevariavel```
	- O nome composto utilize *underline* ```nome_variavel```

### Intergindo com o usuário
- *input* => Entrada de dados de teclado.
	- ```nome = input("Qual o seu nome?")```

### Interpolação
- Forma 1: ```print("O valor R$" + variavel + " é total da compra")```
- Forma 2: ```print("O valor R$ {} é total da compra".format(variavel))```
- Forma 3: ```print("O valor R$ {variavel} é total da compra")```

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

## Métodos reservados do Python
- ```type(variavel)``` exibe o tipo de dado de uma variável

## Informações e dicas
- ```pass``` utilizado para pass o programa em trechos que possa gerar erro por exigir código