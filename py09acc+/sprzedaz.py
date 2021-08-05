# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Plik 'sprzedaz.py' obsługuje sprzedaż magazynową asortymentu
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
from acc import director, actions
from acc_lib.acc_extras import *
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


clearscreen()
line_banner('Procedure "SPRZEDAZ" was started')

director.process()
director.post_process("sprzedaż", actions)
print('-= The procedure was completed successfully =-')

director.export_to_file()
print('-= The action was successfully exported to a file =-')

director.close_actions()
