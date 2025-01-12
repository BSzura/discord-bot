const express = require('express');
const axios = require('axios');
const app = express();

const CLIENT_ID = 'YOUR_CLIENT_ID';
const CLIENT_SECRET = 'YOUR_CLIENT_SECRET';
const REDIRECT_URI = 'http://localhost:3000/callback';

app.get('/login', (req, res) => {
    const oauthURL = `https://discord.com/oauth2/authorize?client_id=${CLIENT_ID}&redirect_uri=${encodeURIComponent(REDIRECT_URI)}&response_type=code&scope=identify%20guilds`;
    res.redirect(oauthURL);
});

app.get('/callback', async (req, res) => {
    const code = req.query.code;

    try {
        // Wymiana kodu na token dostępu
        const tokenResponse = await axios.post('https://discord.com/api/oauth2/token', null, {
            params: {
                client_id: CLIENT_ID,
                client_secret: CLIENT_SECRET,
                grant_type: 'authorization_code',
                code: code,
                redirect_uri: REDIRECT_URI,
            },
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        });

        const accessToken = tokenResponse.data.access_token;

        // Pobieranie danych użytkownika
        const userResponse = await axios.get('https://discord.com/api/users/@me', {
            headers: { Authorization: `Bearer ${accessToken}` },
        });

        res.send(`Witaj, ${userResponse.data.username}!`);
    } catch (error) {
        console.error(error);
        res.send('Błąd podczas autoryzacji.');
    }
});

app.listen(3000, () => {
    console.log('Serwer działa na http://localhost:3000');
});
