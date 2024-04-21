// src/components/SwipeControls.js

// import React from 'react';

// function SwipeControls({ onSwipeUp, onSwipeDown }) {
//     return (
//         <div className="swipe-controls">
//             <button onClick={onSwipeUp}>Swipe Up</button>
//             <button onClick={onSwipeDown}>Swipe Down</button>
//         </div>
//     );
// }

// export default SwipeControls;

//################################################################
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const completion = await openai.chat.completions.create({
    messages: [{ role: "system", content: "You are a helpful assistant." }],
    model: "gpt-3.5-turbo",
  });

  console.log(completion.choices[0]);
}

main();
