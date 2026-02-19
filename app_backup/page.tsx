"use client";
import { useState } from 'react';

export default function Home() {
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    const res = await fetch('http://localhost:8000/api/echo/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: "Hello from Next.js!" })
    });
    
    const data = await res.json();
    setResponse(data.reply);
  };

  return (
    <div style={{ padding: '20px' }}>
      <button onClick={sendMessage}>Send Message to Backend</button>
      <p>Response: {response}</p>
    </div>
  );
}