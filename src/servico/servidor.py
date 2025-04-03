import socket
import threading

from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.base_dados.pilha_comandos import PilhaComandos
from src.comando.comando_me_ajuda import ComandoMeAjuda
from src.comando.pessoa.comando_apagar_pessoa import ComandoApagarPessoa
from src.comando.pessoa.comando_atualizar_pessoa import ComandoAtualizarPessoa
from src.comando.pessoa.comando_criar_pessoa import ComandoCriarPessoa
from src.comando.pessoa.comando_ler_pessoa import ComandoLerPessoa
from src.comando.pessoa.comando_listar_pessoas import ComandoListarPessoas
from src.comando.time.comando_adicionar_pessoa_ao_time import (
    ComandoAdicionarPessoaAoTime,
)
from src.comando.time.comando_apagar_time import ComandoApagarTime
from src.comando.time.comando_atualizar_time import ComandoAtualizarTime
from src.comando.time.comando_criar_time import ComandoCriarTime
from src.comando.time.comando_ler_time import ComandoLerTime
from src.comando.time.comando_listar_times import ComandoListarTimes
from src.comando.time.comando_remover_pessoa_do_time import ComandoRemoverPessoaDoTime
from src.modelo.pessoa import Pessoa
from src.modelo.time import Time
from src.utils import utils


# Servidor Socket
class Servidor:
    def __init__(self, host="127.0.0.1", porta=3334) -> None:
        self.host: str = host
        self.porta: int = porta
        self.__validate()
        self.servidor: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.bind((self.host, self.porta))
        self.servidor.listen(5)
        self.banco: BancoDeDados = BancoDeDadosLocal(iniciar_zerado=False)
        self.pilha_comandos: PilhaComandos = PilhaComandos()
        print(f"Servidor escutando em {self.host}:{self.porta}")

    def __validate(self):
        if not utils.is_valid_host(host=self.host):
            raise ValueError(
                "IP inválido. Exemplos de IPs válidos: 127.0.0.1, 15.15.15.15"
            )

        if not utils.is_valid_port(port=int(self.porta)):
            raise ValueError("Porta deve estar entre 1 e 65535.")

    def handle_cliente(self, conexao, endereco) -> None:
        print(f"Nova conexão de {endereco}")
        while True:
            mensagem = conexao.recv(1024).decode()
            if not mensagem or mensagem.lower() == "sair":
                print(f"Conexão encerrada com {endereco}")
                break

            operacao, *dados = mensagem.split(";")
            comando = None

            # Comandos para Pessoa
            if operacao == "INSERT" and len(dados) == 3:
                pessoa = Pessoa(dados[0], dados[1], dados[2])
                comando = ComandoCriarPessoa(self.banco, pessoa)
            elif operacao == "GET" and len(dados) == 1:
                comando = ComandoLerPessoa(self.banco, dados[0])
            elif operacao == "UPDATE" and len(dados) == 3:
                pessoa = Pessoa(dados[0], dados[1], dados[2])
                comando = ComandoAtualizarPessoa(self.banco, pessoa)
            elif operacao == "DELETE" and len(dados) == 1:
                comando = ComandoApagarPessoa(self.banco, dados[0])
            elif operacao == "LIST":
                comando = ComandoListarPessoas(self.banco)

            # Comandos para Time
            elif operacao == "INSERT_TIME" and len(dados) >= 4:
                nome = dados[0]
                categoria = dados[1]
                pais_origem = dados[2]
                qtd_titulos = dados[3]
                cpfs = dados[4:]
                time = Time(nome, categoria, pais_origem, qtd_titulos)
                comando = ComandoCriarTime(self.banco, time, cpfs)
            elif operacao == "GET_TIME" and len(dados) == 1:
                comando = ComandoLerTime(self.banco, dados[0])
            elif operacao == "UPDATE_TIME" and len(dados) == 4:
                nome = dados[0]
                categoria = dados[1]
                pais_origem = dados[2]
                quantidade_titulos = dados[3]
                time = Time(
                    nome=nome,
                    categoria=categoria,
                    pais_origem=pais_origem,
                    quantidade_titulos=quantidade_titulos,
                )
                comando = ComandoAtualizarTime(self.banco, time=time)
            elif operacao == "DELETE_TIME" and len(dados) == 1:
                comando = ComandoApagarTime(self.banco, dados[0])
            elif operacao == "LIST_TIMES":
                comando = ComandoListarTimes(self.banco)
            elif operacao == "ADD_PESSOA" and len(dados) == 2:
                comando = ComandoAdicionarPessoaAoTime(
                    self.banco, nome_time=dados[0], cpf=dados[1]
                )
            elif operacao == "REMOVE_PESSOA" and len(dados) == 2:
                comando = ComandoRemoverPessoaDoTime(
                    self.banco, nome_time=dados[0], cpf=dados[1]
                )

            # Comandos de controle
            elif operacao == "UNDO":
                resposta = self.pilha_comandos.desfazer()
                conexao.send(resposta.encode())
                continue
            elif operacao == "REDO":
                resposta = self.pilha_comandos.refazer()
                conexao.send(resposta.encode())
                continue
            elif operacao == "HELP":
                comando = ComandoMeAjuda()

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
            thread = threading.Thread(
                target=self.handle_cliente, args=(conexao, endereco)
            )
            thread.start()
