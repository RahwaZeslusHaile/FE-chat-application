export const API_CONFIG = {
  REST_URL: import.meta.env.VITE_REST_URL || "https://backendrahwachatapp.hosting.codeyourfuture.io",
  WS_URL: import.meta.env.VITE_WS_URL || "wss://backendwschat.hosting.codeyourfuture.io/ws",
  USE_WEBSOCKET: import.meta.env.VITE_USE_WEBSOCKET === "true" || false,
};

console.log("API_CONFIG loaded:", API_CONFIG);
console.log("VITE_USE_WEBSOCKET env var:", import.meta.env.VITE_USE_WEBSOCKET);
