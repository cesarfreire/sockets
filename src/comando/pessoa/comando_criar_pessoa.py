from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.modelo.pessoa import Pessoa


class ComandoCriarPessoa(Comando):
    def __init__(self, banco: BancoDeDados, pessoa: Pessoa) -> None:
        self.banco: BancoDeDados = banco
        self.pessoa: Pessoa = pessoa

    def executar(self) -> str:
        return self.banco.criar_pessoa(self.pessoa)

    def desfazer(self) -> str:
        return self.banco.deletar_pessoa(self.pessoa.cpf)

    def refazer(self) -> str:
        return self.executar()
