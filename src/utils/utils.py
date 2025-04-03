def is_valid_host(host: str):
    """
    Verifica se o host é válido.
    :param host: Host a ser verificado.
    :return: True se o host for válido, False caso contrário.
    """
    if not host:
        return False
    if not isinstance(host, str):
        return False
    if len(host.split('.')) != 4:
        return False
    for parte in host.split("."):
        if not 0 <= int(parte) <= 255:
            return False
    return True


def is_valid_port(port: int):
    """
    Verifica se a porta é válida.
    :param port: Porta a ser verificada.
    :return: True se a porta for válida, False caso contrário.
    """
    if not isinstance(port, int):
        return False
    if not (1 <= port <= 65535):
        return False
    return True
