import random
from operator import itemgetter
from Exceptions import *
class Ship():

    def __init__(self, x1, y1, x2, y2):

        #Warunek wystarczajacy dziala rowniez dla jednomasztowca
        if x2 != x1:
            # Statek pionowo y1=y2 stale zmienia sie x w zakresie od x1 do x2
            self.__list_of_coordinates = [(x, y1) for x in range(x1, x2 + 1)]

        else:
            # Statek pionowo x1=x2 stale zmienia sie y w zakresie od y1 do y2
            self.__list_of_coordinates = [(x1, y) for y in range(y1, y2 + 1)]


    def get_list_of_coordinates(self):
        return self.__list_of_coordinates

    def add_coordinate(self,x,y):
        self.__list_of_coordinates.append((x,y))
        if x!=self.__list_of_coordinates[0][0]:
            self.__list_of_coordinates=sorted(self.__list_of_coordinates,key=itemgetter(0))
            self.__setattr__("horizontal",True)
        else:
            self.__list_of_coordinates=sorted(self.__list_of_coordinates,key=itemgetter(1))
            self.__setattr__("horizontal", False)


    def set_state(self,name):
        if name=="Zatopiony":
            self.__setattr__("state",True)
        else:
            self.__setattr__("state", False)

    #miejsca hipotetycznie zajete (zajete+ rogi boki)
    def get_hip_occupied(self):
        """
        Funkcja zwroci w zbiorze pary x,y , ktore
        Są hipotetycznie zajete i nie mozna na nich nic ustawic
        Aby funkcja dzialala wspolrzedne powinny byc ustawione tak ze
        zaleznie od orientacji poziom pion ustawione sa od najmnijeszej do najwiekszej
        czyli xp<xk  oraz yp<yk
        """

        xp = (self.__list_of_coordinates[0])[0]
        yp = (self.__list_of_coordinates[0])[1]

        if(len(self.__list_of_coordinates))>1:
            xk= (self.__list_of_coordinates[-1])[0]
            yk = (self.__list_of_coordinates[-1])[1]
        else:
            #TODO Niech sprawdza tez czy te nowe miejsca mieszcza sie w planszy i tylko te uwzglednia
            xk,yk=xp,yp
        occupied = {(x,y) for x in range(xp-1,xk+2) for y in range(yp-1,yk+2)}
        occupied = occupied & {(x,y) for x in range(1,11) for y in range(1,11)}
        return occupied

class ShipsContainer():
    all_coordinates={(x,y) for x in range(1,11) for y in range(1,11)}   #Dla wszystkich instancji

    def __init__(self, who):
        print("Tworze przechowalnie statkow dla: ",who)
        self.__owner=who
        self.__list_of_ships=[]
        self.__ships_to_set=[]
        self.fill_ships_to_set()

        self.__my_shots=set()
        self.__hit_ships=[]


    def get_owner(self):
        return self.__owner

    def get_list_of_ships(self):
        return self.__list_of_ships

    def get_ships_to_set(self):
        return self.__ships_to_set

    def show_ships_to_set(self):
        string= "Do ustawienia zostalo:\nJednomasztowcow x "+str(self.__ships_to_set.count(1))+"\tDwumasztowcow x "+str(self.__ships_to_set.count(2))+"\tTrzymasztowcow x "+str(self.__ships_to_set.count(3))+"\tCzteromasztowcow x "+str(self.__ships_to_set.count(4))
        return string

    def fill_ships_to_set(self):
        for i in range(0,4):        #Jakie dlugosci
            for j in range (4-i):   #Ile razy
                self.__ships_to_set.append(i+1)

    def initial_state(self):

        if hasattr(self,'turn'):    #usuwam atrybut infoemujacy o tym czyja jest kolej
            delattr(self,'turn')

        if self.__list_of_ships:        #usuwam elementy z tablicy statkow
            self.__list_of_ships.clear()

        if self.__hit_ships:
            self.__hit_ships.clear()

        self.__ships_to_set.clear()
        self.fill_ships_to_set() #Wypelniam tablice informujaca jakie statki powinny zostac ustawione


        if self.__my_shots:
            self.__my_shots.clear()

    def get_my_shots(self):
        return self.__my_shots

    def add_shot(self,coordinates):
        self.__my_shots.add(coordinates)

    def count_ships(self):
        print(len(self.__list_of_ships))

    def add_ship(self, x1, y1, x2, y2):
        # Uwaga zmianiane teraz zwraca komunikaty!

        #Warunek do sprawdzenia zawsze!
        #TODO czesto sie powtarza mozna zrobic metode
        #Warunek na to czy miesci sie w planszy
        if (x1<1 or x1>10  or y1<1 or y1>10 or x2<1 or x2>10 or y2<1 or y2>10):
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

                # Nastepnie stworzenie statku ,dodanie do listy i usuniecie z ships_to_set 1
                s = Ship(x1, y1, x2, y2)
                print(s.get_list_of_coordinates())
                self.__ships_to_set.pop(self.__ships_to_set.index(dl))
                self.__list_of_ships.append(s)
                return 0
            else:
                raise WrongLengthException()

    def search_remove_coordinates(self,x,y):
        # Zwraca 0 jak pudlo 1 jak trafiony 2 jak trafiony zatopiony
        for i in self.__list_of_ships:
            if i.get_list_of_coordinates().count((x, y)):
                ind = i.get_list_of_coordinates().index((x, y))      #Pobieram indeks znalezionych wspolrzednych
                d=i.get_list_of_coordinates().pop(ind)              #Usuwam wartosc i przypisuje do d (co z tym dalej?)
                if self.search_remove_ship():
                    raise HitException("Zatopiony")
                else:
                    raise HitException("Trafiony")
        else:
            raise MissedException()

    def search_remove_ship(self):
        for i in range(len(self.__list_of_ships)):    #Searching for ship with empty list_of_coordinates
            if not self.__list_of_ships[i].get_list_of_coordinates():
                self.__list_of_ships.pop(i)
                return 1
        return 0

    def automatic_set_up(self):
        #TODO Bardziej zaawansowana! Ustawia tylko w poziomie
        print("Przeciwnik rozmieszcza swoje statki...")
        for i in range(0,4):        #Jakie dlugosci
            for j in range (4-i):   #Ile razy
                check=1
                while check:
                    x, y = random.randint(1, 10-i), random.randint(1, 10)
                    print(x,y)
                    x2,y2 = x+i,y   #Tylko w poziomie!
                    try:
                        self.add_ship(x, y, x2, y2)
                    except AddingShipException as e:
                        pass
                    else:
                        check=0
        return"Przeciwnik jest gotowy!"+str(self.count_ships())

    def add_to_hit_ship(self,x,y,name):
        if self.__hit_ships:
            for i in self.__hit_ships:
                if {(x,y)} & i.get_hip_occupied():
                    i.add_coordinate(x,y)
                    i.set_state(name)
                    print("Juz byl stateczek i dodajemy ")
                    print("coo: ", i.get_list_of_coordinates())
                    print("occ from add: ",i.get_hip_occupied())
                    return

            s = Ship(x,y,x,y)
            s.set_state(name)
            self.__hit_ships.append(s)  #Tworze statek z tą wspolrzedna

        else:
            s = Ship(x,y,x,y)
            s.set_state(name)
            self.__hit_ships.append(s)  #Tworze statek z tą wspolrzedna

    def check_hit_ships(self):
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
                return pula
        return self.all_coordinates
