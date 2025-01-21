import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Flask server
app = Flask('')

@app.route('/')
def home():
    return "Bot działa!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

# Server advertisement
server_ad = `
**Jesteś doświadczonym programistą i szukasz forum, gdzie uzyskasz wsparcie i podzielisz się efektem swojej pracy? A może dopiero zaczynasz swoją przygodę z kodowaniem? Niezależnie od stopnia zaawansowania zapraszamy na nasz serwer programistyczny.**

Co oferujemy:
- pomoc programistyczną,
- kanały dostosowane do różnych języków programistycznych,
- sklep z itemami,
- miejsce, gdzie znajdziesz ludzi z pasją,
- stały rozwój serwera.

Kogo szukamy:
- programistów,
- administracji,
- aktywnych użytkowników,
- realizatorów partnerstw.
https://discord.gg/pPss9qWZ6p
https://share.creavite.co/67646e7f0ae0e4f686a629f9.gif
https://share.creavite.co/67646f950ae0e4f686a62a01.gif
`;


# Partnering users list
partnering_users = {}

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} jest gotowy.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "partner" in message.content.lower() and message.author.id not in partnering_users: 
        partnering_users[message.author.id] = None 
        await message.channel.send("🌎 Wyślij swoją reklamę (maksymalnie 1 serwer).")

    elif message.author.id in partnering_users:
        if partnering_users[message.author.id] is None:
            partnering_users[message.author.id] = message.content
            await message.channel.send(f"✅ Wstaw naszą reklamę:\n{server_ad}")
            await message.channel.send("⏰ Daj znać, gdy wstawisz reklamę!")
        elif "wstawi" in message.content.lower():
            guild = discord.utils.get(bot.guilds, id=1316466087570706432)
            if not guild:
                await message.channel.send("❕ Nie znaleziono serwera.")
                return

            if not discord.utils.get(guild.members, id=message.author.id):
                await message.channel.send("❕ Dołącz na serwer, aby kontynuować!")
            else:
                channel = discord.utils.get(guild.text_channels, name="🤝partnerstwa")
token = DISCORD_TOKEN
if token:
    client.login(token)
else:
    print("Token bota nie został ustawiony. Upewnij się, że zmienna środowiskowa DISCORD_TOKEN jest poprawnie skonfigurowana.")











