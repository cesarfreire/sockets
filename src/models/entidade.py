from abc import ABC, abstractmethod

class Entidade(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def __str__(self):
        pass
