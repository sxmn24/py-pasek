-------------------------------------------------------------------------------------------------

                                               WELCOME 

-------------------------------------------------------------------------------------------------

IF YOU ARE READING THIS JUST NOW THAT IF YOU WANT TO RUN THIS PROJECT YOU HAVE TO TYPE THIS CODE:

-------------------------------------------------------------------------------------------------

from pasek import Pasek
from os import get_terminal_size
from time import sleep

szerokosc = get_terminal_size()[0]

pasek = Pasek(szerokosc=szerokosc / 2)
for i in range (50):
    pasek.dalej(procent=i/50)
    sleep(0.1)
pasek.koniec()

-------------------------------------------------------------------------------------------------
