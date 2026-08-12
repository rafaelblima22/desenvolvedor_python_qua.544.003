#TODO - atividade 03
#Crie um programa que receba o nome de um aluno e 3 notas.
#O programa deve calcular a média do aluno e informar se o aluno esta aprovado (media minima = 7) ou reprovado.
#O programa deve gravar esses dados em um JSON.
#Ao final, o usuário deverá escolher se deseja inserir as notas de outro aluno, que deverão ser gravadas no mesmo arquivo JSON.

#SECTION - Importação de bibliotecas.
import json
import os

alunos = []

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    limpar()
    aluno = {}
    aluno['nome'] = input("Informe o nome do aluno: ").strip().title()
    aluno['nota1'] = float(input(f"Informe a 1º nota do {aluno['nome']}: ").strip().replace(',','.'))
    aluno['nota2'] = float(input(f"Informe a 2º nota do {aluno['nome']}: ").strip().replace(',','.'))
    aluno['nota3'] = float(input(f"Informe a 3º nota do {aluno['nome']}: ").strip().replace(',','.'))

    limpar()

    aluno['media'] = round((aluno['nota1'] + aluno['nota2'] + aluno['nota3'])/3 , 2)

    if aluno['media'] < 7:
        aluno['status'] = "Reprovado"
        print(f"O {aluno['nome']} foi {aluno['status']} com media: {aluno['media']}")
    else:
        aluno['status'] = "Aprovado"
        print(f"O {aluno['nome']} foi {aluno['status']} com media: {aluno['media']}")

    alunos.append(aluno)
    with open(f"atividade_03/listaalunos.json","w", encoding="utf8") as f:
        json.dump(alunos, f)

    opcao = input("Você deseja informar outro aluno? (S - para informar outro aluno) (N - para sair)").strip().upper()
    if opcao == "N":
        break
    else:
        continue