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
print(p1.__dict__)
p1.nome = 'João'
print(p1.nome) # get nome
print(p1.__dict__)