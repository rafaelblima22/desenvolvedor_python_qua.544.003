#NOTE -  Declaracao de variaveis
nome = input("Informe seu nome: ").title()
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura em metros").replace(",","."))

#NOTE -  Saida de dados
print(f"Seu nome é {nome}. {type(nome)}")
print(f"Sua idade é {idade} {type(idade)}")
print(f"Sua idade é {altura}m. {type(altura)}")