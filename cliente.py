class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome.title()
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome.title()

    @property
    def cpf(self):
        return self.__cpf