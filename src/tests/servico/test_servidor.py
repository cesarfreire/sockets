def test_servidor_com_host_errado_deve_retornar_erro():
    from src.servico.servidor import Servidor
    # Configurações do servidor
    host = "256.256.256.256"  # IP inválido
    porta = 3334

    try:
        Servidor(host=host, porta=porta)
    except Exception as e:
        assert isinstance(e, ValueError)
        assert str(e) == "IP inválido. Exemplos de IPs válidos: 127.0.0.1, 15.15.15.15"

def test_servidor_com_porta_errada_deve_retornar_erro():
    from src.servico.servidor import Servidor
    # Configurações do servidor
    host = "127.0.0.1"
    porta = 6666666 # porta inválida

    try:
        Servidor(host=host, porta=porta)
    except Exception as e:
        assert isinstance(e, ValueError)
        assert str(e) == "Porta deve estar entre 1 e 65535."

def test_servidor_com_dados_corretos_deve_dar_certo():
    from src.servico.servidor import Servidor
    # Configurações do servidor
    host = "127.0.0.1"
    porta = 3334

    servidor = Servidor(host=host, porta=porta)

    assert servidor.host == host
    assert servidor.porta == porta
    assert isinstance(servidor, Servidor)
