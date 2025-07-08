from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv
import os
 
# Import de la fonction déjà existante
from sql import sauvegarder_echange
 
# --- Chargement des variables d'environnement ---
load_dotenv()
 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")    # Chargement de la cle via notre .env
MODEL_FINE_TUNE = "gpt-4.1-nano-2025-04-14"  # Pas de fine tune,
 
# --- Initialisation client OpenAI ---
client = OpenAI(api_key=OPENAI_API_KEY)
 
# --- Boucle de discussion en console ---
print("Bonjour, je suis vôtre Assistant CGV personalisé. Comment puis-je vous aider ?(tapez 'exit' pour quitter)\n")
 
while True:
    user_input = input("Vôtre question : ") # Texte + on attends l'input user texte
    if user_input.lower() in ["exit", "quit", "stop"]:
        print("Votre assistant vous souhaite une bonne journée ! A bientôt")
        break
 
    try:
        # Appel au modèle (non fine-tuné)
        completion = client.chat.completions.create( # appel API de chat completions qui gère les conversations
            model=MODEL_FINE_TUNE, # appel de notre model
            messages=[
        {
            "role": "system",
            "content": "Tu es un assistant juridique spécialisé dans les Conditions Générales de Vente (CGV). "
            "Tu aides les utilisateurs à comprendre, rédiger ou modifier leurs CGV de manière claire, professionnelle et conforme à la législation française. "
            "Utilise un langage juridique accessible, donne des explications précises, et mentionne les obligations légales quand c’est pertinent. "
            "Si une question n’est pas liée aux CGV, redirige poliment l’utilisateur vers un professionnel du droit compétent."
            "Si tu ne connais pas la réponse, dis le, soit honnête."
        }
        ,
        {
            "role": "user",
            "content": user_input
        }
    ]
)

        response = completion.choices[0].message.content.strip() # Reponse de l'agent, il va choisir la réponse la plus courante (choices[0])
 
        print("Assistant >", response) # Affichage console de la réponse 
 
        # Enregistrement dans la base via la fonction importée
        sauvegarder_echange(
            prompt=user_input,
            reponse=response,
            date=datetime.now(),
            statut=1 # 1 = ok
        )
 
    except Exception as e:
        print("❌ Erreur :", e)
        sauvegarder_echange(
            prompt=user_input,
            reponse="Erreur lors de la génération",
            date=datetime.now(),
            statut=0 # 0 = erreur
        )
 