#-*- coding: utf-8 -*-
import os
from tkinter import *
from tkinter import ttk

#-------------------------------- Funkcja zamknij aplikację
def zamknij(zdarzenie):
	okno.quit()
	okno.destroy()
#-------------------------------- Funkcja wybrania POMPEK
def pompki(zdarzenie):

	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Instrukcja + Pierwszy test", padx = 30, pady = 10)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "By prawidłowo wykonać\n\
 pompki: \n\
\n\
* Wyprostuj się !\n\
* Ułóż stopy blisko siebie !\n\
* Ułóż ręce nieco szerzej !\n\
niż klatka piersiowa !\n\
* Lekko odchyl dłonie na zewnątrz !\n\
* Opuść się, aż w stawie !\n\
 łokciowym utworzy się kąt prosty !", padx = 5, pady = 5)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "Zrób jak najwięcej powtórzeń !", padx = 5, pady = 5)
	etykieta.pack(expand=NO)

	#Przycisk "DALEJ"
	przycisk_dalej = Button(okno, text = "Dalej", width = 6, 		height = 1)
	przycisk_dalej.bind("<Button-1>", wybierz_ile)
	przycisk_dalej.pack(side = BOTTOM, padx = 10, pady = 10)

	okno.mainloop()



#-------------------------------- Funkcja wybrania PRZYSIADÓW
def przysiady(zdarzenie):

	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Instrukcja + Pierwszy test", padx = 30, pady = 10)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "By prawidłowo wykonać\n\
 przysiady: \n\
\n\
* Stań prosto w lekkim rozkroku !\n\
* Wciągnij brzuch, patrz przed siebie !\n\
* Zacznij uginać kolana !\n\
* Wypychaj biodra do przodu !\n\
* Zejdź do kąta 90 stopni !\n\
* Wyprostuj kolana wracając do stójki !", padx = 5, pady = 5)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "Zrób jak najwięcej powtórzeń !", padx = 5, pady = 5)
	etykieta.pack(expand=NO)

	#Przycisk "DALEJ"
	przycisk_dalej = Button(okno, text = "Dalej", width = 6, 		height = 1)
	przycisk_dalej.bind("<Button-1>", wybierz_ile)
	przycisk_dalej.pack(side = BOTTOM, padx = 10, pady = 10)

	okno.mainloop()
#-------------------------------- Funkcja wybrania BRZUSZKÓW
def brzuszki(zdarzenie):

	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Instrukcja + Pierwszy test", padx = 30, pady = 10)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "By prawidłowo wykonać\n\
 brzuszki: \n\
\n\
* Połóż się na plecach !\n\
* Ugnij nogi w kolanach !\n\
* Umieść dłonie za głową !\n\
 (Nie splatach ich, nie chwytaj głowy)\n\
* Weź oddech i napnij brzuch !\n\
* Unieś łopatki kilka cm nad ziemią !\n\
* Z wdechem opuść tułów !", padx = 5, pady = 5)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "Zrób jak najwięcej powtórzeń !", padx = 5, pady = 5)
	etykieta.pack(expand=NO)

	#Przycisk "DALEJ"
	przycisk_dalej = Button(okno, text = "Dalej", width = 6, 		height = 1)
	przycisk_dalej.bind("<Button-1>", wybierz_ile)
	przycisk_dalej.pack(side = BOTTOM, padx = 10, pady = 10)

	okno.mainloop()

