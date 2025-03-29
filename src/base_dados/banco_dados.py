# Banco de Dados Simulado
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.modelo.pessoa import Pessoa
from src.modelo.time import Time


class BancoDeDadosLocal(BancoDeDados):
    def __init__(self, iniciar_zerado: bool = False):
        self.pessoas: dict = {
            "12345678900": "Fulano;Rua A",
            "98765432100": "Ciclano;Rua B",
            "11111111111": "Cesar;Wenceslau Borini"
        } if not iniciar_zerado else {}

        self.times: dict[int, str | None] = {
            1: "Flamengo;Profissional;Brasil;58",
            2: "Corinthians;Profissional;Brasil;2"
        } if not iniciar_zerado else {}

        self.times_pessoas: dict[int, list[str]] = {
            1: ["98765432100"],
            2: ["12345678900"]
        } if not iniciar_zerado else {}

    def criar_pessoa(self, pessoa: Pessoa) -> str:
        if pessoa.cpf in self.pessoas:
            return "Erro: CPF já cadastrado."
        self.pessoas[pessoa.cpf] = f"{pessoa.__str__()}"
        return "Criado com sucesso."

    def ler_pessoa(self, cpf: str) -> str:
        if len(self.pessoas) == 0:
            return "Sem pessoas cadastradas."
        dados: str = self.pessoas.get(cpf)
        if not dados:
            return "Pessoa não encontrada."
        return f"{cpf};{dados.__str__()}"

    def ler_pessoa_objeto(self, cpf: str) -> Pessoa | None:
        dados: str = self.pessoas.get(cpf)
        if not dados:
            return None
        partes: list = dados.split(";")
        return Pessoa(cpf, partes[0], partes[1])

    def atualizar_pessoa(self, pessoa: Pessoa) -> str:
        if pessoa.cpf not in self.pessoas:
            return "Pessoa não encontrada."
        self.pessoas[pessoa.cpf] = f"{pessoa.__str__()}"
        return "Pessoa atualizada com sucesso."

    def deletar_pessoa(self, cpf: str) -> str:
        if len(self.pessoas) == 0:
            return "Sem pessoas cadastradas."
        if cpf not in self.pessoas:
            return "Pessoa não encontrada."
        del self.pessoas[cpf]
        return "Pessoa removida com sucesso."

    def listar_pessoas(self) -> str:
        total: int = len(self.pessoas)
        if total == 0:
            return str(total)

        linhas: list = []
        linha_final = '-' * 50
        for cpf, info in self.pessoas.items():
            linha = f"{cpf};{info}"
            linhas.append(linha)
            linhas.append(linha_final)

        return f"{total}\n" + "\n".join(linhas)

    def criar_time(self, time: Time) -> str:
        # Verifica se o time já existe
        if any(t.split(";")[0] == time.nome for t in self.times.values()):
            return "Erro: Time já cadastrado."

        # Verifica se todas as pessoas associadas existem no banco de dados
        for pessoa in time.participantes:
            if pessoa.cpf not in self.pessoas:
                return f"Erro: Pessoa com CPF {pessoa.cpf} não está cadastrada."

        # Gera novo ID para o time
        novo_id = max(self.times.keys(), default=0) + 1
        self.times[novo_id] = (f"{time.nome};"
                               f"{time.categoria};"
                               f"{time.pais_origem};"
                               f"{time.quantidade_titulos}")
        if novo_id not in self.times_pessoas:
            self.times_pessoas[novo_id] = []
        # Adiciona as pessoas associadas ao time
        for pessoa in time.participantes:
            self.times_pessoas[novo_id].append(pessoa.cpf)

        return "Time criado com sucesso."

    def deletar_time(self, nome: str) -> str:
        for id_time, info in self.times.items():
            partes = info.split(";")
            if partes[0] == nome:
                del self.times[id_time]
                del self.times_pessoas[id_time]
                return "Time removido com sucesso."
        return "Time não encontrado."

    def ler_time(self, nome: str) -> str:
        # para cada time
        for id_time, info in self.times.items():
            partes: list = info.split(";")
            if partes[0] == nome:
                pessoas_cpf = self.times_pessoas[id_time] if id_time in self.times_pessoas else []
                pessoas = [f"{cpf};{self.pessoas[cpf]}" for cpf in pessoas_cpf if pessoas_cpf is not None]

                if len(pessoas) > 0:
                    return f"{info};" + ";".join(pessoas)
                return f"{info}"
        return "Time não encontrado."

    def listar_times(self) -> str:
        total: int = len(self.times)
        if total == 0:
            return str(total)

        linhas: list = []
        for id_time, info in self.times.items():
            pessoas_cpf = self.times_pessoas[id_time] if id_time in self.times_pessoas else []
            pessoas = [f"{cpf};{self.pessoas[cpf]}" for cpf in pessoas_cpf if pessoas_cpf is not None]
            linha_final = '-' * 50
            if len(pessoas) > 0:
                linha = f"{id_time};{info}\nPessoas:\n" + "\n".join(pessoas)
                linhas.append(linha)
                linhas.append(linha_final)
            else:
                linha = f"{id_time};{info}\nPessoas:\nNenhuma"
                linhas.append(linha)
                linhas.append(linha_final)

        return f"{total}\n" + "\n".join(linhas)

    def atualizar_time(self, time: Time) -> str:
        for time_id, time_dados in self.times.items():
            if time.nome == time_dados.split(";")[0]:
                self.times[time_id] = f"{time.__str__()}"
                return "Time atualizado com sucesso."

        return "Time não encontrado."


    def adicionar_pessoa_ao_time(self, time: Time, pessoa: Pessoa) -> str:
        # Verifica se o time existe
        for id_time, info in self.times.items():
            partes = info.split(";")
            if partes[0] == time.nome:
                # Verifica se a pessoa já está associada ao time
                if pessoa.cpf in self.times_pessoas[id_time]:
                    return "Erro: Pessoa já associada ao time."

                # Adiciona a pessoa ao time
                if id_time not in self.times_pessoas:
                    self.times_pessoas[id_time] = []
                self.times_pessoas[id_time].append(pessoa.cpf)
                return "Pessoa adicionada ao time com sucesso."
        return "Time não encontrado."

    def remover_pessoa_do_time(self, time: Time, pessoa: Pessoa) -> str:
        # Verifica se o time existe
        for id_time, info in self.times.items():
            partes = info.split(";")
            if partes[0] == time.nome:
                # Verifica se a pessoa está associada ao time
                if pessoa.cpf not in self.times_pessoas[id_time]:
                    return "Erro: Pessoa não está associada ao time."

                # Remove a pessoa do time
                self.times_pessoas[id_time].remove(pessoa.cpf)
                return "Pessoa removida do time com sucesso."
        return "Time não encontrado."