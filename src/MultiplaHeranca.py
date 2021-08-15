class Animal:

	def __init__(self, nome):
		self.__nome = nome

	def cumprimentar(self):
		return f'Eu sou {self.__nome}'


class Aquatico(Animal):

	def __init__(self, nome):
		super().__init__(nome)

	def cumprimentar(self):
		return f'Eu sou {self._Animal__nome} do Mar!'


class Terrestre(Animal):

	def __init__(self, nome):
		super().__init__(nome)

	def cumprimentar(self):
		return f'Eu sou {self._Animal__nome} da Terra!'


class Pinguim(Terrestre, Aquatico):

	def __init__(self, nome):
		super().__init__(nome)



baleia = Animal('Wally')
print(baleia.cumprimentar())

cachorro = Terrestre('Belinha')
print(cachorro.cumprimentar())

pinguim = Pinguim('Tux')
print(pinguim.cumprimentar())