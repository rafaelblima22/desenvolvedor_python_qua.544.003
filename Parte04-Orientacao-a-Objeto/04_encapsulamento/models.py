class Pessoa:
    def __init__(self,nome,cpf,email,telefone):
#NOTE - Um _ o atributo vira protected
#NOTE - Dois __ o atributo vira private
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone

#SECTION - Metodos de acesso, Primeiro o metodo
#SECTION - Get(acessar valor do atributo)
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def email(self):
        return self.__email
    
    @property
    def telefone(self):
        return self.__telefone

#SECTION - Set(definir valor do atributo)
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @email.setter
    def email(self, email):
        self.__email = email

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
