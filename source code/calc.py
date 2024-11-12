import math

def calc (): 
        # Definizione delle operazioni
    calcoli = {
        "somma": lambda a, b: a + b,
        "sottrazione": lambda a, b: a - b,
        "moltiplicazione": lambda a, b: a * b,
        "divisione": lambda a, b: a / b,
        "radice": lambda a: math.sqrt(a),  # Solo una variabile necessaria per la radice
        "potenza": lambda a, b: a ** b,
        "modulo": lambda a, b: a % b,
        "fattoriale": lambda a: math.factorial(a)  # Solo una variabile necessaria
    }

    # Input dell'utente
    a = int(input("Inserisci il primo numero: "))
    b = None
    ask = input("Inserisci il secondo numero (lascia vuoto se operazione richiede un solo numero): ")

    if ask:  # Se l'utente inserisce un secondo numero
        b = int(ask)

    print("Le operazioni presenti sono:")
    for calcolo in calcoli:
        print(calcolo)

    # Input per l'operazione
    operazione = input("Inserisci il calcolo: ")

    try:
        # Controllo se l'operazione è valida
        if operazione in calcoli:
            if operazione in ["radice", "fattoriale"]:  # Operazioni che richiedono un solo argomento
                print(f"Risultato: {calcoli[operazione](a)}")  # Solo 'a' come argomento
            else:
                print(f"Risultato: {calcoli[operazione](a, b)}")  # Passa entrambi gli argomenti
        else:
            print("Operazione non valida!")
    except ZeroDivisionError:
        print("Non è possibile eseguire la divisione per zero!")
    except ValueError:
        print("Devi inserire numeri validi!")
    except TypeError:
        print("Devi inserire numeri!")
    except Exception as e:
        print("Qualcosa è andato storto!", e)
    finally:
        print("Calcolo terminato!")