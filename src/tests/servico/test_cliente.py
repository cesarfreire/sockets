def test_cliente_com_host_invalido_deve_retornar_erro():
    from src.servico.cliente import Cliente
    # Configurações do cliente
    host = "256.256.256.256"  # IP inválido
    porta = 3334

    try:
        Cliente(host=host, porta=porta)
    except Exception as e:
        assert isinstance(e, ValueError)
        assert str(e) == "IP inválido. Exemplos de IPs válidos: 127.0.0.1, 15.15.15.15"


def test_cliente_com_porta_invalida_deve_retornar_erro():
    from src.servico.cliente import Cliente
    # Configurações do cliente
    host = "127.0.0.1"
    porta = 66666666666

    try:
        Cliente(host=host, porta=porta)
    except Exception as e:
        assert isinstance(e, ValueError)
        assert str(e) == "Porta deve estar entre 1 e 65535."

def test_cliente_com_dados_corretos_deve_dar_certo():
    from src.servico.cliente import Cliente
    # Configurações do cliente
    host = "127.0.0.1"
    porta = 3334

    cliente = Cliente(host=host, porta=porta)
    assert cliente.host == host
    assert cliente.porta == porta
    assert isinstance(cliente, Cliente)