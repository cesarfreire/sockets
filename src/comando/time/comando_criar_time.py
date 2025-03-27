from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.modelo.pessoa import Pessoa
from src.modelo.time import Time


class ComandoCriarTime(Comando):
    def __init__(self, banco: BancoDeDados, time: Time, cpfs: list) -> None:
        self.banco: BancoDeDados = banco
        self.time: Time = time
        self.cpfs: list = cpfs

    def executar(self) -> str:
        for cpf in self.cpfs:
            if not self.banco.ler_pessoa(cpf):
                return f"Pessoa com cpf {cpf} não encontrada."

            dados_pessoa = self.banco.ler_pessoa(cpf)
            dados_pessoa_list = dados_pessoa.split(';')
            pessoa = Pessoa(dados_pessoa_list[0], dados_pessoa_list[1], dados_pessoa_list[2])
            self.time.adicionar_participante(pessoa)
        return self.banco.criar_time(self.time)

    def desfazer(self) -> str:
        return self.banco.deletar_time(self.time.nome)

    def refazer(self) -> str:
        return self.executar()
