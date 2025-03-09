from src.servico.cliente import Cliente
from src.servico.servidor import Servidor

if __name__ == "__main__":
    opcao = input("Digite 'servidor' para iniciar o servidor ou 'cliente' para conectar: ").strip().lower()
    if opcao == 'servidor':
        servidor = Servidor()
        servidor.iniciar()
    elif opcao == 'cliente':
        cliente = Cliente()
        while True:
            msg = input("Digite uma operação (INSERT;cpf;nome;endereco, GET;cpf, UPDATE;cpf;nome;endereco, DELETE;cpf, UNDO, REDO) ou 'sair' para encerrar: ")
            if msg.lower() == 'sair':
                cliente.fechar_conexao()
                break
            cliente.enviar_mensagem(msg)