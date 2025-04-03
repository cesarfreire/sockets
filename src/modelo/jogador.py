from src.modelo.pessoa import Pessoa


class Jogador(Pessoa):
    def __init__(
        self,
        cpf: str,
        nome: str,
        endereco: str,
        posicao: str,
        numero_camisa: int,
        **kwargs,
    ):
        super().__init__(cpf, nome, endereco)
        self.posicao: str = posicao
        self.numero_camisa: int = numero_camisa

    def __str__(self) -> str:
        return f"{super().__str__()};{self.posicao};{self.numero_camisa}"
