import socket
import threading

from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.base_dados.pilha_comandos import PilhaComandos
from src.comando.comando_apagar import ComandoApagar
from src.comando.comando_atualizar import ComandoAtualizar
from src.comando.comando_criar import ComandoCriar
from src.comando.comando_ler import ComandoLer
from src.comando.comando_listar import ComandoListar
from src.modelo.pessoa import Pessoa


# Servidor Socket
class Servidor:
    def __init__(self, host='127.0.0.1', porta=3333) -> None:
        self.host: str = host
        self.porta: int = porta
        self.servidor: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.bind((self.host, self.porta))
        self.servidor.listen(5)
        self.banco: BancoDeDados = BancoDeDadosLocal()
        self.pilha_comandos: PilhaComandos = PilhaComandos()
        print(f"Servidor escutando em {self.host}:{self.porta}")

    def handle_cliente(self, conexao, endereco) -> None:
        print(f"Nova conexão de {endereco}")
        while True:
            mensagem = conexao.recv(1024).decode()
            if not mensagem or mensagem.lower() == 'sair':
                print(f"Conexão encerrada com {endereco}")
                break

            operacao, *dados = mensagem.split(";")
            comando = None

            if operacao == 'INSERT' and len(dados) == 3:
                pessoa = Pessoa(dados[0], dados[1], dados[2])
                comando = ComandoCriar(self.banco, pessoa)
            elif operacao == 'GET' and len(dados) == 1:
                comando = ComandoLer(self.banco, dados[0])
            elif operacao == 'UPDATE' and len(dados) == 3:
                pessoa = Pessoa(dados[0], dados[1], dados[2])
                comando = ComandoAtualizar(self.banco, pessoa)
            elif operacao == 'DELETE' and len(dados) == 1:
                comando = ComandoApagar(self.banco, dados[0])
            if operacao == 'LIST':
                comando = ComandoListar(self.banco)
            elif operacao == 'UNDO':
                resposta = self.pilha_comandos.desfazer()
                conexao.send(resposta.encode())
                continue
            elif operacao == 'REDO':
                resposta = self.pilha_comandos.refazer()
                conexao.send(resposta.encode())
                continue

            if comando:
                resposta = comando.executar()
                self.pilha_comandos.adicionar_comando(comando)
            else:
                resposta = "Comando inválido."
            conexao.send(resposta.encode())
        conexao.close()

    def iniciar(self) -> None:
        while True:
            conexao, endereco = self.servidor.accept()
            thread = threading.Thread(target=self.handle_cliente, args=(conexao, endereco))
            thread.start()
