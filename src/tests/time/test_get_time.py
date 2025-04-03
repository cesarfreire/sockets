from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.comando.time.comando_ler_time import ComandoLerTime


def test_get_time_deve_retornar_sucesso():
    cmd = "GET_TIME;Flamengo"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 1
    banco: BancoDeDados = BancoDeDadosLocal()

    comando_get_time = ComandoLerTime(banco=banco, nome=dados[0])
    assert isinstance(comando_get_time, Comando)
    response_get = comando_get_time.executar()
    assert response_get == "Flamengo;Profissional;Brasil;58;98765432100;Ciclano;Rua B"


def test_get_time_inexistente_deve_retornar_time_nao_encontrado():
    cmd = "GET_TIME;ABOBRINHA"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 1
    banco: BancoDeDados = BancoDeDadosLocal()

    comando_get_time = ComandoLerTime(banco=banco, nome=dados[0])
    assert isinstance(comando_get_time, Comando)
    response_get = comando_get_time.executar()
    assert response_get == "Time não encontrado."
