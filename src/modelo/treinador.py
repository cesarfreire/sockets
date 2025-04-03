from src.modelo.pessoa import Pessoa


class Jogador(Pessoa):
    def __init__(
        self,
        cpf: str,
        nome: str,
        endereco: str,
        estilo_jogo: str,
        anos_experiencia: int,
        **kwargs,
    ):
        super().__init__(cpf, nome, endereco)
        self.estilo_jogo: str = estilo_jogo
        self.anos_experiencia: int = anos_experiencia

    def __str__(self) -> str:
        return f"{super().__str__()};{self.estilo_jogo};{self.anos_experiencia}"
