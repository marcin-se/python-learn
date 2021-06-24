import sys

from acclibrary import Magazyn

magazyn = Magazyn()

magazyn.wczytaj(sys.argv[1])
magazyn.magazyn(sys.argv[2:])
