### Biblioteka z funkcjami dodatkowymi ###
import os

# CLEAR SCREEN
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