from abc import ABC, abstractmethod

from src.models.pessoa import Pessoa


class BancoDeDados(ABC):
    @abstractmethod
    def criar(self, pessoa: Pessoa):
        pass

    @abstractmethod
    def ler(self, cpf: str) -> str:
        pass

    @abstractmethod
    def atualizar(self, pessoa: Pessoa):
        pass

    @abstractmethod
    def deletar(self, cpf: str):
        pass

    @abstractmethod
    def listar(self) -> str:
        pass