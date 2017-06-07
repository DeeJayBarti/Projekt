#-*- coding: utf-8 -*-
import os
from tkinter import *
from tkinter import ttk

def quit(zdarzenie):
	global okno
	okno.quit()	
#-------------------------------- Funkcja zamknij aplikację
def zamknij(zdarzenie):
	okno.quit()
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
	przycisk1_19.bind("<Button-1>", pow1_19)
	przycisk1_19.pack(padx = 2, pady = 2)

	# 20 - 39
	przycisk20_39 = Button(okno, text = "20 - 39 powtórzeń", width=16, height=1)
	przycisk20_39.bind("<Button-1>", pow20_39)
	przycisk20_39.pack(padx = 2, pady = 2)

	# 40 - 59
	przycisk40_59 = Button(okno, text = "40 - 59 powtórzeń", width=16, height=1)
	przycisk40_59.bind("<Button-1>", pow40_59)
	przycisk40_59.pack(padx = 2, pady = 2)

	# 60 - 79
	przycisk60_79 = Button(okno, text = "60 - 79 powtórzeń", width=16, height=1)
	przycisk60_79.bind("<Button-1>", pow60_79)
	przycisk60_79.pack(padx = 2, pady = 2)

	# 80 - 99
	przycisk80_99 = Button(okno, text = "80 - 99 powtórzeń", width=16, height=1)
	przycisk80_99.bind("<Button-1>", pow80_99)
	przycisk80_99.pack(padx = 2, pady = 2)

	# 100 - 119
	przycisk100_119 = Button(okno, text = "100 - 119 powtórzeń", width=16, height=1)
	przycisk100_119.bind("<Button-1>", pow100_119)
	przycisk100_119.pack(padx = 2, pady = 2)

	# 120 - 139
	przycisk120_139 = Button(okno, text = "120 - 139 powtórzeń", width=16, height=1)
	przycisk120_139.bind("<Button-1>", pow120_139)
	przycisk120_139.pack(padx = 2, pady = 2)

	# 140 +
	przycisk140 = Button(okno, text = "Ponad 150 powtórzeń", width=16, height=1)
	przycisk140.bind("<Button-1>", pow140)
	przycisk140.pack(padx = 2, pady = 2)

	okno.mainloop()

#------------------------------------------------------------
#-------------------------------- Poszczególne treningi-----
#-----------------------------------------------------------

def pow1_19(zdarzenie):

	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Oto Twój następny trening !", padx = 30, pady = 10)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "I seria:     10 powtórzeń\n\
\n\
II seria:     13 powtórzeń\n\
\n\
III seria:    11 powtórzeń\n\
\n\
IV seria:     15 powtórzeń\n\
\n\
Przerwa pomiędzy seriami: 60 sekund\n\
\n\
Pamiętaj aby dokładnie wykonywać\n\
każde z powtórzeń !", padx = 5, pady = 5)
	etykieta.pack(expand=NO)

	bottomFrame = Frame(okno)
	bottomFrame.pack()
	
	poddajsie = Button(bottomFrame, text = "Poddaje się", width = 8, height = 2)
	poddajsie.bind("<Button-1>", quit)
	poddajsie.pack(side = LEFT, padx = 2, pady = 2)

	skonczoneb = Button(bottomFrame, text = "Skończone !", width = 8, height = 2)
	skonczoneb.bind("<Button-1>", skonczone)
	skonczoneb.pack(side = RIGHT, padx = 2, pady = 2)

	okno.mainloop()

def pow20_39(zdarzenie):

	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Oto Twój następny trening !", padx = 30, pady = 10)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "I seria:     18 powtórzeń\n\
