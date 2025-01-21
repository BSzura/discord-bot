import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello, I am alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Reklama Twojego serwera
server_ad = """
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
"""

# Lista użytkowników, którzy rozpoczęli proces partnerstwa
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
        await message.channel.send("🌎 Witaj! Jeśli chcesz nawiązać partnerstwo, wyślij proszę swoją reklame (maksymalnie 1 serwer).")
    
    elif message.author.id in partnering_users:
        if partnering_users[message.author.id] is None:
            partnering_users[message.author.id] = message.content  # Przechowaj treść reklamy użytkownika
            await message.channel.send(f"✅ Świetnie! Teraz wstaw naszą reklamę:\n{server_ad}")
            await message.channel.send("⏰ Daj znać gdy wstawisz reklamę, a wtedy my wstawimy twoją!")
        elif "wstawi" in message.content.lower():
            guild = discord.utils.get(bot.guilds, id=1316466087570706432)
            if guild and not discord.utils.get(guild.members, id=message.author.id):
                await message.channel.send("❕ Zanim kontynuujemy, musisz dołączyć na serwer!")
            else:
                channel = discord.utils.get(guild.text_channels, name="🤝partnerstwa")  # Nazwa kanału partnerstwa
                if channel:
                    user_ad = partnering_users[message.author.id]
                    await channel.send(user_ad)  # Wstawienie reklamy użytkownika na kanał partnerstwa
                    await message.channel.send("✅ Dziękujemy za nawiązanie partnerstwa!")
                    partnering_users.pop(message.author.id)  # Usuń użytkownika z listy partnerstw po zakończeniu procesu

    await bot.process_commands(message)

keep_alive()

try:
    bot.run('MTMyNTgwNzI5MTAzOTA5Mjc1Ng.GZm_sa.SRJM7a0WIAHUceNEGVRjW1IRGHNlxfH-ZIf1RQ')
except Exception as e:
    print(f'Error: {e}')
