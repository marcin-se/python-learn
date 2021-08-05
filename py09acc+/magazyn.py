# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Plik 'magazyn.py' zwraca informację o stanach magazynowych
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
from acc import director, actions
from acc_lib.acc_extras import *
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


clearscreen()
line_banner('Procedure "MAGAZYN" was started')

director.process()
director.post_process("magazyn", actions)
print('-= The procedure was completed successfully =-')

director.close_actions()
