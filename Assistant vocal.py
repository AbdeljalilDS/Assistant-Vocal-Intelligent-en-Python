import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialisation de la voix
engine = pyttsx3.init()

def parler(texte):
    print("Bot :", texte)
    engine.say(texte)
    engine.runAndWait()

# Fonction d’écoute
def ecouter():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Je t'écoute...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        texte = r.recognize_google(audio, language='fr-FR')
        print("Tu as dit :", texte)
        return texte.lower()
    except sr.UnknownValueError:
        print("Je n'ai pas compris.")
        parler("Je n'ai pas compris.")
        return ""
    except sr.RequestError:
        print("Service Google non disponible.")
        parler("Erreur de connexion.")
        return ""

# Réponse selon les mots
def repondre(texte):
    if "youtube" in texte:
        parler("J'ouvre YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "musique" in texte or "chanson" in texte or "i wanna be yours" in texte:
        parler("Je lance la chanson I Wanna Be Yours.")
        webbrowser.open("https://youtu.be/nyuo9-OjNNg?si=ycVLqFiE8Qx_RuUn")
    elif "heure" in texte:
        heure = datetime.datetime.now().strftime("%H:%M")
        parler(f"Il est {heure}")
    elif "bonjour" in texte:
        parler("Bonjour à toi aussi !")
    elif "comment ça va" in texte or "comment tu vas" in texte:
        parler("Je vais très bien, merci. Et toi ?")
    elif "stop" in texte or "au revoir" in texte:
        parler("Au revoir.")
        exit()
    else:
        parler("Commande inconnue.")

# Boucle principale
if __name__ == "__main__":
    parler("Bonjour, donne-moi une commande.")
    while True:
        commande = ecouter()
        if commande:
            repondre(commande)
