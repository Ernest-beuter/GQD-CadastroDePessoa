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
    print("5 - Analisar pessoa")
    print("6 - Sair")
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

def analisarIdade(idade):
    if idade < 12:
        print("Faixa etária: Criança")
    elif idade < 18:
        print("Faixa etária: Adolescente")
    elif idade < 30:
        print("Faixa etária: Adulto jovem")
    elif idade < 60:
        print("Faixa etária: Adulto")
    else:
        print("Faixa etária: Idoso")

def analisarEmail(email):
    if email == "":
        print("Cadastro incompleto: sem o e-mail")
        return -1;
    if "@" not in email:
        print("E-mail invalido")
        return -1;
    print("E-mail utilizável");
    return 1;

def analisarProvedorEmail(email):
    if email.endswith("@gmail.com"):
        print("Provedor: Gmail")
    elif email.endswith("@outlook.com"):
        print("Provedor: Outlook")
    elif email.endswith("@hotmail.com"):
        print("Provedor: Hotmail")
    elif email.endswith("@utfpr.edu.br"):
        print("Provedor: UTFPR")
    else:
        print("Provedor: Outro")


def analisarIdadeEEmail(idade, email):
    if idade >= 18 and email != "":
        print("Cadastro apto para contato")
    elif idade >= 18 and email == "":
        print("Maior de idade sem contato")
    elif idade < 18 and email != "":
        print("Menor de idade com contato")
    else:
        print("Menor de idade sem contato")

def analisarPessoa(nomes, idades, emails):
    busca = input("Nome para analisar: ")
    posicao = buscarPessoa(busca, nomes)

    if(posicao==-1):
        print("Pessoa não encontrada")
    else:
        idade = idades[posicao]
        email = emails[posicao]

        analisarIdade(idade)
        emailOk = analisarEmail(email)
        if(emailOk>0):
            analisarProvedorEmail(email)
        analisarIdadeEEmail(idade, email)




nomes = []
idades = []
emails = []

qtd = 0
op = 0

while op != 6:
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
        analisarPessoa(nomes, idades, emails)
    elif op == 6:
        print("Saindo...")

    else:
        print("Opcao invalida")

print("Fim do programa")
