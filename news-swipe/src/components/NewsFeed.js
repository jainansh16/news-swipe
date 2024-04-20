// src/components/NewsFeed.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import NewsCard from './NewsCard';
import SwipeControls from './SwipeControls';

function NewsFeed() {
    const [articles, setArticles] = useState([]);

    useEffect(() => {
        const fetchNews = async () => {
            const result = await axios('https://api.your-news-provider.com/news');
            setArticles(result.data.articles);
        };
        fetchNews();
    }, []);

    const handleSwipeUp = (article) => {
        console.log("Swiped up on", article.title);
        // Further actions can be implemented here
    };

    const handleSwipeDown = (article) => {
        console.log("Swiped down on", article.title);
        // Further actions can be implemented here
    };

    return (
        <div>
            {articles.map(article => (
                <NewsCard key={article.id} article={article} onSwipeUp={handleSwipeUp} onSwipeDown={handleSwipeDown} />
            ))}
            <SwipeControls onSwipeUp={() => handleSwipeUp(articles[0])} onSwipeDown={() => handleSwipeDown(articles[0])} />
        </div>
    );
}

export default NewsFeed;
