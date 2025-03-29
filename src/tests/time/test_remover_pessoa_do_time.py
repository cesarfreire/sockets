from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.comando.time.comando_remover_pessoa_do_time import ComandoRemoverPessoaDoTime


def test_remover_pessoa_do_time_deve_retornar_sucesso():
    cmd = "REMOVE_PESSOA;Flamengo;98765432100"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 2
    banco: BancoDeDados = BancoDeDadosLocal()

    comando_remover_pessoa = ComandoRemoverPessoaDoTime(banco, nome_time=dados[0], cpf=dados[1])
    assert isinstance(comando_remover_pessoa, Comando)
    response_remover = comando_remover_pessoa.executar()
    assert response_remover == "Pessoa removida do time com sucesso."

def test_remover_pessoa_nao_associada_ao_time_deve_retornar_erro():
    cmd = "REMOVE_PESSOA;Corinthians;98765432100"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 2
    banco: BancoDeDados = BancoDeDadosLocal()

    comando_adicionar_pessoa = ComandoRemoverPessoaDoTime(banco, nome_time=dados[0], cpf=dados[1])
    assert isinstance(comando_adicionar_pessoa, Comando)
    response_get = comando_adicionar_pessoa.executar()
    assert response_get == "Erro: Pessoa não está associada ao time."

def test_remover_pessoa_do_time_inexistente_deve_retornar_erro():
    cmd = "REMOVE_PESSOA;Abobrinha;12345678900"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 2
    banco: BancoDeDados = BancoDeDadosLocal()

    comando_adicionar_pessoa = ComandoRemoverPessoaDoTime(banco, nome_time=dados[0], cpf=dados[1])
    assert isinstance(comando_adicionar_pessoa, Comando)
    response_get = comando_adicionar_pessoa.executar()
    assert response_get == "Time não encontrado."

def test_remover_pessoa_inexistente_do_time_deve_retornar_erro():
    cmd = "REMOVE_PESSOA;Corinthians;33333333333"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 2
    banco: BancoDeDados = BancoDeDadosLocal()

    comando_adicionar_pessoa = ComandoRemoverPessoaDoTime(banco, nome_time=dados[0], cpf=dados[1])
    assert isinstance(comando_adicionar_pessoa, Comando)
    response_get = comando_adicionar_pessoa.executar()
    assert response_get == "Pessoa não encontrada."

