# Logogram - Mastermind
from random import choices
from colorama import Fore, init


class Grzybki:
    def __init__(self, color):
        self.color = color
        
        
class Tura:
    def __init__(self, paleta_kolorow, odpowiedzi):
        # Punktacja (czarne - na swoim miejscu, białe - nie na swoim miejscu)
        self.czarne = 0
        self.biale = 0
        self.poz_do_oceny = [0, 1, 2, 3]
        print(f'\n--->   Tura: {i}   <---')
        while True:
            self.odpowiedz = input('Podaj cztery litery odpowiadające kolorom grzybków (kolory mogą się powtarzać): ').upper()
            # Sprawdzenie czy input zawiera 4 litery z palety kolorów
            if len(self.odpowiedz) == 4 and self.odpowiedz[0] in paleta_kolorow and self.odpowiedz[1] in paleta_kolorow and self.odpowiedz[2] in paleta_kolorow and self.odpowiedz[3] in paleta_kolorow:
                break
        odpowiedzi.append(self.odpowiedz)

        # Tupla obiektów odpowiedzi
        self.odp = tuple([Grzybki(self.odpowiedz[x]) for x in range(4)])
        
    def sprawdz_czarne(self, rozwiazanie, dziennik):
        for self.poz_grzyba in range(4):
            if self.odp[self.poz_grzyba].color == rozwiazanie[self.poz_grzyba].color:
                self.czarne += 1
                rozwiazanie[self.poz_grzyba].color = 'disable'
                dziennik.append(f'rozwiazanie[{self.poz_grzyba}] w czarnych zmiana na disable')
                self.poz_do_oceny.remove(self.poz_grzyba)
                
    def sprawdz_biale(self, rozwiazanie, dziennik, punktacja):
        # Pętla po grzybkach odpowiedzi
        for self.poz_grzyba in self.poz_do_oceny:
            # Pętla po grzybach rozwiązania
            for self.poz_pozycja in self.poz_do_oceny:
                if self.odp[self.poz_grzyba].color == rozwiazanie[self.poz_pozycja].color:
                    self.biale += 1
                    # Uniemożliwienie ponownego sparowania z innym grzybkiem odpowiedzi poprzez zmiane koloru grzybka rozwiązania w obecnej turze
                    rozwiazanie[self.poz_pozycja].color = 'disable'
                    dziennik.append(f'rozwiazanie[{self.poz_pozycja}] w białych zmiana na disable')
                    break
        punktacja.append([self.czarne, self.biale])


# Automatyczne przywracanie koloru czcionki
init(autoreset=True)

paleta_kolorow = ('W', 'V', 'G', 'R', 'B', 'Y')
print(f'Grzybki są w sześciu kolorach:\n{Fore.WHITE}White - (W) {Fore.MAGENTA}Violet - (V)  {Fore.GREEN}Green - (G)  {Fore.RED}Red - (R)  {Fore.BLUE}Blue - (B)  {Fore.YELLOW}Yellow - (Y) ')

# Wylosowanie kolorów grzybków
rozwiazanie_lista = choices(paleta_kolorow, k=4)
odpowiedzi = []
punktacja = []
dziennik = []
# Słownik kolorów potrzebny do kolorowania
s_k = {'W': Fore.WHITE, 'V': Fore.MAGENTA, 'G': Fore.GREEN, 'R': Fore.RED, 'B': Fore.BLUE, 'Y': Fore.YELLOW}

for i in range(1, 11):
    # Tupla zawierająca obiekty rozwiązania
    rozwiazanie = [Grzybki(rozwiazanie_lista[z]) for z in range(4)]
    tura = Tura(paleta_kolorow, odpowiedzi)
    tura.sprawdz_czarne(rozwiazanie, dziennik)
    tura.sprawdz_biale(rozwiazanie, dziennik, punktacja)

    for y, linia in enumerate(odpowiedzi):
        print(f'TURA {y + 1}: ( {s_k[linia[0]]}{linia[0]}{Fore.RESET} - {s_k[linia[1]]}{linia[1]}{Fore.RESET} - {s_k[linia[2]]}{linia[2]}{Fore.RESET} - {s_k[linia[3]]}{linia[3]}{Fore.RESET} )', end='')
        print(f'\t{punktacja[y][0]} - {punktacja[y][1]}')

    if tura.czarne == 4:
        print(f'\n{Fore.RED}GRATUALCJE - Wygrałeś w {i} turze !!!')
        break

    elif i == 10:
        print(f'\nPrzegrałeś :( - rozwiązanie to {rozwiazanie_lista}')







