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

def exibirPessoa(nome, idade, email):
    print("Nome: " + nome)
    print("Idade: " + str(idade))
    print("E-mail: " + email)
    print("-------------------------")
 


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

def buscarPessoa(busca, nomes):
    posicao = 0
    while posicao < len(nomes):
        if(busca==nomes[posicao]):
            return posicao
        posicao = posicao + 1
    print("Não encontrado")
    return -1

def consultarPessoa(nomes, idades, emails):
    busca = input("Nome para consultar: ")
    posicao = buscarPessoa(busca, nomes)
    if(posicao!=-1):
        exibirPessoa(nomes[posicao], idades[posicao], emails[posicao])

def alterarPessoa(nomes, idades, emails):
    busca = input("Nome para alterar: ")
    posicao = buscarPessoa(busca, nomes)
    if(posicao!=-1):
        exibirPessoa(nomes[posicao], idades[posicao], emails[posicao])
        nome = input("Novo nome: ")
        idade = int(input("Nova idade: "))
        email = input("Novo e-mail: ")
        if(nome!=""):
            nomes[posicao] = nome
        if(idade>0):
            idades[posicao] = idade
        if(email!=""):
            emails[posicao] = email

def listarPessoas(nomes, idades, emails):
    if(len(nomes)==0):
        print("Nenhum cadastro")
    else:
        posicao = 0;
        while posicao < len(nomes):
            exibirPessoa(nomes[posicao], idades[posicao], emails[posicao])
            posicao = posicao + 1
        print("Total: " + str(len(nomes)))


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
        consultarPessoa(nomes, idades, emails)
    elif op == 3:
        alterarPessoa(nomes, idades, emails)
    elif op == 4:
        listarPessoas(nomes, idades, emails)
    elif op == 5:
        print("Saindo...")

    else:
        print("Opcao invalida")

print("Fim do programa")
