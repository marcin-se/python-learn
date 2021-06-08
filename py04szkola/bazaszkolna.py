# SZKOŁA v1.0
# -*- coding: UTF-8 -*-
import sys, os, shelve

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
fileBase = open("baza.txt", "w+", encoding="utf8")
fileBase.close()


def school_ask():
    print("Chcesz uzyskać informację o: ", end="")
    return str(input())


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def view(self):
        print("{} {}".format(self.firstname, self.lastname))


class Logger:
    def __init__(self, Person):
        self.list = []
    def add(self):
        self.list.append(msg)
    def print(self):
        print("\n".join(self.list))
        self.list = []


class Pupil:
    def __init__(self, clas):
        self.clas = clas
    def ask(self):
        print("Podaj liczbę sztuk")
        return int(input())
    def print(self, howmuch):
        print("Zamówiono {} liczbę sztuk".format(howmuch))
    def price(self, howmuch):
        return howmuch * self.price


class Teacher:
    def __init__(self, price, size):
        self.price = price
        self.size = size
    def ask(self):
        print("Podaj liczbę sztuk")
        return int(input())
    def print(self, howmuch):
        packs = int((howmuch + self.size - 1) / self.size)
        print("Zamówiono {} liczbę paczek".format(packs))
    def price(self, howmuch):
        packs = int((howmuch + self.size - 1) / self.size)
        return packs * self.price


class Educator:
    def __init__(self, price, loss, unit):
        self.price = price
        self.loss = loss
        self.unit = unit
    def ask(self):
        print("Podaj ilość ({})".format(self.unit))
        return floor(input())
    def print(self, howmuch):
        print("Zamówiono {} ({})".format(howmuch, self.unit))
    def price(self, howmuch):
        return self.price * howmuch * (1 + self.loss)


positions: tuple = ("uczeń", "nauczyciel", "wychowawca")
classes: tuple = ("1a", "1b", "1c", "1d", "2a", "2b", "2c", "2d", "3a", "3b",
                  "3c", "3d")
subjects: tuple = ("polski", "angielski", "matematyka", "geografia", "fizyka",
                   "biologia", "chemia")
persons: dict = {
    "Adam Nowak": {"status": 0, "klasa": "1a"},
    "Aleksandra Wrona": {"status": 0, "klasa": "2a"},
    "Wiesław Zasada": {
        "status": 1,
        "przedmiot": "jezyk polski",
        "klasa": ["1a", "1b", "1c", "2a", "2b",
                  "2c", "3a", "3b", "3c"]
    },
    "Danuta Rinn": {
        "status": 1,
        "przedmiot": "matematyka",
        "klasa": ["1a", "1c", "2a", "2b", "3b", "3d"]
    },
    "Bogdan Smoleń": {
        "status": 2,
        "klasa": ["1a", "2b", "3d"]
    },
    "Genowefa Pigwa": {
        "status": 2,
        "klasa": ["2a", "3a"]
    },
}

def print_pupils(kl = ""):
    info = persons.copy()
    i = 0
    for key, value in info.items():
        if value["status"] == 0 and value["klasa"] == kl:
            i += 1
            print("{}. {}".format(i, key))
    if i == 0:
        print("Brak uczniów w tej klasie.")
    print("")

def print_pupil(nm = ""):
    info = persons.copy()
    i = 0
    for key, value in info.items():
        if value["status"] == 1:
            if persons[nm]["klasa"] == value["klasa"]:
                i += 1
                print("{}. Nauczyciel: {}, przedmiot: {}".format(
                    i, key, value["przedmiot"]))
    if i == 0:
        print("{} nie ma zajęć.".format(nm))
    print("")

def print_teacher(nm = ""):
    info = persons.copy()
    i = 0
    print("{}, uczy z przedmiotu: {}.".format(nm, persons[nm]["przedmiot"]))
    for key, value in info.items():
        if value["status"] == 2:
            for klasa in range(len(persons[nm]["klasa"])):
                if value["klasa"][i] == persons[nm]["klasa"]:
                    print("Klasa {}:, wychowawca: {}\n".format(value["klasa"][i], nm))
                    i += 1
    if i == 0:
        print("Brak wychowawców.")
    print("")

def print_educator(nm = ""):
    info = persons.copy()
    for key, value in info.items():
        if value["status"] == 2:
            print("{}, prowadzi klasy:".format(nm))
            for k in range(len(value["klasa"])):
                print("{}".format(value["klasa"][k]))
    print("")

def print_klasa(name = ""):
    #info = shelve.open("baza")
    klasa = classes.index(kl)
    info = persons.copy()
    for key, value in info.items():
        if value["status"] == 2:
            print("{}: {}, klasy:".format(info.get("status"), key))
            for k in range(len(value["klasa"])):
                print("{}".format(value["klasa"][k]))
    print("")

'''
    for i in range(len(info)):
        for j in range(len(info.items())):
            if n in info.items():
                print("Uczniowie: {}\n".format(info([k][n])))
'''
print("Uczniowie: ")
print_pupils("1a")

print("Uczeń: ", end="")
pupil = "Aleksandra Wrona"
print_pupil(pupil)

print("Nauczyciel: ", end="")
teacher = "Danuta Rinn"
print_teacher(teacher)

print("Wychowawca: ", end="")
educator = "Genowefa Pigwa"
print_educator(educator)


'''
print("Nauczyciele: {}".format())
print("Wychowawcy: {}".format())

t = raw_input("Wpisz liczbę od 1 do 59>")
print("Wartość: {}".format(print_uczen()))
'''