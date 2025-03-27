from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.modelo.pessoa import Pessoa


class ComandoAtualizarPessoa(Comando):
    def __init__(self, banco: BancoDeDados, pessoa: Pessoa) -> None:
        self.banco: BancoDeDados = banco
        self.pessoa: Pessoa = pessoa
        self.pessoa_antiga: Pessoa | None = None

    def executar(self) -> str:
        dados_antigos: str = self.banco.ler_pessoa(self.pessoa.cpf)
        if not dados_antigos:
            return "Pessoa não encontrada."

        dados_antigos_list = dados_antigos.split(';')
        self.pessoa_antiga = Pessoa(
            dados_antigos_list[0], dados_antigos_list[1], dados_antigos_list[2]
        )
        return self.banco.atualizar_pessoa(self.pessoa)

    def desfazer(self) -> str:
        return self.banco.atualizar_pessoa(self.pessoa_antiga)

    def refazer(self) -> str:
        return self.executar()
