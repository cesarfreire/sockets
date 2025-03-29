from src.servico.cliente import Cliente
from src.servico.servidor import Servidor

if __name__ == "__main__":
    opcao = input("Digite 'servidor' para iniciar o servidor ou 'cliente' para conectar: ").strip().lower()
    try:
        if opcao == 'servidor':
            servidor = Servidor()
            servidor.iniciar()
        elif opcao == 'cliente':
            cliente = Cliente()
            while True:
                msg = input("Digite uma operação (digite HELP para ajuda) ou 'sair' para encerrar: ")
                if msg.lower() == 'sair':
                    break
                cliente.enviar_mensagem(msg)
    except OSError as e:
        print(f"Ocorreu um erro: {e}")
