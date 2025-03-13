from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comandos.comando_abstrato import Comando
from src.models.pessoa import Pessoa


class ComandoApagar(Comando):
    def __init__(self, banco: BancoDeDados, cpf: str) -> None:
        self.banco: BancoDeDados = banco
        self.cpf: str = cpf
        self.pessoa_apagada: None | Pessoa = None

    def executar(self) -> str:
        dados_pessoa_apagada: str = self.banco.ler(self.cpf)

        if not dados_pessoa_apagada:
            return "Pessoa não encontrada."

        dados_pessoa_apagada_list: list = dados_pessoa_apagada.split(';')
        self.pessoa_apagada = Pessoa(
            dados_pessoa_apagada_list[0], dados_pessoa_apagada_list[1], dados_pessoa_apagada_list[2]
        )
        return self.banco.deletar(self.cpf)

    def desfazer(self) -> str:
        return self.banco.criar(self.pessoa_apagada)

    def refazer(self) -> str:
        return self.executar()
