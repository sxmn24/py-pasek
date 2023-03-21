-------------------------------------------------------------------------------------------------

                                               WELCOME 

-------------------------------------------------------------------------------------------------

WELCOME,
HERE YOU HAVE SOME STEPS HOW TO RUN THAT PROJECT:

1: OPEN VSC (OR OTHER APP)
2: COPY THAT CODE AND PASTE THAT ON YOUR CLEAR FILE
3: IF YOU'VE DONE THAT DOWNLOAD FILE MAIN AND RUN YOUR PROJECT.

GOOD LUCK.

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
