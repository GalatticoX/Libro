class Libro:
    conteggio_libri = 0

    def __init__(self, titolo, autore, n_pagine):
        self.titolo = titolo
        self.autore = autore
        self.n_pagine = n_pagine
        Libro.conteggio_libri += 1

    @classmethod
    def mostra_conteggio_libri(cls):
        return Libro.conteggio_libri

    def lungo(self):
        if self.n_pagine > 300:
            print("Il libro ha più di 300 pagine.")
        elif self.n_pagine == 300:
            print("Il libro ha 300 pagine.")
        else:
            print("Il libro ha meno di 300 pagine.")

    def mostra_info(self):
        return f"Libro: {self.titolo} \nAutore: {self.autore} \nNumero pagine: {self.n_pagine}\n"