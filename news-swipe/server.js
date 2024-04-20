require('dotenv').config();
const express = require('express');
const axios = require('axios');
const app = express();
const PORT = process.env.PORT || 5000;

app.use(express.json());

app.get('/news', async (req, res) => {
    try {
        const response = await axios.get(`https://newsapi.org/v2/top-headlines?country=us&apiKey=${process.env.NEWS_API_KEY}`);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
