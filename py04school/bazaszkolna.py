# SZKOLA v1.3
# -*- coding: UTF-8 -*-
import sys
from library.zapis_odczyt_plik_terminal import dict_from_file, dict_to_file
from library.dodatki import clear_screen, title_line
from library.klasy_metody_funkcje import Pupil, Teacher, Educator, make_group
# if_class, if_class_obj, if_pupil, if_pupil_obj, if_teacher, \
# if_teacher_obj, if_educator, if_educator_obj

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

pathBase: str = "baza.txt"
get_data = ""
states: tuple = ("uczeń", "nauczyciel", "wychowawca")
group_objects: dict = {}
dict_groups: dict = {}
# Struktura słownika z grupami:
#   dict_groups = {
#       nazwa klasy: {
#                     educator: imię nazwisko,
#                     pupils: [imię nazwisko, imię nazwisko, ... ],
#                     teachers: {przedmiot: imię nazwisko,
#                                przedmiot: imię nazwisko, ... }
#   }


# funkcja zwracająca odpowiedź na:  KLASA
def if_class(name=""):
    edu = str(dict_groups[name]["educator"])
    print("W klasie {} wychowcą jest: {}".format(name, edu))
    print("Uczniowie klasy {}:\n".format(name))
    print_pupils(name)


def if_class_obj(name=""):
    edu = group_objects[name].educator
    print("W klasie {} wychowcą jest: {}".format(name, edu))
    print("Uczniowie klasy {}:\n".format(name))
    print_pupils(name)


# funkcja zwracająca odpowiedź na:  UCZEŃ
def if_pupil(name=""):
    for key, value in dict_groups.items():
        if name in dict_groups[key]["pupils"]:
            print("Klasa {} ma przedmioty:".format(key))
            for sub, teach in dict_groups[key]["teachers"].items():
                print("Przedmiot: {}, nauczyciel: {}.".format(sub, teach))


def if_pupil_obj(name=""):
    for key, value in group_objects.items():
        if name in value.pupils:
            print("Klasa {} ma przedmioty:".format(key))
            for sub, teach in value.teachers.items():
                print("Przedmiot: {}, nauczyciel: {}.".format(sub, teach))


# funkcja zwracająca odpowiedź na:  NAUCZYCIEL
def if_teacher(name=""):
    print("Podany nauczyciel ma zajęcia w klasach:")
    for key, value in dict_groups.items():
        if name in dict_groups[key]["teachers"]:
            edu = str(dict_groups[key]["educator"])
            print("Klasa {}, wychowawca: {}".format(key, edu))


def if_teacher_obj(name=""):
    print("Podany nauczyciel ma zajęcia w klasach:")
    for key, value in group_objects.items():
        if name in value.teachers:
            edu = value.educator
            print("Klasa {}, wychowawca: {}".format(key, edu))


# funkcja zwracająca odpowiedź na:  WYCHOWAWCA
def if_educator(name=""):
    print("Podany wychowawca prowadzi klasy:")
    for key, value in dict_groups.items():
        if name in dict_groups["educator"]:
            print("Klasa {}, uczniowie:".format(key))
            print_pupils(key)


def if_educator_obj(name=""):
    print("Podany wychowawca prowadzi klasy:")
    for key, val in group_objects.items():
        if name in val.educator:
            print("Klasa {}, uczniowie:".format(key))
            print_pupils(key)


# funkcja zwracająca listę uczniów danej klasy
def print_pupils(clase_name=""):
    if clase_name in dict_groups:
        for value in dict_groups[clase_name]["pupils"]:
            print(value)


def print_pupils_obj(clase_name=""):
    if clase_name in dict_groups:
        for value in dict_groups[clase_name]["pupils"]:
            print(value)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


clear_screen()
dict_groups.update(dict_from_file(pathBase))    # read data from <*.txt>

if len(sys.argv) == 1:
    title_line(" (edycja) BAZA-SZKOŁA v1.3 ")
    while 1:
        print("Podaj stanowisko (lub 'koniec'): ", end="")
        get_data = str.lower(input())
        if get_data == "koniec":
            break

        if get_data == "uczeń":
            full_name = str.title(input("Imię Nazwisko: "))
            new_pupil = Pupil(full_name)
            clase = str.lower(input("Klasa: "))
            new_group = make_group(clase)
            new_group.pupils.append(new_pupil)
            dict_groups[clase]["pupils"].append(new_pupil)
            new_pupil.set_group(clase)
            continue

        if get_data == "nauczyciel":
            full_name = str.title(input("Imię Nazwisko: "))
            new_teacher = Teacher(full_name)
            new_subject = str.lower(input("Przedmiot: "))
            new_teacher.set_subject(new_subject)
            while 1:
                clase = str.lower(input("Klasa: "))
                if clase:
                    new_group = make_group(clase)
                    new_teacher.set_groups(clase)
                    new_group.teachers[new_subject] = new_teacher
                    dict_groups[clase]["teachers"][new_subject] = new_teacher
                else:
                    break
            continue

        if get_data == "wychowawca":
            full_name = str.title(input("Imię Nazwisko: "))
            new_educator = Educator(full_name)
            while 1:
                clase = str.lower(input("Klasa: "))
                if clase:
                    new_group = make_group(clase)
                    new_educator.set_groups(clase)
                    new_group.educator = new_educator
                    dict_groups[clase]["educator"] = new_educator
                else:
                    break
            continue

if len(sys.argv) > 1:
    title_line(" (przegląd) BAZA-SZKOŁA v1.3 ")
    get_data = str.lower(sys.argv[1])
    while 1:
        if get_data == "koniec":
            break

        if len(sys.argv) == 2:
            if get_data in dict_groups.keys():
                if_class(get_data)
                if_class_obj(get_data)
            else:
                print("Brak podanej klasy w bazie danych!")
            break

        if len(sys.argv) == 3 or len(sys.argv) == 4:
            full_name = str.title(sys.argv[1]) + " " + str.title(sys.argv[2])
            if len(sys.argv) == 4:
                full_name += " " + str.title(sys.argv[3])
            if full_name in dict_groups.values():
                if_pupil(full_name)
                if_pupil_obj(full_name)
            elif full_name in dict_groups.values():
                if_teacher(full_name)
                if_teacher_obj(full_name)
            elif full_name in dict_groups.values():
                if_educator(full_name)
                if_educator_obj(full_name)
            else:
                print("Brak podanej osoby w bazie danych!")
            break

        if len(sys.argv) > 4:
            print("Niewłaściwa liczba argumentów!")
            break
    input("Press any key to continue...")

dict_to_file("baza.txt", dict_groups)   # save data to <*.txt>
