#TODO: atividade 04
# Utilizando conceito de módulo, crie um modulo com funções que façam as seguintes ações:
# - limpa terminal.
# - Calcular a potencia de um numero informado pelo usuario elevado a outro numero informado pelo usuario.
# - Calcula a raiz quadrada de um numero informado pelo usuario.
# - Calcula o volume de um recipiente paralelepipédico.
# - Calcula o volume de um recipiente cilindrico.
# Em seguida, faça um programa que o usuário escolha executar uma dessas funções ou sair do programa.

from modulo import limpar_terminal, potencia, raiz_quadrada, calcular_cilindro, calcular_paralelepipidico

def main():
    limpar_terminal()

    while(True):
        print(f"{"#"*10} MENU {"#"*10}")
        print("1 - Calcular a potencia de um numero")
        print("2 - Calcular raiz quadrada de um numero")
        print("3 - Calcular o volume de um paralelepipédico")
        print("4 - Calcular o volume de um cilindro")
        print("5 - Sair do programa")

        opcao = input("Informe a opção desejada: ")
        limpar_terminal()

        match opcao:
            case "1":
                x = int(input("Informe o valor da base: ").strip())
                y = int(input("Informe o valor da potencia: ").strip())
                limpar_terminal()
                print(f"A potencia de {x} elevado a {y} é: {potencia(x,y)}")
                print("")
                continue

            case "2":
                x = int(input("Informe um numero para calcular sua raiz quadrada: ").strip())
                limpar_terminal()
                print(f"A raiz quadrada de {x} é: {raiz_quadrada(x)}")
                continue

            case "3":
                comprimento = float(input("Informe o valor do comprimento: ").strip())
                largura = float(input("Informe o valor do largura: ").strip())
                altura = float(input("Informe o valor do altura: ").strip())
                limpar_terminal()
                print(f"O volume de um paralelepipédico é: {calcular_paralelepipidico(comprimento, largura, altura)}")
                continue
            case "4":
                altura = float(input("Informe o valor do altura: ").strip())
                raio = float(input("Informe o valor do raio: ").strip())
                limpar_terminal()
                print(f"O volume do cilindro é: {calcular_cilindro(raio, altura)}")
                continue
            case "5":
                break
            case _:
                print("Opção Invalida!")
                continue


if __name__ == "__main__":
    main()