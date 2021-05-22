# -*- coding: UTF-8 -*-
# Program - oprocentowanie kredytu, z uwzglednieniem inflacji.
# import fileinput
# from typing import List
# import txt as txt

szablon = "| {:11s} | {:12} | {:11.2f} | {:10.2f} |"

kredyt = float(input("> Słyszałem, że wziąłeś kredyt!!! Przyznaj się, ile: "))
rata = float(input("> Wysoką masz ratę miesięczną?: "))
inflacja = float(input("> A wiesz, ile wynosi aktualna inflacja?: "))

linia = 57                  # szerokość tabeli
print("*" * linia, "\n")
print("{:25s} {:10.2f} {:5s}".format("\tOK, Twój kredyt to:", kredyt, "zl"))
print("{:25s} {:10.2f} {:5s}".format("\tRata miesięczna to:", rata, "zl"))
print("{:25s} {:10.2f} {:5s}".format("\tWartość inflacji to: ", inflacja, "%"))

x = kredyt
y = 0
print("\n  TABELA - tempo spłaty kredytu, miesięcznie (2 lata).")

print("*" * linia)
print("|   MIESIĄC   |   STOPA %    |  DO SPLATY  |  MNIEJ O   |")
print("*" * linia)
print(szablon.format("", "", x, 0))

flaga = 0
f = open("in.txt", "r")     # otwarcie pliku w trybie czytania
wartosc = kredyt            # zmienna pomocnicza do obl. roznicy
for line in f:
    tekst = line.strip()
    stopa = float(f.readline())          # float, bo bierze udzial w dzialaniu
    x = (1 + ((stopa+inflacja)/1200)) * x - rata
    y = -(x - wartosc)
    if x > 0:
        x = x
    elif x <= 0:
        x = 0
        y = 0
        flaga = 1
    print(szablon.format(tekst, stopa, x, y))
    wartosc = float(x)

print("*" * linia)          # zamknięcie/podkreślenie tabeli
print()
if flaga == 0:
  print("\tI tak będziesz spłacać... i spłacać... :(")
elif flaga == 1:
  print("  GRATULACJE!!! Spłacisz kredyt w krótszym czasie... :D")
f.close()                   # zamknięcie pliku
