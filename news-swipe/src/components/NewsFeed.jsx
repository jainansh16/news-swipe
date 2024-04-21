import React, { useState, useEffect } from 'react';
import axios from 'axios';
import NewsCard from './NewsCard';
import './NewsFeed.css';

function NewsFeed() {
    const [articles, setArticles] = useState([]);
    const [currentIndex, setCurrentIndex] = useState(0);
    const [counter, setCounter] = useState(1);
    const [loading, setLoading] = useState(true);

    // useEffect(() => {
    //     const fetchNews = async () => {
    //         try {
    //             const response = await axios('http://127.0.0.1:5000/news');
    //             console.log(response)
    //             setArticles(response.data.articles);
    //             setLoading(false);
    //         } catch (error) {
    //             console.error("Failed to fetch news:", error);
    //             setLoading(false);
    //         }
    //     };
    //     fetchNews();
    // }, []);

    const fetchNews = async () => {
        try {
            const response = await axios('http://127.0.0.1:5000/news');
            console.log(response)
            setArticles(response.data.articles);
            setLoading(false);
        } catch (error) {
            console.error("Failed to fetch news:", error);
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchNews(); // Call fetchNews inside useEffect
    }, []);

    const handleLike = async () => {
        if (articles.length > 0 && currentIndex < articles.length) {
            const currentArticle = articles[currentIndex];
            try {
                await axios.post('http://127.0.0.1:5000/like', {
                    description: currentArticle.content
                });
            } catch (error) {
                console.error("Error sending like:", error);
            }
            handleNextArticle();
        }
    };

    const handleNextArticle = () => {
        setCurrentIndex(prevIndex => (prevIndex < articles.length - 1 ? prevIndex + 1 : prevIndex));
        handleCounter();
    };

    const handleCounter = async () => {
        console.log("in handle counter");
        if (counter == 10) {
            console.log("inside if statement");
            setCounter(1)
            setCurrentIndex(0)
            try {
                const keywordResponse = await axios.post('http://127.0.0.1:5000/keywords', {
                    result: null
                });
                if (keywordResponse.data.updated) {
                    setLoading(true);
                    fetchNews();
                }
                console.log("sent new axios post");
            } catch (error) {
                console.error("error sending keywords:", error)
            }
        } else {
            console.log("in else");
            setCounter(prevCounter => prevCounter + 1);
        }
    };

    if (loading) {
        return <div>Loading...</div>;
    }

    if (!articles.length) {
        return <div>No articles found.</div>;
    }

    const currentArticle = articles[currentIndex];

    return (
        <div className="news-feed">
            {currentArticle && <NewsCard article={currentArticle} />}
            <div className="button-container">
                <button className="dislike" onClick={handleNextArticle}>Dislike</button>
                <button className="like" onClick={handleLike}>Like</button>
            </div>
        </div>
    );
}

export default NewsFeed;