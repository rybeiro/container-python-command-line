# Manipulação de Arquivos
## CSV
### Lendo arquivos CSV
- CSV - Comma Separated Values - Valores Separados por Vírgula

Para leitura de arquivo CSV é necessário importar a função *reader* do pacote csv
- *from csv import reader*

Lendo dados para em formato de lista
```python
# Leitura do arquivo no formato de lista
from csv import reader

with open("lutadores.csv") as arquivo:
	leitor = reader(arquivo)
	next(leitor) # Nesse caso pula a primeira linha (cabeçalho)
	for leu in leitor:
		print(f"O lutador {leu[0]} é do país {leu[1]} e mede {leu[2]}cm")

# Leitura do arquivo em formato de dicionário
from csv import DictReader
with open("lutadores.csv") as arquivo:
	leitor = DictReader(arquivo)
	for leu in leitor:
		print(f"O lutador {leu['Nome']} é do país {leu['País']} e mede {leu['Altura (em cm)']}cm")

```
## JSON 