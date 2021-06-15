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
        self.teachers = {}

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
        return sorted(self.group)
    def get_subject (self):
        return self.subject

class Pupil(Person):
    def set_state(self):
        self.state = "uczeń"
    def set_group(self, group):
        if group in groups:
            group_obj = groups[group]
        else:
            group_obj = Group(group)
            groups[group] = group_obj
        self.group.append(group)
        group_obj.pupils.append(self)

class Teacher(Person):
    def set_state(self):
        self.state = "nauczyciel"
    def set_subject(self, subject):
        self.subject = subject
    def set_group(self, group):
        if group in groups:
            group_obj = groups[group]
        else:
            group_obj = Group(group)
            groups[group] = group_obj
        self.group.append(group)
        group_obj.teachers[self.name] = self.subject

class Educator(Person):
    def set_state(self):
        self.state = "wychowawca"
    def set_group(self, group):
        if group in groups:
            group_obj = groups[group]
        else:
            group_obj = Group(group)
            groups[group] = group_obj
        self.group.append(group)
        group_obj.educator = self.name

states: tuple = ("uczeń", "nauczyciel", "wychowawca")
groups: dict = {} # name, educator, [pupils], [teachers]


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

def print_pupils(kl):
    if kl in groups:
        for i in range(len(groups[kl].pupils)):
            print("{}. {}".format(i+1, groups[kl][pupils][i]))
    else:
        print("Brak uczniów w tej klasie.")

def if_pupil(name):
    kl = name.get_group()
    for i in range(len(groups.items())):
        if name in kl.groups.pupils:
            if name in kl.groups.teachers:
                print("Podany uczeń ma przedmioty:")
                for key, value in kl.groups.teachers:
                    print(value + ": " + key)
        else:
            print("Błąd 'if_pupil'")

def if_teacher(name):
    for i in range(len(groups.items())):
        if name in groups[i].teachers:
            print("Podany nauczyciel ma zajęcia w klasach:")
            print("Klasa {}, wychowawca: {}".
                  format(groups[i].name, groups[i].educator))
        else:
            print("Błąd 'if_teacher'")

def if_educator(name):
    for i in range(len(groups.items())):
        if name == groups[i].educator:
            print("Podany wychowawca prowadzi klasy:")
            print("Klasa {}, uczniowie:".format(groups[i].name))
            print_pupils(groups[i].name)
        else:
            print("Błąd 'if_educator'")

def if_class(kl):
    for i in range(len(groups.keys())):
        if kl == groups[i]:
            print("Klasa: {}, wychowawca: {}.".format(
                kl, groups[kl]["educator"]))
            print_pupils(kl)
        else:
            print("Błąd 'if_class'")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

argvCurrent: list = []
get_data = ""

pupils: dict = {}
teachers: dict = {}
educators: dict = {}
classes: list = []
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
            # # zapis UCZNIA do pliku >>> baza.txt
            # with open(pathBase, "a+") as fileBase:
            #     fileBase.write("{}\n".format(pupils[full_name][clase]))
            # dividing_line()

            dividing_line()
            x = new_pupil.get_group()
            print("{}: {} \t(klasa {})".format(
                new_pupil.get_state(), new_pupil.get_name(), x[0]))
            dividing_line()

        elif get_data == "nauczyciel":
            full_name = str.title(input("Imię Nazwisko: "))
            new_teacher = Teacher(full_name)
            new_teacher.set_state()
            new_subject = str.lower(input("Przedmiot: "))
            new_teacher.set_subject(new_subject)
            while 1:
                clase = str.lower(input("Klasa: "))
                if clase:
                    new_teacher.set_group(clase)
                else:
                    break

            dividing_line()
            print("{}: {}\t (przedmiot: {})".format(new_teacher.get_state(),
                new_teacher.get_name(), new_teacher.get_subject()))
            dividing_line()
            x = new_teacher.get_group()
            for i in range(len(x)): print(f"{x[i]}  ", end="")
            print()
            dividing_line()
            # # zapis NAUCZYCIELA do pliku >>> baza.txt
            # with open(pathBase, "a+") as fileBase:
            #     fileBase.write("{}\n".format(teachers[full_name][clase]))

        elif get_data == "wychowawca":
            full_name = str.title(input("Imię Nazwisko: "))
            new_educator = Educator(full_name)
            new_educator.set_state()
            while 1:
                clase = str.lower(input("Klasa: "))
                if clase:
                    new_educator.set_group(clase)
                else:
                    break
            # # zapis WYCHOWAWCY do pliku >>> baza.txt
            # with open(pathBase, "a+") as fileBase:
            #     fileBase.write("{}\n".format(educators[full_name][clase]))

            dividing_line()
            print("{}: {}".format(
                new_educator.get_state(), new_educator.get_name()))
            dividing_line()
            x = new_educator.get_group()
            for i in range(len(x)): print(f"{x[i]}  ", end="")
            print()
            dividing_line()

        elif get_data == "koniec":
            break

    dividing_line()
    print(groups)
    dividing_line()
    print(len(groups.items()))
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
        print("Tu jestem...")
        if len(sys.argv) == 2:
            if sys.argv[1] in groups:
                print("...a może 'in groups'")
                if_class(get_data)
            else:
                print("Brak klasy w bazie danych!")
            break

        elif len(sys.argv) == 3:
            full_name = str.title(sys.argv[2]) + " " + str.title(sys.argv[3])
            if full_name:
                print("...a może 'among people'")
                if_pupil(full_name)
                if_teacher(full_name)
                if_educator(full_name)
            else:
                print("Brak podanej osoby w bazie danych!")
            break

                # if full_name in teachers:
                #     print("...a może 'in teachers'")
                #     if_teacher(full_name)
                # else:
                #     print("Brak nauczyciela w bazie danych!")
                #
                # if full_name in educators:
                #     print("...a może 'in educators'")
                #     if_educator(full_name)
                # else:
                #     print("Brak wychowawcy w bazie danych!")

        else:
            print("Niewłaściwa liczba parametrów!")
            break
    input("Press any key to continue...")
