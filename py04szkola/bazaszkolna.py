# SZKOŁA v1.1
# -*- coding: UTF-8 -*-
import sys, os

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

fileBase = open("baza.txt", "w+", encoding="utf8")
fileBase.close()

def clear_screen():
    if os.name == 'posix':  # dla mac i linux
        _ = os.system('clear')
    else:
        _ = os.system('cls')  # dla windows
    return

def dividing_line(stamp="-", repeat=55):
    print(stamp * repeat)
    return

positions: tuple = ("Uczeń", "Nauczyciel", "Wychowawca")

groups: dict = {}
'''
    "1a": {"name": "1a", "educator": "Wiesław Zasada", "pupils": []},
    "1b": {"name": "1b", "educator": "Danuta Zwyczaj", "pupils": []},
    "1c": {"name": "1c", "educator": "Grzegorz Tradycja", "pupils": []},
    "2a": {"name": "2a", "educator": "Zenobia Obyczaj", "pupils": []},
    "2b": {"name": "2b", "educator": "Halina Reguła", "pupils": []}
'''

subjects: dict = {}
'''
    "język polski":
        {"name": "język polski", "teacher": "Bogdan Poznański", "classes": ()},
    "angielski":
        {"name": "angielski", "teacher": "Genowefa Iława", "classes": ()},
    "matematyka":
        {"name": "matematyka", "teacher": "Stefan Krakowski", "classes": ()},
    "geografia":
        {"name": "geografia", "teacher": "Barbara Śląska", "classes": ()},
    "fizyka":
        {"name": "fizyka", "teacher": "Czesław Mazur", "classes": ()},
    "biologia":
        {"name": "biologia", "teacher": "Janina Pisz", "classes": ()},
    "chemia":
        {"name": "chemia", "teacher": "Patryk Szczeciński", "classes": ()}
'''

class Person:
    def __init__(self, name, state):
        self.name = name
        self.state = state
        print("--- Pomyślnie utworzono konto! ---")
    def get_name (self):
        return self.name
    def get_state (self):
        return self.state
    def get_group (self):
        pass

class Group:
    def __init__(self, name):
        self.name = name
        self.educator = ""
        self.pupils = []
        self.subjects = []
    def who_in_class(self):
        if self.name in groups:
            print(enumerate(self.pupils))
        else:
            print("--- Brak uczniów w tej klasie! ---")


class Subject:
    def __init__(self, name):
        self.name = name
        self.teacher = ""
        self.classes = []
    def who_teaches(self):
        if self.name in subjects:
            print(f"Nauczyciel: {groups[self.name]['teacher']} ({self.name})")
        else:
            print("--- Brak przedmiotu w bazie! ---")

class Pupil(Person):
    def set_group(self, get_class):
        if get_class in groups:
            class_obj = groups[get_class]
        else:
            class_obj = Group(get_class)
            groups[get_class] = class_obj
        self.group = class_obj
        class_obj.pupils.append(self)
    def get_group (self):
        return self.group

class Teacher(Person):
    def set_subject(self, get_subject):
        if get_subject in subjects:
            subject_obj = subjects[get_subject]
        else:
            subject_obj = Subject(get_subject)
            subjects[get_subject] = subject_obj
        self.subject = subject_obj
        subject_obj.teacher = self
    def add_group(self, get_class):
        if get_class in groups:
            class_obj = groups[get_class]
        else:
            class_obj = Group(get_class)
            groups[get_class] = class_obj
        class_obj.subjects.append(self.subject)


class Educator(Person):
    def set_group(self, get_class):
        if get_class in groups:
            class_obj = groups[get_class]
        else:
            class_obj = Group(get_class)
            groups[get_class] = class_obj
        self.group = class_obj
        class_obj.educator = self.name


'''
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
        print("Podany uczeń nie ma zajęć z żadnym nauczycielem.")
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
        print("Podany wychowawca nie prowadzi żadnych uczniów.")
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
'''

