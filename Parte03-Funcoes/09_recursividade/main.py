def fatorial(n):
    return 1 if n == 1 else n*fatorial(n-1)

def main():
    n = int(input("Informe um numero inteiro: ").strip())
    if n > 0:
        print(f"Fatorial de {n}! é {fatorial(n)}")
    elif n == 0:
        print(f"Fatorial de {n}! é 1")
    else:
        print("Não pode ser menor que 0")

if __name__ == "__main__":
    main()