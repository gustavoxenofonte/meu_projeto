from .usuario import Usuario
from .livro import Livro
from .emprestimo import Emprestimo

def main():
    gustavo = Usuario("Gustavo", "123")
    harry_potter = Livro("Harry Potter", "JK Rowling", "001")

    print("-"*30)
    print("Livro antes do empréstimo")
    print(harry_potter)

    emprestimo = Emprestimo(harry_potter, gustavo)

    print("-"*30)
    print("Estado antes de devolver")
    print(harry_potter)

    emprestimo.devolver()
    print("-"*30)
    print("Estado depois de devolver")
    print(harry_potter)

main()