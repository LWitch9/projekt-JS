import random


class Ship():

    #def __init__(self, x1, y1, x2, y2):

    # konstruktor dla jednomasztowca
    def __init__(self, x1, y1):

class PrzechowywaczStatkow():

    def __init__(self, who):
        print("Tworze przechowalnie statkow dla: ",who)
        self.__owner=who
        self.__list_of_ships=[]
        self.__ships_to_set=[4,3,3,2,2,2,1,1,1,1]

    def add_ship(self):
        if not self.__ships_to_set:
            print("Ustawiles juz wszystkie statki! Przejdz do gry")
            return
        print("Podaj wspolrzedne statku: ")
        x = int(input("Podaj x: "))     #Wspolrzedne jednego konca sktaku
        y = int(input("Podaj y: "))

        x2 = int(input("Podaj x: "))    #Wspolrzedne drugiego konca sktaku
        y2 = int(input("Podaj y: "))



if __name__ == '__main__':

