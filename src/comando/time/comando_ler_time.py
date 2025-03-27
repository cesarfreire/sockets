from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando


class ComandoLerTime(Comando):
    def __init__(self, banco: BancoDeDados, nome: str) -> None:
        self.banco: BancoDeDados = banco
        self.nome: str = nome

    def executar(self) -> str:
        return self.banco.ler_time(self.nome)

    def desfazer(self) -> str:
        return "Não é possível desfazer a leitura."

    def refazer(self) -> str:
        return self.executar()
