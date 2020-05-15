import random
class Ship():

    def __init__(self, x1, y1, x2, y2):

        self.__list_of_coordinates = []
        if not x2:      #Jezeli x2 i y2 sa zerami to jednomasztowiec
            self.__list_of_coordinates = [(x1,y1)]
        else:
            if x2 != x1:
                # Statek pionowo y1=y2 stale zmienia sie x w zakresie od x1 do x2
                self.__list_of_coordinates = [(x, y1) for x in range(x1, x2 + 1)]

            else:
                # Statek pionowo x1=x2 stale zmienia sie y w zakresie od y1 do y2
                self.__list_of_coordinates = [(x1, y) for y in range(y1, y2 + 1)]

    def get_list_of_coordinates(self):
        return self.__list_of_coordinates

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
        return occupied



class ShipsContainer():

    def __init__(self, who):
        print("Tworze przechowalnie statkow dla: ",who)
        self.__owner=who
        self.__list_of_ships=[]
        self.__my_shots=set()
        self.__ships_to_set=[4,3,3,2,2,2,1,1,1,1]

    def get_owner(self):
        return self.__owner

    def get_list_of_ships(self):
        return self.__list_of_ships

    def get_ships_to_set(self):
        return self.__ships_to_set

    def get_my_shots(self):
        return self.__my_shots

    def add_shot(self,coordinates):
        self.__my_shots.add(coordinates)

    def count_ships(self):
        print(len(self.__list_of_ships))

    def add_ship(self, x1, y1, x2, y2):
        # jezeli statek z jakis wzgledow nie zostanie ustawiony zwroci 1

        #Warunek do sprawdzenia zawsze!
        #TODO czesto sie powtarza mozna zrobic metode
        if(x1<1 or x1>10  or y1<1 or y1>10 ):
            print("Plansza jes wymiarow 10 x 10! Podane wpolrzedne nie mieszcza sie w planszy")
            return 1
        dl = 0

        #Warunek sprawdzajacy czy jednomasztowiec czy niee
        if not x2 or not y2:
            print("Jednomasztowiec ustawiam dlugosc")   #Jednomasztowiec to dlugosc=1
            dl=1

        #Warunek na to czy miesci sie w planszy
        elif (x2<1 or x2>10 or y2<1 or y2>10):
            print("Plansza jes wymiarow 10 x 10! Podane wpolrzedne nie mieszcza sie w planszy")

        # Sprawdzenie pion/poziom po tym czy ktores wspolrzedne sa takie same
        elif x2 != x1 and y2 != y1:
            print("Statek moze byc ustawiony tylko w poziomie lub pionie")
            return 1
        else:   #Wykona sie jesli: nie jednomasztowiec oraz wspolrzedne sa poprawne
                #Sprawdzi orientacje statku i poda jego dlugosc
            if x2 != x1:
                dl = abs(x2 - x1) + 1  # dlugosc zadanego statku (+1 bo nie liczylo wlacznie z pierwszym polem)
                if x2 < x1:
                    x1, x2 = x2, x1   #Ustawienie wspolrzednych tak aby x wskazywala na mniejsza a x2 na wieksza

            else:
                dl = abs(y2 - y1) + 1
                if y2 < y1:
                    y1, y2 = y2, y1   #Ustawienie wspolrzednych tak aby y wskazywala na mniejsza a y2 na wieksza

        #Wykona sie dla wszystkich statkow o poprawnych danych (jedno i wielo masztowce)
        if self.__ships_to_set.count(dl):
            for i in self.__list_of_ships:
            #Sprawdz czy pierwsze x1,y2 nie są hip_occupied
            #Lub jezeli wielo-masztowiec czy rowniez x2,y2 nie sa hip_occupied
                if i.get_hip_occupied()&{(x1, y1)} or (dl>1 and i.get_hip_occupied() & {(x2, y2)}):
                    print("Juz tu cos jest")
                    return 1
            print("Nie ma ustawiam")
            # Nastepnie stworzenie statku ,dodanie do listy i usuniecie z ships_to_set 1
            s = Ship(x1, y1, x2, y2)
            print(s.get_list_of_coordinates())
            self.__ships_to_set.pop(self.__ships_to_set.index(dl))
            self.__list_of_ships.append(s)
            return 0

        else:
            print("Ustawiles juz wszystkie statki o dlugosci: ", dl, " lub nie ma takiego statku do ustawienia")

    def search_remove_coordinates(self,x,y):
        for i in self.__list_of_ships:
            if i.get_list_of_coordinates().count((x, y)):
                ind = i.get_list_of_coordinates().index((x, y))      #Pobieram indeks znalezionych wspolrzednych
                d=i.get_list_of_coordinates().pop(ind)              #Usuwam wartosc i przypisuje do d (co z tym dalej?)
                print("Trafiony")
                print(i.get_list_of_coordinates())
                self.search_remove_ship()
                return 0
        print("Pudlo")
        return 1

    def search_remove_ship(self):
        for i in range(len(self.__list_of_ships)):    #Searching for ship with empty list_of_coordinates

            if not self.__list_of_ships[i].get_list_of_coordinates():
                print("Zatopiony!")
                self.__list_of_ships.pop(i)
                return

    def automatic_set_up(self):
        #TODO Bardziej zaawansowana! Ustawia tylko w poziomie
        print("Przeciwnik rozmieszcza swoje statki...")
        for i in range(0,4):        #Jakie dlugosci
            for j in range (4-i):   #Ile razy
                check=1
                while check:
                    x, y = random.randint(1, 10-i), random.randint(1, 10)
                    x2,y2 = x+i,y   #Tylko w poziomie!
                    check=self.add_ship(x, y, x2, y2)
        print("Przeciwnik jest gotowy!")
        self.count_ships()
