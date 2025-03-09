# Banco de Dados Simulado
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.models.pessoa import Pessoa


class BancoDeDadosLocal(BancoDeDados):
    def __init__(self):
        self.dados = {
            "12345678900": "Fulano;Rua A",
            "98765432100": "Ciclano;Rua B",
            "10481485996": "Cesar;Wenceslau Borini"
        }

    def criar(self, pessoa: Pessoa) -> str:
        if pessoa.cpf in self.dados:
            return "Erro: CPF já cadastrado."
        self.dados[pessoa.cpf] = f"{pessoa.__str__()}"
        return "Criado com sucesso."

    def ler(self, cpf: str) -> str:
        dados = self.dados.get(cpf)
        if not dados:
            return "Pessoa não encontrada."
        return f"{cpf};{dados.__str__()}"

    def atualizar(self, pessoa: Pessoa) -> str:
        if pessoa.cpf not in self.dados:
            return "Pessoa não encontrada."
        self.dados[pessoa.cpf] = f"{pessoa.__str__()}"
        return "Pessoa atualizada com sucesso."

    def deletar(self, cpf: str) -> str:
        if len(self.dados) == 0:
            return "Sem pessoas cadastradas."
        if cpf not in self.dados:
            return "Pessoa não encontrada."
        del self.dados[cpf]
        return "Pessoa removida com sucesso."

    def listar(self) -> str:
        total = len(self.dados)
        if total == 0:
            return str(total)

        linhas = []
        for cpf, info in self.dados.items():
            linha = f"{cpf};{info}"
            linhas.append(linha)

        return f"{total}\n" + "\n".join(linhas)