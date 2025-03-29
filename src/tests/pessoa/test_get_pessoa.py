from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.comando.pessoa.comando_criar_pessoa import ComandoCriarPessoa
from src.comando.pessoa.comando_ler_pessoa import ComandoLerPessoa
from src.modelo.pessoa import Pessoa


def test_get_pessoa_deve_retornar_sucesso():
    cmd = "INSERT;10481485996;CESAR;WENCESLAU BORINI"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 3
    banco: BancoDeDados = BancoDeDadosLocal()
    pessoa = Pessoa(
        cpf=dados[0],
        nome=dados[1],
        endereco=dados[2]
    )
    assert isinstance(pessoa, Pessoa)
    comando_insert = ComandoCriarPessoa(banco, pessoa=pessoa)
    assert isinstance(comando_insert, Comando)

    response = comando_insert.executar()
    assert response == "Criado com sucesso."

    response_get = ComandoLerPessoa(banco=banco, cpf=pessoa.cpf)
    assert isinstance(response_get, Comando)
    response_get = response_get.executar()
    assert response_get == f"{pessoa.cpf};{pessoa.nome};{pessoa.endereco}"



def test_get_pessoa_inexistente_deve_retornar_nao_encontrada():
    banco: BancoDeDados = BancoDeDadosLocal()
    comando_insert = ComandoLerPessoa(banco, cpf="555555555555")
    assert isinstance(comando_insert, Comando)

    response = comando_insert.executar()
    assert response == "Pessoa não encontrada."