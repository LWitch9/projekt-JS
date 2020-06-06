from Functionality import *
import random
from tkinter import *
import time

class InterfaceUser():
    def __init__(self, master):

        self.__canvas = Canvas(master, height=600, width=900)
        self.__canvas.pack()

        # background
        self.__back_frame = Frame(master, bg='#00b3b3')
        self.__back_frame.place(relwidth=1,relheight=1)

        #Pole na komunikaty
        self.__frame_message = Frame(self.__back_frame, bg='black')
        self.__frame_message.place(x=90, y=60, width=720, height=60)

        #Label na komunikaty
        self.__label_message= Label(self.__frame_message,bg='grey')
        self.__label_message.pack(expand=True, fill=BOTH)

        # Pole planszy lewej
        self.__board_left = Frame(self.__back_frame, bg='black')
        self.__board_left.place(x=90, y=150, width=300, height=300)

        # Pole planszy prawej
        self.__board_right = Frame(self.__back_frame, bg='black')
        self.__board_right.place(x=510, y=150, width=300, height=300)

        #Ustawiam przyciski na planszach
        self.buttons_left(self.__board_left, 1, 3, "Light Yellow")
        self.buttons_right(self.__board_right, 1, 3, "Light Yellow")

        #Labes user
        self.__label_user= Label(self.__board_left,height=2, width=43,bg='grey',text='user')
        self.__label_user.grid(column=0,row=11,columnspan=10,rowspan=2)

        #Labes opponent
        self.__label_opponent= Label(self.__board_right,height=2, width=43,bg='grey',text='opponent')
        self.__label_opponent.grid(column=0,row=11,columnspan=10,rowspan=2)

        #Pole na reset gry
        self.__frame_reset = Frame(self.__back_frame, bg='black')
        self.__frame_reset.place(x=150, y=480, width=180, height=60)

        #Przycisk reset gry
        self.__button_reset = Button(self.__frame_reset, command=lambda: self.reset_game(), bg='grey', justify=CENTER,text="Reset")
        self.__button_reset.pack(expand=True, fill=BOTH)

        #Pole na start gry
        self.__frame_start = Frame(self.__back_frame, bg='black')
        self.__frame_start.place(x=570, y=480, width=180, height=60)

        #Przycisk start gry
        self.__button_start = Button(self.__frame_start, command=lambda: self.start_game(), bg='grey', justify=CENTER,text="Battle!")
        self.__button_start.pack(expand=True, fill=BOTH)

        #Tworze liste zbierajaca klikniecia
        self.__clicked_coords=[]

        #Tworze Przechowywalnie statkow dla 2 graczy (user, PC)
        self.__us = ShipsContainer("user")
        self.__pc=ShipsContainer("PC")

        #Wyswietlenie wiadomosci powitalnej
        self.display_message("Witaj w grze! Zacznij rozstawic statki.\n" + self.__us.show_ships_to_set())

    def buttons_left(self,board_left,h,w,color,):

        """ Wszystkie przyciski lewej planszy"""
        self.__A1 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((1, 1)), bg=color, anchor="sw", text="A1")
        self.__A2 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((1, 2)), bg=color, anchor="sw", text="2")
        self.__A3 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((1, 3)), bg=color, anchor="sw", text="3")
        self.__A4 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((1, 4)), bg=color, anchor="sw", text="4")
        self.__A5 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((1, 5)), bg=color, anchor="sw", text="5")
        self.__A6 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((1, 6)), bg=color, anchor="sw", text="6")
        self.__A7 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((1, 7)), bg=color, anchor="sw", text="7")
        self.__A8 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((1, 8)), bg=color, anchor="sw", text="8")
        self.__A9 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((1, 9)), bg=color, anchor="sw", text="9")
        self.__A10= Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((1, 10)), bg=color, anchor="sw", text="10")
        self.__B1 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((2, 1)), bg=color, anchor="sw", text="B")
        self.__B2 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((2, 2)), bg=color, anchor="sw")
        self.__B3 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((2, 3)), bg=color, anchor="sw")
        self.__B4 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((2, 4)), bg=color, anchor="sw")
        self.__B5 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((2, 5)), bg=color, anchor="sw")
        self.__B6 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((2, 6)), bg=color, anchor="sw")
        self.__B7 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((2, 7)), bg=color, anchor="sw")
        self.__B8 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((2, 8)), bg=color, anchor="sw")
        self.__B9 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((2, 9)), bg=color, anchor="sw")
        self.__B10= Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((2, 10)), bg=color, anchor="sw")
        self.__C1 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((3, 1)), bg=color, anchor="sw", text="C")
        self.__C2 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((3, 2)), bg=color, anchor="sw")
        self.__C3 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((3, 3)), bg=color, anchor="sw")
        self.__C4 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((3, 4)), bg=color, anchor="sw")
        self.__C5 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((3, 5)), bg=color, anchor="sw")
        self.__C6 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((3, 6)), bg=color, anchor="sw")
        self.__C7 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((3, 7)), bg=color, anchor="sw")
        self.__C8 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((3, 8)), bg=color, anchor="sw")
        self.__C9 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((3, 9)), bg=color, anchor="sw")
        self.__C10= Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((3, 10)), bg=color, anchor="sw")
        self.__D1 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((4, 1)), bg=color, anchor="sw", text="D")
        self.__D2 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((4, 2)), bg=color, anchor="sw")
        self.__D3 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((4, 3)), bg=color, anchor="sw")
        self.__D4 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((4, 4)), bg=color, anchor="sw")
        self.__D5 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((4, 5)), bg=color, anchor="sw")
        self.__D6 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((4, 6)), bg=color, anchor="sw")
        self.__D7 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((4, 7)), bg=color, anchor="sw")
        self.__D8 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((4, 8)), bg=color, anchor="sw")
        self.__D9 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((4, 9)), bg=color, anchor="sw")
        self.__D10= Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((4, 10)), bg=color, anchor="sw")
        self.__E1 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((5, 1)), bg=color, anchor="sw", text="E")
        self.__E2 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((5, 2)), bg=color, anchor="sw")
        self.__E3 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((5, 3)), bg=color, anchor="sw")
        self.__E4 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((5, 4)), bg=color, anchor="sw")
        self.__E5 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((5, 5)), bg=color, anchor="sw")
        self.__E6 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((5, 6)), bg=color, anchor="sw")
        self.__E7 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((5, 7)), bg=color, anchor="sw")
        self.__E8 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((5, 8)), bg=color, anchor="sw")
        self.__E9 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((5, 9)), bg=color, anchor="sw")
        self.__E10= Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((5, 10)), bg=color, anchor="sw")
        self.__F1 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((6, 1)), bg=color, anchor="sw", text="F")
        self.__F2 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((6, 2)), bg=color, anchor="sw")
        self.__F3 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((6, 3)), bg=color, anchor="sw")
        self.__F4 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((6, 4)), bg=color, anchor="sw")
        self.__F5 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((6, 5)), bg=color, anchor="sw")
        self.__F6 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((6, 6)), bg=color, anchor="sw")
        self.__F7 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((6, 7)), bg=color, anchor="sw")
        self.__F8 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((6, 8)), bg=color, anchor="sw")
        self.__F9 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((6, 9)), bg=color, anchor="sw")
        self.__F10= Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((6, 10)), bg=color, anchor="sw")
        self.__G1 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((7, 1)), bg=color, anchor="sw", text="G")
        self.__G2 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((7, 2)), bg=color, anchor="sw")
        self.__G3 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((7, 3)), bg=color, anchor="sw")
        self.__G4 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((7, 4)), bg=color, anchor="sw")
        self.__G5 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((7, 5)), bg=color, anchor="sw")
        self.__G6 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((7, 6)), bg=color, anchor="sw")
        self.__G7 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((7, 7)), bg=color, anchor="sw")
        self.__G8 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((7, 8)), bg=color, anchor="sw")
        self.__G9 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((7, 9)), bg=color, anchor="sw")
        self.__G10= Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((7, 10)), bg=color, anchor="sw")
        self.__H1 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((8, 1)), bg=color, anchor="sw", text="H")
        self.__H2 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((8, 2)), bg=color, anchor="sw")
        self.__H3 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((8, 3)), bg=color, anchor="sw")
        self.__H4 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((8, 4)), bg=color, anchor="sw")
        self.__H5 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((8, 5)), bg=color, anchor="sw")
        self.__H6 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((8, 6)), bg=color, anchor="sw")
        self.__H7 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((8, 7)), bg=color, anchor="sw")
        self.__H8 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((8, 8)), bg=color, anchor="sw")
        self.__H9 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((8, 9)), bg=color, anchor="sw")
        self.__H10= Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((8, 10)), bg=color, anchor="sw")
        self.__I1 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((9, 1)), bg=color, anchor="sw", text="I")
        self.__I2 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((9, 2)), bg=color, anchor="sw")
        self.__I3 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((9, 3)), bg=color, anchor="sw")
        self.__I4 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((9, 4)), bg=color, anchor="sw")
        self.__I5 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((9, 5)), bg=color, anchor="sw")
        self.__I6 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((9, 6)), bg=color, anchor="sw")
        self.__I7 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((9, 7)), bg=color, anchor="sw")
        self.__I8 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((9, 8)), bg=color, anchor="sw")
        self.__I9 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((9, 9)), bg=color, anchor="sw")
        self.__I10= Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((9, 10)), bg=color, anchor="sw")
        self.__J1 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((10, 1)), bg=color, anchor="sw", text="J")
        self.__J2 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((10, 2)), bg=color, anchor="sw")
        self.__J3 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((10, 3)), bg=color, anchor="sw")
        self.__J4 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((10, 4)), bg=color, anchor="sw")
        self.__J5 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((10, 5)), bg=color, anchor="sw")
        self.__J6 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((10, 6)), bg=color, anchor="sw")
        self.__J7 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((10, 7)), bg=color, anchor="sw")
        self.__J8 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((10, 8)), bg=color, anchor="sw")
        self.__J9 = Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((10, 9)), bg=color, anchor="sw")
        self.__J10= Button(board_left, height=h, width=w, command=lambda: self.set_up_ship((10, 10)), bg=color, anchor="sw")

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

    def buttons_right(self,board_right,h,w,color):

        """ Wszystkie przyciski prawej planszy"""
        self.__rA1 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((1, 1)), bg=color,anchor="sw", text="A1")
        self.__rA2 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((1, 2)), bg=color,anchor="sw", text="2")
        self.__rA3 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((1, 3)), bg=color,anchor="sw", text="3")
        self.__rA4 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((1, 4)), bg=color,anchor="sw", text="4")
        self.__rA5 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((1, 5)), bg=color,anchor="sw", text="5")
        self.__rA6 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((1, 6)), bg=color,anchor="sw", text="6")
        self.__rA7 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((1, 7)), bg=color,anchor="sw", text="7")
        self.__rA8 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((1, 8)), bg=color,anchor="sw", text="8")
        self.__rA9 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((1, 9)), bg=color,anchor="sw", text="9")
        self.__rA10 =Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((1, 10)), bg=color,anchor="sw", text="10")
        self.__rB1 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((2, 1)), bg=color, anchor="sw", text="B")
        self.__rB2 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((2, 2)), bg=color, anchor="sw")
        self.__rB3 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((2, 3)), bg=color,anchor="sw")
        self.__rB4 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((2, 4)), bg=color,anchor="sw")
        self.__rB5 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((2, 5)), bg=color,anchor="sw")
        self.__rB6 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((2, 6)), bg=color,anchor="sw")
        self.__rB7 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((2, 7)), bg=color, anchor="sw")
        self.__rB8 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((2, 8)), bg=color,anchor="sw")
        self.__rB9 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((2, 9)), bg=color,anchor="sw")
        self.__rB10 =Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((2, 10)), bg=color,anchor="sw")
        self.__rC1 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((3, 1)), bg=color,anchor="sw", text="C")
        self.__rC2 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((3, 2)), bg=color,anchor="sw")
        self.__rC3 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((3, 3)), bg=color,anchor="sw")
        self.__rC4 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((3, 4)), bg=color,anchor="sw")
        self.__rC5 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((3, 5)), bg=color,anchor="sw")
        self.__rC6 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((3, 6)), bg=color,anchor="sw")
        self.__rC7 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((3, 7)), bg=color,anchor="sw")
        self.__rC8 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((3, 8)), bg=color,anchor="sw")
        self.__rC9 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((3, 9)), bg=color,anchor="sw")
        self.__rC10 =Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((3, 10)), bg=color,anchor="sw")
        self.__rD1 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((4, 1)), bg=color,anchor="sw", text="D")
        self.__rD2 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((4, 2)), bg=color,anchor="sw")
        self.__rD3 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((4, 3)), bg=color,anchor="sw")
        self.__rD4 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((4, 4)), bg=color,anchor="sw")
        self.__rD5 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((4, 5)), bg=color,anchor="sw")
        self.__rD6 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((4, 6)), bg=color,anchor="sw")
        self.__rD7 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((4, 7)), bg=color,anchor="sw")
        self.__rD8 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((4, 8)), bg=color, anchor="sw")
        self.__rD9 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((4, 9)), bg=color,anchor="sw")
        self.__rD10 =Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((4, 10)), bg=color,anchor="sw")
        self.__rE1 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((5, 1)), bg=color,anchor="sw", text="E")
        self.__rE2 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((5, 2)), bg=color,anchor="sw")
        self.__rE3 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((5, 3)), bg=color,anchor="sw")
        self.__rE4 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((5, 4)), bg=color,anchor="sw")
        self.__rE5 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((5, 5)), bg=color,anchor="sw")
        self.__rE6 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((5, 6)), bg=color, anchor="sw")
        self.__rE7 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((5, 7)), bg=color,anchor="sw")
        self.__rE8 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((5, 8)), bg=color,anchor="sw")
        self.__rE9 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((5, 9)), bg=color,anchor="sw")
        self.__rE10 =Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((5, 10)), bg=color, anchor="sw")
        self.__rF1 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((6, 1)), bg=color,anchor="sw", text="F")
        self.__rF2 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((6, 2)), bg=color,anchor="sw")
        self.__rF3 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((6, 3)), bg=color,anchor="sw")
        self.__rF4 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((6, 4)), bg=color,anchor="sw")
        self.__rF5 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((6, 5)), bg=color,anchor="sw")
        self.__rF6 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((6, 6)), bg=color,anchor="sw")
        self.__rF7 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((6, 7)), bg=color,anchor="sw")
        self.__rF8 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((6, 8)), bg=color,anchor="sw")
        self.__rF9 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((6, 9)), bg=color, anchor="sw")
        self.__rF10 =Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((6, 10)), bg=color,anchor="sw")
        self.__rG1 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((7, 1)), bg=color,anchor="sw", text="G")
        self.__rG2 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((7, 2)), bg=color,anchor="sw")
        self.__rG3 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((7, 3)), bg=color,anchor="sw")
        self.__rG4 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((7, 4)), bg=color,anchor="sw")
        self.__rG5 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((7, 5)), bg=color,anchor="sw")
        self.__rG6 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((7, 6)), bg=color,anchor="sw")
        self.__rG7 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((7, 7)), bg=color,anchor="sw")
        self.__rG8 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((7, 8)), bg=color,anchor="sw")
        self.__rG9 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((7, 9)), bg=color,anchor="sw")
        self.__rG10= Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((7, 10)), bg=color,anchor="sw")
        self.__rH1 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((8, 1)), bg=color,anchor="sw", text="H")
        self.__rH2 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((8, 2)), bg=color,anchor="sw")
        self.__rH3 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((8, 3)), bg=color,anchor="sw")
        self.__rH4 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((8, 4)), bg=color,anchor="sw")
        self.__rH5 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((8, 5)), bg=color,anchor="sw")
        self.__rH6 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((8, 6)), bg=color,anchor="sw")
        self.__rH7 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((8, 7)), bg=color,anchor="sw")
        self.__rH8 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((8, 8)), bg=color,anchor="sw")
        self.__rH9 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((8, 9)), bg=color,anchor="sw")
        self.__rH10 =Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((8, 10)), bg=color, anchor="sw")
        self.__rI1 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((9, 1)), bg=color,anchor="sw", text="I")
        self.__rI2 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((9, 2)), bg=color,anchor="sw")
        self.__rI3 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((9, 3)), bg=color,anchor="sw")
        self.__rI4 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((9, 4)), bg=color,anchor="sw")
        self.__rI5 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((9, 5)), bg=color,anchor="sw")
        self.__rI6 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((9, 6)), bg=color,anchor="sw")
        self.__rI7 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((9, 7)), bg=color,anchor="sw")
        self.__rI8 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((9, 8)), bg=color,anchor="sw")
        self.__rI9 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((9, 9)), bg=color,anchor="sw")
        self.__rI10 =Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((9, 10)), bg=color,anchor="sw")
        self.__rJ1 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((10, 1)), bg=color,anchor="sw", text="J")
        self.__rJ2 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((10, 2)), bg=color,anchor="sw")
        self.__rJ3 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((10, 3)), bg=color,anchor="sw")
        self.__rJ4 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((10, 4)), bg=color,anchor="sw")
        self.__rJ5 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((10, 5)), bg=color,anchor="sw")
        self.__rJ6 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((10, 6)), bg=color,anchor="sw")
        self.__rJ7 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((10, 7)), bg=color,anchor="sw")
        self.__rJ8 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((10, 8)), bg=color,anchor="sw")
        self.__rJ9 = Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((10, 9)), bg=color,anchor="sw")
        self.__rJ10= Button(board_right, height=h, width=w, command=lambda: self.shoot_ship((10, 10)), bg=color,anchor="sw")

        # Placeing buttons on board
        Alist = [self.__rA1, self.__rA2, self.__rA3, self.__rA4, self.__rA5, self.__rA6, self.__rA7, self.__rA8, self.__rA9, self.__rA10]
        Blist = [self.__rB1, self.__rB2, self.__rB3, self.__rB4, self.__rB5, self.__rB6, self.__rB7, self.__rB8, self.__rB9, self.__rB10]
        Clist = [self.__rC1, self.__rC2, self.__rC3, self.__rC4, self.__rC5, self.__rC6, self.__rC7, self.__rC8, self.__rC9, self.__rC10]
        Dlist = [self.__rD1, self.__rD2, self.__rD3, self.__rD4, self.__rD5, self.__rD6, self.__rD7, self.__rD8, self.__rD9,  self.__rD10]
        Elist = [self.__rE1, self.__rE2, self.__rE3, self.__rE4, self.__rE5, self.__rE6, self.__rE7, self.__rE8, self.__rE9, self.__rE10]
        Flist = [self.__rF1, self.__rF2, self.__rF3, self.__rF4, self.__rF5, self.__rF6, self.__rF7, self.__rF8, self.__rF9, self.__rF10]
        Glist = [self.__rG1, self.__rG2, self.__rG3, self.__rG4, self.__rG5, self.__rG6, self.__rG7, self.__rG8, self.__rG9,self.__rG10]
        Hlist = [self.__rH1, self.__rH2, self.__rH3, self.__rH4, self.__rH5, self.__rH6, self.__rH7, self.__rH8, self.__rH9,self.__rH10]
        IList = [self.__rI1, self.__rI2, self.__rI3, self.__rI4, self.__rI5, self.__rI6, self.__rI7, self.__rI8, self.__rI9,self.__rI10]
        JList = [self.__rJ1, self.__rJ2, self.__rJ3, self.__rJ4, self.__rJ5, self.__rJ6, self.__rJ7, self.__rJ8, self.__rJ9,self.__rJ10]

        self.__list_of_columns_right = [Alist, Blist, Clist, Dlist, Elist, Flist, Glist, Hlist, IList, JList]

        self.place_buttons((self.__list_of_columns_right))

    def place_buttons(self, list_of_columns):
        for i in range(10):
            for j in range(10):
                list_of_columns[i][j].grid(row=j, column=i)
    """
    def change_state_color(self,list_of_columns, coor, color, state):
        # Ustawienie koloru i stanu przyciskow statku
        list_of_columns[coor[0] - 1][coor[1] - 1]['bg'] = color
        list_of_columns[coor[0] - 1][coor[1] - 1]['state'] = state

    def add_click(self,coordinate):
        x, y = coordinate
        self.__clicked_coords.append(coordinate)
    """

    def set_up_ship(self, coordinate):
        """
        Sprawdzam na jakim etapie gry jestesmy. Jezeli nie ma statkow do ustawienia dla usera to nie wyskoczy blad.
        Poniewaz user nie moze zestrzeliwac swoich statkow a skoro wszystkie jez rozmiescil to nie ma powodu by tam klikac
        """

        if  self.__us.get_ships_to_set():
            x, y = coordinate
            self.__clicked_coords.append(coordinate)
            self.display_message("wybrano miejsce :" + str(coordinate))

            # Sprawdzam ile wspolrzednych kliknieto. Jezeli dwie rozpoczynam proces dodawania
            if len(self.__clicked_coords) == 2:
                x1, y1 = self.__clicked_coords[0]
                x2, y2 = self.__clicked_coords[1]
                try:
                    self.__us.add_ship(x1, y1, x2, y2)
                except WrongOrientationException:
                    self.display_message("Statek moze byc ustawiony tylko w poziomie lub pionie\n" + self.__us.show_ships_to_set())
                except WrongLengthException:
                    self.display_message("Podana dlugosc statku nie odpowiada mozliwym do ustawienia\n" + self.__us.show_ships_to_set())
                except CoordinatesOutOfRangeException:
                    self.display_message("Plansza jest wymiarow 10 x 10! Podane wpolrzedne nie mieszcza sie w planszy\n" + self.__us.show_ships_to_set())
                except OccupiedException:
                    self.display_message("Juz tu cos jest\n" + self.__us.show_ships_to_set())
                else:
                    for coor in self.__us.get_list_of_ships()[-1].get_list_of_coordinates():
                        #Ustawienie koloru i stanu przyciskow statku
                        self.__list_of_columns_left[coor[0] - 1][coor[1] - 1]['bg'] = 'black'
                        self.__list_of_columns_left[coor[0] - 1][coor[1] - 1]['state'] = 'disabled'
                        self.display_message("Statek zostal ustawiony pomyslnie!\n" + self.__us.show_ships_to_set())

                # Czyszcze liste kliknietych wspolrzednych!
                self.__clicked_coords.clear()
                self.__us.count_ships()
        else:
            self.display_message("Zwariowales? Nie mozesz zestrzelic swojego statku. Juz wszystkie ustawiles. Przejdz do gry lub zresetuj")
            for i in self.__us.get_list_of_ships():
                print(i.get_list_of_coordinates())


    def start_game(self):

        if self.__us.get_ships_to_set():
            self.display_message("Najpierw musisz ustawic wszystkie statki")
            return
        #Jezeli PC posiad jakies statki oznacza to ze jest w trakcie gry wiec nie mozna jej ropoczac
        elif self.__pc.get_list_of_ships():
            self.display_message("Jestes juz w trakcje pojedynku")
            return

        self.display_message("Rozpoczynam gre... Twoj przeciwnik rozstawia statki")
        self.__pc.automatic_set_up()
        #Losuje ktory gracz pierwszy
        if random.randint(0,1):
            #Zaczyna Przeciwnik (PC)
            #self.__us.__setattr__("turn", False)
            #self.auto_shoot()
            pass
        else:
            #Zaczyna user (us)
            self.__us.__setattr__("turn", True)

    def reset_game(self):
        self.display_message("Resetuje gre...")

        self.__pc.initial_state()
        self.__us.initial_state()
        #Resetuje plansze
        for i in self.__list_of_columns_left:
            for j in range(10):
                # Ustawienie koloru i stanu przyciskow statku
                i[j]['bg'] = 'white'
                i[j]['state'] = 'normal'

        for i in self.__list_of_columns_right:
            for j in range(10):
                # Ustawienie koloru i stanu przyciskow statku
                i[j]['bg'] = 'white'
                i[j]['state'] = 'normal'

    def display_message(self, message):
        self.__label_message["text"] = message

    def auto_shoot(self):

        #Part of choosing random coordinates
        #TODO usprawnic losowanie zeby nie losowal miejsc juz strzelanych
        #TODO Musi probowac zestrzelic statek do konca
        x, y = random.randint(1, 10), random.randint(1, 10)
        if self.__pc.get_my_shots() &{(x, y)}:
            self.auto_shoot()  # Jeszcze raz strzelaj jezeli strzeliles  w to samo miejsce
        else:
            self.__pc.add_shot((x, y))
            print(x,y)
            # Szukanie i usuwanie zestrzelonych pol/ statkow
            if not self.__us.search_remove_coordinates(x, y):  # Jesli 0- trafiony/zatopiony; jesli 1- pudlo
                self.__list_of_columns_left[x - 1][y - 1]['bg'] = 'blue'
                self.__list_of_columns_left[x - 1][y - 1]['state'] = 'disabled'

                self.__us.__setattr__("turn", True)
                self.display_message("Twoja kolej")
                return
            else:
                print("pc", self.__us.get_list_of_ships())
                self.__list_of_columns_left[x - 1][y - 1]['bg'] = 'red'
                self.__list_of_columns_left[x - 1][y - 1]['state'] = 'disabled'

                if self.__us.get_list_of_ships():  # Jezeli lista statkow przeciwnika nie jest pusta
                    self.auto_shoot()  # Opponent ma kolejny ruch

                else:
                    self.__us.__setattr__("turn", False)
                    self.EndGame(self.__pc.get_owner())  # W przeciwnym razie koniec gry User wygral

    def shoot_ship(self,coordinate):

        """
        Jezeli ships_to_set jest pelna (PC nie ustawil jeszcze swoich statkow)
        oraz zmienna turn nie zostala ustawiona to nie mozna strzelic
        """
        if self.__pc.get_ships_to_set() and not hasattr(self.__us, "turn") :
            self.display_message("Spokojnie jeszcze nie czas. Najpierw rozpocznij gre i daj przeciwnikowi ustawic statki")

        elif not self.__us.turn:
            self.display_message("Badz cierpliwy. Teraz nie jest twoja kolej")
        else:
            x,y=coordinate
            # Po wykonaniu strzalu zostaje on zapisany do zbioru my shots!!!!
            if self.__us.get_my_shots() & {(x, y)}:
                self.display_message("Tu juz strzelales! wspolrzedne: "+str((x,y)))
                return #Wyjdz z funkcji jesli juz strzeliles w to miejsce by moc znowu sprobowac
            else:
                self.__us.add_shot((x, y))
                try:
                    self.__pc.search_remove_coordinates(x, y)  # Jesli 1/2- trafiony/zatopiony; jesli 0- pudlo
                except MissedException:
                    # Ustawienie koloru i stanu przycisku - niebieski pudlo
                    self.__list_of_columns_right[x - 1][y - 1]['bg'] = 'blue'
                    self.__list_of_columns_right[x - 1][y - 1]['state'] = 'disabled'

                    self.display_message("Pudlo! Kolej przeciwnika!")
                    # Ustawiam atrybuut turn ( user -false przeciwnik -true)
                    self.__us.__setattr__("turn", False)
                    self.auto_shoot()
                except ShootingShipException as ex:
                    print("user: ", self.__pc.get_list_of_ships())
                    # Ustawienie koloru i stanu przycisku - niebieski pudlo
                    self.__list_of_columns_right[x - 1][y - 1]['bg'] = 'red'
                    self.__list_of_columns_right[x - 1][y - 1]['state'] = 'disabled'
                    if ex == HitException:
                        self.display_message("Trafiony! Probuj dalej")
                    else:
                        self.display_message("Zatopiony! Probuj dalej")

                    #Sprawdzam czy koniec gry
                    if self.__pc.get_list_of_ships():  # Jezeli lista statkow przeciwnika nie jest pusta
                        # Uzytkownik nadal ma swoja kolej
                        pass
                    else:
                        self.__us.__setattr__("turn", False)
                        self.EndGame(self.__us.get_owner())  # W przeciwnym razie koniec gry User wygral


    def EndGame(self,name):
        self.display_message("Wygral: "+name)
        return

if __name__ == '__main__':
    # Creating root window
    root = Tk()
    x = InterfaceUser(root)

    root.mainloop()