#----------------------------------------- ilość powtórzeń (wybierz)
def wybierz_ile(zdarzenie):

	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Kliknij na swój wynik !", padx = 30, pady = 10)
	etykieta.pack(expand=NO)

	# 1 - 19
	przycisk1_19 = Button(okno, text = "1 - 19 powtórzeń", width=16, height=1)
	przycisk1_19.bind("<Button-1>")
	przycisk1_19.pack(padx = 2, pady = 2)

	# 20 - 39
	przycisk20_39 = Button(okno, text = "20 - 39 powtórzeń", width=16, height=1)
	przycisk20_39.bind("<Button-1>")
	przycisk20_39.pack(padx = 2, pady = 2)

	# 40 - 59
	przycisk40_59 = Button(okno, text = "40 - 59 powtórzeń", width=16, height=1)
	przycisk40_59.bind("<Button-1>")
	przycisk40_59.pack(padx = 2, pady = 2)

	# 60 - 79
	przycisk60_79 = Button(okno, text = "60 - 79 powtórzeń", width=16, height=1)
	przycisk60_79.bind("<Button-1>")
	przycisk60_79.pack(padx = 2, pady = 2)

	# 80 - 99
	przycisk80_99 = Button(okno, text = "80 - 99 powtórzeń", width=16, height=1)
	przycisk80_99.bind("<Button-1>")
	przycisk80_99.pack(padx = 2, pady = 2)

	# 100 - 119
	przycisk100_119 = Button(okno, text = "100 - 119 powtórzeń", width=16, height=1)
	przycisk100_119.bind("<Button-1>")
	przycisk100_119.pack(padx = 2, pady = 2)

	# 120 - 139
	przycisk120_139 = Button(okno, text = "120 - 139 powtórzeń", width=16, height=1)
	przycisk120_139.bind("<Button-1>")
	przycisk120_139.pack(padx = 2, pady = 2)

	# 140 +
	przycisk140 = Button(okno, text = "Ponad 150 powtórzeń", width=16, height=1)
	przycisk140.bind("<Button-1>")
	przycisk140.pack(padx = 2, pady = 2)

	okno.mainloop()
#-------------------------------- Funkcja wybrania PODCIĄGNIĘĆ
def podciagniecia(zdarzenie):

	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Instrukcja + Pierwszy test", padx = 30, pady = 10)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "By prawidłowo wykonać\n\
 podciągnięcia: \n\
\n\
* Wyprostuj ręce i głowę !\n\
* Podciągnij się jednym ruchem !\n\
* Nie bujaj się i nie szarp !\n\
* Ciało prowadź jak najbliżej drążka !\n\
* Broda powinna być przy drążku !\n\
* Opuść się do wyprostowanych rąk !", padx = 5, pady = 5)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "Zrób jak najwięcej powtórzeń !", padx = 5, pady = 5)
	etykieta.pack(expand=NO)

	#Przycisk "DALEJ"
	przycisk_dalej = Button(okno, text = "Dalej", width = 6, 		height = 1)
	przycisk_dalej.bind("<Button-1>", wybierz_ile)
	przycisk_dalej.pack(side = BOTTOM, padx = 10, pady = 10)
	
	okno.mainloop()
#-------------------------------- Program startowy

def wyjdz():
	okno.quit()
	okno.destroy()

okno = Tk()
okno.title("4ForFit")
okno.geometry("240x300")
etykieta = Label(okno, text = "Witamy w aplikacji 4ForFit !", padx = 30, pady = 10)
etykieta.pack(expand=NO)
etykieta1 = Label(okno, text = "Wybierz ćwiczenie: ", padx = 10, pady = 10)
etykieta1.pack(expand=NO)

topFrame = Frame(okno)
topFrame.pack()

przycisk1 = Button(topFrame, text = "Pompki", width=8, height=3)
przycisk2 = Button(topFrame, text = "Przysiady", width=8, height=3)

bottomFrame = Frame(okno)
bottomFrame.pack()

przycisk3 = Button(bottomFrame, text = "Brzuszki", width=8, height=3)
przycisk4 = Button(bottomFrame, text = "Podciągnięcia", width=8, height=3)
przycisk = Button(okno, text = "Wyjście")

przycisk.bind("<Button-1>", zamknij)
przycisk1.bind("<Button-1>", pompki)
przycisk2.bind("<Button-1>", przysiady)
przycisk3.bind("<Button-1>", brzuszki)
przycisk4.bind("<Button-1>", podciagniecia)
przycisk1.pack(side = LEFT, padx = 10, pady = 10)
przycisk2.pack(side = RIGHT, padx = 10, pady = 10)
przycisk3.pack(side = LEFT, padx = 10, pady = 10)
przycisk4.pack(side = RIGHT, padx = 10,  pady = 10)
przycisk.pack(side = BOTTOM, padx = 10, pady = 10)


okno.mainloop()
