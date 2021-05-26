# PAKOWACZ v2.0 - z obsługą plików
# -*- coding: UTF-8 -*-
import sys
import os
from time import sleep
path_in = "data_in.txt"
path_out = "data_out.txt"


def clear_screen():
    if os.name == 'posix':  # dla mac i linux
        _ = os.system('clear')
    else:
        _ = os.system('cls')  # dla windows


def animation(sign, repeat):
    while repeat:
        print("\t{}".format(sign, end=" "))
        sleep(0.3)
        repeat -= 1
    print("\t... wysłano!!! ")


def dividing_line(stamp, repeat):
    print("\n", stamp * repeat)


clear_screen()
file_in = open(path_in, "r", encoding="utf8")
file_out = open(path_out, "w+", encoding="utf8")

quantity_parcels = int(sys.argv[1])
print("\n |???| LICZBA PRZESYŁEK DO WYSŁANIA: ", quantity_parcels)
file_out.write("\t\t DEKLAROWANA lICZBA PRZESYŁEK: {}.\n".format(quantity_parcels))
file_out.write("* * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
parcels: list[float] = []
packs: list[float] = []
total_weight: float = round(0, 3)
parcel_num, pack_num, to_ship, if_full = 0, 0, False, False
weight, pack_weight = float(round(0, 3)), float(round(0, 3))

while quantity_parcels:
    weight = float(file_in.readline())
    print("\n |<| Pobrany ciężar przesyłki: {}".format(weight))
    to_ship = 1
    if weight < 0:
        print(" |!| Nieprawidłowa wartość dla przesyłki.")
        continue
    if weight == 0:
        print(" |!| Wczytano wartość 0. Zakończono odczyt przesyłek.")
        break
    if 0 < weight < 1 or weight > 10:
        print(" |!| NIEPRAWIDŁOWA WAGA!!! Przesyłka nie będzie wysłana!")
        continue
    if pack_weight + weight >= 20:
        parcel_num += 1
        parcels.append(float(round(weight, 3)))
        total_weight += weight
        if pack_weight + weight == 20:
            pack_weight += weight
            print(" |>| Przesyłkę nr {}. ({:6.3f} kg) dodano do PACZKI NR [{}].".
                  format(parcel_num, weight, pack_num + 1))
            file_out.write("Przesyłka nr {}.\t{:6.3f} kg\tPACZKA NR [{}]\n".
                  format(parcel_num, float(round(weight, 3)), pack_num + 1))
            if_full = False
        else:
            print(" |>| Przesyłkę nr {}. ({:6.3f} kg), przekierowano do nowej PACZKI NR [{}].".
                format(parcel_num, weight, pack_num + 2))
            file_out.write(" Przesyłka nr {}.\t{:6.3f} kg\tPACZKA NR [{}]\n".
               format(parcel_num, float(round(weight, 3)), pack_num + 2))
            if_full = True
    else:
        parcels.append(float(round(weight, 3)))
        pack_weight += weight
        total_weight += weight
        parcel_num += 1
        print(" |>| Przesyłkę nr {}. ({:6.3f} kg) dodano do PACZKI NR [{}].".format(
            parcel_num, weight, pack_num + 1))
        file_out.write(" Przesyłka nr {}.\t{:6.3f} kg\tPACZKA NR [{}]\n".
           format(parcel_num, float(round(weight, 3)), pack_num + 1))
        if quantity_parcels == 1:
            to_ship = True
        else:
            to_ship = False
    quantity_parcels -= 1
    while to_ship and total_weight > 0:
        print(
            " |>>>| PACZKA NR [{}], o łącznej wadze przesyłek {:6.3f} kg, oczekuje... ".
            format(pack_num + 1, pack_weight))
        animation("* ", 1)
        file_out.write("\t >>> PACZKA NR [{}]\t({:6.3f} kg)\tstatus: wysłana\n".
           format(pack_num + 1, float(round(pack_weight, 3))))
        packs.append(float(round(pack_weight, 3)))
        if if_full:
            pack_weight = weight
            if_full = False
            if not quantity_parcels:
                pack_num += 1
                continue
        else:
            pack_weight = 0
        to_ship = False
        pack_num += 1

if not weight and total_weight > 0:
    print(
        " |>>>| PACZKA NR [{}], o łącznej wadze przesyłek: {:6.3f} kg, oczekuje... ".
        format(pack_num + 1, pack_weight))
    animation("* ", 1)
    file_out.write("\t >>> PACZKA NR [{}]\t({:6.3f} kg)\tstatus: wysłana\n".
       format(pack_num + 1, float(round(pack_weight, 3))))
    packs.append(float(round(pack_weight, 3)))
    pack_num += 1

if not parcel_num:
    print(" |i| Nie otrzymano przesyłek do wysłania. Żadnej PACZKI nie nadano.")
    file_out.write(" PODANO lICZBĘ PRZESYŁEK: 0.\n")
else:
    dividing_line("*", 80)
    file_out.write("* * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
    print("\n |i| Wszystkie przyjęte przesyłki wysłano.")
    print(" |i| Łącznie wysłano PACZEK: {}, w których umieszczono przesyłek: {}.".
        format(len(packs), len(parcels)))
    file_out.write("Razem PACZEK: {}, w tym przesyłek: {}.\n".
                   format(len(packs), len(parcels)))
    print(" |i| Łącznie wszystkie wysłane przesyłki ważyły:\t{:6.3f} kg".
          format(float(round(total_weight, 3))))
    file_out.write("Łączna waga wysłanych przesyłek: {:6.3f} kg.\n".
                   format(round(total_weight, 3)))
    y = round(float(20 * pack_num - total_weight), 3)
    print(" |i| Pusta przestrzeń w PACZKACH wyniosła:\t\t{:6.3f} kg".format(y))
    file_out.write("Pusta przestrzeń w paczkach: {:6.3f} kg.\n".format(y))
    min_pack_weight, id_pack = float(round(20, 3)), 0
    for i in range(pack_num):
        if packs[i] < min_pack_weight:
            min_pack_weight = packs[i]
            id_pack = i
    print(" |i| Najmniej ekonomiczna paczka:\t\t\tPACZKA NR [{}]".format(
        id_pack + 1))
    file_out.write("Nieekonomiczna: PACZKA NR [{}].\n".format(id_pack + 1))
    file_out.write("* * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
dividing_line("*", 80)
file_in.close()
file_out.close()
