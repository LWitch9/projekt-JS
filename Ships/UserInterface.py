import Functionality as f


class InterfaceUser():
    def __init__(self):
        """
        Tworzy:
        1. Wygląd interface (wyswietla dwie plansze i przycinski)
        przechowalnie statkow dla uzytkownika i dla komputera ???
        """
        self.us = f.ShipsContainer("user")
    #def Gra(self):
        """

        :return:
        """
    def Faza_rozmieszcanie(self):
        """
        :return:
        """
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
                self.us.podglad_statkow()
            else:
                self.us.add_ship(x, y)
            print("Chcesz dodac statek:")
            x = int(input("1/0: "))
   # def Faza_strzelanie(self):
        """

        :return:
        """
if __name__ == '__main__':
    x= InterfaceUser()
    x.Faza_rozmieszcanie()