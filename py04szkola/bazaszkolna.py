# SZKOŁA v1.0
# -*- coding: UTF-8 -*-
import sys, os

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
fileBase = open("baza.txt", "w+", encoding="utf8")
fileBase.close()

'''
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
'''

positions: tuple = ("Uczeń", "Nauczyciel", "Wychowawca")
classes: tuple = ("1a", "1b", "1c", "1d", "2a", "2b", "2c", "2d", "3a", "3b",
                  "3c", "3d")
subjects: tuple = ("język polski", "angielski", "matematyka", "geografia",
                   "fizyka", "biologia", "chemia")
persons: dict = {
    "Adam Nowak": {"status": "Uczeń", "klasa": ("1a")},
    "Aleksandra Wrona": {"status": "Uczeń", "klasa": ("2b")},
    "Wiesław Zasada": {
            "status": "Nauczyciel",
            "przedmiot": "jezyk polski",
            "klasa": ("1a", "1b", "1c", "2a", "2b", "2c", "3a", "3b", "3c")},
    "Danuta Rinn": {
            "status": "Nauczyciel",
            "przedmiot": "matematyka",
            "klasa": ("1a", "1c", "2a", "2b", "3b", "3d")},
    "Bogdan Smoleń": {
            "status": "Wychowawca",
            "klasa": ("1a", "1c", "2c", "3a")},
    "Genowefa Pigwa": {
            "status": "Wychowawca",
            "klasa": ("1b", "2a", "2b", "3a")},
    }
pupils: list = ["Adam Nowak", "Aleksandra Wrona"]
teachers: list = ["Wiesław Zasada", "Danuta Rinn"]
educators: list = ["Bogdan Smoleń", "Genowefa Pigwa"]

def print_info(nm = "", **opcje):
    if opcje.get("get") == "stat": return persons[nm]["status"]
    if opcje.get("get") == "sub": return persons[nm]["przedmiot"]
    if opcje.get("get") == "kl": return persons[nm]["klasa"]

def print_pupils(kl = ""):
    info = persons.copy()
    i = 0
    for key, value in info.items():
        if value["status"] == "Uczeń" and value["klasa"] == kl:
            i += 1
            print("{}. {}".format(i, key))
    if not i:
        print("Brak uczniów w tej klasie.")
    print("")

def print_person(nm = ""):
    status = print_info(nm, get="stat")
    clas = print_info(nm, get="kl")
    if status == "Uczeń":
        print("{}: {}, klasa: {}".format(status, nm, clas))
    elif status == "Nauczyciel":
        subject = print_info(nm, get="sub")
        print("{}: {}, przedmiot: {}".format(status, nm, subject))
    elif status == "Wychowawca":
        print("{}: {}".format(status, nm))
    print("")

def if_pupil(nm = ""):
    info = persons.copy()
    clas = print_info(nm, get="kl")
    i = 0
    for key, value in info.items():
        if persons[key]["status"] == "Nauczyciel":
            for i in range(len(persons[key]["klasa"])):
                if clas == persons[key]["klasa"][i]:
                    print_person(key)
    if not i:
        print("Uczeń {} nie ma zajęć z żadnym nauczycielem.".format(nm))
    print("")

def if_teacher(nm = ""):
    info = persons.copy()
    status = print_info(nm, get="stat")
    clas = print_info(nm, get="kl")
    i = 0
    for key, value in info.items():
        if persons[key]["status"] == "Wychowawca":
            for i in range(len(persons[key]["klasa"])):
                for j in range(len(clas)):
                    if persons[key]["klasa"][i] == clas[j]:
                        print("Klasa", clas[j], end=". ")
                        print_person(key)
    if not i:
        print("Brak korelacji tego nauczyciela z wychowawcami.")
    print("")

def if_educator(nm = ""):
    info = persons.copy()
    clas = print_info(nm, get="kl")
    i = 0
    for key, value in info.items():
        if persons[key]["status"] == "Uczeń":
            for i in range(len(clas)):
                if persons[key]["klasa"] == clas[i]:
                        print("Klasa", clas[i])
                        print_pupils(clas[i])
    if not i:
        print("Brak uczniów, których prowadzi ten wychowawca.")
    print("")

