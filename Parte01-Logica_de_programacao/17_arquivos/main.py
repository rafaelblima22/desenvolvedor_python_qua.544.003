import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

limpar()
while True:
    print("1 - Gravar arquivo")
    print("2 - Ler arquivo")
    print("3 - Sair")

    opcao = input("Informe a opção desejada: ").strip()

    limpar()
    
    match opcao:
        case "1":
            novo_texto = input("Digite o seu texto: ")
            nome_arquivo = input("Informe o nome do arquivo sem a extensão: ").strip()

            #SECTION -  Gravar novo arquivo
            #NOTE - w -> escreve/escreve sobre o que ja esta escrito no arquivo.
            #NOTE - a -> escreve/escreve a frente do que ja esta escrito.
            with open(f"17_arquivos/arquivos/{nome_arquivo}.txt", "w", encoding="utf-8") as f:
                f.write(novo_texto)
        case "2":
             nome_arquivo = input("Informe o nome do arquivo sem a extensão: ").strip()
             try:
                 with open(f"17_arquivos/arquivos/{nome_arquivo}.txt", "r", encoding="utf-8") as f:
                     conteudo = f.read()
                 print(conteudo)
                 print("")
                 print("")
                 continue
             except FileNotFoundError:
                 print("Arquivo não encontrado!")
             continue
        case "3":
            print("programa Encerrado")
            break
        case _:
            print("opção invalida!")
            continue


