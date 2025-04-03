# Cliente Socket
import socket

from src.utils import utils


class Cliente:
    def __init__(self, host="127.0.0.1", porta=3334):
        self.host: str = host
        self.porta: int = porta
        self.__validate()

    def __validate(self):
        if not utils.is_valid_host(host=self.host):
            raise ValueError(
                "IP inválido. Exemplos de IPs válidos: 127.0.0.1, 15.15.15.15"
            )

        if not utils.is_valid_port(port=int(self.porta)):
            raise ValueError("Porta deve estar entre 1 e 65535.")

    def enviar_mensagem(self, mensagem: str) -> None:
        with socket.create_connection((self.host, self.porta)) as cliente:
            cliente.send(mensagem.encode())
            resposta = cliente.recv(1024).decode()
            print(f"Resposta do servidor: {resposta}")
