import tweepy
import random
import os

# Configuración de la API (tus claves irán aquí)
client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET")
)

# Lee las frases desde el archivo
with open('frases_finanzas.txt', 'r', encoding='utf-8') as f:
    frases = [line.strip() for line in f.readlines() if line.strip()]

# Elige una frase al azar
frase = random.choice(frases)

# Publica el tweet
client.create_tweet(text=frase)
print(f"✅ Tweet publicado: {frase}")