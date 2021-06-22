### Biblioteka z klasami i funkcjami do obsługi szkolnych etatów ###


# słownik zawierający dane słownikowe i listy
groups_dict: dict = {}
                # Struktura słownika:
                #   dict_groups = {
                #       nazwa klasy: {
                #           educator: imię nazwisko,
                #           pupils: [imię nazwisko, imię nazwisko, ... ],
                #           teachers: {przedmiot: imię nazwisko,
                #           przedmiot: imię nazwisko, ... }}


# słownik zawierający nazwy grup jako klucze, wartości to obiekty
group_objects: dict = {}
                # Struktura słownika:
                #   group_objects = { nazwa klasy: <__main__.Group object ...>,
                #                     nazwa klasy: <__main__.Group object ...> }


# klasa tworząca obiekty grup klasowych
class Group:
    def __init__(self, name):
        self.name = name
        self.educator = ""
        self.pupils = []
        self.teachers = {}


# klasa tworząca obiekty uczniów
class Pupil:
    def __init__(self, name):
        self.name = name
        self.state = "uczeń"
        self.group = ""
    def set_group(self, get_group):
        self.group = get_group
    def get_name(self):
        return self.name
    def get_group(self):
        return self.group


# klasa tworząca obiekty nauczycieli
class Teacher:
    def __init__(self, name):
        self.name = name
        self.state = "nauczyciel"
        self.groups = []
        self.subject = ""
    def set_subject(self, get_subject):
        self.subject = get_subject
    def set_groups(self, get_group):
        self.groups.append(get_group)
    def get_name(self):
        return self.name
    def get_subject(self):
        return self.subject
    def get_groups(self):
        return self.groups


# klasa tworząca obiekty wychowawców
class Educator:
    def __init__(self, name):
        self.name = name
        self.state = "wychowawca"
        self.groups = []
    def set_groups(self, get_group):
        self.groups.append(get_group)
    def get_name(self):
        return self.name
    def get_groups(self):
        return self.groups


# funkcja sprawdzająca istnienie grupy w słowniku
def make_group(group_name, dict_name):
    if group_name not in dict_name:
        dict_name[group_name] = {}
        dict_name[group_name]["pupils"] = []
        dict_name[group_name]["teachers"] = {}
        dict_name[group_name]["educator"] = ""
    return dict_name


# funkcja sprawdzająca istnienie obiektu grupy w słowniku
def make_group_obj(group_name, dict_name_obj):
    if group_name not in dict_name_obj:
        new_group_obj = Group(group_name)
        dict_name_obj[group_name] = new_group_obj
    else:
        new_group_obj = dict_name_obj[group_name]
    return new_group_obj


# funkcja zwracająca odpowiedź na:  KLASA
def if_class(cl_name, dict_name):
    edu = dict_name[cl_name]["educator"]
    print("W klasie '{}' wychowawcą jest:\n  {}".format(cl_name, edu))
    print("Uczniowie:".format(cl_name))
    return print_pupils(cl_name, dict_name)


# funkcja zwracająca odpowiedź na:  KLASA (obiektowo)
def if_class_obj(cl_name, dict_name):
    edu = group_objects[cl_name].educator
    print("W klasie {} wychowcą jest: {}".format(cl_name, edu))
    print("Uczniowie klasy {}:\n".format(cl_name))
    print_pupils(cl_name, dict_name)


# funkcja zwracająca odpowiedź na:  UCZEŃ
def if_pupil(pup_name, dict_name):
    for key, value in dict_name.items():
        if pup_name in dict_name[key]["pupils"]:
            print("Klasa {} ma przedmioty:".format(key))
            for sub, teach in dict_name[key]["teachers"].items():
                print("Przedmiot: {}, nauczyciel: {}.".format(sub, teach))


# funkcja zwracająca odpowiedź na:  UCZEŃ (obiektowo)
def if_pupil_obj(pup_name, dict_name):
    for key, value in dict_name.items():
        if pup_name in value.pupils:
            print("Klasa {} ma przedmioty:".format(key))
            for sub, teach in value.teachers.items():
                print("Przedmiot: {}, nauczyciel: {}.".format(sub, teach))


# funkcja zwracająca odpowiedź na:  NAUCZYCIEL
def if_teacher(teach_name, dict_name):
    print("Podany nauczyciel ma zajęcia w klasach:")
    for key, value in groups_dict.items():
        if teach_name in dict_name[key]["teachers"]:
            edu = dict_name[key]["educator"]
            print("Klasa {}, wychowawca: {}".format(key, edu))


# funkcja zwracająca odpowiedź na:  NAUCZYCIEL (obiektowo)
def if_teacher_obj(teach_name, dict_name):
    print("Podany nauczyciel ma zajęcia w klasach:")
    for key, value in dict_name.items():
        if teach_name in value.teachers:
            edu = value.educator
            print("Klasa {}, wychowawca: {}".format(key, edu))


# funkcja zwracająca odpowiedź na:  WYCHOWAWCA
def if_educator(edu_name, dict_name):
    print("Podany wychowawca prowadzi klasy:")
    for key, value in dict_name.items():
        if edu_name in dict_name["educator"]:
            print("Klasa {}, uczniowie:".format(key))
            print_pupils(key, dict_name)


# funkcja zwracająca odpowiedź na:  WYCHOWAWCA (obiektowo)
def if_educator_obj(edu_name, dict_name):
    print("Podany wychowawca prowadzi klasy:")
    for key, val in dict_name.items():
        if edu_name in val.educator:
            print("Klasa {}, uczniowie:".format(key))
            print_pupils(key, dict_name)


# funkcja zwracająca listę uczniów danej klasy
def print_pupils(cl_name, dict_name):
    if cl_name in dict_name:
        count = 0
        for value in dict_name[cl_name]["pupils"]:
            count += 1
            print("{:2}) {}".format(count, value))


# funkcja zwracająca listę uczniów danej klasy (obiektowo)
def print_pupils_obj(cl_name, dict_name):
    if cl_name in dict_name:
        count = 0
        for value in dict_name[cl_name]["pupils"]:
            count += 1
            print("{:2}) {}".format(count, value))
