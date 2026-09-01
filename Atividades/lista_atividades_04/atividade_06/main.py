import os
from models import Conta,Pessoa

def limpar():
    os.system("cls" if os.name =="nt" else "clear")

def main():
    limpar()

    usuario = Pessoa("","")

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o cpf: ").strip()

    cc = Conta(usuario,"","",0.0)
    cc.agencia = input("Informe a agencia: ").strip()
    cc.n_conta = input("Informe o numero da conta: ").strip()

    limpar()

    while True:
        print("1 - Consultar dados")
        print("2 - Gerar extrato")
        print("3 - Depositar")
        print("4 - Sacar")
        print("0 - Sair")

        opcao = input("Informe a opção desejada: ").strip()

        match opcao:
            case "1":
                limpar()
                print(cc.consultar_dados())
                continue
            case "2":
                limpar()
                print(cc.gerar_extrato())
                continue
            case "3":
                limpar()
                valor = float(input("Informe o valor do deposito: ").replace(",","."))
                if valor >=0 :
                    print("Deposito efetuado com sucesso!")
                    print(f"Saldo atual: {cc.depositar(valor)}")
                else:
                    print("Deposito não pode ser efetuado.")
                continue
            case "4":
                limpar()
                valor = float(input("Informe o valor do saque: R$").replace(",","."))
                if valor >=0:
                    if valor <= cc.saldo:
                        print(f"Saldo atual: R$  {cc.sacar(valor):.2f}")
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("Valor não pode ser sacado.")
                continue
            case "0":
                break
            case __:
                print("Opção invalida!")
                continue

if __name__ == "__main__":
    main()