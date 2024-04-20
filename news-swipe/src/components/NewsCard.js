import React from 'react';
import { useSwipeable } from 'react-swipeable';

function NewsCard({ article, onSwipeUp, onSwipeDown }) {
    const handlers = useSwipeable({
        onSwipedUp: () => onSwipeUp(article),
        onSwipedDown: () => onSwipeDown(article)
    });

    return (
        <div {...handlers} className="news-card">
            <h4>{article.title}</h4>
            <p>{article.summary}</p>
            <img src={article.imageUrl} alt={article.title} style={{ width: '100%' }} />
        </div>
    );
}

export default NewsCard;