from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.modelo.pessoa import Pessoa
from src.modelo.time import Time


class ComandoAdicionarPessoaAoTime(Comando):
    def __init__(self, banco: BancoDeDados, nome_time: str, cpf: str) -> None:
        self.banco: BancoDeDados = banco
        self.nome_time: str = nome_time
        self.cpf: str = cpf
        self.time: Time | None = None
        self.pessoa: Pessoa | None = None

    def executar(self) -> str:
        dados_time = self.banco.ler_time(self.nome_time)
        if dados_time == "Time não encontrado.":
            return dados_time

        dados_time_list = dados_time.split(";")
        self.time = Time(
            dados_time_list[0],
            dados_time_list[1],
            dados_time_list[2],
            int(dados_time_list[3]),
        )
        dados_pessoa = self.banco.ler_pessoa(self.cpf)
        if (
            dados_pessoa == "Pessoa não encontrada."
            or dados_pessoa == "Sem pessoas cadastradas."
        ):
            return dados_pessoa
        dados_pessoa_list = dados_pessoa.split(";")
        self.pessoa = Pessoa(
            dados_pessoa_list[0], dados_pessoa_list[1], dados_pessoa_list[2]
        )

        return self.banco.adicionar_pessoa_ao_time(time=self.time, pessoa=self.pessoa)

    def desfazer(self) -> str:
        if not self.time or not self.pessoa:
            return "Time ou pessoa não encontrados."
        return self.banco.remover_pessoa_do_time(time=self.time, pessoa=self.pessoa)

    def refazer(self) -> str:
        return self.executar()
