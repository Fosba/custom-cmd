import os
import time
def creafile():
    testo = input("inserire il nome del file da creare: ")
    estensione = input("inserire l'estensione del file: ")
    f = open(testo + estensione, "x")
    print ("file creato con successo")
