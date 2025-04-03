from src.comando.comando_abstrato import Comando


class ComandoMeAjuda(Comando):
    def executar(self) -> str:
        texto: str = ""
        texto += "Para utilizar o CLI, utilize um dos parâmetros abaixo:\n\n"
        texto += "Operações com Pessoa:\n"
        texto += "INSERT;cpf;nome;endereco  --> Adiciona uma pessoa\n"
        texto += "GET;cpf                   --> Busca uma pessoa\n"
        texto += "UPDATE;cpf;nome;endereco  --> Atualiza uma pessoa\n"
        texto += "DELETE;cpf                --> Apaga uma pessoa\n\n"
        texto += "Operações com Time:\n"
        texto += "INSERT_TIME;nome;categoria;pais_origem;qtd_titulos;cpf1;cpf2  --> Adiciona um time (CPF's opcionais)\n"
        texto += "GET_TIME;nome                                                 --> Busca um time\n"
        texto += "UPDATE_TIME;nome;categoria;pais_origem;qtd_titulos            --> Atualiza um time\n"
        texto += "DELETE_TIME;nome                                              --> Apaga um time\n"
        texto += "ADD_PESSOA;nome_time;cpf_pessoa                               --> Adiciona pessoa ao time\n"
        texto += "REMOVE_PESSOA;nome_time;cpf_pessoa                            --> Remove pessoa do time\n\n"
        texto += 'Utilize o delimitador ";" para informar os dados.\n'
        texto += "-" * 50
        return texto

    def desfazer(self) -> str:
        return ""

    def refazer(self) -> str:
        return self.executar()
