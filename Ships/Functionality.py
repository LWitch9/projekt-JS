import random


class Ship():

    #def __init__(self, x1, y1, x2, y2):

    # konstruktor dla jednomasztowca
    def __init__(self, x1, y1):
        self.__list_of_coordinates=[(x1,y1)]

    def take_list(self):
        return self.__list_of_coordinates

    #miejsca hipotetycznie zajete (zajete+ rogi boki)
    def get_miejsca(self):
        """
        Funkcja zwroci w liscie wartosci maxX minX maxY minY
        Wszystkie miejsca takie że (x<=maxX and x>=minX) || (y<=maxY and y>=minY)
        Są hipotetycznie zajete i nie mozna na nich nic ustawic
        Aby funkcja dzialala wspolrzedne powinny byc ustawione tak ze
        zaleznie od orientacji poziom pion ustawione sa od najmnijeszej do najwiekszej
        """
        occupied=[]
        m=self.__list_of_coordinates[0]

        occupied.append(m[0]+1)
        occupied.append(m[0] -1)
        occupied.append(m[1] + 1)
        occupied.append(m[1] - 1)
        return occupied

class ShipsContainer():

    def __init__(self, who):
        print("Tworze przechowalnie statkow dla: ",who)
        self.__owner=who
        self.__list_of_ships=[]
        self.__ships_to_set=[1,1,1,1]

    def add_ship(self):
        if not self.__ships_to_set:
            print("Ustawiles juz wszystkie statki! Przejdz do gry")
            return
        print("Podaj wspolrzedne statku: ")
        x = int(input("Podaj x: "))     #Wspolrzedne jednego konca sktaku
        y = int(input("Podaj y: "))

        if self.__ships_to_set.count(1):
            #Akcje sprawdzające czy dany statek moze zostac umieszczony
            print("Hello stranger")
            for i in self.__list_of_ships:
                if i.take_list().count((x,y)):
                    print("Juz tu cos jest")
                    return
            print("Nie ma ustawiam")
            # Nastepnie stworzenie statku ,dodanie do listy i usuniecie z ships_to_set 1
            s = Ship(x, y)
            s.get_miejsca() #tmp
            self.__ships_to_set.pop()
            self.__list_of_ships.append(s)

        else:
            print("Ustawiles juz wszystkie jednomasztowce!")

    def podglad_statkow(self):
        print(len(self.__list_of_ships))

if __name__ == '__main__':

    us=ShipsContainer("user")
    print("Chcesz dodac statek:")
    x= int(input("1/0: "))
    while x:
        us.add_ship()
        us.podglad_statkow()
        print("Chcesz dodac statek:")
        x = int(input("1/0: "))