from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando


class ComandoMeAjuda(Comando):
    def executar(self) -> str:
        texto: str = ""
        texto += "Para utilizar o CLI, utilize um dos parâmetros abaixo:\n\n"
        texto += "Operações com Pessoa:\n"
        texto += "INSERT;cpf;nome;endereco\n"
        texto += "GET;cpf\n"
        texto += "UPDATE;cpf;nome;endereco\n"
        texto += "DELETE;cpf\n\n"
        texto += "Operações com Time:\n"
        texto += "INSERT_TIME;nome;categoria;pais_origem;qtd_titulos;cpf1;cpf2\n"
        texto += "GET_TIME;nome\n"
        texto += "UPDATE_TIME;nome;categoria;pais_origem;qtd_titulos\n"
        texto += "DELETE_TIME;nome\n\n"
        texto += "Utilize o delimitador \";\" para informar os dados.\n"
        texto += "-"*50
        return texto

    # nome = dados[0]
    #                 categoria = dados[1]
    #                 pais_origem = dados[2]
    #                 qtd_titulos = dados[3]
    #                 cpfs = dados[4:]

    def desfazer(self) -> str:
        return ""

    def refazer(self) -> str:
        return self.executar()
