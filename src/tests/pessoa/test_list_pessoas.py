from src.base_dados.banco_dados import BancoDeDadosLocal
from src.base_dados.banco_dados_abstrato import BancoDeDados
from src.comando.comando_abstrato import Comando
from src.comando.pessoa.comando_criar_pessoa import ComandoCriarPessoa
from src.comando.pessoa.comando_listar_pessoas import ComandoListarPessoas
from src.modelo.pessoa import Pessoa


def test_list_pessoas_deve_retornar_sucesso():
    banco: BancoDeDados = BancoDeDadosLocal(iniciar_zerado=True)

    cmd = "INSERT;10481485996;CESAR;WENCESLAU BORINI"
    operacao, *dados = cmd.split(";")
    assert len(dados) == 3
    pessoa = Pessoa(cpf=dados[0], nome=dados[1], endereco=dados[2])
    assert isinstance(pessoa, Pessoa)
    comando_insert = ComandoCriarPessoa(banco, pessoa=pessoa)
    assert isinstance(comando_insert, Comando)
    response = comando_insert.executar()
    assert response == "Criado com sucesso."

    comando = ComandoListarPessoas(banco)
    assert isinstance(comando, Comando)
    response = comando.executar()
    assert (
        response
        == "1\n10481485996;CESAR;WENCESLAU BORINI\n--------------------------------------------------"
    )


def test_list_pessoas_sem_dados_deve_retornar_zero():
    banco: BancoDeDados = BancoDeDadosLocal(iniciar_zerado=True)

    comando = ComandoListarPessoas(banco)
    assert isinstance(comando, Comando)
    response = comando.executar()
    assert response == "0"
