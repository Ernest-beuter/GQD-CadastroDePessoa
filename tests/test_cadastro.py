from cadastro import CadastroPessoa

def testCadastrarPessoa():
    cadastro = CadastroPessoa()
    cadastro.cadastrar("Jean", 23, "jean@seibert.moe")

    pessoas = cadastro.listar()
    assert len(pessoas) == 1
    assert pessoas[0].getNome() == "Jean"
    assert pessoas[0].getIdade() == 23
    assert pessoas[0].getEmail() == "jean@seibert.moe"

def testBuscarPorNome():
    cadastro = CadastroPessoa()
    cadastro.cadastrar("Jean", 23, "jean@seibert.moe")

    encontrada = cadastro.buscarPorNome("Jean")

    assert encontrada is not None
    assert encontrada.getNome() == "Jean"
    assert encontrada.getIdade() == 23
    assert encontrada.getEmail() == "jean@seibert.moe"
