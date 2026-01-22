import React from "react";
import Header from "./Header.js";
import MessageList from "./MessageList.js";
import MessageInput from "./MessageInput.js";

function ChatWindow({ messages, onSendMessage , children }){ {
    return(
        <div className="flex flex-col h-full">
            <Header />
            <MessageList messages={messages} />
            <MessageInput onSend={onSendMessage} />
            <div className="flex-1 overflow-y-auto p-4">
                {children} 
            </div>
        </div>  
    )
}
}
export default ChatWindow;