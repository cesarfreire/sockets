from src.servico.cliente import Cliente
from src.servico.servidor import Servidor
from src.utils import utils

if __name__ == "__main__":
    opcao = (
        input("Digite 'servidor' para iniciar o servidor ou 'cliente' para conectar: ")
        .strip()
        .lower()
    )
    try:
        if opcao == "servidor":
            host = input("Digite o ip do servidor [default = 127.0.0.1]: ") or "127.0.0.1"
            if not utils.is_valid_host(host=host):
                raise ValueError(
                    "IP inválido. Exemplos de IPs válidos: 127.0.0.1, 15.15.15.15"
                )

            porta = input("Digite a porta do servidor [default = 3334]: ") or "3334"
            if not utils.is_valid_port(port=int(porta)):
                raise ValueError("Porta deve estar entre 1 e 65535.")
            porta = int(porta)
            servidor = Servidor(
                host=host, porta=porta
            )
            servidor.iniciar()
        elif opcao == "cliente":
            host = input(
                "Digite o ip do servidor onde deseja se conectar [default = 127.0.0.1]: "
            ) or "127.0.0.1"
            if not utils.is_valid_host(host=host):
                raise ValueError(
                    "IP inválido. Exemplos de IPs válidos: 127.0.0.1, 15.15.15.15"
                )

            porta = input(
                "Digite a porta do servidor onde deseja se conectar [default = 3334]: "
            ) or "3334"
            if not utils.is_valid_port(port=int(porta)):
                raise ValueError("Porta deve estar entre 1 e 65535.")

            cliente = Cliente(
                host=host if host else "127.0.0.1", porta=porta if porta else 3334
            )
            while True:
                msg = input(
                    "Digite uma operação (digite HELP para ajuda) ou 'sair' para encerrar: "
                )
                if msg.lower() == "sair":
                    break
                cliente.enviar_mensagem(msg)
    except OSError as e:
        print(f"Ocorreu um erro: {e}")
    except ValueError as e:
        print(f"O valor informado é inválido: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
