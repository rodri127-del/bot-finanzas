import tweepy
import random
import os

# Configuración de la API
client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET")
)

# Lista de hashtags
hashtags = [
    "#FinanzasPersonales", "#Ahorro", "#Inversion", "#LibertadFinanciera",
    "#Presupuesto", "#Dinero", "#InterésCompuesto", "#EducaciónFinanciera",
    "#FondoDeEmergencia", "#Gastos", "#Deudas", "#Productividad"
]

# Lee las frases desde el archivo
with open('frases_finanzas.txt', 'r', encoding='utf-8') as f:
    frases = [line.strip() for line in f.readlines() if line.strip()]

# Lee los libros desde el archivo
try:
    with open('libros.txt', 'r', encoding='utf-8') as f:
        libros = [line.strip() for line in f.readlines() if line.strip()]
except FileNotFoundError:
    libros = []

# Elige una acción aleatoria: frase normal (80%) o recomendación de libro (20%)
if libros and random.random() < 0.2:  # 20% de probabilidad
    tweet = random.choice(libros) + " " + " ".join(random.sample(hashtags, 2))
else:
    frase = random.choice(frases)
    tweet = frase + " " + " ".join(random.sample(hashtags, 3))

# Publica el tweet
client.create_tweet(text=tweet)
print(f"✅ Tweet publicado: {tweet}")
