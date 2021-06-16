# SZKOLA v1.3
# -*- coding: UTF-8 -*-
import sys, os, pickle

pathCast: str = "obsada.txt"
pathBase: str = "baza.txt"

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

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

states: tuple = ("uczeń", "nauczyciel", "wychowawca")
dict_groups: dict = {} # name, educator, [pupils], {teachers}
# list_pupils: list = [] # name, state, [group]
# list_teachers: list = [] # name, state, [group], subject
# list_educators: list = [] # name, state, [group]

class Group:
    # klasa tworząca obiekty grup klasowych
    def __init__(self, name):
        self.name = name
        self.educator = ""
        self.pupils = []
        self.teachers = {}
    def print_pupils(self):
        if self.name in dict_groups:
            for pos in dict_groups["pupils"]:
                print("{:2}. {}".format(pos.index() + 1, pos))
        else:
            print("Błąd 'print_pupils'")
    def if_class(self):
        if self.name in dict_groups:
            edu = self.name["educator"]
            print("W klasie {} wychowcą jest: {}".format(self.name, edu))
            print("Uczniowie klasy {}:\n".format(self.name))
            Group.print_pupils(self.name)
        else:
            print("Błąd 'if_class'")

class Person:
    # klasa bazowa dla klas: uczeń/nauczyciel/wychowawca
    def __init__(self, name):
        self.name = None
        self.state = None
        self.group = None
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
    # klasa tworząca obiekty uczniów
    def set_state(self):
        self.state = "uczeń"
    def set_group(self, get_group):
        if get_group in dict_groups:
            group_obj = dict_groups[get_group]
        else:
            group_obj = Group(get_group)
            dict_groups[get_group] = group_obj
        self.group.append(group_obj)
        group_obj.pupils.append(self)
    def if_pupil(self):
        if self.name in dict_groups:
            kl = dict_groups.__name__
            print("Podany uczeń (klasa {}) ma przedmioty:".format(kl))
            for pos in dict_groups["teachers"]:
                subj = dict_groups["teachers"][pos]
                print("Przedmiot: {}, nauczyciel: {}.".format(subj, pos))
        else:
            print("Błąd 'if_pupil'")

class Teacher(Person):
    # klasa tworząca obiekty nauczycieli
    def set_state(self):
        self.state = "nauczyciel"
    def set_subject(self, get_subject):
        self.subject = get_subject
    def set_group(self, get_group):
        if get_group in dict_groups:
            group_obj = dict_groups[get_group]
        else:
            group_obj = Group(get_group)
            dict_groups[get_group] = group_obj
        self.group.append(group_obj)
        group_obj.teachers[self.name] = self.subject
    def if_teacher(self):
        if self.name in dict_groups["teachers"]:
            kl = dict_groups.__name__
            edu = dict_groups["educator"]
            print("Podany nauczyciel ma zajęcia w klasach:")
            print("Klasa {}, wychowawca: {}".format(kl, edu))
        else:
            print("Błąd 'if_teacher'")

class Educator(Person):
    # klasa tworząca obiekty wychowawców
    def set_state(self):
        self.state = "wychowawca"
    def set_group(self, get_group):
        if get_group in dict_groups:
            group_obj = dict_groups[get_group]
        else:
            group_obj = Group(get_group)
            dict_groups[get_group] = group_obj
        self.group.append(group_obj)
        group_obj.educator = self.name
    def if_educator(self):
        if self.name in dict_groups["educator"]:
            kl = dict_groups.__name__
            print("Podany wychowawca prowadzi klasy:")
            print("Klasa {}, uczniowie:".format(kl))
            Group.print_pupils(kl)
        else:
            print("Błąd 'if_educator'")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# def if_pupil(name):
#     for i in dict_groups:
#         if name in i.pupils:
#             kl = i.name
#             print("Podany uczeń (klasa '{})' ma przedmioty:".format(kl))
#             for j in i.teachers:
#                 teach = i.teachers[j]
#                 subj = Person.get_subject(teach)
#                 print("Przedmiot: {}, nauczyciel: {}.".format(subj, teach))
#         else:
#             print("Błąd 'if_pupil'")

