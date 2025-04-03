from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.comando.pessoa.comando_apagar_pessoa import ComandoApagarPessoa
from src.comando.pessoa.comando_criar_pessoa import ComandoCriarPessoa
from src.modelo.pessoa import Pessoa


def test_delete_pessoa_deve_retornar_sucesso():
    cmd = "INSERT;10481485996;CESAR;WENCESLAU BORINI"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 3
    banco: BancoDeDados = BancoDeDadosLocal()
    pessoa = Pessoa(cpf=dados[0], nome=dados[1], endereco=dados[2])
    assert isinstance(pessoa, Pessoa)
    comando_insert = ComandoCriarPessoa(banco, pessoa=pessoa)
    assert isinstance(comando_insert, Comando)

    response_create = comando_insert.executar()
    assert response_create == "Criado com sucesso."

    comando_delete = ComandoApagarPessoa(banco=banco, cpf=pessoa.cpf)
    response_delete = comando_delete.executar()
    assert response_delete == "Pessoa removida com sucesso."


def test_delete_pessoa_inexistente_deve_retornar_pessoa_nao_encontrada():
    cmd = "DELETE;123"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 1
    banco: BancoDeDados = BancoDeDadosLocal()

    comando_delete = ComandoApagarPessoa(banco=banco, cpf=dados[0])
    response_delete = comando_delete.executar()
    assert response_delete == "Pessoa não encontrada."


def test_delete_pessoa_com_banco_zerado_deve_retornar_nenhuma_pessoa_cadastrada():
    cmd = "DELETE;123"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 1
    banco: BancoDeDados = BancoDeDadosLocal(iniciar_zerado=True)

    comando_delete = ComandoApagarPessoa(banco=banco, cpf=dados[0])
    response_delete = comando_delete.executar()
    assert response_delete == "Sem pessoas cadastradas."
