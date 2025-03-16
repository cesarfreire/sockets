# Cliente Socket
import socket

class Cliente:
    def __init__(self, host='127.0.0.1', porta=3333):
        self.host: str = host
        self.porta: int = porta


    def enviar_mensagem(self, mensagem) -> None:
        with socket.create_connection((self.host, self.porta)) as cliente:
            cliente.send(mensagem.encode())
            resposta = cliente.recv(1024).decode()
            print(f"Resposta do servidor: {resposta}")
