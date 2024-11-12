#funzione per vedere l'orario e con la possibilita di scegliere di quale paese 

import requests
def orario():
# Inserisci il tuo nome utente di GeoNames
    USERNAME = 'username'  # Sostituisci con il tuo username

    def ottieni_coordinate(pais):
        """Restituisce la latitudine e longitudine del paese fornito."""
        url = f"http://api.geonames.org/searchJSON?q={pais}&maxRows=1&username={USERNAME}"
        risposta = requests.get(url)
        if risposta.status_code == 200:
            dati = risposta.json()
            if dati['totalResultsCount'] > 0:
                lat = dati['geonames'][0]['lat']
                lng = dati['geonames'][0]['lng']
                return lat, lng
            else:
                print("Nessun risultato trovato.")
                return None
        else:
            print(f"Errore nella richiesta per il paese: {risposta.status_code} - {risposta.reason}")
            return None

    def ottieni_fuso_orario(lat, lng):
        """Restituisce il fuso orario per le coordinate fornite."""
        url = f"http://api.geonames.org/timezoneJSON?lat={lat}&lng={lng}&username={USERNAME}"
        risposta = requests.get(url)
        if risposta.status_code == 200:
            dati = risposta.json()
            if 'timezoneId' and 'time' in dati:
                fuso_orario = dati['timezoneId']
                return fuso_orario 
            else:
                print("Errore nella risposta dell'API:", dati.get('message', ''))
                return None
        else:
            print(f"Errore nella richiesta per il fuso orario: {risposta.status_code} - {risposta.reason}")
            return None
    def ottieni_time(lat, lng):
        """Restituisce il fuso orario per le coordinate fornite."""
        url = f"http://api.geonames.org/timezoneJSON?lat={lat}&lng={lng}&username={USERNAME}"
        risposta = requests.get(url)
        if risposta.status_code == 200:
            dati = risposta.json()
            if 'time' in dati:
                time = dati['time']
                return  time
            else:
                print("Errore nella risposta dell'API:", dati.get('message', ''))
                return None
        else:
            print(f"Errore nella richiesta per il fuso orario: {risposta.status_code} - {risposta.reason}")
            return None

    def main():
        paese = input("Inserisci il nome di un paese: ")
        coordinate = ottieni_coordinate(paese)
        if coordinate:
            lat, lng = coordinate
            fuso_orario = ottieni_fuso_orario(lat, lng)
            time = ottieni_time(lat, lng)
            if fuso_orario:
                print(f"Il fuso orario per {paese} è: {fuso_orario} ovvero {time}")
                
    main()


