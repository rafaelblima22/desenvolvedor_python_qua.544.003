#NOTE - declaração de variaveis
nome = input("Informe seu nome: ").title()
nota = float(input(f"Informe a nota do {nome}: ").replace(",","."))

#NOTE -  verificar se a nota é valida
if nota >= 0 and nota <= 10:
    if nota >= 7:
        print(f"{nome} esta aprovado")
    elif nota >= 5:
        print(f"{nome} esta de recuperação")
    else:
        print(f"{nome} esta reprovado")
else:
    print(f"Nota de {nome} invalida.")