\n\
II seria:     22 powtórzenia\n\
\n\
III seria:    25 powtórzeń\n\
\n\
IV seria:     17 powtórzeń\n\
\n\
V seria:     20 powtórzeń\n\
\n\
VI seria:     22 powtórzenia\n\
\n\
Przerwa pomiędzy seriami: 60 sekund", padx = 5, pady = 5)
	etykieta.pack(expand=NO)

	bottomFrame = Frame(okno)
	bottomFrame.pack()
	
	poddajsie = Button(bottomFrame, text = "Poddaje się", width = 8, height = 2)
	poddajsie.bind("<Button-1>", quit)
	poddajsie.pack(side = LEFT, padx = 2, pady = 2)

	skonczoneb = Button(bottomFrame, text = "Skończone !", width = 8, height = 2)
	skonczoneb.bind("<Button-1>", skonczone)
	skonczoneb.pack(side = RIGHT, padx = 2, pady = 2)

	okno.mainloop()

def pow40_59(zdarzenie):

	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Oto Twój następny trening !", padx = 30, pady = 10)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "I seria:     25 powtórzeń\n\
\n\
II seria:     29 powtórzeń\n\
\n\
III seria:    24 powtórzenia\n\
\n\
IV seria:     30 powtórzeń\n\
\n\
V seria:     31 powtórzeń\n\
\n\
VI seria:     27 powtórzeń\n\
\n\
Przerwa pomiędzy seriami: 60 sekund", padx = 5, pady = 5)
	etykieta.pack(expand=NO)

	bottomFrame = Frame(okno)
	bottomFrame.pack()
	
	poddajsie = Button(bottomFrame, text = "Poddaje się", width = 8, height = 2)
	poddajsie.bind("<Button-1>", quit)
	poddajsie.pack(side = LEFT, padx = 2, pady = 2)

	skonczoneb = Button(bottomFrame, text = "Skończone !", width = 8, height = 2)
	skonczoneb.bind("<Button-1>", skonczone)
	skonczoneb.pack(side = RIGHT, padx = 2, pady = 2)

	okno.mainloop()

def pow60_79(zdarzenie):

	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Oto Twój następny trening !", padx = 30, pady = 10)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "I seria:     30 powtórzeń\n\
\n\
II seria:     35 powtórzeń\n\
\n\
III seria:    29 powtórzeń\n\
\n\
IV seria:     30 powtórzeń\n\
\n\
V seria:     34 powtórzenia\n\
\n\
VI seria:     36 powtórzeń\n\
\n\
Przerwa pomiędzy seriami: 60 sekund", padx = 5, pady = 5)
	etykieta.pack(expand=NO)

	bottomFrame = Frame(okno)
	bottomFrame.pack()
	
	poddajsie = Button(bottomFrame, text = "Poddaje się", width = 8, height = 2)
	poddajsie.bind("<Button-1>", quit)
	poddajsie.pack(side = LEFT, padx = 2, pady = 2)

	skonczoneb = Button(bottomFrame, text = "Skończone !", width = 8, height = 2)
	skonczoneb.bind("<Button-1>", skonczone)
	skonczoneb.pack(side = RIGHT, padx = 2, pady = 2)

	okno.mainloop()

def pow80_99(zdarzenie):

	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Oto Twój następny trening !", padx = 30, pady = 10)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "I seria:     40 powtórzeń\n\
\n\
II seria:     45 powtórzeń\n\
\n\
III seria:    42 powtórzenia\n\
\n\
IV seria:     47 powtórzeń\n\
\n\
V seria:     50 powtórzeń\n\
\n\
VI seria:     52 powtórzenia\n\
\n\
Przerwa pomiędzy seriami: 60 sekund", padx = 5, pady = 5)
	etykieta.pack(expand=NO)

	bottomFrame = Frame(okno)
	bottomFrame.pack()
	
	poddajsie = Button(bottomFrame, text = "Poddaje się", width = 8, height = 2)
	poddajsie.bind("<Button-1>", quit)
	poddajsie.pack(side = LEFT, padx = 2, pady = 2)

	skonczoneb = Button(bottomFrame, text = "Skończone !", width = 8, height = 2)
	skonczoneb.bind("<Button-1>", skonczone)
	skonczoneb.pack(side = RIGHT, padx = 2, pady = 2)

	okno.mainloop()

def pow100_119(zdarzenie):

	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Oto Twój następny trening !", padx = 30, pady = 10)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "I seria:     50 powtórzeń\n\
