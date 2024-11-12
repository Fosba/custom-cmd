import time 
from creafile import creafile
from ip import get_ip_address
from feedback import collect_feedback
from ai import apri_file
from meteo import get_weather
from calc import calc
from orario import orario

funzioni = [
          {
              "nome": "!new",
              "funzione_help": ' Per creare un file e rinominarlo',
              "funzione":'e stata scelta la funzione new',
              "def": creafile
          },
          {
              "nome": "!file",
              "funzione_help": ' Per aprire un file',
              "funzione":'e stata scelta la funzione file, inserire la directory del file '
              ##"def": aprifile()
          },
          {
              "nome": "!ip",
              "funzione_help": " Per visualizzare l'ip del client ",
              "funzione":'e stata scelta la funzione ip',
              "def": get_ip_address
          },
          {
              "nome": "!feedback",
              "funzione_help": " Per lasciare un feedback  ",
              "funzione":'e stata scelta la funzione feedbacck',
              "def": collect_feedback
          },
          {
              "nome": "!ai",
              "funzione_help": " Per utilizare l'ai nel cmd(non funziona perche sono un fis de put)",
              "funzione":'e stata scelta la funzione AI',
              "def": apri_file
          },
          {
              "nome": "!meteo",
              "funzione_help": " Per visualizzare il meteo di una specifica citta",
              "funzione":'e stata scelta la funzione meteo',
              "def": get_weather
          },
          {
              "nome": "!calcolatrice",
              "funzione_help": " Per effettuare calcoli",
              "funzione":'e stata scelta la funzione calcolatrice',
              "def": calc
          },
          {
              "nome": "!orario",
              "funzione_help": " Per ottenere l'orario locale ",
              "funzione":'e stata scelta la funzione orario',
              "def": orario
          }
          
      ]

print("Fosba Corporation (C) 2024 ")

time.sleep(0.4)
while True:
    scelta = input(r"C:\Users\Administrator\Desktop\python\custom_cmd> ").lower()
    ##for i in funzioni:
        ##if scelta == i["nome"]:
            ##break
    if scelta == "!help":
        time.sleep(0.4)
        print("Di seguito sono elencate tutte le funzioni che possono essere svolte: \n")
        print("------------------")
        for funzione in funzioni:
            print(f" {funzione['nome']}" , ":"  , f"{funzione['funzione_help']}\n")
            print("------------------")
    for i in funzioni:
        if scelta == i["nome"]:
            print(i["funzione"])
            i['def']()