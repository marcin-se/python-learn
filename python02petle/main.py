# PAKOWACZ v1.0 - z obsługą plików
# -*- coding: UTF-8 -*-
import sys
import os
from time import sleep
from typing import List


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
quantity_parcels = round(int(input("\n |???| LICZBA PRZESYŁEK DO WYSŁANIA: ")), 0)
# quantity_parcels = int(sys.argv[1])
dividing_line("*", 80)

parcels: list[float] = []
packs: list[float] = []
total_weight: float = round(0, 3)
parcel_num, pack_num, to_ship, if_full = 0, 0, False, False
weight, pack_weight = float(round(0, 3)), float(round(0, 3))

while quantity_parcels:
    weight = round(float(input("\n |<| Podaj ciężar przesyłki: ")), 3)
    to_ship = True
    if weight < 0:
        print(" |!| Wprowadzono nieprawidłową wartość dla przesyłki.\n\tSpróbuj jeszcze raz.")
        continue
    if weight == 0:
        print(" |!| Wprowadzono 0. Zakończono przyjmowanie przesyłek.")
        break
    if 0 < weight < 1 or weight > 10:
        print(" |!| NIEPRAWIDŁOWA WAGA!!! Przesyłka nie będzie wysłana!\n\tSpróbuj jeszcze raz.")
        continue
    if pack_weight + weight >= 20:
        parcel_num += 1
        parcels.append(float(round(weight, 3)))
        total_weight += weight
        if pack_weight + weight == 20:
            pack_weight += weight
            print(" |>| Przesyłkę nr {}. ({} kg) dodano do PACZKI NR [{}].".format(
                parcel_num, weight, pack_num + 1))
            if_full = False
        else:
            print(" |>| Przesyłkę nr {}. ({} kg), przekierowano do nowej PACZKI NR [{}].".format(
            parcel_num, weight, pack_num + 2))
            if_full = True
    else:
        parcels.append(float(round(weight, 3)))
        pack_weight += weight
        total_weight += weight
        parcel_num += 1
        print(" |>| Przesyłkę nr {}. ({} kg) dodano do PACZKI NR [{}].".format(
            parcel_num, weight, pack_num + 1))
        if quantity_parcels == 1:
            to_ship = True
        else:
            to_ship = None
    quantity_parcels -= 1
    while to_ship and total_weight > 0:
        print(" |>>>| PACZKA NR [{}], o łącznej wadze {} kg, w przygotowaniu... ".format(
            pack_num + 1, pack_weight))
        animation("* ", 2)
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
    print(" |>>>| PACZKA NR [{}], o łącznej wadze przesyłek: {} kg, w przygotowaniu... ".format(
        pack_num + 1, pack_weight))
    animation("* ", 2)
    packs.append(float(round(pack_weight, 3)))
    pack_num += 1

if not parcel_num:
    print(" |i| Nie otrzymano przesyłek do wysłania. Żadnej PACZKI nie nadano.")
else:
    dividing_line("*", 80)
    print("\n |i| Wszystkie przyjęte przesyłki wysłano.")
    print(" |i| Łącznie wysłano PACZEK: {}, w których umieszczono przesyłek: {}.".format(
        len(packs), len(parcels)))
    print(" |i| Łącznie wszystkie wysłane przesyłki ważyły:\t{} kg".format(
        round(total_weight), 3))
    y = float(round((20 * pack_num - total_weight), 3))
    print(" |i| Pusta przestrzeń w PACZKACH wyniosła:\t\t{} kg".format(y))
    min_pack_weight, id_pack = float(round(20, 3)), 0
    for i in range(pack_num):
        if packs[i] < min_pack_weight:
            min_pack_weight = packs[i]
            id_pack = i
    print(" |i| Najmniej ekonomiczna paczka:\t\t\tPACZKA NR [{}]".format(
        id_pack + 1))
dividing_line("*", 80)
