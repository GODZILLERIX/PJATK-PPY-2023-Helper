"""
Lab08
"""

#Importowanie modułu

import datetime
czas = datetime.time(9,25,7)

#Stosowanie aliasów

import datetime as dt
czas = dt.time(9, 25, 7)

#Importowanie funkcji z modułu

from datetime import time

czas = time(9, 25, 7)

print(czas)
print(str(czas.hour) + "-" + str(czas.minute) + "-" + str(czas.second))