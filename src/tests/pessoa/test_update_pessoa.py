from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.comando.pessoa.comando_atualizar_pessoa import ComandoAtualizarPessoa
from src.comando.pessoa.comando_criar_pessoa import ComandoCriarPessoa
from src.modelo.pessoa import Pessoa


def test_update_pessoa_deve_retornar_sucesso():
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

    cmd2 = "UPDATE;10481485996;CESAR;WENCESLAU BORINI NOVO"
    operacao2, *dados2 = cmd2.split(";")
    assert len(dados2) == 3

    pessoa2 = Pessoa(cpf=dados2[0], nome=dados2[1], endereco=dados2[2])
    assert isinstance(pessoa2, Pessoa)
    comando_update = ComandoAtualizarPessoa(banco, pessoa=pessoa2)
    assert isinstance(comando_update, Comando)
    response_update = comando_update.executar()
    assert response_update == "Pessoa atualizada com sucesso."
    response_get = banco.ler_pessoa(pessoa2.cpf)
    assert response_get == f"{pessoa2.cpf};{pessoa2.nome};{pessoa2.endereco}"


def test_update_pessoa_inexistente_deve_retornar_nao_encontrado():
    cmd2 = "UPDATE;555555555555;SEILA_MEU;ABOBRINHA"
    banco: BancoDeDados = BancoDeDadosLocal()
    operacao2, *dados2 = cmd2.split(";")
    assert len(dados2) == 3

    pessoa2 = Pessoa(cpf=dados2[0], nome=dados2[1], endereco=dados2[2])
    assert isinstance(pessoa2, Pessoa)
    comando_update = ComandoAtualizarPessoa(banco, pessoa=pessoa2)
    assert isinstance(comando_update, Comando)
    response_update = comando_update.executar()
    assert response_update == "Pessoa não encontrada."
