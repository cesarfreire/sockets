from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.comando.time.comando_adicionar_pessoa_ao_time import ComandoAdicionarPessoaAoTime
from src.comando.time.comando_criar_time import ComandoCriarTime
from src.modelo.time import Time


def test_adicionar_pessoa_ao_time_deve_retornar_sucesso():
    cmd = "ADD_PESSOA;Flamengo;11111111111"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 2
    banco: BancoDeDados = BancoDeDadosLocal()

    comando_adicionar_pessoa = ComandoAdicionarPessoaAoTime(banco, nome_time=dados[0], cpf=dados[1])
    assert isinstance(comando_adicionar_pessoa, Comando)
    response_get = comando_adicionar_pessoa.executar()
    assert response_get == "Pessoa adicionada ao time com sucesso."

def test_adicionar_pessoa_ja_associada_ao_time_deve_retornar_erro():
    cmd = "ADD_PESSOA;Corinthians;12345678900"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 2
    banco: BancoDeDados = BancoDeDadosLocal()

    comando_adicionar_pessoa = ComandoAdicionarPessoaAoTime(banco, nome_time=dados[0], cpf=dados[1])
    assert isinstance(comando_adicionar_pessoa, Comando)
    response_get = comando_adicionar_pessoa.executar()
    assert response_get == "Erro: Pessoa já associada ao time."

def test_adicionar_pessoa_ao_time_inexistente_deve_retornar_erro():
    cmd = "ADD_PESSOA;Abobrinha;12345678900"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 2
    banco: BancoDeDados = BancoDeDadosLocal()

    comando_adicionar_pessoa = ComandoAdicionarPessoaAoTime(banco, nome_time=dados[0], cpf=dados[1])
    assert isinstance(comando_adicionar_pessoa, Comando)
    response_get = comando_adicionar_pessoa.executar()
    assert response_get == "Time não encontrado."

def test_adicionar_pessoa_inexistes_ao_time_deve_retornar_erro():
    cmd = "ADD_PESSOA;Corinthians;33333333333"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 2
    banco: BancoDeDados = BancoDeDadosLocal()

    comando_adicionar_pessoa = ComandoAdicionarPessoaAoTime(banco, nome_time=dados[0], cpf=dados[1])
    assert isinstance(comando_adicionar_pessoa, Comando)
    response_get = comando_adicionar_pessoa.executar()
    assert response_get == "Pessoa não encontrada."

def test_adicionar_pessoa_ao_time_sem_pessoas_cadastradas_deve_retornar_erro():
    cmd = "INSERT;Bangu;Amador;Brasil;3"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 4
    banco: BancoDeDados = BancoDeDadosLocal(iniciar_zerado=True)
    time = Time(
        nome=dados[0],
        categoria=dados[1],
        pais_origem=dados[2],
        quantidade_titulos=dados[3]
    )

    comando_insert = ComandoCriarTime(
        banco=banco,
        time=time,
        cpfs=[]
    )
    assert isinstance(comando_insert, Comando)
    response_get = comando_insert.executar()
    assert response_get == "Time criado com sucesso."

    cmd = "ADD_PESSOA;Bangu;33333333333"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 2


    comando_adicionar_pessoa = ComandoAdicionarPessoaAoTime(banco, nome_time=dados[0], cpf=dados[1])
    assert isinstance(comando_adicionar_pessoa, Comando)
    response_get = comando_adicionar_pessoa.executar()
    assert response_get == "Sem pessoas cadastradas."
