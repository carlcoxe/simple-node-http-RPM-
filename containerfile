FROM registry.access.redhat.com/ubi8/nodejs-18

WORKDIR /app

COPY SOURCES/server.js /app/server.js
COPY SOURCES/config.env /app/config.env

ENV NODE_ENV=production
ENV PORT=3000

EXPOSE 3000

CMD ["node", "server.js"]

