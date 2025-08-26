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

# Lista de hashtags financieros (elige 2-3 al azar)
hashtags = [
    "#FinanzasPersonales", "#Ahorro", "#Inversion", "#LibertadFinanciera",
    "#Presupuesto", "#Dinero", "#InterésCompuesto", "#FondoDeEmergencia",
    "#Gastos", "#Deudas", "#Invertir", "#Productividad", "#EducaciónFinanciera"
]

# Lee las frases desde el archivo
with open('frases_finanzas.txt', 'r', encoding='utf-8') as f:
    frases = [line.strip() for line in f.readlines() if line.strip()]

# Elige una frase al azar
frase = random.choice(frases)

# Añade 3 hashtags aleatorios (sin repetir)
frase_con_hashtags = frase + " " + " ".join(random.sample(hashtags, 3))

# Publica el tweet
client.create_tweet(text=frase_con_hashtags)
print(f"✅ Tweet publicado: {frase_con_hashtags}")
