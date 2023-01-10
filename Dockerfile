# ---> Build Stage
FROM node:18-bullseye as node-Build

ENV NODE_ENV=production
WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN yarn install --silent --production=true --frozen-lockfile
RUN yarn build --silent


# ---> Serve Stage
FROM nginx:stable-alpine
COPY --from=node-build /usr/src/app/dist usr/share/nginx/html

