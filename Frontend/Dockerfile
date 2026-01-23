FROM node:20-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

RUN npm run build

# Serve with a static server
RUN npm install -g serve

EXPOSE 5173
CMD ["sh", "-c", "serve -s dist -l ${PORT:-5173}"]
