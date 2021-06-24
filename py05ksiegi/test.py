

from acclibrary import Magazyn, stop

magazyn = Magazyn()
with open("in.txt") as data:


    while True:
        pozycja = data.tell()
        akcja = data.readline().rstrip()
        if not akcja:
            break

        elif akcja == "saldo":
            operacja = int(data.readline().rstrip())
            comment = data.readline().rstrip()
            magazyn.saldo(operacja, comment)

        elif akcja == "zakup":
            produkt = str(data.readline().rstrip())
            cena = int(data.readline().rstrip())
            ilosc = int(data.readline().rstrip())
            magazyn.zakup(produkt, cena, ilosc)

        elif akcja == "sprzedaz":
            produkt = str(data.readline().rstrip())
            cena = int(data.readline().rstrip())
            ilosc = int(data.readline().rstrip())
            magazyn.sprzedaz(produkt, cena, ilosc)

        elif akcja == "stop":
            data.seek(pozycja)
            stop(akcja)
            break

print(magazyn.historia)
# wrapper(konto, magazyn, towar)

