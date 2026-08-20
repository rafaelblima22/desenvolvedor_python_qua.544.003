#classe pessoa
class Pessoa:
    #mpetodo construtor
    def __init__(self,nome,idade,email,altura):
        #atributos da classe
        self.nome = nome
        self.idade = idade
        self.email = email
        self.altura = altura

    #método
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Email: {self.email}")
        print(f"Altura: {self.altura}")


def main():
    #intancia a classe (criar objeto)
    usuario = Pessoa(nome="", idade=0, email="", altura=0.0)

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Indorme a idade: "))
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.altura = float(input("Informe a altura em metros: ").replace(",","."))

    usuario.exibir_dados()


if __name__ == "__main__":
    main()