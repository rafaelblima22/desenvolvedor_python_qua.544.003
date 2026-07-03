try:
    n = int(input("Informe um numero inteiro: "))

    #NOTE - laco de repetição
    while n >= 0:
        print(n)
        n -= 1

except:
    print("Não foi possivel exibir a contagem")