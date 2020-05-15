from tkinter import *
#Pillow package for uploading images

HEIGHT = 600
WIDTH =900

root = Tk()    #create root window

canvas = Canvas(root, height=HEIGHT, width=WIDTH)       #domyślny rozmiar
canvas.pack() #pack it in the root

#background
back_frame = Frame(root, bg='green')
back_frame.place(relwidth=1,relheight=1) #place it in the root ( podaje dokladne wymiary gdzie ma sie znajdowac)




#Pole komunikatu
frame = Frame(back_frame, bg='Olive Drab')
frame.place(x=90,y=60,width=720,height=60)  #place it in the root ( podaje dokladne wymiary gdzie ma sie znajdowac)

#Pole planszy lewej
board_left = Frame(back_frame, bg='black')
board_left.place(x=90,y=150,width=300,height=300)

button=Button(board_left, text="A1", bg='gray', fg='black')  #create button

squares = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","B1","B2","B3","B4","B5","B6","B7","B8","C1","C2","C3","C4","C5","C6","C7","C8","D1","D2","D3","D4","D5","D6","D7","D8","E1","E2","E3","E4","E5","E6","E7","E8","F1","F2","F3","F4","F5","F6","F7","F8","G1","G2","G3","G4","G5","G6","G7","G8","H1","H2","H3","H4","H5","H6","H7","H8"]
A1 = Button(board_left, height = 1, width = 3, command = lambda: click("A1"), bg ="Olive Drab", anchor ="sw", text ="A1")
A2 = Button(board_left, height = 1, width = 3, command = lambda: click("A2"), bg ="Light Yellow", anchor ="sw", text ="2")
A3 = Button(board_left, height = 1, width = 3, command = lambda: click("A3"), bg ="Olive Drab", anchor ="sw", text ="3")
A4 = Button(board_left, height = 1, width = 3, command = lambda: click("A4"), bg ="Light Yellow", anchor ="sw", text ="4")
A5 = Button(board_left, height = 1, width = 3, command = lambda: click("A5"), bg ="Olive Drab", anchor ="sw", text ="5")
A6 = Button(board_left, height = 1, width = 3, command = lambda: click("A6"), bg ="Light Yellow", anchor ="sw", text ="6")
A7 = Button(board_left, height = 1, width = 3, command = lambda: click("A7"), bg ="Olive Drab", anchor ="sw", text ="7")
A8 = Button(board_left, height = 1, width = 3, command = lambda: click("A8"), bg ="Light Yellow", anchor ="sw", text ="8")
A9 = Button(board_left, height = 1, width = 3, command = lambda: click("A9"), bg ="Olive Drab", anchor ="sw", text ="9")
A10= Button(board_left, height = 1, width = 3, command = lambda: click("A10"), bg ="Light Yellow", anchor ="sw", text ="10")
B1 = Button(board_left, height = 1, width = 3, command = lambda: click("B1"), bg ="Light Yellow", anchor ="sw", text ="B")
B2 = Button(board_left, height = 1, width = 3, command = lambda: click("B2"), bg ="Olive Drab", anchor ="sw")
B3 = Button(board_left, height = 1, width = 3, command = lambda: click("B3"), bg ="Light Yellow", anchor ="sw")
B4 = Button(board_left, height = 1, width = 3, command = lambda: click("B4"), bg ="Olive Drab", anchor ="sw")
B5 = Button(board_left, height = 1, width = 3, command = lambda: click("B5"), bg ="Light Yellow", anchor ="sw")
B6 = Button(board_left, height = 1, width = 3, command = lambda: click("B6"), bg ="Olive Drab", anchor ="sw")
B7 = Button(board_left, height = 1, width = 3, command = lambda: click("B7"), bg ="Light Yellow", anchor ="sw")
B8 = Button(board_left, height = 1, width = 3, command = lambda: click("B8"), bg ="Olive Drab", anchor ="sw")
B9 = Button(board_left, height = 1, width = 3, command = lambda: click("B8"), bg ="Olive Drab", anchor ="sw")
B10= Button(board_left, height = 1, width = 3, command = lambda: click("B8"), bg ="Olive Drab", anchor ="sw")
C1 = Button(board_left, height = 1, width = 3, command = lambda: click("C1"), bg ="Olive Drab", anchor ="sw", text ="C")
C2 = Button(board_left, height = 1, width = 3, command = lambda: click("C2"), bg ="Light Yellow", anchor ="sw")
C3 = Button(board_left, height = 1, width = 3, command = lambda: click("C3"), bg ="Olive Drab", anchor ="sw")
C4 = Button(board_left, height = 1, width = 3, command = lambda: click("C4"), bg ="Light Yellow", anchor ="sw")
C5 = Button(board_left, height = 1, width = 3, command = lambda: click("C5"), bg ="Olive Drab", anchor ="sw")
C6 = Button(board_left, height = 1, width = 3, command = lambda: click("C6"), bg ="Light Yellow", anchor ="sw")
C7 = Button(board_left, height = 1, width = 3, command = lambda: click("C7"), bg ="Olive Drab", anchor ="sw")
C8 = Button(board_left, height = 1, width = 3, command = lambda: click("C8"), bg ="Light Yellow", anchor ="sw")
C9 = Button(board_left, height = 1, width = 3, command = lambda: click("C8"), bg ="Light Yellow", anchor ="sw")
C10= Button(board_left, height = 1, width = 3, command = lambda: click("C8"), bg ="Light Yellow", anchor ="sw")
D1 = Button(board_left, height = 1, width = 3, command = lambda: click("D1"), bg ="Light Yellow", anchor ="sw", text ="D")
D2 = Button(board_left, height = 1, width = 3, command = lambda: click("D2"), bg ="Olive Drab", anchor ="sw")
D3 = Button(board_left, height = 1, width = 3, command = lambda: click("D3"), bg ="Light Yellow", anchor ="sw")
D4 = Button(board_left, height = 1, width = 3, command = lambda: click("D4"), bg ="Olive Drab", anchor ="sw")
D5 = Button(board_left, height = 1, width = 3, command = lambda: click("D5"), bg ="Light Yellow", anchor ="sw")
D6 = Button(board_left, height = 1, width = 3, command = lambda: click("D6"), bg ="Olive Drab", anchor ="sw")
D7 = Button(board_left, height = 1, width = 3, command = lambda: click("D7"), bg ="Light Yellow", anchor ="sw")
D8 = Button(board_left, height = 1, width = 3, command = lambda: click("D8"), bg ="Olive Drab", anchor ="sw")
D9 = Button(board_left, height = 1, width = 3, command = lambda: click("D8"), bg ="Olive Drab", anchor ="sw")
D10= Button(board_left, height = 1, width = 3, command = lambda: click("D8"), bg ="Olive Drab", anchor ="sw")
E1 = Button(board_left, height = 1, width = 3, command = lambda: click("E1"), bg ="Olive Drab", anchor ="sw", text ="E")
E2 = Button(board_left, height = 1, width = 3, command = lambda: click("E2"), bg ="Light Yellow", anchor ="sw")
E3 = Button(board_left, height = 1, width = 3, command = lambda: click("E3"), bg ="Olive Drab", anchor ="sw")
E4 = Button(board_left, height = 1, width = 3, command = lambda: click("E4"), bg ="Light Yellow", anchor ="sw")
E5 = Button(board_left, height = 1, width = 3, command = lambda: click("E5"), bg ="Olive Drab", anchor ="sw")
E6 = Button(board_left, height = 1, width = 3, command = lambda: click("E6"), bg ="Light Yellow", anchor ="sw")
E7 = Button(board_left, height = 1, width = 3, command = lambda: click("E7"), bg ="Olive Drab", anchor ="sw")
E8 = Button(board_left, height = 1, width = 3, command = lambda: click("E8"), bg ="Light Yellow", anchor ="sw")
E9 = Button(board_left, height = 1, width = 3, command = lambda: click("E8"), bg ="Light Yellow", anchor ="sw")
E10= Button(board_left, height = 1, width = 3, command = lambda: click("E8"), bg ="Light Yellow", anchor ="sw")
F1 = Button(board_left, height = 1, width = 3, command = lambda: click("F1"), bg ="Light Yellow", anchor ="sw", text ="F")
F2 = Button(board_left, height = 1, width = 3, command = lambda: click("F2"), bg ="Olive Drab", anchor ="sw")
F3 = Button(board_left, height = 1, width = 3, command = lambda: click("F3"), bg ="Light Yellow", anchor ="sw")
F4 = Button(board_left, height = 1, width = 3, command = lambda: click("F4"), bg ="Olive Drab", anchor ="sw")
F5 = Button(board_left, height = 1, width = 3, command = lambda: click("F5"), bg ="Light Yellow", anchor ="sw")
F6 = Button(board_left, height = 1, width = 3, command = lambda: click("F6"), bg ="Olive Drab", anchor ="sw")
F7 = Button(board_left, height = 1, width = 3, command = lambda: click("F7"), bg ="Light Yellow", anchor ="sw")
F8 = Button(board_left, height = 1, width = 3, command = lambda: click("F8"), bg ="Olive Drab", anchor ="sw")
F9 = Button(board_left, height = 1, width = 3, command = lambda: click("F8"), bg ="Olive Drab", anchor ="sw")
F10= Button(board_left, height = 1, width = 3, command = lambda: click("F8"), bg ="Olive Drab", anchor ="sw")
G1 = Button(board_left, height = 1, width = 3, command = lambda: click("G1"), bg ="Olive Drab", anchor ="sw", text ="G")
G2 = Button(board_left, height = 1, width = 3, command = lambda: click("G2"), bg ="Light Yellow", anchor ="sw")
G3 = Button(board_left, height = 1, width = 3, command = lambda: click("G3"), bg ="Olive Drab", anchor ="sw")
G4 = Button(board_left, height = 1, width = 3, command = lambda: click("G4"), bg ="Light Yellow", anchor ="sw")
G5 = Button(board_left, height = 1, width = 3, command = lambda: click("G5"), bg ="Olive Drab", anchor ="sw")
G6 = Button(board_left, height = 1, width = 3, command = lambda: click("G6"), bg ="Light Yellow", anchor ="sw")
G7 = Button(board_left, height = 1, width = 3, command = lambda: click("G7"), bg ="Olive Drab", anchor ="sw")
G8 = Button(board_left, height = 1, width = 3, command = lambda: click("G8"), bg ="Light Yellow", anchor ="sw")
G9 = Button(board_left, height = 1, width = 3, command = lambda: click("G8"), bg ="Light Yellow", anchor ="sw")
G10= Button(board_left, height = 1, width = 3, command = lambda: click("G8"), bg ="Light Yellow", anchor ="sw")
H1 = Button(board_left, height = 1, width = 3, command = lambda: click("H1"), bg ="Light Yellow", anchor ="sw", text ="H")
H2 = Button(board_left, height = 1, width = 3, command = lambda: click("H2"), bg ="Olive Drab", anchor ="sw")
H3 = Button(board_left, height = 1, width = 3, command = lambda: click("H3"), bg ="Light Yellow", anchor ="sw")
H4 = Button(board_left, height = 1, width = 3, command = lambda: click("H4"), bg ="Olive Drab", anchor ="sw")
H5 = Button(board_left, height = 1, width = 3, command = lambda: click("H5"), bg ="Light Yellow", anchor ="sw")
H6 = Button(board_left, height = 1, width = 3, command = lambda: click("H6"), bg ="Olive Drab", anchor ="sw")
H7 = Button(board_left, height = 1, width = 3, command = lambda: click("H7"), bg ="Light Yellow", anchor ="sw")
H8 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
H9 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
H10= Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
I1 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
I2 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
I3 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
I4 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
I5 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
I6 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
I7 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
I8 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
I9 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
I10= Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
J1 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
J2 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
J3 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
J4 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
J5 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
J6 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
J7 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
J8 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
J9 = Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")
J10= Button(board_left, height = 1, width = 3, command = lambda: click("H8"), bg ="Olive Drab", anchor ="sw")

