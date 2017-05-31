#-*- coding: utf-8 -*-
import os

#--------------------------------------- Funkcja wyboru podciągnięć

def podciagniecia():

	print("Podczas podciągania pracujemy jedynie rękoma. Reszta ciała powinna pozostawać w stanie nieruchomym. Machanie nogami, podrzucanie ich do góry tuż przed podciągnięciem i inne techniki na dociąganie są błędnę i powodują, że trening jest mniej efektywny ! Aby prawidłowo wykonać podciąganie na drążku skup się na tych kilku elementach: \n\
\n\
* Ręce miej wyprostowane do końca a głowę trzymaj w jednej lini z osią ciała.\n\
* Podciągnięcie wykonuj jednym, płynnym ruchem.\n\
* Podczas podciągania utrzymuj stałą pozycję. Nie bujaj się i nie szarp.\n\
* Ciało prowadź jak najbliżej drążka.\n\
* Podciąganie na drążku to ruch z pełnego zwisu, aż do momentu, gdy broda znajdzie się na wysokości drążka.\n\
* Opuść się do wyprostowanych rąk.\n")
	liczba_powtorzen = int(input("Spróbuj wykonać jak najwięcej podciągnięć i podaj ilość: "))
	if liczba_powtorzen > 20:
		os.system("clear")
		print("Gratulację ! Udało Ci się zrobić powyżej 20 powtórzeń !\n\
Twój następny trening wygląda następująco: \n\
\n\
I seria: 15 podciągnięć\n\
II seria: 17 podciągnięć\n\
III seria: 19 podciągnięć\n\
IV seria: 16 podciągnięć\n\
V seria: 18 podciągnięć\n\
VI seria: 20 podciągnięć\n\
\nPowodzenia !")
	elif liczba_powtorzen < 20:
		os.system("clear")
		print ("Nie udało Ci się przekroczyć progu 20 powtórzeń, ale się nie załamuj ! Trenuj ciężko, w pełnym skupieniu !\n\
\n\
Twój następny trening wygląda następująco: \n\
\n\
I seria: 5 podciągnięć\n\
II seria: 7 podciągnięć\n\
III seria: 9 podciągnięć\n\
IV seria: 6 podciągnięć\n\
V seria: 8 podciągnięć\n\
VI seria: 10 podciągnięć\n\
\nPowodzenia !")

#--------------------------------------- Funkcja wyboru brzuszków

def brzuszki ():
	print("Brzuszki to jedne z najpopularniejszych ćwiczeń. Istnieje kilka rodzajów brzuszków jednak tutaj, zajmiemy się brzuszkami klasycznymi. Zatem do dzieła !\n\
\n\
* Połóż się na plecach (najlepiej na czymś średnio miękkim\n\
* Nogi ugnij w kolanach a stopy oprzyj na podłodze.\n\
* Dłonie umieść za głową, lecz nie spalataj ich i nie chwytaj za głowę.\n\
* Rozszerz łokcie i patrz przed siebie.\n\
* Napnij brzuch, zrób głęboki wdech, a następnie na wydech unieś łopatki kilka centrymetrów nad ziemię.\n\
* Przy maksymalnym spięciu mięśni brzucha, przytrzymaj ruch na 1 sekundę po czym z wdechem opuść tułów do pozycji leżącej.\n")
	liczba_powtorzen = int(input("Spróbuj wykonać jak najwięcej brzuszków i podaj ilość: "))
	if liczba_powtorzen > 20:
		os.system("clear")
		print("Gratulację ! Udało Ci się zrobić powyżej 20 powtórzeń !\n\
Twój następny trening wygląda następująco: \n\
\n\
I seria: 15 brzuszków\n\
II seria: 17 brzuszków\n\
III seria: 19 brzuszków\n\
IV seria: 16 brzuszków\n\
V seria: 18 brzuszków\n\
VI seria: 20 brzuszków\n\
\nPowodzenia !")
	elif liczba_powtorzen < 20:
		os.system("clear")
		print ("Nie udało Ci się przekroczyć progu 20 powtórzeń, ale się nie załamuj ! Trenuj ciężko, w pełnym skupieniu !\n\
\n\
Twój następny trening wygląda następująco: \n\
\n\
I seria: 5 brzuszków\n\
II seria: 7 brzuszków\n\
III seria: 9 brzuszków\n\
IV seria: 6 brzuszków\n\
V seria: 8 brzuszków\n\
VI seria: 10 brzuszków\n\
\nPowodzenia !")


#------------------------------------ Funkcja wyboru przysiadów

