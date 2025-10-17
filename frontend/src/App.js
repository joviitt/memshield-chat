import React, { useState, useEffect } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:5000");

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  useEffect(() => {
    socket.on("message", (msg) => {
      setChat((prev) => [...prev, msg]);
    });
    return () => socket.off("message");
  }, []);

  const sendMessage = (e) => {
    e.preventDefault();
    socket.emit("message", message);
    setMessage("");
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>Memeshield Chat 💬</h2>
      <div
        style={{
          border: "1px solid #ccc",
          width: "400px",
          margin: "auto",
          padding: "10px",
          borderRadius: "10px",
          height: "300px",
          overflowY: "scroll",
        }}
      >
        {chat.map((msg, index) => (
          <p key={index}>{msg}</p>
        ))}
      </div>
      <form onSubmit={sendMessage}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..."
          style={{ width: "300px", marginTop: "10px" }}
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;
