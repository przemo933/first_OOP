class Audi:
    #parametry inicjalizujace obiekt
    def __init__(self, barwa, info_wprowadzone):
        self.tryb = None
        self.kolor = barwa
        self.ilosc_paliwa = 10
        self.kondycja = info_wprowadzone
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.max_predkosc = 220
    #napis ktory sie wydrukuje prz y obiekcie
    def __str__(self):
        napis = f'Audi ma kolor {self.kolor} i jest w kondycji {self.kondycja}'
        return napis
    #metody
    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100
        return round(zasieg)

    def ustaw_tryb(self, tryb):
        self.tryb = tryb
        if self.tryb == 'eco':
            self.spalanie_na_100 = 10
            self.tryb_ekonomiczny = True
        if self.tryb == 'normal':
            self.spalanie_na_100 = 14
            self.tryb_ekonomiczny = False

    def ustaw_eco(self):
        self.spalanie_na_100 = 10
        self.tryb_ekonomiczny = True
        self.max_predkosc = 160
        print('Tryb eco włączony')

    def ustaw_normal(self):
        self.spalanie_na_100 = 14
        self.tryb_ekonomiczny = False
        self.max_predkosc = 220
        print('Tryb normal włączony')

    def tankowanie(self, ilosc_litrow):
        if ilosc_litrow < 5:
            print('Za mała ilosc paliwa, musisz zatankować min. 5l')
        elif  (ilosc_litrow + self.ilosc_paliwa) < 70:
            self.ilosc_paliwa += ilosc_litrow
            print(f'Zatankowano {ilosc_litrow}l paliwa, aktualny poziom {self.ilosc_paliwa}l')
        else:
            print(f'Zbiornik ma pojemnosc 70l, możesz aktualnie zatankować maksymalnie {70 - self.ilosc_paliwa}l')


moje_auto = Audi('czerwony', 4)
print(moje_auto.ilosc_paliwa)
print(moje_auto.kondycja)
moje_auto.kondycja += 1
print(moje_auto.kondycja)

auto_sasiada = Audi('zielony', 5)
print(auto_sasiada.kondycja)
print(auto_sasiada)

print(moje_auto.zasieg())
moje_auto.ustaw_tryb('eco')
print(moje_auto.zasieg())
moje_auto.ustaw_tryb('normal')
print(moje_auto.zasieg())
moje_auto.tankowanie(60)