def przysiady():
	print("Aby prawidłowo wykonywać przysiady, potrzebna jest znajomość techniki. Źle robione mogą skutkować przeciążeniem stawów kolanowych, nadwyrężeniem kręgosłupa czy nawet bolesną kontuzją.\n\
\n\
Aby prawidłowo wykonać przysiad należy: \n\
\n\
* Stanąc prosto w lekkim rozkroku(głowa powinna być przedłużeniem kręgosłupa, wzrok skierowany przed siebie, brzuch wciągnięty)\n\
* Powoli zaczynać uginać kolana jednocześnie wypychając biodra do tyłu(kolana nie powinny wychodzić przed palce stóp, stopy całe przylegają do podłoża a kąt między udem a podudziem powinien wynosić maksymalnie 90 stopni\n\
* Prostować kolona, powracając do pozycji wyjściowej\n")
	liczba_powtorzen = int(input("Spróbuj wykonać jak najwięcej przysiadów i podaj ilość: "))
	if liczba_powtorzen > 20:
		os.system("clear")
		print("Gratulację ! Udało Ci się zrobić powyżej 20 powtórzeń !\n\
Twój następny trening wygląda następująco: \n\
\n\
I seria: 15 przysiadów\n\
II seria: 17 przysiadów\n\
III seria: 19 przysiadów\n\
IV seria: 16 przysiadów\n\
V seria: 18 przysiadów\n\
VI seria: 20 przysiadów\n\
\nPowodzenia !")
	elif liczba_powtorzen < 20:
		os.system("clear")
		print ("Nie udało Ci się przekroczyć progu 20 powtórzeń, ale się nie załamuj ! Trenuj ciężko, w pełnym skupieniu !\n\
\n\
Twój następny trening wygląda następująco: \n\
\n\
I seria: 5 przysiadów\n\
II seria: 7 przysiadów\n\
III seria: 9 przysiadów\n\
IV seria: 6 przysiadów\n\
V seria: 8 przysiadów\n\
VI seria: 10 przysiadów\n\
\nPowodzenia !")

#------------------------------------ Funkcja wyboru pompek

def pompki():
	print("Pompki to dość proste ćwiczenie, lecz wiele osób wykonuje je źle. By prawidłowo wykonać pompki pamiętaj aby: \n\
\n\
* Ciało było wyprostowane\n\
* Stopy były ułożone blisko siebie (opieraj się na palcach)\n\
* Ręcę były ułożone nieco szerzej niż klatka piersiowa\n\
* Dłonie powinny być lekko odchylone na zewnątrz\n\
* Opuszczać się do momentu, aż w stawie łokciowym utworzy się kąt prost (pamiętaj o prostych plecach !\n")
	liczba_powtorzen = int(input("Spróbuj wykonać jak najwięcej pompek i podaj ilość: "))
	if liczba_powtorzen > 20:
		os.system("clear")
		print("Gratulację ! Udało Ci się zrobić powyżej 20 powtórzeń !\n\
Twój następny trening wygląda następująco: \n\
\n\
I seria: 15 pompek\n\
II seria: 17 pompek\n\
III seria: 19 pompek\n\
IV seria: 16 pompek\n\
V seria: 18 pompek \n\
VI seria: 20 pompek\n\
\nPowodzenia !")
	elif liczba_powtorzen < 20:
		os.system("clear")
		print ("Nie udało Ci się przekroczyć progu 20 powtórzeń, ale się nie załamuj ! Trenuj ciężko, w pełnym skupieniu !\n\
\n\
Twój następny trening wygląda następująco: \n\
I seria: 5 pompek\n\
II seria: 7 pompek\n\
III seria: 9 pompek\n\
IV seria: 6 pompek\n\
V seria: 8 pompek \n\
VI seria: 10 pompek\n\
\nPowodzenia !")

#----------------------------------- Funkcja wybierania ćwiczenia

def wybierz_cwiczenie():

	wybor = int(input("Wybierz ćwiczenie: \n\
\n\
1 - Pompki\n\
2 - Przysiady\n\
3 - Brzuszki\n\
4 - Podciągnięcia\n\
-----------------\n"))
	if wybor == 1:
		os.system("clear")
		pompki()
	elif wybor == 2:
		os.system("clear")
		przysiady()
	elif wybor == 3:
		os.system("clear")
		brzuszki()
	elif wybor == 4:
		os.system("clear")
		podciagniecia()
	else:
		print("Upewnij się, że podałeś dobrą cyfrę !")


#----------------------------------- Program
os.system("clear")
print ("Witam Cię w 4ForFit ! Co chcesz zrobić?\n ")

wybor = int(input("Wybierz: \n\
\n\
1 - START\n\
2 - Ustawienia\n\
-----------------\n"))
if wybor == 1:
		os.system("clear")
		wybierz_cwiczenie()
elif wybor == 2:
		os.system("clear")
		srednia()
else:
		print("Upewnij się, że podałeś dobrą cyfrę !")
		os.system("clear")
	
