### Biblioteka z funkcjami dodatkowymi ###



# CLEAR SCREEN
import time


def clear_screen():
    if os.name == 'posix':  # dla mac i linux
        _ = os.system('clear')
    else:
        _ = os.system('cls')  # dla windows
    return



# LINE OF SIGNS
# ------------------------------------------------------------- #
def dividing_line(stamp="-", repeat=55):
    print("+" + stamp * repeat + "+")
    return



# EFFECTIVE PRINT
def effective_print(text):
    for i in range(len(text)):
        print(f'{text[i]}', end='')
        time.sleep(0.2)
    return



# ------------------------------------------------------------- #
# ---------------------- TITLE BANNER ------------------------- #
# ------------------------------------------------------------- #
def title_line(text="none"):
    repeat = 55
    textline = str(text.upper())
    dividing_line("-", repeat)
    lenght = round((repeat - 2 - len(text))/2)
    print("|{} {} {}|".format("-"*lenght, textline, "-"*lenght))
    dividing_line("-", repeat)
    return

# FORMAT - PRINT CSV FILES
# ------------------------------------------------------------- #
TPL_FORMAT_argv = "Rekord: {:3},\tKolumna: {:3},\tDane: {:5}"
TPL_FORMAT_csv = "{:5}\t {:2}\t {:2}\t {:2}\t {:3}\t {:6}\t"
