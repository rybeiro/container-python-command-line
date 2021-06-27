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