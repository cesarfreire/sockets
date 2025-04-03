from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.comando.time.comando_atualizar_time import ComandoAtualizarTime
from src.comando.time.comando_criar_time import ComandoCriarTime
from src.modelo.time import Time


def test_update_time_deve_retornar_sucesso():
    cmd = "UPDATE_TIME;Flamengo;Amador;Brasil;9999"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 4
    banco: BancoDeDados = BancoDeDadosLocal()
    time = Time(
        nome=dados[0],
        categoria=dados[1],
        pais_origem=dados[2],
        quantidade_titulos=dados[3]
    )

    comando_update = ComandoAtualizarTime(
        banco=banco,
        time=time
    )
    assert isinstance(comando_update, Comando)
    response_get = comando_update.executar()
    assert response_get == "Time atualizado com sucesso."


def test_update_time_inexistente_deve_retornar_erro():
    cmd = "UPDATE_TIME;Abobrinha;Amador;Paraguai;123"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 4
    banco: BancoDeDados = BancoDeDadosLocal()
    time = Time(
        nome=dados[0],
        categoria=dados[1],
        pais_origem=dados[2],
        quantidade_titulos=dados[3]
    )

    comando_update = ComandoAtualizarTime(
        banco=banco,
        time=time
    )
    assert isinstance(comando_update, Comando)
    response_get = comando_update.executar()
    assert response_get == "Time não encontrado."