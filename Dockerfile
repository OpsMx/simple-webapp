# Use a base image with Node.js (e.g., Node.js 14)
FROM node:14-alpine

# Set the working directory
WORKDIR /usr/src/app

# Copy the application files to the container
COPY index.html .
COPY server.js .

# Expose port 8080 for web traffic
EXPOSE 8080

# Start the Node.js server
CMD ["node", "server.js"]
