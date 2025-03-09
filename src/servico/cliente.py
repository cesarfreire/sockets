# Cliente Socket
import socket


class Cliente:
    def __init__(self, host='127.0.0.1', porta=3333):
        self.host = host
        self.porta = porta
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __connect__(self):
        self.cliente.connect((self.host, self.porta))

    def __disconnect__(self):
        self.cliente.close()

    def enviar_mensagem(self, mensagem):
        self.__connect__()
        self.cliente.send(mensagem.encode())
        resposta = self.cliente.recv(1024).decode()
        print(f"Resposta do servidor: {resposta}")
        self.__disconnect__()

    def fechar_conexao(self):
        self.cliente.send("sair".encode())
        self.cliente.close()