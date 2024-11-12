import openai
openai.api_key = 'API'  # sostituisci con la tua chiave API reale
def domanda():
    prompt = input("Fai qualsiasi domanda alla quale l'AI risponderà: ").lower()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # specifica il modello da utilizzare
        messages=[
            {"role": "user", "content": prompt}  # messaggio inviato dall'utente
        ]
    )
    print (response['choices'][0]['message']['content'])  # restituisce la risposta generata
    
domanda()