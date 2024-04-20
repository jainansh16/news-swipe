// src/components/NewsCard.js

// import React from 'react';
// import { useSwipeable } from 'react-swipeable';
// import './NewsCard.css'; // Make sure to create a CSS file for styling if you haven't already

// function NewsCard({ article, onSwipeUp, onSwipeDown }) {
//   const swipeHandlers = useSwipeable({
//     onSwipedUp: () => onSwipeUp(article),
//     onSwipedDown: () => onSwipeDown(article),
//     // Prevent default touch action to allow smooth swiping on touch devices
//     preventDefaultTouchmoveEvent: true,
//     trackMouse: true // Optional: This allows you to swipe with mouse on desktop as well
//   });

//   return (
//     <div {...swipeHandlers} className="news-card">
//       <img src={article.urlToImage} alt={article.title} className="news-image" />
//       <div className="news-content">
//         <h3 className="news-title">{article.title}</h3>
//         <p className="news-description">{article.description}</p>
//         <div className="news-footer">
//           <span className="news-source">{article.source.name}</span>
//           <a href={article.url} target="_blank" rel="noopener noreferrer" className="read-more">Read more</a>
//         </div>
//       </div>
//     </div>
//   );
// }

// export default NewsCard;

// src/components/NewsCard.js

import React from 'react';
import './NewsCard.css'; // Assuming you have created this CSS file for styling

function NewsCard({ article }) {
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