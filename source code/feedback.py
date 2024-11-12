def collect_feedback():
    feedback = input("Inserisci il tuo feedback: ")
    with open("feedback.txt", "a") as f:
        f.write(feedback + "\n")
    print("Feedback ricevuto!")