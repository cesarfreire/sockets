from src.models.entidade import Entidade


class Pessoa(Entidade):
    def __init__(self, cpf: str, nome: str, endereco: str, **kwargs):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

    def __str__(self) -> str:
        return f'{self.nome};{self.endereco}'
