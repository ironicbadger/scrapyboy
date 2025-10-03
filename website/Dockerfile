FROM node:20-slim

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies (use npm install to generate lock file)
RUN npm install

# Copy source code (excluding transcripts directory)
COPY . .

# Remove the transcripts symlink/directory and recreate as symlink to mounted volume
RUN rm -rf src/content/transcripts

# Expose port
EXPOSE 4321

# Default command (can be overridden)
CMD ["npm", "run", "dev"]
