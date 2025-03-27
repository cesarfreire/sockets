from abc import ABC, abstractmethod

from src.modelo.pessoa import Pessoa
from src.modelo.time import Time


class BancoDeDados(ABC):
    # Métodos para Pessoa
    @abstractmethod
    def criar_pessoa(self, pessoa: Pessoa) -> str:
        pass

    @abstractmethod
    def ler_pessoa(self, cpf: str) -> str:
        pass

    @abstractmethod
    def ler_pessoa_objeto(self, cpf: str) -> Pessoa | None:
        pass

    @abstractmethod
    def atualizar_pessoa(self, pessoa: Pessoa) -> str:
        pass

    @abstractmethod
    def deletar_pessoa(self, cpf: str) -> str:
        pass

    @abstractmethod
    def listar_pessoas(self) -> str:
        pass

    # Métodos para Time
    @abstractmethod
    def criar_time(self, time: Time) -> str:
        pass

    @abstractmethod
    def ler_time(self, nome: str) -> str:
        pass

    @abstractmethod
    def atualizar_time(self, time: Time) -> str:
        pass

    @abstractmethod
    def deletar_time(self, nome: str) -> str:
        pass

    @abstractmethod
    def listar_times(self) -> str:
        pass