# - - - - - - - - - - - - - S - T - A - R - T - - - - - - - - - - - - - - - - #

while 1:
    if len(sys.argv) == 1:
        clear_screen()
        dividing_line()
        get_data, status, right_data = "", "", 0
        print("(Aby zakończyć: wpisz 'KONIEC')")

        while get_data != "koniec":
            # (2.1) POBRANIE STANOWISKA #
            dividing_line()
            print("Podaj, stanowisko osoby wprowadzanej: ", end="")
            get_data = str.title(input()).strip()
            if get_data == str.title("koniec"):
                print("< < < < <   K O N I E C   > > > > > ")
                break
            elif get_data not in positions:
                print("--- Wprowadzono nieprawidłowe dane! ---")
                break
            else:
                print("Podaj imię i nazwisko osoby wprowadzanej: ", end="")
                full_name = str.title(input()).strip()
                if full_name in groups or full_name in subjects:
                    print("--- Ta osoba istnieje już w bazie danych ---")
                    continue
                if get_data == str.title("Uczeń"):
                # (2.1.1.1) POBRANIE KLASY I UTWORZENIE UCZNIA - - - #
                    print("Do której klasy przypisać? (np. 1a) ", end="")
                    clas = str.strip(input())
                    clas.title()
                    pup = Pupil(full_name, "Uczeń")
                    pup.set_group(clas)
                    print(pup.get_state())
                    print(pup.get_name())
                    print(pup.get_group())
                continue
        break

dividing_line()
dividing_line()
for k, v in groups:
    print(groups.values())
dividing_line()
for k, v in groups:
    print(subjects.values())


'''
# (1) - - PRZESZUKIWANIE BAZY - - - - #
while 1:
    clear_screen()
    if len(sys.argv) == 2:
        data_ask = str.strip(sys.argv[1]).title()
        print("Poniżej przedstawiam informacje dotyczące: {}".format(data_ask))
        data_ask = data_ask.lower()
        dividing_line()
        if data_ask in groups:
            if_klasa(data_ask)
        else:
            print("--- Klasa nie istnieje w bazie danych! ---")
            continue
        data_ask = data_ask.title()
        dividing_line()
        if data_ask in persons.keys():
            print_person(data_ask)
            if persons[data_ask]["status"] == "Uczeń":
                if_pupil()
            if persons[data_ask]["status"] == "Nauczyciel":
                if_teacher()
            if persons[data_ask]["status"] == "Wychowawca":
                if_educator()
            dividing_line()
        else:
            print("--- Osoba ta nie istnieje w bazie danych! ---")
            continue
'''

'''
    if len(sys.argv) == 1:
        get_data, right_data = "", 0
        dividing_line()
        print("<< Aby zakończyć: wpisz 'KONIEC' >>")
        while get_data != str.title("Koniec"):
            get_state()
            if get_data == str.title("koniec"):
                get_stop()
            get_name()
            check_name()
            if get_data == str.title("Uczeń"):
                get_classes()
                save_data()
                right_data = 1
            if get_data == str.title("Nauczyciel"):
                get_classes()
                get_subject()
                save_data()
                right_data = 1
            if get_data == str.title("Wychowawca"):
                get_classes()
                save_data()
                right_data = 1
            if right_data:
                print("--- Pomyślnie wprowadzono osobę do bazy ---")
                dividing_line()
                continue
            else:
                print("--- NIE dodano osoby do bazy! Niepełne dane! ---")
                dividing_line()
                continue
    else:
        break
'''


