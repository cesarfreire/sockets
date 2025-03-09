# Classe para armazenar comandos
from src.comandos.comando_abstrato import Comando


class PilhaComandos:
    def __init__(self) -> None:
        self.pilha_desfazer = []
        self.pilha_refazer = []

    def adicionar_comando(self, comando: Comando) -> None:
        self.pilha_desfazer.append(comando)
        self.pilha_refazer.clear()

    def desfazer(self) -> str:
        if self.pilha_desfazer:
            comando = self.pilha_desfazer.pop()
            self.pilha_refazer.append(comando)
            return comando.desfazer()
        return "Nada para desfazer."

    def refazer(self) -> str:
        if self.pilha_refazer:
            comando = self.pilha_refazer.pop()
            self.pilha_desfazer.append(comando)
            return comando.executar()
        return "Nada para refazer."