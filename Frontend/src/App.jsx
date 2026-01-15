import { useState } from "react";

function App() {
  const [message, setMessage] = useState([
    { id: 1, user: 'Rahwa', text: 'Hi there!', timeStamp: "10:00 AM" },
    { id: 2, user: 'Selam', text: 'Hello!', timeStamp: "10:01 AM" }
  ]);

  return (
    <div className="flex justify-center items-start min-h-screen bg-gray-100 p-6">
      <div className="w-full max-w-md p-4 bg-white shadow-md rounded">
        <h1 className="text-center text-xl font-bold mb-4">Chat App</h1>
        <ul>
          {message.map((mse) => (
            <li key={mse.id}>
              <strong>{mse.user}</strong>: {mse.text} <em>({mse.timeStamp})</em>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
