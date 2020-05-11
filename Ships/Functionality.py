import random
class Ship():

    def __init__(self, x1, y1, x2, y2):
        self.__list_of_coordinates = [(x1, y1),(x2,y2)]

    #TODO po odkomentowaniu konstruktora dla jednomaszt nie działa konstruktor wyzej dlaczego?
    #konstruktor dla jednomasztowca
    #def __init__(self, x1, y1):
    #    self.__list_of_coordinates=[(x1,y1)]

    def take_list(self):
        return self.__list_of_coordinates

    #miejsca hipotetycznie zajete (zajete+ rogi boki)
    def get_miejsca(self):
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
            xk,yk=xp,yp
        occupied = {(x,y) for x in range(xp-1,xk+2) for y in range(yp-1,yk+2)}
        return occupied



class ShipsContainer():

    def __init__(self, who):
        print("Tworze przechowalnie statkow dla: ",who)
        self.__owner=who
        self.__list_of_ships=[]
        self.__ships_to_set=[4,3,3,2,2,2,1,1,1,1]

    def add_ship(self,x,y):
        if not self.__ships_to_set:
            print("Ustawiles juz wszystkie statki! Przejdz do gry")
            return

        if(x<1 or x>10 or y<1 or y>10):
            print("Plansza jes wymiarow 10 x 10! Podane wpolrzedne nie mieszcza sie w planszy")
            return
        if self.__ships_to_set.count(1):
            #Akcje sprawdzające czy dany statek moze zostac umieszczony
            for i in self.__list_of_ships:
                if i.get_miejsca()&{(x,y)}:
                    print("Juz tu cos jest")
                    return
            print("Nie ma ustawiam")
            # Nastepnie stworzenie statku ,dodanie do listy i usuniecie z ships_to_set 1
            s = Ship(x, y)
            print(s.get_miejsca()) #tmp
            self.__ships_to_set.pop()  #TODO usuwa ostatni z listy! powinien konkretny element
            self.__list_of_ships.append(s)

        else:
            print("Ustawiles juz wszystkie jednomasztowce!")

    def add_ship2(self,x,y,x2,y2):
        if not self.__ships_to_set:
            print("Ustawiles juz wszystkie statki! Przejdz do gry")
            return

        if(x<1 or x>10 or x2<1 or x2>10 or y<1 or y>10 or y2<1 or y2>10):
            print("Plansza jes wymiarow 10 x 10! Podane wpolrzedne nie mieszcza sie w planszy")
            return
        if x2 != x and y2 != y:  # Sprawdzenie pion/poziom po tym czy ktores wspolrzedne sa takie same
            print("Statek moze byc ustawiony tylko w poziomie lub pionie")
            return
        else:
            dl=0
            if x2 != x:
                dl = abs(x2 - x)+1  # dlugosc zadanego statku (+1 bo nie liczylo wlacznie z pierwszym polem)
                if x2 < x:
                    x, x2 = x2, x   #Ustawienie wspolrzednych tak aby x wskazywala na mniejsza a x2 na wieksza

            else:
                dl = abs(y2 - y)+1
                if y2 < y:
                    y, y2 = y2, y   #Ustawienie wspolrzednych tak aby y wskazywala na mniejsza a y2 na wieksza

        if self.__ships_to_set.count(dl):
            for i in self.__list_of_ships:
                if i.get_miejsca()&{(x,y)} or i.get_miejsca() & {(x2,y2)}:
                    print("Juz tu cos jest")
                    return
            print("Nie ma ustawiam")
            # Nastepnie stworzenie statku ,dodanie do listy i usuniecie z ships_to_set 1
            s = Ship(x, y, x2, y2)

            #self.__ships_to_set.pop()
            self.__list_of_ships.append(s)
        else:
            print("Ustawiles juz wszystkie statki o dlugosci: ", dl, " lub nie ma takiego statku do ustawienia")


    def podglad_statkow(self):
        print(len(self.__list_of_ships))

if __name__ == '__main__':

    us=ShipsContainer("user")
    print("Chcesz dodac statek:")
    x= int(input("1/0: "))
    while x:
        print("Podaj wspolrzedne statku: ")
        x = int(input("Podaj x: "))     #Wspolrzedne jednego konca sktaku
        y = int(input("Podaj y: "))

        _longer_ship=int(input("Czy twoj statek jest dluzszy? 1/0:"))
        if _longer_ship:
            print("Podaj wspolrzedne statku: ")
            x2 = int(input("Podaj x: "))     #Wspolrzedne drugiego konca sktaku
            y2 = int(input("Podaj y: "))
            us.add_ship2(x,y,x2,y2)
            us.podglad_statkow()
        else:
            us.add_ship(x,y)
        print("Chcesz dodac statek:")
        x = int(input("1/0: "))