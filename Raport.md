# Raport
## Narzędzia
Korzystałam ze środowiska programistycznego PyCharm.
Do tworzenia GUI wykorzystałam bibliotekę TkInter
## Założenia programowe
Celem projektu było zrealizowanie popularnej gry w Statki według opisu opis_Okręty.
Gra miała odbywać się między użytkownikiem a komputerem. Należało zatem zaimplementować odpowiednią sztuczną inteligencje dla komputera tak aby rozgrywka przebiegała jak między dwoma niezależnymi graczami.

## Budowa
Program został rozdzielony na trzy pliki: UserInterface, Functionality oraz Exceptions. Całą funkcjonalność programu starałam się zawrzeć w pliku Functionality. Główną klasą odpowiadającą za logikę jest klasa ShipsContainer która pełni rolę swego rodzaju planszy/ kontenera na statki. Zajmuje się ona wszelkimi operacjami związanymi z umieszczaniem Statków, szukaniem ich współrzędnych po zestrzeleniu oraz usuwaniem. Posiada również metody gwarantujące losowe rozstawianie statków oraz ich zestrzeliwanie (które gwarantuje próbę zestrzelenie trafionego statku do końca oraz omijanie pól , które na pewno nie mogą być zajęte przez statki). Każdy z graczy posiadać będzie swój własny obiekt tylko ShipContainer. Statki reprezentowane są natomiast przez klasę Ships która przechowuje współrzędne danego statku.
Klasa UserInterface odopwiada za stworzenie GUI oraz jego obsługę. Zawiera przyciski odpowiadające każdemu polu plansz, oraz te odpowiadające za rozpoczęcie i reset gry. Są one połaćzone z odpowiadającymi im metodami. W tej klasie tworzoen są również obiekty ShipsContainer dla obu graczy na których będzie się operować w trakcie gry. Używając przycisków w celu dodania/zestrzelnia statku , zresetowania gry lub jej rozpoczęcia wyświetlone zostaną komunikaty na górnej etykiecie informujące o przebiegu działania. Metody związane dodawaniem i zestrzeleniem statku używane są w bloku try ponieważ resultaty związane z tymi działaniami mogą rzucać wyjątki które zostały stworzone w module Exceptions.

## Realizacja
Uważam, że udało misię zrealizować wszystkie elementy według opisu projektu. Graficzny interface posiada wszystkie elementy pozwalające na płynne przejścia w grze. Uzytkownik rozmieszcza swoje statki na planszy przycisków gdzie w razie nieprawidłowości wyświetlane są odpowiednie komunikaty aby mógł skorygować ustawienie. Kiedy wszystkie statki są ustawione uzytkownik klikając w swoje pole otrzymuje informacje, że czas rozpocząć grę. Klikając przycisk Komputer (w sposób losowy) rozmieszcza statki i w zależności od wyniku losowania on albo użytkownik może rozpocząć strzelanie. Zakończenie gry sygnalizowane jest komunikatem wyświetlonym w okienku informacyjnym. Po jego zamknięciu (jeżeli przegraliśmy) na planszy pojawiają się pozostałe statki oponenta , tak żebyśmy mogli zobaczyć które pominęliśmy. Naciskanie przycisków którejkolwiek z plansz skutkuje jedynie wyświetleniem komunikatów. W celu rozpoczęcia ponownej rozgrywki wystarczy kliknąć reset. 
## Napotkane problemy
Największy problem sprawiła mi prawdopodobnie organizacja programu tak aby rozdzielić funkcjonalność od interface. Wydaje mi sie że poradziałam sobie jednak z tym problemem w miarę możliwości. Kolejnym aspektem była sztuczna inteligencja oponenta. Automatyczne rozstawianie statków czasami powodowało wykonywanie się pętli w nieskończoność. Jednak odkąd usprawniłam tą metodę nie napotkałam tego problemu. Również inteligentne zestrzeliwanie statków było problematyczne. Początkowo przeciwnik robił to całkowicie losowo. Aby usprawnić tą metodę potrzebowałam kolejnej listy przechowującej zestrzelone statki i pare metod z nią związanych. Dzięki temu jeżeli jakiś statek nie został jeszcze zatopiony ale został trafiony zwracany jest zbiór współrzędnych sugerujący położenie jego kolejnych pól.
## Linki do istotnych fragmentów kodu
### a. Lambda-wyrażenia 
- [Obsługa przycisków lewej planszy](https://github.com/LWitch9/projektJS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/UserInterface.py#L174)
- [Obsługa przycisków prawej planszy](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/UserInterface.py#L299)
### b. List Comprehensions
- [Tworzenie listy do losowania współrzędnych przy strzelaniu](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/UserInterface.py#L542)
- [Tworzenie listy współrzędnych statku poziomego](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/Functionality.py#L52)
- [Tworzenie listy współrzędnych statku poziomego](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/Functionality.py#L56)
- [Tworzy listę niechcianych współrzędnych przy ustawianiu statków](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/Functionality.py#L372)
### c. Klasy
- [Odpowiedzialna za funkcjonalność programu](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/Functionality.py#L117)
- [Odpowiedzialność za interface](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/UserInterface.py#L6)
### d. Wyjątki
Dodawanie statku
- [Klasy wyjątków dodawania](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/Exceptions.py#L1)
- [Rzucanie wyjątku CoordinatesOutOfRangeException](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/Functionality.py#L293)
- [Rzucanie wyjątku WrongOrientationException](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/Functionality.py#L297)
- [Rzucanie wyjątku OccupiedException](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/Functionality.py#L315)
- [Rzucanie wyjątku WrongLengthException](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/Functionality.py#L323)
- [Użycie bloku try](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/UserInterface.py#L455)

Strzelanie do statku
- [Klasy wyjątków strzelania](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/Exceptions.py#L18)
- [Rzucanie wyjątku HitException](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/Functionality.py#L344)
- [Rzucanie wyjątku MissedException](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/Functionality.py#L348)
- [Użycie bloku try w strzelaniu automatycznym](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/UserInterface.py#L549)
- [Użycie bloku try w strzelaniu użytkownika](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/UserInterface.py#L600)

### e. Moduły
- [Moduł Exceptions: import](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/Functionality.py#L3)
- [Moduł Functionality: import](https://github.com/LWitch9/projekt-JS/blob/536a8674939cfc14843cdd46f0d792640c53b035/Ships/UserInterface.py#L1)
