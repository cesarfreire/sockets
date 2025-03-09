from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comandos.comando_abstrato import Comando
from src.models.pessoa import Pessoa


class ComandoApagar(Comando):
    def __init__(self, banco: BancoDeDados, cpf: str) -> None:
        self.banco = banco
        self.cpf = cpf
        self.pessoa_apagada = None

    def executar(self) -> str:
        dados_pessoa_apagada = self.banco.ler(self.cpf)

        if not dados_pessoa_apagada:
            return "Pessoa não encontrada."

        dados_pessoa_apagada = dados_pessoa_apagada.split(';')
        self.pessoa_apagada = Pessoa(
            dados_pessoa_apagada[0], dados_pessoa_apagada[1], dados_pessoa_apagada[2]
        )
        return self.banco.deletar(self.cpf)

    def desfazer(self) -> str:
        return self.banco.criar(self.pessoa_apagada)

    def refazer(self) -> str:
        return self.executar()