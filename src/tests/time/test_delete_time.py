from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.comando.time.comando_apagar_time import ComandoApagarTime
from src.comando.time.comando_ler_time import ComandoLerTime


def test_delete_timne_deve_retornar_sucesso():
    cmd = "DELETE_TIME;Flamengo"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 1
    banco: BancoDeDados = BancoDeDadosLocal()

    comando_delete_time = ComandoApagarTime(banco=banco, nome=dados[0])
    assert isinstance(comando_delete_time, Comando)
    response_get = comando_delete_time.executar()
    assert response_get == "Time removido com sucesso."

def test_delete_time_inexistente_deve_retornar_time_nao_encontrado():
    cmd = "DELETE_TIME;ABOBRINHA"
    operacao, *dados = cmd.split(";")

    assert len(dados) == 1
    banco: BancoDeDados = BancoDeDadosLocal()

    comando_get_time = ComandoLerTime(banco=banco, nome=dados[0])
    assert isinstance(comando_get_time, Comando)
    response_get = comando_get_time.executar()
    assert response_get == "Time não encontrado."
