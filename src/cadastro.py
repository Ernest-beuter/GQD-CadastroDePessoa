from pessoa import Pessoa


class CadastroPessoa:
    """Mantém e controla o conjunto de pessoas cadastradas"""
    def __init__(self):
        self.__pessoas = []

    def cadastrar(self, nome, idade, email):
        pessoa = Pessoa(nome, idade, email)
        self.__pessoas.append(pessoa)
        return pessoa

    def buscarPorNome(self, nome):
        for pessoa in self.__pessoas:
            if pessoa.getNome() == nome:
                return pessoa
        return None

    def listar(self):
        return self.__pessoas

    def alterar(self, nome, novoNome, novaIdade, novoEmail):
        pessoa = self.buscarPorNome(nome)
        if pessoa is None:
            return None
        pessoa.setNome(novoNome)
        pessoa.setIdade(novaIdade)
        pessoa.setEmail(novoEmail)
        return pessoa
