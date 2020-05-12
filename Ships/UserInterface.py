import Functionality as f
import random

class InterfaceUser():
    def __init__(self):
        """
        Tworzy:
        1. Wygląd interface (wyswietla dwie plansze i przycinski)
        przechowalnie statkow dla uzytkownika i dla komputera ???
        """
        self.us = f.ShipsContainer("user")
        self.pc=f.ShipsContainer("PC")
    #def Gra(self):
        """

        :return:
        """
    def Faza_rozmieszczanie_PC(self):
        #TODO Bardziej zaawansowana! Ustawia tylko w poziomie
        print("Przeciwnik rozmieszcza swoje statki...")
        for i in range(1,4):        #Jakie dlugosci
            for j in range (4-i):   #Ile razy
                check=1
                while check:
                    x, y = random.randint(1, 10-i), random.randint(1, 10)
                    x2,y2 = x+i,y   #Tylko w poziomie!
                    check=self.pc.add_ship2(x, y, x2, y2)
        print("Przeciwnik jest gotowy!")
        self.pc.count_ships()

    def Faza_rozmieszczanie_user(self):

        print("Chcesz dodac statek:")
        x = int(input("1/0: "))
        while x:
            print("Podaj wspolrzedne statku: ")
            x = int(input("Podaj x: "))  # Wspolrzedne jednego konca sktaku
            y = int(input("Podaj y: "))

            longer_ship = int(input("Czy twoj statek jest dluzszy? 1/0:"))
            if longer_ship:
                print("Podaj wspolrzedne statku: ")
                x2 = int(input("Podaj x: "))  # Wspolrzedne drugiego konca sktaku
                y2 = int(input("Podaj y: "))
                self.us.add_ship2(x, y, x2, y2)
                self.us.count_ships()
            else:
                self.us.add_ship(x, y)
            print("Chcesz dodac statek:")
            x = int(input("1/0: "))

    def Faza_strzelanie_PC(self):

        #Part of choosing random coordinates
        #TODO usprawnic losowanie zeby nie losowal miejsc juz strzelanych
        #TODO Musi probowac zestrzelic statek do konca
        x, y = random.randint(1, 10), random.randint(1, 10)
        if self.pc.get_my_shots() &{(x,y)}:
            self.Faza_strzelanie_PC()  # Jeszcze raz strzelaj jezeli strzeliles  w to samo miejsce
        else:
            self.pc.add_shot((x,y))

        # Szukanie i usuwanie zestrzelonych pol/ statkow
        if self.pc.search_remove_coordinates(x, y):  # Jesli 0- trafiony/zatopiony; jesli 1- pudlo
            self.Faza_strzelanie_user()
        else:
            if self.us.get_list_of_ships():  # Jezeli lista statkow przeciwnika nie jest pusta
                self.Faza_strzelanie_PC()  # User ma kolejny ruch
            else:
                self.EndGame(self.us.get_owner())  # W przeciwnym razie koniec gry User wygral

    def Faza_strzelanie_user(self):
        print("Twoja kolej!")
        print("Podaj wspolrzedne : ")
        x = int(input("Podaj x: "))
        y = int(input("Podaj y: "))

        if (x < 1 or x > 10 or y < 1 or y > 10):
            print("Plansza jes wymiarow 10 x 10! Podane wpolrzedne nie mieszcza sie w planszy")
            self.Faza_strzelanie_user()     #Jeszcze raz strzelaj bo dane bledne

        #Po wykonaniu strzalu zostaje on zapisany do zbioru my shots!!!!
        if self.us.get_my_shots() &{(x,y)}:
            print("Tu juz strzelales!")
            self.Faza_strzelanie_user()  # Jeszcze raz strzelaj jezeli strzeliles  w to samo miejsce
        else:
            self.us.add_shot((x,y))

        if self.pc.search_remove_coordinates(x, y): #Jesli 0- trafiony/zatopiony; jesli 1- pudlo
            print("Kolej przeciwnika!")
            self.Faza_strzelanie_PC()
        else:
            if self.pc.get_list_of_ships():         #Jezeli lista statkow przeciwnika nie jest pusta
                self.Faza_strzelanie_user()         #User ma kolejny ruch
            else:
                self.EndGame(self.us.get_owner())           #W przeciwnym razie koniec gry User wygral


    def EndGame(self,name):
        print("Wygral: ",name)
        return

if __name__ == '__main__':
    x= InterfaceUser()
    x.Faza_rozmieszczanie_PC()
    x.Faza_rozmieszczanie_user()
    x.Faza_strzelanie_user()
