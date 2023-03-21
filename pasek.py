# Pasek ładowania

import time
import urllib.request
import urllib.error
import asyncio
from asyncio import wait
import time
from datetime import datetime, timedelta
import threading
import time

class Pasek:
    def __init__(self, znak = '#' , start = 0, szerokosc = 10, pusto = '-'):
        self.znak = znak
        self.start = start
        self.szerokosc = int(szerokosc)
        self.pusto = pusto

    def dalej(self, procent = 0):
        linia = "{" + format(round(procent*100, 0), ".0f") + "%}["
        for i in range(self.szerokosc):
            wartosc = i
            aktwartosc = wartosc / self.szerokosc
            if aktwartosc <= procent:
                linia += self.znak
            else:
                linia += self.pusto
        linia += ']'
        print(linia, end = "\r")

    def koniec(self, procent = 1):
        self.dalej(procent = 1)
        time.sleep(1)
        
def main():
    pasek1 = Pasek()

# you have to make another file and import this class.
# Language i've made it: Python