# def if_teacher(name):
#     for i in dict_groups:
#         if name in i.teachers:
#             print("Podany nauczyciel ma zajęcia w klasach:")
#             print("Klasa {}, wychowawca: {}".format(i.name, i.educator))
#         else:
#             print("Błąd 'if_teacher'")

# def if_educator(name):
#     for i in list_groups:
#         if name == i.educator:
#             print("Podany wychowawca prowadzi klasy:")
#             print("Klasa {}, uczniowie:".format(i.name))
#             print_pupils(i.name)
#         else:
#             print("Błąd 'if_educator'")

# def print_pupils(kl):
#     if kl in dict_groups:
#         for pos in dict_groups["pupils"]:
#             print("{}. {}".format(pos.index()+1, pos))
#     else:
#         print("Błąd 'print_pupils'")

# def if_class(kl):
#     if kl in dict_groups:
#         kl = dict_groups.__name__
#         edu = dict_groups["educator"]
#         print("W klasie {} wychowcą jest: {}".format(kl, edu))
#         print("Uczniowie klasy {}:\n".format(kl))
#         print_pupils(kl)
#     else:
#         print("Błąd 'if_class'")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# def main():

clear_screen()
get_data = ""
# data from <*.txt>
with open(pathCast, "a+", encoding="utf8") as fileCast:
    line_file = pickle.dumps(fileCast.readlines())
    for line in line_file:
        dict_groups = pickle.loads(line_file)

if len(sys.argv) == 1:
    title_line(" (edycja) BAZA-SZKOŁA v1.3 ")
    while True:
        print("Podaj stanowisko (lub 'koniec'): ", end="")
        get_data = str.lower(input())
        if get_data == "koniec":
            break

        if get_data == "uczeń":
            full_name = str.title(input("Imię Nazwisko: "))
            new_pupil = Pupil(full_name)
            new_pupil.set_state()
            clase = str.lower(input("Klasa: "))
            new_pupil.set_group(clase)
            # # zapis UCZNIA do pliku >>> baza.txt
            # with open(pathBase, "a+") as fileBase:
            #     fileBase.write("{}\n".format(...)
            continue

        if get_data == "nauczyciel":
            full_name = str.title(input("Imię Nazwisko: "))
            new_teacher = Teacher(full_name)
            new_teacher.set_state()
            new_subject = str.lower(input("Przedmiot: "))
            new_teacher.set_subject(new_subject)
            while 1:
                clase = str.lower(input("Klasa: "))
                if clase: new_teacher.set_group(clase)
                else: break
            # # zapis NAUCZYCIELA do pliku >>> baza.txt
            # with open(pathBase, "a+") as fileBase:
            #     fileBase.write("{}\n".format(...)
            continue

        if get_data == "wychowawca":
            full_name = str.title(input("Imię Nazwisko: "))
            new_educator = Educator(full_name)
            new_educator.set_state()
            while 1:
                clase = str.lower(input("Klasa: "))
                if clase: new_educator.set_group(clase)
                else: break
            # # zapis WYCHOWAWCY do pliku >>> baza.txt
            # with open(pathBase, "a+") as fileBase:
            #     fileBase.write("{}\n".format(...)
            continue

elif len(sys.argv) > 1:
    title_line(" (przegląd) BAZA-SZKOŁA v1.3 ")
    get_data = str.lower(sys.argv[1])
    while get_data != "koniec":
        if len(sys.argv) == 2:
            if sys.argv[1] in dict_groups:
                kl = sys.argv[1].get_group()
                Group.if_class(kl)
            else: print("Brak klasy w bazie danych!")
            break

        if len(sys.argv) == 3:
            full_name = str.title(sys.argv[2]) + " " + str.title(sys.argv[3])

            if full_name in dict_groups["pupils"]: Pupil.if_pupil(full_name)
            elif full_name in dict_groups: Teacher.if_teacher(full_name)
            elif full_name in dict_groups: Educator.if_educator(full_name)
            else: print("Brak podanej osoby w bazie danych!")
            break

        else:
            print("Niewłaściwa liczba parametrów!")
            break
    input("Press any key to continue...")

# data to <*.txt>
with open(pathBase, "w+", encoding="utf8") as fileBase:
    for line in dict_groups:
        fileBase.write("{}\n".format(line))


# if __name__ == "__main__": main()