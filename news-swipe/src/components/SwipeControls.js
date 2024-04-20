// src/components/SwipeControls.js

import React from 'react';

function SwipeControls({ onSwipeUp, onSwipeDown }) {
    return (
        <div className="swipe-controls">
            <button onClick={onSwipeUp}>Swipe Up</button>
            <button onClick={onSwipeDown}>Swipe Down</button>
        </div>
    );
}

export default SwipeControls;