Alist = [A1,A2,A3,A4,A5,A6,A7,A8,A9,A10]
Blist = [B1,B2,B3,B4,B5,B6,B7,B8,B9,B10]
Clist = [C1,C2,C3,C4,C5,C6,C7,C8,C9,C10]
Dlist = [D1,D2,D3,D4,D5,D6,D7,D8,D9,D10]
Elist = [E1,E2,E3,E4,E5,E6,E7,E8,E9,E10]
Flist = [F1,F2,F3,F4,F5,F6,F7,F8,F9,F10]
Glist = [G1,G2,G3,G4,G5,G6,G7,G8,G9,G10]
Hlist = [H1,H2,H3,H4,H5,H6,H7,H8,H9,H10]
IList = [I1,I2,I3,I4,I5,I6,I7,I8,I9,I10]
JList = [J1,J2,J3,J4,J5,J6,J7,J8,J9,J10]

list_of_columns = [Alist, Blist, Clist, Dlist, Elist, Flist, Glist, Hlist, IList, JList]


#place the buttons in a grid layout
for i in range(10):
	for j in range(10):
		list_of_columns[i][j].grid(row=10 - j, column=i)

def click(square):
    print("what")
#Pole planszy prawej

board_right = Frame(back_frame, bg='black')
board_right.place(x=510,y=150,width=300,height=300)





root.mainloop()

"""
Pojecia
root - whole window
frame - pewna wyznaczona w nim przestrzec (moze cajmowac cale okno lub nie)
Entry - widget for input
Label - widget for label ( just to show text)

#relative (relwidth,relheight) -sprawiaja ze rozmiar zmienia się relatywnie
pack(), grid(), place()
"""