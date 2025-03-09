from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comandos.comando_abstrato import Comando
from src.models.pessoa import Pessoa


class ComandoAtualizar(Comando):
    def __init__(self, banco: BancoDeDados, pessoa: Pessoa) -> None:
        self.banco = banco
        self.pessoa = pessoa
        self.pessoa_antiga = None

    def executar(self) -> str:
        dados_antigos = self.banco.ler(self.pessoa.cpf)
        if not dados_antigos:
            return "Pessoa não encontrada."

        dados_antigos = dados_antigos.split(';')
        self.pessoa_antiga = Pessoa(
            dados_antigos[0], dados_antigos[1], dados_antigos[2]
        )
        return self.banco.atualizar(self.pessoa)

    def desfazer(self) -> str:
        return self.banco.atualizar(self.pessoa_antiga)

    def refazer(self) -> str:
        return self.executar()