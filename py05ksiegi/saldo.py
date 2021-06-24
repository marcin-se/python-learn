import sys

from acclibrary import Magazyn

magazyn = Magazyn()

magazyn.wczytaj(sys.argv[1])
magazyn.saldo(sys.argv[2], sys.argv[3])

magazyn.zapisz_saldo("saldo", sys.argv[2], sys.argv[3])
