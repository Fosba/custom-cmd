# Funzione per aprire un file batch 
import subprocess

def apri_file():
    try:
        # Esegue il file batch 'ai.bat' in una nuova finestra del prompt dei comandi
        subprocess.run(['cmd.exe', '/c', 'start', 'cmd.exe', '/k', 'ai.bat'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Si è verificato un errore durante l'esecuzione del file batch: {e}")
    except FileNotFoundError:
        print("Il file 'ai.bat' non è stato trovato.")

