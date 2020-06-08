import random
from operator import itemgetter
from Exceptions import *

class Ship():
    """
    klasa Ship reprezentuje pojedynczy statek

    Atrybuty:
    __list_of_coordinates : list
        lista zawiera współrzędne danego statku

    Kolejne atrybuty są ustawiane za pomocą __setattr__ w fazie strzelania tylko dla statków wtedy zestrzelonych

    Zatopiony: bool
        zmienna informująca o stanie trafionego statku
    horizonatll: bool
        zmienna informująca o orientacji danego statku

    Metody:
    get_list_of_coordinates
        zwraca prywatną zmienną __list_of_coordinates
    add_coordinate(x,y)
        dodaje współrzędne do listy __list_of_coordinates zwiększając długość statku
        Ustawia zmienną "horizontal" na True jeżeli orientacja statku jest pozioma w przeciwnym razie na False
        metoda uzywana jest dopiero przy zestrzeliwaniu statków gdy drugie pole statku zostanie trafione
    set_state(name)
        Ustawia zmienną "Zatopiony". Jeżeli zmienna name == "Zatopiony" ustawia na True w przewnym razie False
    get_hip_occupied
        zwraca zmienną occupied : set
        Jest zbiorem współrzędnych hipotetycznie zajętych dla danego statku.
        Zawiera zarówno współrzędne statku jak i współrzędne z nim sąsiadujące (rogi, boki)

    """

    def __init__(self, x1, y1, x2, y2):
        """
        konstruktor klasy
        W konstruktorze odbywa się sprawdzenie orientacji statku dla podanych współrzędnych, a następnie
        według tej orientacji uzupełnienie listy __list_of_coordinates współrzędnymi
        W przypadku gdy x1=x2 i y1=y2 powstaje jednomasztowiec o takich współrzędnych

        :param x1: współrzędna x pierwszego końca statku
        :param y1: współrzędna y pierwszego końca statku
        :param x2: współrzędna x drugiego końca statku
        :param y2: współrzędna y drugiego końca statku
        """

        #Warunek wystarczajacy dziala rowniez dla jednomasztowca
        if x2 != x1:
            # Statek pionowo y1=y2 stale zmienia sie x w zakresie od x1 do x2
            self.__list_of_coordinates = [(x, y1) for x in range(x1, x2 + 1)]

        else:
            # Statek pionowo x1=x2 stale zmienia sie y w zakresie od y1 do y2
            self.__list_of_coordinates = [(x1, y) for y in range(y1, y2 + 1)]

    def get_list_of_coordinates(self):
        """
        Zwraca listę wszystkich współrzędnych danego statku
        :return: __list_of_coordinates :list
        """
        return self.__list_of_coordinates

    def add_coordinate(self,x,y):
        """
        Dodaje współrzędne do listy __list_of_coordinates zwiększając długość statku
        Ustawia zmienną "horizontal" na True jeżeli orientacja statku jest pozioma w przeciwnym razie na False
        W zaleznosci od orientacji sortuje __list_of_coordinates po pierwszej lub drugiej współrzędnej
        Metoda uzywana jest dopiero przy zestrzeliwaniu statków gdy drugie pole statku zostanie trafione
        :param x: pierwsza współrzędna wybranego pola
        :param y: druga współrzędna wybranego pola
        """
        self.__list_of_coordinates.append((x,y))
        if x!=self.__list_of_coordinates[0][0]:
            self.__list_of_coordinates=sorted(self.__list_of_coordinates,key=itemgetter(0))
            self.__setattr__("horizontal",True)
        else:
            self.__list_of_coordinates=sorted(self.__list_of_coordinates,key=itemgetter(1))
            self.__setattr__("horizontal", False)

    def set_state(self,name):
        """
        Ustawia zmienną "Zatopiony". Jeżeli zmienna name == "Zatopiony" ustawia na True w przewnym razie False
        :param name: nazwa stanu w jakim jest statek może być : Zatopiony lub Trafiony
        """
        if name=="Zatopiony":
            self.__setattr__("state",True)
        else:
            self.__setattr__("state", False)

    def get_hip_occupied(self):
        """
        zwraca zmienną occupied

        :return: occupied : set ; jest zbiorem współrzędnych hipotetycznie zajętych dla danego statku.
             Zawiera zarówno współrzędne statku jak i współrzędne z nim sąsiadujące (rogi, boki)
        """

        xp = (self.__list_of_coordinates[0])[0]
        yp = (self.__list_of_coordinates[0])[1]

        if(len(self.__list_of_coordinates))>1:  #Przypadek wielomasztowca
            xk= (self.__list_of_coordinates[-1])[0]
            yk = (self.__list_of_coordinates[-1])[1]
        else:   #Przypadek jednomasztowca (współrzedne jednego końca równe współrzędnym drugiego)
            xk,yk=xp,yp

        #Tworzę zbiór par współrzędnych
        #będą zawierały współrzędne statku jak i współrzędne z nim sąsiadujące (rogi, boki)
        occupied = {(x,y) for x in range(xp-1,xk+2) for y in range(yp-1,yk+2)}

        #Wybieram tylko te współrzędne które mieszczą się w planszy 10x10
        occupied = occupied & {(x,y) for x in range(1,11) for y in range(1,11)}
        return occupied

