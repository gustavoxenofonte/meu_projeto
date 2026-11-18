from .usuario import Usuario
from .livro import Livro

class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario, ativo = True):
        self.livro = livro
        self.usuario = usuario
        self.ativo = ativo

    @property
    def livro(self):
        return self._livro

    @livro.setter
    def livro(self, livro: Livro):
        if livro.disponivel is False:
            raise ValueError
        else:
            self._livro = livro
            livro.disponivel = False

    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True