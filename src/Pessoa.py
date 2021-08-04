class Pessoa:
    
    contador = 0

    @classmethod
    def contador_de_usuarios(cls):
    	print(f'Temos {cls.contador} online')

    def __init__(self, nome, sobrenome):
        self.__nome = nome # atributo privado representado por __
        self.__sobrenome = sobrenome


    # Método de Instância, necessitam da instância para ser acessados
    def saudacao(self):
        print(f"Seja bem vindo, {self.__nome} {self.__sobrenome}")


p1 = Pessoa('Nome', 'Sobrenome')

p1.saudacao()

cont = Pessoa.contador_de_usuarios()
print(cont)

