import React from 'react';
import MessageReaction from './MessageReaction.jsx';

export default function ReplyList({ replies = [], onReactionChange }) {
  if (!replies || replies.length === 0) {
    return null;
  }

  return (
    <div className="ml-6 mt-3 border-l-2 border-gray-200 pl-4 space-y-3">
      {replies.map((reply) => (
        <div key={reply.id} className="bg-gray-50 rounded-lg p-3">
          <div className="flex justify-between items-start">
            <div>
              <p className="font-semibold text-sm text-gray-700">{reply.username}</p>
              <p className="text-gray-500 text-xs">{reply.timestamp}</p>
            </div>
          </div>
          <p
            className="text-sm mt-2"
            style={{
              color: reply.text_color || '#111827',
              fontWeight: reply.is_bold ? '700' : '400',
              fontStyle: reply.is_italic ? 'italic' : 'normal',
            }}
          >
            {reply.content}
          </p>
          <MessageReaction
            messageId={reply.id}
            likes={reply.likes}
            dislikes={reply.dislikes}
            onReactionChange={onReactionChange}
          />
        </div>
      ))}
    </div>
  );
}
