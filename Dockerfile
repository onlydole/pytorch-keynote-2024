# Build stage for React app
FROM node:lts-alpine as build-stage

WORKDIR /app
COPY package*.json ./
RUN npm install --only=production
COPY . .
RUN npm run build

# Production stage
FROM python:3.12-slim-bullseye

WORKDIR /app

# Copy build artifacts from the build stage
COPY --from=build-stage /app/build ./build

# Copy Python files and requirements
COPY *.py ./
COPY requirements.txt ./

# Install system dependencies and Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  gcc \
  gfortran \
  libopenblas-dev \
  && pip install --no-cache-dir -r requirements.txt \
  && apt-get purge -y --auto-remove \
  build-essential \
  gcc \
  gfortran \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /root/.cache/pip

# Create non-root user
RUN useradd -m pytorch

# Create a directory for generated files
RUN mkdir /app/generated

# Change ownership of the application directory
RUN chown -R pytorch:pytorch /app

# Switch to non-root user
USER pytorch

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]