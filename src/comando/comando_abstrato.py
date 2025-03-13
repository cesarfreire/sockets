from abc import ABC, abstractmethod


# Padrão Command
class Comando(ABC):
    @abstractmethod
    def executar(self) -> str:
        pass

    @abstractmethod
    def desfazer(self) -> str:
        pass

    @abstractmethod
    def refazer(self) -> str:
        pass
