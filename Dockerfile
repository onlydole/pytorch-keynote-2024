# Build stage for React app
FROM node:lts-bullseye as build-stage

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Production stage
FROM python:3.12-bullseye

WORKDIR /app

# Copy build artifacts from the build stage
COPY --from=build-stage /app/build ./build

# Copy Python files and requirements
COPY *.py ./
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]