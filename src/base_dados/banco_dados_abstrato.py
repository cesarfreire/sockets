from abc import ABC, abstractmethod

from src.modelo.pessoa import Pessoa


class BancoDeDados(ABC):
    @abstractmethod
    def criar(self, pessoa: Pessoa) -> str:
        pass

    @abstractmethod
    def ler(self, cpf: str) -> str:
        pass

    @abstractmethod
    def atualizar(self, pessoa: Pessoa) -> str:
        pass

    @abstractmethod
    def deletar(self, cpf: str) -> str:
        pass

    @abstractmethod
    def listar(self) -> str:
        pass