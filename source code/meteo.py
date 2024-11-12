import requests
#usa openweather api per avere le info sul meteo http://api.openweathermap.org

def get_weather():
    api_key = "API_KEY"
    city1 = input("Inserisci la città : ")
    city2 = input("Inserisci la sigla dello stato: ")
    city = city1 + "," + city2
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parametri per la richiesta
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'it'  # Lingua italiana
    }
    
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']
        
        print(f"Temperatura: {temperature}°C")
        print(f"Umidità: {humidity}%")
        print(f"Descrizione: {description.capitalize()}")
    else:
        print(f"Errore nella richiesta: {response.status_code} - {response.text}")

