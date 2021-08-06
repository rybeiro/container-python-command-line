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
		self.__matricula = matricula

	# sobreescrita de método

	def nome_completo(self):
		return f'{self._Pessoa__nome} {self._Pessoa__sobrenome} o número de sua matricula é {self.__matricula}'



func1 = Funcionario('Fabio', 'Ribeiro', '987.098.654-32', 1234)

print(func1.nome_completo())