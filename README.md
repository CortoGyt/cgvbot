CGVbot
 
Un chatbot en ligne de commande capable de répondre automatiquement aux questions liées aux Conditions Générales de Vente (CGV) : rétractation, livraison, garanties, données personnelles, etc.
 
Fonctionnalités
 
   Envoi de questions via la console
   Génération de réponses via un modèle OpenAI fine-tuné
   🗄Enregistrement des échanges dans une base MySQL (via Docker)
   Possibilité d’accéder à la BDD avec Adminer
   Pré-prompt métier intégré dans les données d’entraînement
Technologies utilisées
 
   -Python 3.10+
   -OpenAI API
   -MySQL 8 + Adminer
   -Docker / Docker Compose
   -python-dotenv, mysql-connector-python
 
Installation
 
1. Cloner le projet
 
   git clone https://github.com/<ton-pseudo>/chatbot-cgv-moneshop.git
 
   cd chatbot-cgv-moneshop
 
2. Créer un fichier .env
 
   OPENAI_API_KEY=xxxxxxxxxxxx
 
Ne partage jamais ta clé API sur GitHub – le fichier .env est ignoré grâce à .gitignore.
 
3. Installer les dépendances Python
 
Active ton environnement virtuel puis installe :
 
   pip install -r requirements.txt
 
4. Lancer la base de données avec Docker
   docker-compose up -d
 
Structure du projet
 
chatbot_cgv/
```
├── chatbot_console.py     # Interface console
 
├── sql.py                 # Fonctions pour enregistrer les échanges
 
├── train/train.jsonl      # Fichier d'entraînement JSONL (fine-tuning)
 
├── docker-compose.yml     # Services MySQL + Adminer
 
├── requirements.txt       # Dépendances Python
 
├── .env                   # Clé API OpenAI (non commitée)
 
├── .gitignore             # Fichiers ignorés par Git
 
└── README.md              # Documentation
 ```
Créateurs du projet
 
[Khaoula MILI](https://github.com/khaoulaMili123)
 
[Corto Gayet](https://github.com/CortoGyt)
