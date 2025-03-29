from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.comando.time.comando_ler_time import ComandoLerTime
from src.comando.time.comando_listar_times import ComandoListarTimes


def test_list_times_sem_dados_deve_retornar_zero():
    banco: BancoDeDados = BancoDeDadosLocal(iniciar_zerado=True)
    comando_list_times = ComandoListarTimes(banco=banco)
    assert isinstance(comando_list_times, Comando)
    response_list = comando_list_times.executar()
    assert response_list == "0"

def test_list_times_deve_retornar_dados():
    banco: BancoDeDados = BancoDeDadosLocal(iniciar_zerado=False)
    comando_list_times = ComandoListarTimes(banco=banco)
    assert isinstance(comando_list_times, Comando)
    response_list = comando_list_times.executar()
    assert response_list == """2
1;Flamengo;Profissional;Brasil;58
Pessoas:
98765432100;Ciclano;Rua B
--------------------------------------------------
2;Corinthians;Profissional;Brasil;2
Pessoas:
12345678900;Fulano;Rua A
--------------------------------------------------"""
