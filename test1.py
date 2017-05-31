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
	etykieta = Label(okno, text = "Zrób jak najwięcej powtórzeń !\n\
Podaj wynik: ", padx = 5, pady = 5)
	etykieta.pack(expand=NO)
	entry = Entry(okno)
	entry.pack()

	#Przycisk "DALEJ"
	przycisk_dalej = Button(okno, text = "Dalej", width = 6, 		height = 1)
	przycisk_dalej.bind("<Button-1>")
	przycisk_dalej.pack(side = BOTTOM, padx = 10, pady = 10)

	okno.mainloop()



#-------------------------------- Funkcja wybrania PRZYSIADÓW
#def przysiady(zdarzenie):
#-------------------------------- Funkcja wybrania BRZUSZKÓW
#def brzuszki(zdarzenie):
#-------------------------------- Funkcja wybrania PODCIĄGNIĘĆ
#def podciagniecia(zdarzenie):
#-------------------------------- Program startowy

okno = Tk()
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
przycisk2.bind("<Button-1>")
przycisk3.bind("<Button-1>")
przycisk4.bind("<Button-1>")
przycisk1.pack(side = LEFT, padx = 10, pady = 10)
przycisk2.pack(side = RIGHT, padx = 10, pady = 10)
przycisk3.pack(side = LEFT, padx = 10, pady = 10)
przycisk4.pack(side = RIGHT, padx = 10,  pady = 10)
przycisk.pack(side = BOTTOM, padx = 10, pady = 10)


okno.mainloop()
