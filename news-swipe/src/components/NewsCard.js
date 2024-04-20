import React from 'react';
import './NewsCard.css'; // Assuming you have created this CSS file for styling

function NewsCard({article}) {
    return (
        <div className="news-card">
            <img src={article.urlToImage} alt={article.title} className="news-image" />
            <div className="news-content">
                <h3 className="news-title">{article.title}</h3>
                <p className="news-description">{article.description}</p>
                <div className="news-footer">
                    <span className="news-source">{article.source.name}</span>
                    <a href={article.url} target="_blank" rel="noopener noreferrer" className="read-more">Read more</a>
                </div>
            </div>
        </div>
    );
}

export default NewsCard;