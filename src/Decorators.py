# Exemplo sem parâmetros
# def saudacao(funcao):
# 	def execucao():
# 		print('Seja bem vindo!')
# 		funcao()
# 		print('Até logo')
# 	return execucao

# @saudacao
# def nome():
# 	print(f'Eu sou o Qualquer')

# nome()


# Exemplo com parâmetros

def pedido(func):
	def exec(*args, **kwargs):
		return func(*args, **kwargs)
	return exec


@pedido
def escolha(principal):
	print(f'Minha escolha é {principal}')


escolha('Lasanha')