\n\
II seria:     56 powtórzeń\n\
\n\
III seria:    62 powtórzenia\n\
\n\
IV seria:     57 powtórzeń\n\
\n\
V seria:     55 powtórzeń\n\
\n\
VI seria:     63 powtórzenia\n\
\n\
Przerwa pomiędzy seriami: 60 sekund", padx = 5, pady = 5)
	etykieta.pack(expand=NO)

	bottomFrame = Frame(okno)
	bottomFrame.pack()
	
	poddajsie = Button(bottomFrame, text = "Poddaje się", width = 8, height = 2)
	poddajsie.bind("<Button-1>", quit)
	poddajsie.pack(side = LEFT, padx = 2, pady = 2)

	skonczoneb = Button(bottomFrame, text = "Skończone !", width = 8, height = 2)
	skonczoneb.bind("<Button-1>", skonczone)
	skonczoneb.pack(side = RIGHT, padx = 2, pady = 2)

	okno.mainloop()

def pow120_139(zdarzenie):

	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Oto Twój następny trening !", padx = 30, pady = 10)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "I seria:     65 powtórzeń\n\
\n\
II seria:     70 powtórzeń\n\
\n\
III seria:    73 powtórzenia\n\
\n\
IV seria:     68 powtórzeń\n\
\n\
V seria:     65 powtórzeń\n\
\n\
VI seria:     75 powtórzeń\n\
\n\
Przerwa pomiędzy seriami: 60 sekund", padx = 5, pady = 5)
	etykieta.pack(expand=NO)

	bottomFrame = Frame(okno)
	bottomFrame.pack()
	
	poddajsie = Button(bottomFrame, text = "Poddaje się", width = 8, height = 2)
	poddajsie.bind("<Button-1>", quit)
	poddajsie.pack(side = LEFT, padx = 2, pady = 2)

	skonczoneb = Button(bottomFrame, text = "Skończone !", width = 8, height = 2)
	skonczoneb.bind("<Button-1>", skonczone)
	skonczoneb.pack(side = RIGHT, padx = 2, pady = 2)

	okno.mainloop()

def pow140(zdarzenie):

	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Oto Twój następny trening !", padx = 30, pady = 10)
	etykieta.pack(expand=NO)
	etykieta = Label(okno, text = "I seria:     70 powtórzeń\n\
\n\
II seria:     76 powtórzeń\n\
\n\
III seria:    80 powtórzeń\n\
\n\
IV seria:     77 powtórzeń\n\
\n\
V seria:     85 powtórzeń\n\
\n\
VI seria:     90 powtórzeń\n\
\n\
Przerwa pomiędzy seriami: 60 sekund", padx = 5, pady = 5)
	etykieta.pack(expand=NO)

	bottomFrame = Frame(okno)
	bottomFrame.pack()
	
	poddajsie = Button(bottomFrame, text = "Poddaje się", width = 8, height = 2)
	poddajsie.bind("<Button-1>", quit)
	poddajsie.pack(side = LEFT, padx = 2, pady = 2)

	skonczoneb = Button(bottomFrame, text = "Skończone !", width = 8, height = 2)
	skonczoneb.bind("<Button-1>", skonczone)
	skonczoneb.pack(side = RIGHT, padx = 2, pady = 2)

	okno.mainloop()
#---------------------------------------------- Zakonczenie treningu
def skonczone(zdarzenie):
	
	okno = Tk()
	okno.title("4ForFit")
	okno.geometry("240x300")
	etykieta = Label(okno, text = "Gratulacje !\n\
\n\
Udało Ci się zakończyć trening !\n\
\n\
\n\
Teraz pora zregenerować organizm.\n\
\n\
Pamiętaj o jutrzejszym treningu !", padx = 30, pady = 10)
	etykieta.pack(expand=NO)
	
	bottomFrame = Frame(okno)
	bottomFrame.pack()
	
	wyjdz = Button(bottomFrame, text = "Wyjdź", width = 8, 		height = 3)
	wyjdz.bind("<Button-1>", quit)
	wyjdz.pack(side = BOTTOM, padx = 10, pady = 10)
	
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
