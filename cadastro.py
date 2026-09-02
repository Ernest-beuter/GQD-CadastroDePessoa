# Sistema de Cadastro de Pessoas - versao 2
# novos requisitos: menu, consulta, alteracao e listagem

def printMenu():
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    return int(input("Escolha uma opcao: "))

def cadastrarPessoa(nomes, idades, emails):
    nome = input("Informe o nome: ")
    nomes.append(nome)
    idade = int(input("Informe a idade: "))
    idades.append(idade)
    email = input("Informe o e-mail: ")
    emails.append(email)
    if idade >= 18:
        print("Situação: Maior de idade")
    else:
        print("Situação: Menor de idade")

 

nomes = []
idades = []
emails = []

qtd = 0
op = 0

while op != 5:
    op = printMenu() 
    if op == 1:
        cadastrarPessoa(nomes, idades, emails)
    elif op == 2:
        busca = input("Nome para consultar: ")
        pos = 0;
        achou = 0;
        while pos < len(nomes) and achou == 0:
            if(busca==nomes[pos]):
                print("Nome: " + nomes[pos])
                print("Idade: " + str(idades[pos]))
                print("E-mail: " + emails[pos])
                print("-------------------------")
                achou = 1
            pos = pos + 1
        if achou == 0:
            print("Nao encontrado")
    elif op == 3:
        busca = input("Nome para alterar: ")
        pos = 0;
        achou = 0;
        while pos < len(nomes) and achou == 0:
            if(busca==nomes[pos]):
                print("Nome: " + nomes[pos])
                print("Idade: " + str(idades[pos]))
                print("E-mail: " + emails[pos])
                print("-------------------------")
                nome = input("Novo nome: ")
                idade = int(input("Nova idade: "))
                email = input("Novo e-mail: ")
                nomes[pos] = nome
                idades[pos] = idade
                if email != "":
                    emails[pos] = email
                achou = 1
            pos = pos + 1
        if achou == 0:
            print("Nao encontrado")
    elif op == 4:
        if(len(nomes)==0):
            print("Nenhum cadastro")
        else:
            pos = 0;
            while pos < len(nomes):
                print("Nome: " + nomes[pos])
                print("Idade: " + str(idades[pos]))
                print("E-mail: " + emails[pos])
                print("-------------------------")
                pos = pos + 1
            print("Total: " + str(len(nomes)))
    elif op == 5:
        print("Saindo...")

    else:
        print("Opcao invalida")

print("Fim do programa")
