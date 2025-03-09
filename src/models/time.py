from src.models.entidade import Entidade
from src.models.pessoa import Pessoa


class Time(Entidade):
    def __init__(self, nome: str, categoria: str, pais_origem: str, quantidade_titulos: int, **kwargs):
        self.nome: str = nome
        self.categoria: str = categoria
        self.pais_origem: str = pais_origem
        self.quantidade_titulos: int = quantidade_titulos
        self.jogadores: list[Pessoa] = []

    def __str__(self) -> str:
        return f'{self.nome};{self.categoria};{self.pais_origem};{self.quantidade_titulos}'