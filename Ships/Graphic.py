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


#relative (relwidth,relheight) -sprawiaja ze rozmiar zmienia się relatywnie

#Pole komunikatu
frame = Frame(back_frame, bg='#03fc90')
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)  #place it in the root ( podaje dokladne wymiary gdzie ma sie znajdowac)

#Pole planszy lewej
board_left = Frame(back_frame, bg='#03fc90')
board_left.place(relx=0.1,rely=0.25,relwidth=(10./27),relheight=0.5)

#Pole planszy prawej
"""
board_right = Frame(back_frame, bg='black')
board_right.place(relx=0.55,rely=0.25,relwidth=(10./27),relheight=0.5)
"""



root.mainloop()

"""
Pojecia
root - whole window
frame - pewna wyznaczona w nim przestrzec (moze cajmowac cale okno lub nie)
Entry - widget for input
Label - widget for label ( just to show text)

pack(), grid(), place()
"""