def if_klasa(kl = ""):
    info = persons.copy()
    i = 0
    for key, value in info.items():
        clas = print_info(key, get="kl")
        status = print_info(key, get="stat")
        for i in range(len(persons[key]["klasa"])):
            if status == "Wychowawca" and clas[i] == kl:
                print_person(key)
                print_pupils(kl)
    if not i:
        print("Do tej klasy nikt nie należy.")
    print("")


if len(sys.argv) == 2:
    data_ask = sys.argv[2]

    pupil = "Aleksandra "
    teacher = "Danuta Rinn"
    educator = "Genowefa Pigwa"
    print_pupils("1a")
    print_person(pupil)
    if_pupil(pupil)
    print_person(teacher)
    if_teacher(teacher)
    print_person(educator)
    x = print_info(educator, get="kl")
    print(x)
    print_person(educator)
    if_educator(educator)
    if_klasa("2b")



if len(sys.argv) == 1:
    get_data = ""
    print("[[Aby zakończyć, wpisz 'koniec']]")
    while 1:
        # (2) POBRANIE FUNKCJI I NAZWISKA
        print("Podaj, stanowisko osoby wprowadzanej: ", end="")
        get_data = str.title(input().strip())
        firstname, lastname, status, right_data = "", "", "", 0
        class_list: list = []
        if get_data == "koniec":
            print("Zakończono wprowadzanie danych.")
            break
        elif get_data not in positions:
            print("Wprowadzono nieprawidłowe dane.")
        else:
            print('Podaj nazwisko osoby wprowadzanej: ', end="")
            lastname = str.title(input()).strip()
            print('Podaj, imie osoby wprowadzanej: ', end="")
            firstname = str.title(input()).strip()
            full_name = firstname + " " + lastname
            if full_name in pupils or full_name in teachers or full_name in educators:
                print("Podana osoba istnieje już w bazie danych.")
                continue
            if get_data == "Uczeń":
                pupils.append(full_name)
                print('Podaj, do jakiej klasy należy uczeń? (np. 1a ) ', end="")
                clas = str.strip(input())
                clas.lower()
                if clas in classes:
                    persons = {
                        full_name: {
                            "status": "Uczeń",
                            "klasa": clas}
                    }
                    right_data = 1
                else:
                    print("Podana klasa nie istnieje.")
                    continue
            elif get_data == "Nauczyciel":
                teachers.append(full_name)
                print('Podaj, jakiego przedmiotu uczy? (np. angielski) ', end="")
                subject = str.strip(input())
                subject.lower()
                if not subject in subjects:
                    print("Podanego przedmiotu nie uczą w tej szkole.")
                    continue
                print("[[Aby zakończyć, pozostaw pustą linię + 'ENTER']]")
                while get_data != "":
                    print('Podaj, jaką klasę uczy? (np. 1a) ', end="")
                    clas = str.strip(input())
                    clas.lower()
                    if clas in classes:
                        class_list.append(clas)
                        right_data = 1
                    else:
                        print("Podana klasa nie istnieje.")
                        continue
                persons = {
                    full_name: {
                        "status": "Nauczyciel",
                        "przedmiot": subject,
                        "klasa": class_list}
                }
            elif get_data == "Wychowawca":
                educators.append(full_name)
                print("[[Aby zakończyć, pozostaw pustą linię + 'ENTER']]")
                clas = " "
                while clas != "":
                    print('Podaj, którą klasę prowadzi? (np. 1a) ', end="")
                    clas = str.strip(input())
                    clas.lower()
                    if clas in classes:
                        class_list.append(clas)
                        right_data = 1
                    else:
                        print("Podana klasa nie istnieje.")
                        continue
                persons = {
                    full_name: {
                        "status": "Wychowawca",
                        "klasa": class_list}
                }
            clas = ""
            if right_data:
                print("Wprowadzono osobę do bazy.")
            else:
                print("Podano za mało danych, by dodać osobę do bazy.")
                continue


