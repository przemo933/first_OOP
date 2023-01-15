class Audi:
    def __init__(self):
        self.kolor = 'czerwony'
        self.ilosc_paliwa = 10
        self.kondycja = 4
    def __str__(self):
        napis = (f'Audi ma kolor {self.kolor} i jest w kondycji {self.kondycja}')
        return napis


moje_auto = Audi()
print(moje_auto.ilosc_paliwa)
print(moje_auto.kondycja)
moje_auto.kondycja += 1
print(moje_auto.kondycja)

auto_sasiada = Audi()
print(auto_sasiada.kondycja)
print(auto_sasiada)