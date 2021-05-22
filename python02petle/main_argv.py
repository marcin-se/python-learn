# PAKOWACZ
# -*- coding: UTF-8 -*-
import sys
import os
from time import sleep


def clear_screen():
    if os.name == 'posix':  # dla mac i linux
        _ = os.system('clear')
    else:
        _ = os.system('cls')  # dla windows


def animacja(znak, ilosc):
    while ilosc:
        print("\t{}".format(znak, end=""))
        sleep(0.5)
        ilosc -= 1
    print("\t... i już płynie kontenerem do Chin! ")


def linia(znaczek, liczba):
    print("\n", znaczek * liczba)


clear_screen()
# ilosc_przesylek = int(input("\n | ? | Ilość przesyłek do wysłania: "))
ilosc_przesylek = int(sys.argv[1])
print("\n | ? | Ilość przesyłek do wysłania: ", ilosc_przesylek)
linia("*", 70)

przesylki: list[int] = []
paczki: list[int] = []
waga_paczki = 0
waga_razem: int = 0
nr_przesylki, nr_paczki, sent = 0, 0, 0

while ilosc_przesylek:
    waga = int(input("\n | < | Podaj ciężar przesyłki: "))

    if waga < 0:
        print(
            " | ! | Wprowadzono nieprawidłową wartość dla przesyłki.\n\tSpróbuj jeszcze raz.")
        continue
    elif waga == 0:
        print(
            " | ! | Wprowadzono wartość 0 kg.\n\tZakończono pakowanie przesyłek.")
        break
    elif waga > 10:
        print(" | ! | Za duży ciężar! Przesyłka nie będzie wysłana!")
        continue
    elif waga_paczki + waga > 20:
        nr_przesylki += 1
        print(" |>>>| Paczka nr [{}] w przygotowaniu... ".format(
            nr_paczki + 1))
        animacja(". ", 3)
        paczki.append(int(waga_paczki))
        przesylki.append(int(waga))
        nr_paczki += 1
        waga_razem += waga
        print(" | > | Przesyłkę nr <{}> dodano do nowej paczki nr [{}].".format(
            nr_przesylki, nr_paczki + 1))
        waga_paczki = waga
        ilosc_przesylek -= 1
        sent = 0
    elif waga_paczki + waga == 20:
        przesylki.append(int(waga))
        nr_przesylki += 1
        print(" | > | Przesyłkę nr <{}> dodano do paczki nr [{}].".format(
            nr_przesylki, nr_paczki + 1))
        print(" |>>>| Paczka nr {} w przygotowaniu... ".format(
            nr_paczki + 1))
        animacja(". ", 3)
        waga_paczki += waga
        paczki.append(int(waga_paczki))
        waga_razem += waga
        nr_paczki += 1
        waga_paczki = 0
        ilosc_przesylek -= 1
        sent = 1
    else:
        przesylki.append(int(waga))
        waga_paczki += waga
        waga_razem += waga
        nr_przesylki += 1
        print(" | > | Przesyłkę nr <{}> dodano do paczki nr [{}].".format(
            nr_przesylki, nr_paczki + 1))
        ilosc_przesylek -= 1
        sent = 0

if not sent and waga_razem != 0:
    print(" |>>>| Paczka nr [{}] w przygotowaniu... ".format(
        nr_paczki + 1))
    animacja(". ", 3)
    paczki.append(int(waga_paczki))

if not nr_przesylki:
    print(
        " | i | Nie otrzymano przesyłek do wysłania. Rzadnej paczki nie nadano.")


else:
    linia("*", 70)
    print("\n | i | Wszystkie otrzymane przesyłki odpłynęły! :D")
    print(
        " | i | Łącznie wysłano paczek: {}., w których umieszczono przesyłek: {}.".format(
            len(paczki), len(przesylki)))
    print(" | i | Łącznie wszystkie wysłane przesyłki ważyły:\t{} kg".format(
        waga_razem))
    y = 20 * (nr_paczki + 1) - waga_razem
    print(" | i | Pusta przestrzeń w paczkach wyniosła:\t\t{} kg".format(y))
    waga_paczki_min, paczka_id, y = 20, 0, 0
    for i in range(0, nr_paczki + 1):
        if paczki[i] < waga_paczki_min:
            waga_paczki_min = paczki[i]
            paczka_id = i
    print(" | i | Najmniej ekonomiczna paczka, to paczka nr: [{}].".format(
        paczka_id + 1))
linia("*", 70)

