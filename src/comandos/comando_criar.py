from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comandos.comando_abstrato import Comando
from src.models.pessoa import Pessoa


class ComandoCriar(Comando):
    def __init__(self, banco: BancoDeDados, pessoa: Pessoa) -> None:
        self.banco = banco
        self.pessoa = pessoa

    def executar(self) -> str:
        return self.banco.criar(self.pessoa)

    def desfazer(self) -> str:
        return self.banco.deletar(self.pessoa.cpf)

    def refazer(self) -> str:
        return self.executar()