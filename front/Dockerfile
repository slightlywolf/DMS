# Stage 1
FROM node:16.10-alpine AS build

WORKDIR /usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY ["package.json", "package-lock.json", "./"]


RUN npm install
RUN npm install -g @angular/cli
RUN npm install --save-dev @angular-devkit/build-angular

COPY . .

# Stage 2
# original port is 4200
EXPOSE 5020/tcp 
CMD ng serve --open --configuration development --watch --live-reload --poll=1000 --host=0.0.0.0
