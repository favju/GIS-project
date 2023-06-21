# Base image
FROM node:lts

# Set the working directory
WORKDIR /var/www/html/app

# Copy package.json and package-lock.json
COPY vue-leaflet/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 8080

WORKDIR /var/www/html/app/vue-leaflet

# Start the development server
CMD ["npm", "run", "dev"]