class ShipsContainer():
    """
    Klasa ShipsCointainer reprezentująca plansze dla każdego gracza
    Jest główną klasą w której odbywa się funkcjonalnąś programu

    Atrybuty:
    all_coordinates : set
        zmienna wspólna dla wszytkich instancji zawierająca wszystkie współrzędne planszy 10X10
    __owner : string
        zmienna zawierająca nazwę gracza
    __list_of_ships : list
        zmienna zawierająca wszystkie statki umieszczone przez gracza na planszy
    __ships_to_set : list
        zmienna zawierająca liczby typu int odpowiadające długości statków pozostałych do ustawienia
    __my_shots : set
        zmienna zawierajaca pary liczb będące współrzędnymi pól jakie gracz wybrał podczas strzelania w
        plansze przeciwnika
    __hit_ships :list
        zmienna zawierająca obiekty będące statkami które gracz zestrzelił z planszy przeciwnika

    Kolejny atrybut jest ustawiany za pomocą __setattr__

    turn : bool
        zmienna informująca o tym czy jest konej uzytkownika(True) czy oponenta(False)

    Metody:
    get_owner
        zwraca prywatną zmienną __owner
    get_list_of_ships
        zwraca prywatną zmienną __list_of_ships
    get_ships_to_set
        zwraca prywatną zmienną __ships_to_set
     get_my_shots
        zwraca prywatną zmienną __my_shots
    show_ships_to_set
        zwraca obiekt typu string zawierający informacje o tym ile statków jakiego typu pozostało do ustawienia
    fill_ships_to_set
        wypełania zmienną __ships_to_set obiektami typu int będących długościami statków jakie należy ustawić
    initail_state
        resetuje atrybuty klasy do stanu w jakim były na początku gry
    add_shot(coordinates)
        dodaje do listy __my_shot parę wybranych współrzędnych (coordinates)
    add_ship(x1, y1, x2, y2)
        dodawanie statku do __list_of_ships po uprzednim sprawdzeniu warunków czy statek o podanych współrzędnych
        może być stworzony i ustawiony w danym miejscu
        Jeżeli nie rzucony zostanie odopiwedni wyjątek jeżeli tak zwróci 0
    search_remove_coordinates(x,y)
        Metoda szuka czy w __list_of_ships występują współrzędne które zostały podane podczas strzelania
        Jezeli tak usuwa daną współrzędną ze statku który ją zawiera
        Ponadto jeżeli po usunięciu Statek będzie pusty (nie będzie zawierał już żadnych współrzędnych)
        oznaczać to będzie że statek został zatopiony
        W obu przypadkach zostanie rzucony wyjątek HitException do którego przekazana zostanie odpowiednia nazwa
        W przeciwnym wypadku (gdy współrzędnej nie ma na liście) rzucony zostanie wyjątek MissedException
    search_remove_ship
        Sprawdz czy któryś ze statków w __list_of_ships nie jest pusty. Jeśli tak zwraca 1 jeśli nie 0
    automatic_set_up
        metoda losowo rozstawia statki na planszy
    add_to_hit_ship(x,y,name)
        Dodaje wybrane pole (na którym znajdował się statek przeciwnika) do listy __hit_ships
        Albo do już istniejącego statku albo tworząc nowy
        Sprawdza też czy po trafieniu danego pola statek jest wciąż do zestrzelenia czy już zatopiony
        nadając mu odpowiednią wartość zmiennej Zatopiony za pomocą metody set_state
    occupied_by_hit_ships
        Metoda zwraca zbiór zawierający sume zbiorów współrzędnych hipotetycznie zajętych przez Zatopione statki
        z __hit_ships (przy pomocy metody get_hip_occupied)
    check_hit_ships
        Metoda zwraca zbior z ktorego ma sie odbyc losowanie kolejnych wspolrzednych
        Jezeli statek nie jest zatopiony :
            Dla statku o jednej wspolrzednej : wspolrzene statku oraz jego boki
            Dla statku o więcej niż jednej wspolrzendej: wspolrzene statku oraz jego boki(tylko te na jakie wskazuje orientacja)
        Jezeli jest zatopiony:
            wszystkie wspolrzedne planszy
        w każdym przypadku od danego zbiory odejmowany jest zbior niechciane zawierający wykonane strzały + occupied_by_hit_ships
    """
    all_coordinates={(x,y) for x in range(1,11) for y in range(1,11)}   #Dla wszystkich instancji

    def __init__(self, who):
        """
        konstruktor
        :param who: string ; nazwa gracza , posiadacza planszy
        """
        print("Tworze przechowalnie statkow dla: ",who)
        self.__owner=who
        self.__list_of_ships=[]
        self.__ships_to_set=[]
        self.fill_ships_to_set()

        self.__my_shots=set()
        self.__hit_ships=[]

    def get_owner(self):
        """
        zwraca prywatna zmienna zawierająca nazwę gracza
        :return: __owner : string
        """
        return self.__owner

    def get_list_of_ships(self):
        """
        zwraca prywatną zmienną __list_of_ships lista zawierająca statki umieszczone na planszy gracza
        :return: __list_of_ships : list
        """
        return self.__list_of_ships

    def get_ships_to_set(self):
        """
        zwraca prywatną zmienną __ships_to_set informujacą o statkach do ustawienia
        :return: __ships_to_set :set
        """
        return self.__ships_to_set

    def get_my_shots(self):
        """
        zwraca prywatną zmienną __my_shots
        :return: __my_shots :set
        """
        return self.__my_shots

    def show_ships_to_set(self):
        """
        zwraca obiekt typu string zawierający informacje o tym ile statków jakiego typu pozostało do ustawienia
        :return: string : string
        """
        string= "Do ustawienia zostalo:\nJednomasztowcow x "+str(self.__ships_to_set.count(1))+"\tDwumasztowcow x "+str(self.__ships_to_set.count(2))+"\tTrzymasztowcow x "+str(self.__ships_to_set.count(3))+"\tCzteromasztowcow x "+str(self.__ships_to_set.count(4))
        return string

    def fill_ships_to_set(self):
        """
         wypełania zmienną __ships_to_set obiektami typu int będących długościami statków jakie należy ustawić
        """
        for i in range(0,4):        #Jakie dlugosci
            for j in range (4-i):   #Ile razy
                self.__ships_to_set.append(i+1)

    def initial_state(self):
        """
        resetuje atrybuty klasy do stanu w jakim były na początku gry
        """
        if hasattr(self,'turn'):    #usuwam atrybut infoemujacy o tym czyja jest kolej
            delattr(self,'turn')

        if self.__list_of_ships:        #usuwam elementy z tablicy statkow
            self.__list_of_ships.clear()

        if self.__hit_ships:            #usuwam elementy z tablicy zestrzelonych statkow
            self.__hit_ships.clear()

        self.__ships_to_set.clear()     #usuwam elementy z tablicy statkow do ustawienia
        self.fill_ships_to_set() #Wypelniam tablice informujaca jakie statki powinny zostac ustawione


        if self.__my_shots:             #usuwam elementy ze zbioru wykonanych strzałów
            self.__my_shots.clear()

    def add_shot(self,coordinates):
        """
        dodaje do listy __my_shot parę wybranych współrzędnych (coordinates)
        :param coordinates: tuple ; zawiera współrzędne x,y wykonanego strzału
        """
        self.__my_shots.add(coordinates)

    def add_ship(self, x1, y1, x2, y2):
        """
        dodawanie statku do __list_of_ships po uprzednim sprawdzeniu warunków czy statek o podanych współrzędnych
        może być stworzony i ustawiony w danym miejscu
        Jeżeli nie rzucony zostanie odopiwedni wyjątek

        :param x1: współrzędna x pierwszego końca statku
        :param y1: współrzędna y pierwszego końca statku
        :param x2: współrzędna x drugiego końca statku
        :param y2: współrzędna y drugiego końca statku
        :return:
        """

        #Warunek na to czy miesci sie w planszy
        if not ({(x1,y1)} & self.all_coordinates and {(x2,y2)} & self.all_coordinates):
            raise CoordinatesOutOfRangeException()

        # Sprawdzenie pion/poziom po tym czy ktores wspolrzedne sa takie same
        elif x2 != x1 and y2 != y1:
            raise WrongOrientationException()
        else:   #Sprawdza orientacje i dlugosc
            dl=0
            if x2 != x1:
                dl = abs(x2 - x1) + 1  # dlugosc zadanego statku (+1 bo nie liczylo wlacznie z pierwszym polem)
                if x2 < x1:
                    x1, x2 = x2, x1   #Ustawienie wspolrzednych tak aby x wskazywala na mniejsza a x2 na wieksza

            else:
                dl = abs(y2 - y1) + 1
                if y2 < y1:
                    y1, y2 = y2, y1   #Ustawienie wspolrzednych tak aby y wskazywala na mniejsza a y2 na wieksza

            if self.__ships_to_set.count(dl):   #Sprawdza czy jeszcze mozna postawic statek o danej dlugosci
                for i in self.__list_of_ships:
                    # Sprawdz czy pierwsze x1,y2 nie są hip_occupied
                    # Lub jezeli wielo-masztowiec czy rowniez x2,y2 nie sa hip_occupied
                    if i.get_hip_occupied() & {(x1, y1)} or (dl > 1 and i.get_hip_occupied() & {(x2, y2)}):
                        raise OccupiedException()

                # Nastepnie stworzenie statku ,dodanie do listy i usuniecie z ships_to_set numeru = dlugosci statku
                s = Ship(x1, y1, x2, y2)
                self.__ships_to_set.pop(self.__ships_to_set.index(dl))
                self.__list_of_ships.append(s)
            else:
                #Jezeli nie mozna postawic statku danej dlugości
                raise WrongLengthException()

    def search_remove_coordinates(self,x,y):
        """
        Metoda szuka czy w __list_of_ships występują współrzędne które zostały podane podczas strzelania
        Jezeli tak usuwa daną współrzędną ze statku który ją zawiera
        Ponadto jeżeli po usunięciu Statek będzie pusty (nie będzie zawierał już żadnych współrzędnych)
        oznaczać to będzie że statek został zatopiony
        W obu przypadkach zostanie rzucony wyjątek HitException do którego przekazana zostanie odpowiednia nazwa
        W przeciwnym wypadku (gdy współrzędnej nie ma na liście) rzucony zostanie wyjątek MissedException

        :param x : pierwsza współrzędna wybranego pola
        :param y: druga współrzędna wybranego pola

        """
        # Zwraca 0 jak pudlo 1 jak trafiony 2 jak trafiony zatopiony
        for i in self.__list_of_ships:
            if i.get_list_of_coordinates().count((x, y)):
                ind = i.get_list_of_coordinates().index((x, y))      #Pobieram indeks znalezionych wspolrzednych
                x,y=i.get_list_of_coordinates().pop(ind)              #Usuwam wartosc i przypisuje do d (co z tym dalej?)
                if self.search_remove_ship():
                    raise HitException("Zatopiony")
                else:
                    raise HitException("Trafiony")
        else:
            raise MissedException()

    def search_remove_ship(self):
        """
        Sprawdz czy któryś ze statków w __list_of_ships nie jest pusty.
        :return: 1 jeśli pusta 0 jeśli nie
        """
        for i in range(len(self.__list_of_ships)):    #Searching for ship with empty list_of_coordinates
            if not self.__list_of_ships[i].get_list_of_coordinates():
                self.__list_of_ships.pop(i)
                return 1
        return 0

    def automatic_set_up(self):
        """
        metoda losowo rozstawia statki na planszy
        Losuje współrzędne z różnicy zbioró: wszystkich współrzędnych - niechciane
        Gdzie niechciane zawierają pola na których nie można ustawić statku czyli
        Sumy zbiorów get_hip_occupied dla każdego statku który już jest postawiony
        """

        pula_niechcianych=set()
        for i in range(0,4):        #Jakie dlugosci
            for j in range (4-i):   #Ile razy
                available_filds = [zb for zb in self.all_coordinates -pula_niechcianych ]

                while True:
                    x, y = random.choice(available_filds)   #Losuje współrzędne jednego końca
                    x2,y2 = x+i,y       # współrzędne drugiego końca w poziomie według aktualnej długości i
                    if {(x2,y2)} & pula_niechcianych:       #Jezeli drugie współrzędne leżą w miejscu niedozwolonym tworze w pionie
                        x2,y2=x,y+i
                    try:
                        self.add_ship(x, y, x2, y2)     #Proba dodania statku
                        #Jezeli wybrana (pion/poziom) wersja rowniez lezy w niedozwolonym miejscu rzucony bedzie wyjątek i
                        # I procedura wykona się raz jeszcze
                    except AddingShipException as e:
                        pass
                    else:
                        #Jezeli statek został poprawnie umieszczony powiększam pule_niechcianych o get_hip_occupied statku
                        #i przerywam pętle
                        pula_niechcianych = pula_niechcianych | self.__list_of_ships[-1].get_hip_occupied()
                        break

    def add_to_hit_ship(self,x,y,name):
        """
        Dodaje wybrane pole (na którym znajdował się statek przeciwnika) do listy __hit_ships
        Albo do już istniejącego statku albo tworząc nowy
        Sprawdza też czy po trafieniu danego pola statek jest wciąż do zestrzelenia czy już zatopiony
        nadając mu odpowiednią wartość zmiennej Zatopiony za pomocą metody set_state
        :param x: pierwsza współrzędna wybranego zestrzelonego pola
        :param y: druga współrzędna wybranego zestrzelonego pola
        :param name: nazwa stanu (czy statek został już zatopiony czy tylko trafiony)
        :return:
        """
        if self.__hit_ships:
            for i in self.__hit_ships:
                if {(x,y)} & i.get_hip_occupied():
                    i.add_coordinate(x,y)
                    i.set_state(name)
                    return

            s = Ship(x,y,x,y)
            s.set_state(name)
            self.__hit_ships.append(s)  #Tworze statek z tą wspolrzedna

        else:
            s = Ship(x,y,x,y)
            s.set_state(name)
            self.__hit_ships.append(s)  #Tworze statek z tą wspolrzedna

    def occupied_by_hit_ships(self):
        """
        Metoda zwraca zbiór zawierający sume zbiorów współrzędnych hipotetycznie zajętych przez Zatopione statki
        z __hit_ships (przy pomocy metody get_hip_occupied)
        :return: pula :set
        """
        pula=set()
        for i in self.__hit_ships:
            if i.state:
                pula=pula | i.get_hip_occupied()
        return pula

    def check_hit_ships(self):
        """
        Metoda zwraca zbior z ktorego ma sie odbyc losowanie kolejnych wspolrzednych
        Jezeli statek nie jest zatopiony :
            Dla statku o jednej wspolrzednej : wspolrzene statku oraz jego boki
            Dla statku o więcej niż jednej wspolrzendej: wspolrzene statku oraz jego boki(tylko te na jakie wskazuje orientacja)
        Jezeli jest zatopiony:
            wszystkie wspolrzedne planszy
        w każdym przypadku od danego zbiory odejmowany jest zbior niechciane zawierający wykonane strzały + occupied_by_hit_shi
        :return: pula -niechciane :set Jezeli statek nie jest zatopiony
                self.all_coordinates - niechciane : set Jezeli statek jest zatopiony
        """
        niechciane = self.occupied_by_hit_ships() | self.__my_shots
        for i in self.__hit_ships:
            if not i.state:
                if hasattr(i,"horizontal"): #Kiedy wiecej niz jeden trafione pole w statku
                    if i.horizontal:
                        pula={zb for zb in i.get_hip_occupied() if zb[1]==i.get_list_of_coordinates()[0][1]}
                    else:
                        pula = {zb for zb in i.get_hip_occupied() if zb[0] == i.get_list_of_coordinates()[0][0]}
                else:
                    pula1 = {zb for zb in i.get_hip_occupied() if zb[0] == i.get_list_of_coordinates()[0][0]}
                    pula2 = {zb for zb in i.get_hip_occupied() if zb[1] == i.get_list_of_coordinates()[0][1]}
                    pula = pula1 | pula2
                return pula - niechciane
        return self.all_coordinates - niechciane  #Inteligentne omija pola na ktorych na pewno nie ma statkow


if __name__ == '__main__':
    us = ShipsContainer("user")
    pc = ShipsContainer("pc")

    #Test1
    try:
        us.add_ship(2,2,2,3)
        us.add_ship(3,2,3,3)
    except OccupiedException:
        print("Tu nie mozna nic postawic")





