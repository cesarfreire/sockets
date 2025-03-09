from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comandos.comando_abstrato import Comando


class ComandoLer(Comando):
    def __init__(self, banco: BancoDeDados, cpf: str) -> None:
        self.banco = banco
        self.cpf = cpf

    def executar(self) -> str:
        return self.banco.ler(self.cpf)

    def desfazer(self) -> str:
        return "Não é possível desfazer a leitura."

    def refazer(self) -> str:
        return self.executar()