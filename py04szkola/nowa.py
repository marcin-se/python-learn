# SZKOLA v1.2
# -*- coding: UTF-8 -*-
import sys, os
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
pathCast: str = "obsada.txt"
pathBase: str = "baza.txt"

fileCast = open(pathCast, "a+", encoding="utf8")
fileCast.close()
fileBase = open(pathBase, "a+", encoding="utf8")
fileBase.close()

def clear_screen():
    if os.name == 'posix':  # dla mac i linux
        _ = os.system('clear')
    else:
        _ = os.system('cls')  # dla windows
    return
def dividing_line(stamp="-", repeat=55):
    print("+" + stamp * repeat + "+")
    return
def title_line(text="none"):
    repeat = 55
    textline = str(text.upper())
    dividing_line("-", repeat)
    lenght = round((repeat - 2 - len(text))/2)
    print("|{} {} {}|".format("-"*lenght, textline, "-"*lenght))
    dividing_line("-", repeat)

# def check_file_append(path):
#     try:
#         if os.path.exists(path):
#             file = open(path, "a+", encoding="utf8")
#             file.close()
#         else:
#             print("Ścieżka do pliku nie istnieje!")
#     except IOError:
#         print("Błąd przetwarzania pliku!")
#
# def check_file_read(path):
#     try:
#         if os.path.exists(path):
#             file = open(path, "r+", encoding="utf8")
#             file.close()
#         else:
#             print("Ścieżka do pliku nie istnieje!")
#     except IOError:
#         print("Błąd przetwarzania pliku!")

class Group:
    def __init__(self, name):
        self.name = name
        self.educator = ""
        self.pupils = []
        self.teachers = []

class Person:
    def __init__(self, name):
        self.name = name
        self.state = ""
        self.group = []
        self.subject = None
    def get_name(self):
        return self.name
    def get_state (self):
        return self.state
    def get_group (self):
        return self.group
    def get_subject (self):
        return self.subject

class Pupil(Person):
    def set_state(self):
        self.state = "uczeń"
    def set_group(self, group):
        if group in list_groups:
            ind = list_groups.index(group)
            group_obj = list_groups[ind]
        else:
            group_obj = Group(group)
            list_groups.append(group_obj)
        self.group.append(group)
        self.group = sorted(self.group)
        group_obj.pupils.append(self)

class Teacher(Person):
    def set_state(self):
        self.state = "nauczyciel"
    def set_subject(self, subject):
        self.subject = subject
    def set_group(self, group):
        if group in list_groups:
            ind = list_groups.index(group)
            group_obj = list_groups[ind]
        else:
            group_obj = Group(group)
            list_groups.append(group_obj)
        self.group.append(group)
        self.group = sorted(self.group)
        group_obj.teachers[self.name] = self.subject

class Educator(Person):
    def set_state(self):
        self.state = "wychowawca"
    def set_group(self, group):
        if group in list_groups:
            ind = list_groups.index(group)
            group_obj = list_groups[ind]
        else:
            group_obj = Group(group)
            list_groups.append(group_obj)
        self.group.append(group)
        self.group = sorted(self.group)
        group_obj.educator = self.name

states: tuple = ("uczeń", "nauczyciel", "wychowawca")
list_groups: list = [] # name, educator, [pupils], [teachers]
list_pupils: list = [] # name, state, [group]
list_teachers: list = [] # name, state, [group], subject
list_educators: list = [] # name, state, [group]


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# def print_info(nm = "", **opcje):
#     if opcje.get("get") == "stat":
#         if nm in pupils:
#             return pupils[nm]["status"]
#         if nm in teachers:
#             return teachers[nm]["status"]
#         if nm in educators:
#             return educators[nm]["status"]
#     if opcje.get("get") == "sub":
#         if nm in pupils:
#             return pupils[nm]["przedmiot"]
#         if nm in teachers:
#             return teachers[nm]["przedmiot"]
#         if nm in educators:
#             return educators[nm]["przedmiot"]
#     if opcje.get("get") == "kl":
#         if nm in classes:
#             return subjects[classes][nm]["klasa"]

def if_pupil(name):
    for i in range(len(list_groups)):
        if name in list_groups[i].pupils:
            kl = list_groups[i].name
            print("Podany uczeń z klasą '{}' ma przedmioty:".format(kl))
            for j in range(len(list_groups[i].teachers)):
                teach = list_groups[i].teachers[j]
                subj = Person.get_subject(teach)
                print("Przedmiot: {}, nauczyciel: {}.".format(subj, teach))
        else:
            print("Błąd 'if_pupil'")

