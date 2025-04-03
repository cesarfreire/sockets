from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.modelo.time import Time


class ComandoAtualizarTime(Comando):
    def __init__(self, banco: BancoDeDados, time: Time) -> None:
        self.banco: BancoDeDados = banco
        self.time: Time = time
        self.time_antigo: Time | None = None

    def executar(self) -> str:
        dados_antigos: str = self.banco.ler_time(self.time.nome)
        if dados_antigos == "Time não encontrado.":
            return dados_antigos

        dados_antigos_list = dados_antigos.split(";")
        self.time_antigo: Time = Time(
            nome=dados_antigos_list[0],
            categoria=dados_antigos_list[1],
            pais_origem=dados_antigos_list[2],
            quantidade_titulos=int(dados_antigos_list[3]),
        )
        return self.banco.atualizar_time(self.time)

    def desfazer(self) -> str:
        return self.banco.atualizar_time(self.time)

    def refazer(self) -> str:
        return self.executar()
