import React, { useState, useEffect } from 'react';
import axios from 'axios';
import NewsCard from './NewsCard';
import './NewsFeed.css';

function NewsFeed() {
    const [articles, setArticles] = useState([]);
    const [currentIndex, setCurrentIndex] = useState(0); // Current article index
    const [loading, setLoading] = useState(true); // Loading state

    useEffect(() => {
        const fetchNews = async () => {
            try {
                const response = await axios('http://127.0.0.1:5000/news');
                console.log(response)
                setArticles(response.data.articles);
                setLoading(false); // Set loading to false once data is fetched
            } catch (error) {
                console.error("Failed to fetch news:", error);
                setLoading(false); // Ensure loading is false even if there is an error
            }
        };
        fetchNews();
    }, []);

    const handlePrevArticle = () => {
        // Decrement current index to show the previous article
        setCurrentIndex((prevIndex) => (prevIndex > 0 ? prevIndex - 1 : 0));
    };

    const handleNextArticle = () => {
        // Increment current index to show the next article
        setCurrentIndex((prevIndex) => (prevIndex < articles.length - 1 ? prevIndex + 1 : prevIndex));
    };

    // Show a loading message or a spinner
    if (loading) {
        return <div>Loading...</div>;
    }

    // No articles fetched
    if (!articles.length) {
        return <div>No articles found.</div>;
    }

    // Current article to display
    const currentArticle = articles[currentIndex];

    return (
        <div className="news-feed">
            {currentArticle && <NewsCard article={currentArticle} />}
            <div className="button-container">
                {(
                    <button className="dislike" onClick={handlePrevArticle}>Dislike</button>
                )}
                {(
                    <button className="like" onClick={handleNextArticle}>Like</button>
                )}
            </div>
        </div>
    );
}

export default NewsFeed;