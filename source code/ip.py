import socket

def get_ip_address():
    try:
        # per fare hostname
        hostname = socket.gethostname()
        
        #per prendere ip del hostname
        ip_address = socket.gethostbyname(hostname)
        
        return print("Il tuo ip è :", ip_address)
    except Exception as e:
        print("errore durante la fase di acquisizione dell'ip :", e)
