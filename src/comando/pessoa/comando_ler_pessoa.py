from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando


class ComandoLerPessoa(Comando):
    def __init__(self, banco: BancoDeDados, cpf: str) -> None:
        self.banco: BancoDeDados = banco
        self.cpf: str = cpf

    def executar(self) -> str:
        return self.banco.ler_pessoa(self.cpf)

    def desfazer(self) -> str:
        return "Não é possível desfazer a leitura."

    def refazer(self) -> str:
        return self.executar()
