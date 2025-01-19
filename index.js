const Discord = require('discord.js');
const { exec } = require('child_process');

// Bot
const bot = new Discord.Client();

// Reklama serwera
const serverAd = `
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

// Lista użytkowników partnerstwa
const partneringUsers = {};

bot.on('ready', () => {
    console.log(`Self-bot ${bot.user.tag} jest gotowy.`);
});

bot.on('message', async message => {
    if (message.author.id !== bot.user.id) return; // Tylko wiadomości od self-bota

    if (message.content.toLowerCase().includes('partner') && !partneringUsers[message.author.id]) {
        partneringUsers[message.author.id] = null;
        message.channel.send('🌎 Wyślij swoją reklamę (maksymalnie 1 serwer).');
    } else if (partneringUsers[message.author.id] !== undefined) {
        if (partneringUsers[message.author.id] === null) {
            partneringUsers[message.author.id] = message.content;
            message.channel.send(`✅ Wstaw naszą reklamę:\n${serverAd}`);
            message.channel.send('⏰ Daj znać, gdy wstawisz reklamę!');
        } else if (message.content.toLowerCase().includes('wstawi')) {
            const guild = bot.guilds.cache.get('1316466087570706432');
            if (!guild) {
                message.channel.send('❕ Nie znaleziono serwera.');
                return;
            }

            const member = guild.members.cache.get(message.author.id);
            if (!member) {
                message.channel.send('❕ Dołącz na serwer, aby kontynuować!');
            } else {
                const channel = guild.channels.cache.find(ch => ch.name === '🤝partnerstwa');
                if (!channel) {
                    message.channel.send('Nie znaleziono kanału "🤝partnerstwa".');
                    return;
                }

                const userAd = partneringUsers[message.author.id];
                channel.send(userAd);
                message.channel.send('✅ Dziękujemy za partnerstwo!');
                delete partneringUsers[message.author.id];
            }
        }
    }
});

// Uruchomienie self-bota
const token = process.env.DISCORD_TOKEN;
if (token) {
    bot.login(token);
} else {
    console.log('Token nie został ustawiony. Upewnij się, że zmienna środowiskowa DISCORD_TOKEN jest poprawnie skonfigurowana.');
}
