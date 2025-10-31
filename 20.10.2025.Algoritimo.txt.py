def coletar_notas():
    with open("notas.txt", "w", encoding="utf-8") as arquivo:
        while True:
            nome = input("Nome do aluno (ou 'fim' para encerrar): ")
            if nome.lower() == "fim":
                break
            try:
                n1 = float(input("Nota 1: "))
                n2 = float(input("Nota 2: "))
                n3 = float(input("Nota 3: "))
            except ValueError:
                print(" Digite apenas números para as notas!")
                continue

            arquivo.write(f"{nome};{n1};{n2};{n3}\n")
    print("\n Dados salvos em notas.txt\n")

#.............................................................................................................

def classificar_alunos():
    with open("notas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    aprovados = []
    exame = []
    reprovados = []

    for linha in linhas:
        nome, n1, n2, n3 = linha.strip().split(";")
        media = (float(n1) + float(n2) + float(n3)) / 3

        if media >= 7:
            aprovados.append(f"{nome};{media:.2f};Aprovado\n")
        elif media >= 5:
            exame.append(f"{nome};{media:.2f}\n")
        else:
            reprovados.append(f"{nome};{media:.2f};Reprovado\n")

    
    with open("aprovados.txt", "w", encoding="utf-8") as a:
        a.writelines(aprovados)
    with open("exame.txt", "w", encoding="utf-8") as e:
        e.writelines(exame)
    with open("reprovados.txt", "w", encoding="utf-8") as r:
        r.writelines(reprovados)

    print(" Arquivos criados: aprovados, exame , reprovados\n")

#....................................................................................................................

def processar_exame():
    try:
        with open("exame.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print(" Arquivo exame.txt não encontrado!")
        return

    if not linhas:
        print("Nenhum aluno para exame.")
        return

    for linha in linhas:
        nome, media_antiga = linha.strip().split(";")
        media_antiga = float(media_antiga)
        try:
            nota_exame = float(input(f"Digite a nota do exame de {nome}: "))
        except ValueError:
            print(" Valor inválido! Pulando aluno...")
            continue

        media_final = (media_antiga + nota_exame) / 2

        if media_final >= 5:
            with open("aprovados.txt", "a", encoding="utf-8") as a:
                a.write(f"{nome};{media_final:.2f};Aprovado após exame\n")
        else:
            with open("reprovados.txt", "a", encoding="utf-8") as r:
                r.write(f"{nome};{media_final:.2f};Reprovado após exame\n")

    print("\n Exames processados e resultados atualizados!\n")

#.....................................................................................................................

def mostrar_resultados():
    print("=====  ALUNOS APROVADOS =====")
    with open("aprovados.txt", "r", encoding="utf-8") as a:
        print(a.read())

    print("=====  ALUNOS REPROVADOS =====")
    with open("reprovados.txt", "r", encoding="utf-8") as r:
        print(r.read())

#.....................................................................................................................

while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Coletar notas dos alunos")
    print("2 - Classificar alunos (Aprovado/Exame/Reprovado)")
    print("3 - Processar alunos em exame")
    print("4 - Mostrar resultados finais")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        coletar_notas()
    elif opcao == "2":
        classificar_alunos()
    elif opcao == "3":
        processar_exame()
    elif opcao == "4":
        mostrar_resultados()
    elif opcao == "5":
        print("Encerrando o programa...")
        break
    else:
        print(" Opção inválida!")