from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.modelo.pessoa import Pessoa
from src.modelo.time import Time
import re


class ComandoApagarTime(Comando):
    def __init__(self, banco: BancoDeDados, nome: str) -> None:
        self.banco: BancoDeDados = banco
        self.nome: str = nome
        self.time_apagado: None | Time = None

    def executar(self) -> str:
        dados_time_apagado: str = self.banco.ler_time(self.nome)

        if not dados_time_apagado:
            return "Time não encontrado."

        dados_time_apagado_list: list = dados_time_apagado.split(';', 4)
        nome: str = dados_time_apagado_list[0]
        categoria: str = dados_time_apagado_list[1]
        pais_origem: str = dados_time_apagado_list[2]
        qtdade_titulos: int = int(dados_time_apagado_list[3])
        participantes: str = str(dados_time_apagado_list[4:])

        print(f"Participantes: {participantes}")

        cpfs = re.findall(r"'(\d{11})", participantes)
        print(f"CPFs: {cpfs}")
        self.time_apagado = Time(nome, categoria, pais_origem, qtdade_titulos)
        for cpf in cpfs:
            print(f"CPF: {cpf}")
            pessoa = self.banco.ler_pessoa_objeto(cpf)
            if not pessoa:
                return f"Pessoa com cpf {cpf} não encontrada. Parece que o banco não está íntegro."

            self.time_apagado.adicionar_participante(pessoa)

        return self.banco.deletar_time(self.nome)

    def desfazer(self) -> str:
        return self.banco.criar_time(self.time_apagado)

    def refazer(self) -> str:
        return self.executar()
