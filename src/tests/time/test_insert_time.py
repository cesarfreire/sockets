from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.comando.time.comando_criar_time import ComandoCriarTime
from src.modelo.time import Time


def test_insert_time_sem_pessoas_deve_retornar_sucesso():
    cmd = "INSERT;Bangu;Amador;Brasil;3"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 4
    banco: BancoDeDados = BancoDeDadosLocal()
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


def test_insert_time_com_pessoas_deve_retornar_sucesso():
    cmd = "INSERT;Fluminense;Profissional;Brasil;1"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 4
    banco: BancoDeDados = BancoDeDadosLocal()
    time = Time(
        nome=dados[0],
        categoria=dados[1],
        pais_origem=dados[2],
        quantidade_titulos=dados[3]
    )

    comando_insert = ComandoCriarTime(
        banco=banco,
        time=time,
        cpfs=["11111111111"]
    )
    assert isinstance(comando_insert, Comando)
    response_get = comando_insert.executar()
    assert response_get == "Time criado com sucesso."