from Libro import Libro


class Biblioteca:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)

    def mostra_libri(self):
        for libro in self.libri:
            print(libro.mostra_info())

    def salva_file(self, nome_file):
        file_txt = open(nome_file, "w")
        file_txt.write("Titolo, Autore , Numero pagine\n")
        for libro in self.libri:
            file_txt.write(f'{libro.titolo}, {libro.autore}, {libro.n_pagine}\n')
        file_txt.close()
        print(f"Inventario salvato in {nome_file}")


biblioteca = Biblioteca()

libro1 = Libro("Boh", "Daje", 300)
libro2 = Libro("Li", "Sium", 200)
libro3 = Libro("Ah", "Qualcuno", 301)

biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
biblioteca.aggiungi_libro(libro3)
biblioteca.mostra_libri()
print("Il numero dei libri è:", str(Libro.mostra_conteggio_libri()))

libro1.lungo()
libro2.lungo()
libro3.lungo()

biblioteca.salva_file('inventario_biblioteca.txt')

