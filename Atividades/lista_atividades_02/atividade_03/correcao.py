import json
import os

alunos = []

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

limpar()
while True:
    print("1 - Informar dado")
    print("2 - Sair do programa")

    opcao = input("Informar opção: ").strip()
    limpar()

    match opcao:
        case '1':
            aluno = {}
            notas = [0,0,0]

            aluno['nome'] = input("Informe o nome do aluno: ").strip().title()
            for i in range(len(notas)):
                notas[i] = float(input(f"Informa a {i+1}º nota: ").replace(",","."))

            aluno['notas'] = notas
            aluno['media'] = sum(notas)/len(notas)
            aluno['resultados'] = "aprovado" if aluno["media"] >= 7 else "reprovado"
            alunos.append(aluno)

            #REVIEW - UTF8 dando erro
            with open(f"atividade_03/arquivo.json", "w", encoding="utf8") as f:
                json.dump(alunos, f)
            print("Dados do aluno gravados com sucesso!")
            continue
        case'2':
            break
        case _:
            print("opção invalida")
            continue