FROM node:10.9.0

COPY package*.json /opt/server/app/

WORKDIR /opt/server/app

RUN npm install

COPY app.js .

CMD ["node", "app.js"]
