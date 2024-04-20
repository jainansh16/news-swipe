// // // src/components/NewsFeed.js
// import React, { useState, useEffect } from 'react';
// import axios from 'axios';
// import NewsCard from './NewsCard';
// import TinderCard from 'react-tinder-card';

// function NewsFeed() {
//     const [articles, setArticles] = useState([]);

//     useEffect(() => {
//         const fetchNews = async () => {
//             try {
//                 const response = await axios('http://localhost:5000/news');
//                 setArticles(response.data.articles);
//             } catch (error) {
//                 console.error("Failed to fetch news:", error);
//             }
//         };
//         fetchNews();
//     }, []);

//     const onSwipe = (direction, swipedArticle) => {
//         console.log(`Swiped ${direction} on article: ${swipedArticle.title}`);
//         // Filter out the swiped article
//         setArticles(prevArticles =>
//             prevArticles.filter(article => article.title !== swipedArticle.title)
//         );
//     };

//     return (
//         <div className="news-feed">
//             {articles.map((article, index) => (
//                 <TinderCard
//                     key={article.title} // title is assumed to be unique; use a unique identifier if available
//                     onSwipe={(dir) => onSwipe(dir, article)}
//                     preventSwipe={['up', 'down']}
//                 >
//                     <NewsCard article={article} />
//                 </TinderCard>
//             ))}
//         </div>
//     );
// }

// export default NewsFeed;

import React, { useState, useEffect } from 'react';
import TinderCard from 'react-tinder-card';
import NewsCard from './NewsCard';
// You may need axios or another HTTP library to fetch articles from your backend
import axios from 'axios';

const NewsFeed = () => {
  const [articles, setArticles] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    // Fetch articles from your backend
    const fetchArticles = async () => {
      try {
        const response = await axios.get('/api/articles'); // Adjust with your actual endpoint
        setArticles(response.data.articles);
      } catch (error) {
        console.error('Error fetching articles:', error);
      }
    };

    fetchArticles();
  }, []);

  const onSwipe = (direction) => {
    // You can add additional logic based on the swipe direction
    setCurrentIndex(currentIndex + 1); // Show next article
  };

  const canSwipe = currentIndex < articles.length;

  return (
    <div>
      {canSwipe ? (
        <TinderCard
          key={articles[currentIndex].url}
          onSwipe={onSwipe}
          preventSwipe={['left', 'right']} // Optional: if you want to allow only up and down swipes
        >
          <NewsCard {...articles[currentIndex]} />
        </TinderCard>
      ) : (
        <div>No more articles</div>
      )}
    </div>
  );
};

export default NewsFeed;