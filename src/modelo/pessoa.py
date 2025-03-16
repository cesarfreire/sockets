from src.modelo.entidade import Entidade


class Pessoa(Entidade):
    def __init__(self, cpf: str, nome: str, endereco: str, **kwargs) -> None:
        self.cpf: str = cpf
        self.nome: str = nome
        self.endereco: str = endereco

    def __str__(self) -> str:
        return f'{self.nome};{self.endereco}'