'''
# (2) - - POBIERANIE DANYCH DO BAZY - - - - #

if len(sys.argv) == 1:
        get_data = ""
        dividing_line()
        print("<< Aby zakończyć: wpisz 'KONIEC' >>")
        while get_data != str.title("Koniec"):
        # (2.1) POBRANIE STANOWISKA #
            firstname, lastname, status, right_data = "", "", "", 0
            class_list: list = []
            dividing_line()
            print("Podaj, stanowisko osoby wprowadzanej: ", end="")
            get_data = str.title(input().strip())
            if get_data == str.title("koniec"):
                print("< < < < <   K O N I E C   > > > > > ")
                break
            elif get_data not in positions:
                print("--- Wprowadzono nieprawidłowe dane! ---")
                continue
            else:
            # (2.1.1) POBRANIE NAZWISKA/IMIENIA - - - #
                dividing_line()
                print('Podaj nazwisko osoby wprowadzanej: ', end="")
                lastname = str.title(input()).strip()
                dividing_line()
                print('Podaj, imie osoby wprowadzanej: ', end="")
                firstname = str.title(input()).strip()
                full_name = firstname + " " + lastname
                if full_name in pupils or full_name in teachers or \
                                                        full_name in educators:
                    print("--- Ta osoba istnieje już w bazie danych ---")
                    continue
                if get_data == str.title("Uczeń"):
                # (2.1.1.1) POBRANIE SKŁADOWYCH UCZNIA - - - #
                    pupils.append(full_name)
                    dividing_line()
                    print("Do której klasy należy? (np. 1a) ", end="")
                    clas = str.strip(input())
                    clas.lower()
                    if clas in groups:
                        persons = {
                            full_name: {
                                "status": "Uczeń",
                                "klasa": clas}
                        }
                        right_data = 1
                    else:
                        print("--- Podana klasa nie istnieje! ---")
                        continue
                elif get_data == str.title("Nauczyciel"):
                # (2.1.1.2) POBRANIE SKŁADOWYCH NAUCZYCIELA - - - #
                    teachers.append(full_name)
                    dividing_line()
                    print("Jakiego przedmiotu uczy? (np. angielski) ", end="")
                    subject = str.strip(input())
                    subject.lower()
                    if not subject in subjects:
                        print("--- Tego przedmiotu nie ma w tej szkole! ---")
                        continue
                    dividing_line()
                    print("\n<< Aby zakończyć: wciśnij 'ENTER' >>")
                    clas = " "
                    while clas != "":
                        dividing_line()
                        print("Podaj, jaką klasę uczy? (np. 1a) ", end="")
                        clas = str.strip(input())
                        clas.lower()
                        if clas in groups:
                            class_list.append(clas)
                            right_data = 1
                        elif clas not in groups and right_data:
                            print("--- Klasy wprowadzono poprawnie ---")
                        else:
                            print("--- Podana klasa nie istnieje! ---")
                            continue
                    persons = {
                        full_name: {
                            "status": "Nauczyciel",
                            "przedmiot": subject,
                            "klasa": class_list}
                    }
                    clas = ""
                elif get_data == str.title("Wychowawca"):
                # (2.1.1.3) POBRANIE SKŁADOWYCH WYCHOWAWCY - - - #
                    educators.append(full_name)
                    dividing_line()
                    print("\n<< Aby zakończyć: wciśnij 'ENTER' >>")
                    clas = " "
                    while clas != "":
                        dividing_line()
                        print("Którą klasę prowadzi? (np. 1a) ", end="")
                        clas = str.strip(input())
                        clas.lower()
                        if clas in groups:
                            class_list.append(clas)
                            right_data = 1
                        elif clas not in groups and right_data:
                            print("--- Klasy wprowadzono poprawnie ---")
                        else:
                            print("--- Podana klasa nie istnieje! ---")
                            continue
                    persons = {
                        full_name: {
                            "status": "Wychowawca",
                            "klasa": class_list}
                    }
                    clas = ""
            dividing_line()
            if right_data:
            # (2.1.2) POTWIERDZENIE DANYCH - - - #
                print("--- Pomyślnie wprowadzono osobę do bazy ---")
                dividing_line()
                continue
            else:
                print("--- NIE dodano osoby do bazy! Niepełne dane! ---")
                dividing_line()
                continue
        # (2.2) POWRÓT NA POCZĄTEK PĘTLI "while KONIEC" - - - #
'''
