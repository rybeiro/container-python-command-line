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
pluto.falar()