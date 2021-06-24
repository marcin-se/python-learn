import sys

from acclibrary import Magazyn

magazyn = Magazyn()

magazyn.wczytaj(sys.argv[1])
magazyn.sprzedaz(sys.argv[2], sys.argv[3], sys.argv[4])

magazyn.zapisz_zs("sprzedaz", sys.argv[2], sys.argv[3], sys.argv[4])
