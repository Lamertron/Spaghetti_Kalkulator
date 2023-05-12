# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Kalkulator:
    liczba1 = 0
    liczba2 = 0
    dzialania = []

    def __init__(self, list):
        komunikat = "Uruchomiono kalkulator"
        self.dzialania = list
        print(komunikat)

    def odejmowanie(self):
        self.odejmowanio = self.liczba1-self.liczba2
        print(self.odejmowanio)
    def dodawanie(self):
        self.dodawanio = self.liczba1 + self.liczba2
        print(self.dodawanio)
    def mnozenie(self):
        self.mnozenio = self.liczba1 * self.liczba2
        print(self.mnozenio)
    def dzielenie(self):
        self.dzielenio = self.liczba1 / self.liczba2
        print(self.dzielenio)
    def liczby(self):
        print('dej numerki')
        self.liczba1 = float(input("Podaj pierwsza liczbe:\n"))

        print(f'wpisales {self.liczba1}')

        self.liczba2 = float(input("Podaj druga liczbe:\n"))

        print(f'wpisales {self.liczba2}')
        print('dozwolone dzialania')
        print(self.dzialania)
        self.dzialanio = input('masz wynik kurwiu')

    def dzialanie(self):
        if("-" == self.dzialanio) : self.odejmowanie()
        if("+" == self.dzialanio) : self.dodawanie()
        if("*" == self.dzialanio) : self.mnozenie()
        if("/" == self.dzialanio) : self.dzielenie()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dzialania = ['-', '*', '/', "+"]
    Kalkulator = Kalkulator(dzialania)
    print(Kalkulator.dzialania)
    Kalkulator.liczby()
    Kalkulator.dzialanie()