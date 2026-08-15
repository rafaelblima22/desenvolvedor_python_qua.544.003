from modulo import limpar, equacao_segundo_grau

def main():
    limpar()
    a = int(input("Informe o valor de 'a': "))
    b = int(input("Informe o valor de 'b': "))
    c = int(input("Informe o valor de 'c': "))
    limpar()

    result = equacao_segundo_grau(a,b,c)

    for x in result:
        print(f"x = {x}")

    
if __name__ == "__main__":
    main()