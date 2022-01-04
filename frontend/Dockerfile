# docker run -it -v /home/neil/product_review/frontend:/frontend product_review_frontend:0.1 

#Base image
FROM node:lts-alpine

#Install serve package
RUN npm i -g @vue/cli

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json ./

RUN npm install


# Executables
#CMD [ "serve", "-s", "dist" ]
CMD ["npm", "run", "serve"]