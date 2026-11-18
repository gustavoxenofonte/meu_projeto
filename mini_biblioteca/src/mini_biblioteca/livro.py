class Livro:
    def __init__(self, titulo: str, autor: str, codigo: str, disponivel = True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = disponivel

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nCódigo: {self.codigo}\nDisponível: {self.disponivel}"