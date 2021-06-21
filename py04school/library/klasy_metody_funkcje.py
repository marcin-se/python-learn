### Biblioteka z klasami i funkcjami do obsługi szkolnych etatów ###
# from bazaszkolna import dict_groups, group_objects

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




# funkcja sprawdzająca m.in. istnienie obiektu grupy :)
def make_group(name):
    if name in group_objects:
        new_group = group_objects[name]
    else:
        dict_groups[name] = {}
        new_group = Group(name)
    return new_group



# funkcja zwracająca odpowiedź na:  KLASA
def if_class(name):
    edu = dict_groups[name]["educator"]
    print("W klasie {} wychowcą jest: {}".format(name, edu))
    print("Uczniowie klasy {}:\n".format(name))
    print_pupils(name)

def if_class_obj(name):
    edu = group_objects[name].educator
    print("W klasie {} wychowcą jest: {}".format(name, edu))
    print("Uczniowie klasy {}:\n".format(name))
    print_pupils(name)



# funkcja zwracająca odpowiedź na:  UCZEŃ
def if_pupil(name):
    for key, value in dict_groups.items():
        if name in dict_groups[key]["pupils"]:
            print("Klasa {} ma przedmioty:".format(key))
            for sub, teach in dict_groups[key]["teachers"].items():
                print("Przedmiot: {}, nauczyciel: {}.".format(sub, teach))

def if_pupil_obj(name):
    for key, value in group_objects.items():
        if name in value.pupils:
            print("Klasa {} ma przedmioty:".format(key))
            for sub, teach in value.teachers.items():
                print("Przedmiot: {}, nauczyciel: {}.".format(sub, teach))



# funkcja zwracająca odpowiedź na:  NAUCZYCIEL
def if_teacher(name):
    print("Podany nauczyciel ma zajęcia w klasach:")
    for key, value in dict_groups.items():
        if name in dict_groups[key]["teachers"]:
            edu = dict_groups[key]["educator"]
            print("Klasa {}, wychowawca: {}".format(key, edu))

def if_teacher_obj(name):
    print("Podany nauczyciel ma zajęcia w klasach:")
    for key, value in group_objects.items():
        if name in value.teachers:
            edu = value.educator
            print("Klasa {}, wychowawca: {}".format(key, edu))



# funkcja zwracająca odpowiedź na:  WYCHOWAWCA
def if_educator(name):
    print("Podany wychowawca prowadzi klasy:")
    for key, value in dict_groups.items():
        if name in dict_groups["educator"]:
            print("Klasa {}, uczniowie:".format(key))
            print_pupils(key)

def if_educator_obj(name):
    print("Podany wychowawca prowadzi klasy:")
    for key, val in group_objects.items():
        if name in val.educator:
            print("Klasa {}, uczniowie:".format(key))
            print_pupils(key)



# funkcja zwracająca listę uczniów danej klasy
def print_pupils(clase_name):
    if clase_name in dict_groups:
        for value in dict_groups[clase_name]["pupils"]:
            print(value)

def print_pupils_obj(clase_name):
    if clase_name in dict_groups:
        for value in dict_groups[clase_name]["pupils"]:
            print(value)