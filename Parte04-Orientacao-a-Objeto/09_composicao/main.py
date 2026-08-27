from models import Carro 


def main ():
    carro = Carro(input("Informe o modelo do carro: ").strip(),int(input("Informe a potencia do motor: ")))

 #   carro.modelo = input("Informe o modelo do carro: ").strip()
 #   carro.potencia = int(input("Informe a potencia do motor: "))  #Aqui deu erro

    print(carro.detalhes())

if __name__ == "__main__":
    main()