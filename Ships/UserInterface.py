from Functionality import *
import random
from tkinter import *

class InterfaceUser():
    def __init__(self, master):
        """
        Tworzy:
        1. Wygląd interface (wyswietla dwie plansze i przycinski)
        przechowalnie statkow dla uzytkownika i dla komputera ???
        """
        #todo Czy zmienne frame itp powinny byc self?????
        canvas = Canvas(master, height=600, width=900)
        canvas.pack()

        # background
        back_frame = Frame(master, bg='green')
        back_frame.place(relwidth=1,relheight=1)

        # Pole planszy lewej
        board_left = Frame(back_frame, bg='black')
        board_left.place(x=90, y=150, width=300, height=300)

        self.buttons_left(board_left)

        #Tworze liste zbierajaca klikniecia
        self.__clicked_coords=[]

        #Tworze Przechowywalnie statkow dla 2 graczy (user, PC)
        self.us = ShipsContainer("user")
        self.pc=ShipsContainer("PC")

    def buttons_left(self,board_left):

        """ Wszystkie przyciski lewej planszy"""
        self.__A1 = Button(board_left, height=1, width=3, command=lambda: self.click((1, 1)), bg="Olive Drab",anchor="sw",text="A1")
        self.__A2 = Button(board_left, height=1, width=3, command=lambda: self.click((2, 1)), bg="Light Yellow",anchor="sw",text="2")
        self.__A3 = Button(board_left, height=1, width=3, command=lambda: self.click((3, 1)), bg="Olive Drab",anchor="sw",text="3")
        self.__A4 = Button(board_left, height=1, width=3, command=lambda: self.click((4, 1)), bg="Light Yellow",anchor="sw",text="4")
        self.__A5 = Button(board_left, height=1, width=3, command=lambda: self.click((5, 1)), bg="Olive Drab",anchor="sw",text="5")
        self.__A6 = Button(board_left, height=1, width=3, command=lambda: self.click((6, 1)), bg="Light Yellow",anchor="sw",text="6")
        self.__A7 = Button(board_left, height=1, width=3, command=lambda: self.click((7, 1)), bg="Olive Drab",anchor="sw",text="7")
        self.__A8 = Button(board_left, height=1, width=3, command=lambda: self.click((8, 1)), bg="Light Yellow",anchor="sw",text="8")
        self.__A9 = Button(board_left, height=1, width=3, command=lambda: self.click((9, 1)), bg="Olive Drab",anchor="sw",text="9")
        self.__A10= Button(board_left, height=1, width=3, command=lambda: self.click((10, 1)), bg="Light Yellow",anchor="sw", text="10")
        self.__B1 = Button(board_left, height=1, width=3, command=lambda: self.click((2,1)), bg="Light Yellow",anchor="sw",text="B")
        self.__B2 = Button(board_left, height=1, width=3, command=lambda: self.click((2,2)), bg="Olive Drab",anchor="sw")
        self.__B3 = Button(board_left, height=1, width=3, command=lambda: self.click((2,3)), bg="Light Yellow",anchor="sw")
        self.__B4 = Button(board_left, height=1, width=3, command=lambda: self.click((2,4)), bg="Olive Drab",anchor="sw")
        self.__B5 = Button(board_left, height=1, width=3, command=lambda: self.click((2,5)), bg="Light Yellow",anchor="sw")
        self.__B6 = Button(board_left, height=1, width=3, command=lambda: self.click((2,6)), bg="Olive Drab",anchor="sw")
        self.__B7 = Button(board_left, height=1, width=3, command=lambda: self.click((2,7)), bg="Light Yellow",anchor="sw")
        self.__B8 = Button(board_left, height=1, width=3, command=lambda: self.click((2,8)), bg="Olive Drab",anchor="sw")
        self.__B9 = Button(board_left, height=1, width=3, command=lambda: self.click((2,9)), bg="Olive Drab",anchor="sw")
        self.__B10= Button(board_left, height=1, width=3, command=lambda: self.click((2,10)), bg="Olive Drab",anchor="sw")
        self.__C1 = Button(board_left, height=1, width=3, command=lambda: self.click((3,1)), bg="Olive Drab",anchor="sw",text="C")
        self.__C2 = Button(board_left, height=1, width=3, command=lambda: self.click((3,2)), bg="Light Yellow",anchor="sw")
        self.__C3 = Button(board_left, height=1, width=3, command=lambda: self.click((3,3)), bg="Olive Drab",anchor="sw")
        self.__C4 = Button(board_left, height=1, width=3, command=lambda: self.click((3,4)), bg="Light Yellow",anchor="sw")
        self.__C5 = Button(board_left, height=1, width=3, command=lambda: self.click((3,5)), bg="Olive Drab",anchor="sw")
        self.__C6 = Button(board_left, height=1, width=3, command=lambda: self.click((3,6)), bg="Light Yellow",anchor="sw")
        self.__C7 = Button(board_left, height=1, width=3, command=lambda: self.click((3,7)), bg="Olive Drab",anchor="sw")
        self.__C8 = Button(board_left, height=1, width=3, command=lambda: self.click((3,8)), bg="Light Yellow",anchor="sw")
        self.__C9 = Button(board_left, height=1, width=3, command=lambda: self.click((3,9)), bg="Light Yellow",anchor="sw")
        self.__C10= Button(board_left, height=1, width=3, command=lambda: self.click((3,10)), bg="Light Yellow",anchor="sw")
        self.__D1 = Button(board_left, height=1, width=3, command=lambda: self.click((4,1)), bg="Light Yellow",anchor="sw",text="D")
        self.__D2 = Button(board_left, height=1, width=3, command=lambda: self.click((4,2)), bg="Olive Drab",anchor="sw")
        self.__D3 = Button(board_left, height=1, width=3, command=lambda: self.click((4,3)), bg="Light Yellow",anchor="sw")
        self.__D4 = Button(board_left, height=1, width=3, command=lambda: self.click((4,4)), bg="Olive Drab",anchor="sw")
        self.__D5 = Button(board_left, height=1, width=3, command=lambda: self.click((4,5)), bg="Light Yellow",anchor="sw")
        self.__D6 = Button(board_left, height=1, width=3, command=lambda: self.click((4,6)), bg="Olive Drab",anchor="sw")
        self.__D7 = Button(board_left, height=1, width=3, command=lambda: self.click((4,7)), bg="Light Yellow",anchor="sw")
        self.__D8 = Button(board_left, height=1, width=3, command=lambda: self.click((4,8)), bg="Olive Drab",anchor="sw")
        self.__D9 = Button(board_left, height=1, width=3, command=lambda: self.click((4,9)), bg="Olive Drab",anchor="sw")
        self.__D10= Button(board_left, height=1, width=3, command=lambda: self.click((4,10)), bg="Olive Drab",anchor="sw")
        self.__E1 = Button(board_left, height=1, width=3, command=lambda: self.click((5,1)), bg="Olive Drab",anchor="sw",text="E")
        self.__E2 = Button(board_left, height=1, width=3, command=lambda: self.click((5,2)), bg="Light Yellow",anchor="sw")
        self.__E3 = Button(board_left, height=1, width=3, command=lambda: self.click((5,3)), bg="Olive Drab", anchor="sw")
        self.__E4 = Button(board_left, height=1, width=3, command=lambda: self.click((5,4)), bg="Light Yellow",anchor="sw")
        self.__E5 = Button(board_left, height=1, width=3, command=lambda: self.click((5,5)), bg="Olive Drab",anchor="sw")
        self.__E6 = Button(board_left, height=1, width=3, command=lambda: self.click((5,6)), bg="Light Yellow",anchor="sw")
        self.__E7 = Button(board_left, height=1, width=3, command=lambda: self.click((5,7)), bg="Olive Drab",anchor="sw")
        self.__E8 = Button(board_left, height=1, width=3, command=lambda: self.click((5,8)), bg="Light Yellow",anchor="sw")
        self.__E9 = Button(board_left, height=1, width=3, command=lambda: self.click((5,9)), bg="Light Yellow",anchor="sw")
        self.__E10= Button(board_left, height=1, width=3, command=lambda: self.click((5,10)), bg="Light Yellow",anchor="sw")
        self.__F1 = Button(board_left, height=1, width=3, command=lambda: self.click((6,1)), bg="Light Yellow",anchor="sw",text="F")
        self.__F2 = Button(board_left, height=1, width=3, command=lambda: self.click((6,2)), bg="Olive Drab",anchor="sw")
        self.__F3 = Button(board_left, height=1, width=3, command=lambda: self.click((6,3)), bg="Light Yellow",anchor="sw")
        self.__F4 = Button(board_left, height=1, width=3, command=lambda: self.click((6,4)), bg="Olive Drab",anchor="sw")
        self.__F5 = Button(board_left, height=1, width=3, command=lambda: self.click((6,5)), bg="Light Yellow",anchor="sw")
        self.__F6 = Button(board_left, height=1, width=3, command=lambda: self.click((6,6)), bg="Olive Drab",anchor="sw")
        self.__F7 = Button(board_left, height=1, width=3, command=lambda: self.click((6,7)), bg="Light Yellow",anchor="sw")
        self.__F8 = Button(board_left, height=1, width=3, command=lambda: self.click((6,8)), bg="Olive Drab",anchor="sw")
        self.__F9 = Button(board_left, height=1, width=3, command=lambda: self.click((6,9)), bg="Olive Drab",anchor="sw")
        self.__F10= Button(board_left, height=1, width=3, command=lambda: self.click((6,10)), bg="Olive Drab",anchor="sw")
        self.__G1 = Button(board_left, height=1, width=3, command=lambda: self.click((7,1)), bg="Olive Drab",anchor="sw",text="G")
        self.__G2 = Button(board_left, height=1, width=3, command=lambda: self.click((7,2)), bg="Light Yellow",anchor="sw")
        self.__G3 = Button(board_left, height=1, width=3, command=lambda: self.click((7,3)), bg="Olive Drab",anchor="sw")
        self.__G4 = Button(board_left, height=1, width=3, command=lambda: self.click((7,4)), bg="Light Yellow",anchor="sw")
        self.__G5 = Button(board_left, height=1, width=3, command=lambda: self.click((7,5)), bg="Olive Drab",anchor="sw")
        self.__G6 = Button(board_left, height=1, width=3, command=lambda: self.click((7,6)), bg="Light Yellow",anchor="sw")
        self.__G7 = Button(board_left, height=1, width=3, command=lambda: self.click((7,7)), bg="Olive Drab",anchor="sw")
        self.__G8 = Button(board_left, height=1, width=3, command=lambda: self.click((7,8)), bg="Light Yellow",anchor="sw")
        self.__G9 = Button(board_left, height=1, width=3, command=lambda: self.click((7,9)), bg="Light Yellow",anchor="sw")
        self.__G10= Button(board_left, height=1, width=3, command=lambda: self.click((7,10)), bg="Light Yellow",anchor="sw")
        self.__H1 = Button(board_left, height=1, width=3, command=lambda: self.click((8,1)), bg="Light Yellow",anchor="sw",text="H")
        self.__H2 = Button(board_left, height=1, width=3, command=lambda: self.click((8,2)), bg="Olive Drab",anchor="sw")
        self.__H3 = Button(board_left, height=1, width=3, command=lambda: self.click((8,3)), bg="Light Yellow",anchor="sw")
        self.__H4 = Button(board_left, height=1, width=3, command=lambda: self.click((8,4)), bg="Olive Drab",anchor="sw")
        self.__H5 = Button(board_left, height=1, width=3, command=lambda: self.click(8,5), bg="Light Yellow",anchor="sw")
        self.__H6 = Button(board_left, height=1, width=3, command=lambda: self.click((8,6)), bg="Olive Drab",anchor="sw")
        self.__H7 = Button(board_left, height=1, width=3, command=lambda: self.click((8,7)), bg="Light Yellow",anchor="sw")
        self.__H8 = Button(board_left, height=1, width=3, command=lambda: self.click((8,8)), bg="Olive Drab",anchor="sw")
        self.__H9 = Button(board_left, height=1, width=3, command=lambda: self.click((8,9)), bg="Olive Drab",anchor="sw")
        self.__H10= Button(board_left, height=1, width=3, command=lambda: self.click((8,10)), bg="Olive Drab",anchor="sw")
        self.__I1 = Button(board_left, height=1, width=3, command=lambda: self.click((9,1)), bg="Olive Drab",anchor="sw")
        self.__I2 = Button(board_left, height=1, width=3, command=lambda: self.click((9,2)), bg="Olive Drab",anchor="sw")
        self.__I3 = Button(board_left, height=1, width=3, command=lambda: self.click((9,3)), bg="Olive Drab",anchor="sw")
        self.__I4 = Button(board_left, height=1, width=3, command=lambda: self.click((9,4)), bg="Olive Drab",anchor="sw")
        self.__I5 = Button(board_left, height=1, width=3, command=lambda: self.click((9,5)), bg="Olive Drab",anchor="sw")
        self.__I6 = Button(board_left, height=1, width=3, command=lambda: self.click((9,6)), bg="Olive Drab",anchor="sw")
        self.__I7 = Button(board_left, height=1, width=3, command=lambda: self.click((9,7)), bg="Olive Drab",anchor="sw")
        self.__I8 = Button(board_left, height=1, width=3, command=lambda: self.click((9,8)), bg="Olive Drab",anchor="sw")
        self.__I9 = Button(board_left, height=1, width=3, command=lambda: self.click((9,9)), bg="Olive Drab",anchor="sw")
        self.__I10= Button(board_left, height=1, width=3, command=lambda: self.click((9,10)), bg="Olive Drab",anchor="sw")
        self.__J1 = Button(board_left, height=1, width=3, command=lambda: self.click((10,1)), bg="Olive Drab",anchor="sw")
        self.__J2 = Button(board_left, height=1, width=3, command=lambda: self.click((10,2)), bg="Olive Drab",anchor="sw")
        self.__J3 = Button(board_left, height=1, width=3, command=lambda: self.click((10,3)), bg="Olive Drab",anchor="sw")
        self.__J4 = Button(board_left, height=1, width=3, command=lambda: self.click((10,4)), bg="Olive Drab",anchor="sw")
        self.__J5 = Button(board_left, height=1, width=3, command=lambda: self.click((10,5)), bg="Olive Drab",anchor="sw")
        self.__J6 = Button(board_left, height=1, width=3, command=lambda: self.click((10,6)), bg="Olive Drab",anchor="sw")
        self.__J7 = Button(board_left, height=1, width=3, command=lambda: self.click((10,7)), bg="Olive Drab",anchor="sw")
        self.__J8 = Button(board_left, height=1, width=3, command=lambda: self.click((10,8)), bg="Olive Drab",anchor="sw")
        self.__J9 = Button(board_left, height=1, width=3, command=lambda: self.click((10,9)), bg="Olive Drab",anchor="sw")
        self.__J10= Button(board_left, height=1, width=3, command=lambda: self.click((10,10)), bg="Olive Drab",anchor="sw")

        # Placeing buttons on board
        Alist = [self.__A1, self.__A2, self.__A3, self.__A4, self.__A5, self.__A6, self.__A7, self.__A8, self.__A9, self.__A10]
        Blist = [self.__B1, self.__B2, self.__B3, self.__B4, self.__B5, self.__B6, self.__B7, self.__B8, self.__B9, self.__B10]
        Clist = [self.__C1, self.__C2, self.__C3, self.__C4, self.__C5, self.__C6, self.__C7, self.__C8, self.__C9, self.__C10]
        Dlist = [self.__D1, self.__D2, self.__D3, self.__D4, self.__D5, self.__D6, self.__D7, self.__D8, self.__D9, self.__D10]
        Elist = [self.__E1, self.__E2, self.__E3, self.__E4, self.__E5, self.__E6, self.__E7, self.__E8, self.__E9, self.__E10]
        Flist = [self.__F1, self.__F2, self.__F3, self.__F4, self.__F5, self.__F6, self.__F7, self.__F8, self.__F9, self.__F10]
        Glist = [self.__G1, self.__G2, self.__G3, self.__G4, self.__G5, self.__G6, self.__G7, self.__G8, self.__G9, self.__G10]
        Hlist = [self.__H1, self.__H2, self.__H3, self.__H4, self.__H5, self.__H6, self.__H7, self.__H8, self.__H9, self.__H10]
        IList = [self.__I1, self.__I2, self.__I3, self.__I4, self.__I5, self.__I6, self.__I7, self.__I8, self.__I9, self.__I10]
        JList = [self.__J1, self.__J2, self.__J3, self.__J4, self.__J5, self.__J6, self.__J7, self.__J8, self.__J9, self.__J10]

        self.__list_of_columns_left = [Alist, Blist, Clist, Dlist, Elist, Flist, Glist, Hlist, IList, JList]

        self.place_buttons((self.__list_of_columns_left))

    def place_buttons(self, list_of_columns):
        for i in range(10):
            for j in range(10):
                list_of_columns[i][j].grid(row=i, column=j)

    def click(self,coordinate):
        self.__clicked_coords.append(coordinate)
        print("wybrano miejsce :", coordinate)

        """
        Sprawdzam na jakim etapie gry jestesmy. Jezeli nie ma statkow do ustawienia dla usera to nie wyskoczy blad.
        Poniewaz user nie moze zestrzeliwac swoich statkow a skoro wszystkie jez rozmiescil to nie ma powodu by tam klikac
        """

        if  self.us.get_ships_to_set():
            print("Ahoj kamracie. Dodaje statek!")
            # Sprawdzam ile wspolrzednych kliknieto. Jezeli dwie rozpoczynam proces dodawania
            if len(self.__clicked_coords) == 2:
                x1, y1 = self.__clicked_coords[0]
                x2, y2 = self.__clicked_coords[1]
                self.us.add_ship(x1, y1, x2, y2)

                # Czyszcze liste kliknietych wspolrzednych!
                self.__clicked_coords.clear()
                self.us.count_ships()
        else:
            print("Zwariowales? Nie mozesz zestrzelic swojego statku. Juz wszystkie ustawiles. Przejdz do gry lub zresetuj")


    def automatic_shooting_faze(self):

        #Part of choosing random coordinates
        #TODO usprawnic losowanie zeby nie losowal miejsc juz strzelanych
        #TODO Musi probowac zestrzelic statek do konca
        x, y = random.randint(1, 10), random.randint(1, 10)
        if self.pc.get_my_shots() &{(x,y)}:
            self.automatic_shooting_faze()  # Jeszcze raz strzelaj jezeli strzeliles  w to samo miejsce
        else:
            self.pc.add_shot((x,y))

        # Szukanie i usuwanie zestrzelonych pol/ statkow
        if self.pc.search_remove_coordinates(x, y):  # Jesli 0- trafiony/zatopiony; jesli 1- pudlo
            self.Faza_strzelanie_user()
        else:
            if self.us.get_list_of_ships():  # Jezeli lista statkow przeciwnika nie jest pusta
                self.automatic_shooting_faze()  # User ma kolejny ruch
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
            self.automatic_shooting_faze()
        else:
            if self.pc.get_list_of_ships():         #Jezeli lista statkow przeciwnika nie jest pusta
                self.Faza_strzelanie_user()         #User ma kolejny ruch
            else:
                self.EndGame(self.us.get_owner())           #W przeciwnym razie koniec gry User wygral


    def EndGame(self,name):
        print("Wygral: ",name)
        return

if __name__ == '__main__':
    # Creating root window
    root = Tk()
    x = InterfaceUser(root)
    root.mainloop()





