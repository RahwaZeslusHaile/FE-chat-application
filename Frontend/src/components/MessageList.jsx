import React from 'react';
import MessageItem from './MessageItem.jsx';

function MessageList({ messages }) {
    return (
        <div className="flex flex-col p-4 space-y-4 overflow-y-auto h-full">
            {messages.map((msg) => (
                <MessageItem key={msg.id} message={msg} />    
            ))}
        </div>
    );
}

export default MessageList;
