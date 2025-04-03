from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.comando.pessoa.comando_criar_pessoa import ComandoCriarPessoa
from src.modelo.pessoa import Pessoa


def test_insert_pessoa_deve_retornar_sucesso():
    cmd = "INSERT;10481485996;CESAR;WENCESLAU BORINI"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 3
    banco: BancoDeDados = BancoDeDadosLocal()
    pessoa = Pessoa(cpf=dados[0], nome=dados[1], endereco=dados[2])
    assert isinstance(pessoa, Pessoa)
    comando_insert = ComandoCriarPessoa(banco, pessoa=pessoa)
    assert isinstance(comando_insert, Comando)

    response = comando_insert.executar()
    assert response == "Criado com sucesso."


def test_insert_pessoa_duplicada_deve_retornar_erro():
    cmd = "INSERT;10481485996;CESAR;WENCESLAU BORINI"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 3
    banco: BancoDeDados = BancoDeDadosLocal()
    pessoa = Pessoa(cpf=dados[0], nome=dados[1], endereco=dados[2])
    assert isinstance(pessoa, Pessoa)
    comando_insert = ComandoCriarPessoa(banco, pessoa=pessoa)
    assert isinstance(comando_insert, Comando)

    response = comando_insert.executar()
    assert response == "Criado com sucesso."

    response2 = comando_insert.executar()
    assert response2 == "Erro: CPF já cadastrado."