def if_teacher(name):
    for i in range(len(list_groups.items())):
        if name in list_groups[i].list_teachers:
            print("Podany nauczyciel ma zajęcia w klasach:")
            print("Klasa {}, wychowawca: {}".
                  format(list_groups[i].name, list_groups[i].educator))
        else:
            print("Błąd 'if_teacher'")

def if_educator(name):
    for i in range(len(list_groups.items())):
        if name == list_groups[i].educator:
            print("Podany wychowawca prowadzi klasy:")
            print("Klasa {}, uczniowie:".format(list_groups[i].name))
            print_pupils(list_groups[i].name)
        else:
            print("Błąd 'if_educator'")

def print_pupils(kl):
    for i in range(len(list_groups)):
        if kl == list_groups[i].name:
            for j in range(len(list_groups[i].pupils)):
                print("{}. {}".format(j+1, list_groups[i].pupils[j]))
        else:
            print("Błąd 'print_pupils'")

def if_class(kl):
    for i in range(len(list_groups)):
        if kl == list_groups[i].name:
            print("Klasa: {}, wychowawca: {}.".format(
                kl, list_groups[i].educator))
            print_pupils(kl)
        else:
            print("Błąd 'if_class'")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

get_data = ""
clear_screen()

if len(sys.argv) == 1:
    title_line("BAZA-SZKOŁA v1.2 (Edycja)")
    while get_data != "koniec":
        print("Wpisz 'koniec' lub podaj stanowisko: ", end="")
        get_data = str.lower(input())

        if get_data == "uczeń":
            full_name = str.title(input("Imię Nazwisko: "))
            new_pupil = Pupil(full_name)
            new_pupil.set_state()
            clase = str.lower(input("Klasa: "))
            new_pupil.set_group(clase)
            list_pupils.append(new_pupil)
            # # zapis UCZNIA do pliku >>> baza.txt
            # with open(pathBase, "a+") as fileBase:
            #     fileBase.write("{}\n".format(pupils[full_name][clase]))
            # dividing_line()

        elif get_data == "nauczyciel":
            full_name = str.title(input("Imię Nazwisko: "))
            new_teacher = Teacher(full_name)
            new_teacher.set_state()
            new_subject = str.lower(input("Przedmiot: "))
            new_teacher.set_subject(new_subject)
            while 1:
                clase = str.lower(input("Klasa: "))
                if clase: new_teacher.set_group(clase)
                else: break
            list_teachers.append(new_teacher)
            # # zapis NAUCZYCIELA do pliku >>> baza.txt
            # with open(pathBase, "a+") as fileBase:
            #     fileBase.write("{}\n".format(teachers[full_name][clase]))

        elif get_data == "wychowawca":
            full_name = str.title(input("Imię Nazwisko: "))
            new_educator = Educator(full_name)
            new_educator.set_state()
            while 1:
                clase = str.lower(input("Klasa: "))
                if clase: new_educator.set_group(clase)
                else: break
            list_educators.append(new_educator)
            # # zapis WYCHOWAWCY do pliku >>> baza.txt
            # with open(pathBase, "a+") as fileBase:
            #     fileBase.write("{}\n".format(educators[full_name][clase]))

        elif get_data == "koniec":
            break

    dividing_line()
    print(list_groups)
    dividing_line()
    print(len(list_groups.items()))
    dividing_line()
    if_pupil("Jan Nowak")
    if_teacher("Sam Dan")
    if_educator("Dan Mat")
    if_class("1a")
    # print(groups[teachers])
    dividing_line()
    # print(subjects)
    # print(subjects[classes])
    dividing_line()

elif len(sys.argv) > 1:
    title_line("BAZA-SZKOŁA v1.2 (Przzegląd)")
    get_data = str.lower(sys.argv[1])
    while get_data != "koniec":
        if len(sys.argv) == 2:
            if sys.argv[1] in list_groups: if_class(get_data)
            else: print("Brak klasy w bazie danych!")
            break

        elif len(sys.argv) == 3:
            full_name = str.title(sys.argv[2]) + " " + str.title(sys.argv[3])
            if full_name in list_pupils: if_pupil(full_name)
            elif full_name in list_teachers: if_teacher(full_name)
            elif full_name in list_educators: if_educator(full_name)
            else: print("Brak podanej osoby w bazie danych!")
            break

        else:
            print("Niewłaściwa liczba parametrów!")
            break
    input("Press any key to continue...")
