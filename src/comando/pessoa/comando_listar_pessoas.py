from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando


class ComandoListarPessoas(Comando):
    def __init__(self, banco: BancoDeDados) -> None:
        self.banco: BancoDeDados = banco

    def executar(self) -> str:
        return self.banco.listar_pessoas()

    def desfazer(self) -> str:
        return "Não é possível desfazer a listagem."

    def refazer(self) -> str:
        return self.executar()
