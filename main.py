import random


class Lista:
    def __init__(self, rozmiar):
        self.rozmiar = rozmiar
        self.lista = [None] * rozmiar

    def dodaj(self, wartosc):
        for i in range(self.rozmiar):
            if self.lista[i] is None:
                self.lista[i] = wartosc
                return 0

    def usun(self, indeks):
        if indeks < 0 or indeks >= self.rozmiar or self.lista[indeks] is None:
            return 0
        for i in range(indeks, self.rozmiar - 1):
            self.lista[i] = self.lista[i + 1]
        self.lista[self.rozmiar - 1] = None

    def pobierz(self, indeks):
        if indeks < 0 or indeks >= self.rozmiar or self.lista[indeks] is None:
            return None
        return self.lista[indeks]

    def display(self):
        elementy = [i for i in self.lista if i is not None]
        print("Lista:", elementy)


def main():
    lista_nowa = Lista(3)
    lista_nowa.dodaj(10)
    lista_nowa.dodaj(20)
    lista_nowa.dodaj(30)
    lista_nowa.usun(1)
    lista_nowa.display()

if __name__ == "__main__":
    main()
