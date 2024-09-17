# PyTorch Keynote 2024 Demo

[![CI](https://github.com/onlydole/pytorch-keynote-2024/actions/workflows/build.yml/badge.svg)](https://github.com/onlydole/pytorch-keynote-2024/actions/workflows/build.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Overview

This project is a unique demonstration of PyTorch's capabilities, created for the PyTorch Conference 2024.
It combines computer vision and audio synthesis to generate melodic sounds based on input images.
The application uses a PyTorch neural network to analyze images and extract features, which are then used to create varied, electronic-style music.
This cloud native, open source project showcases the power of machine learning in creative applications.

## Features

- Upload any image and receive a unique musical composition based on that image
- PyTorch-powered image analysis using a custom CNN model
- Dynamic music generation influenced by image features
- Web-based interface for easy interaction
- Dockerized application for simple deployment and scalability
- Kubernetes configuration for cloud native deployment

## Tech Stack

- Frontend: React with Tailwind CSS for styling
- Backend: Flask with Flask-CORS for API
- ML Framework: PyTorch for image analysis
- Audio Processing: NumPy and SciPy for sound generation
- Image Processing: Pillow (PIL) for image handling
- Containerization: Docker and Docker Compose
- Orchestration: Kubernetes

## Prerequisites

- Docker and Docker Compose for local development
- Kubernetes cluster for cloud deployment (Kind can be used for local Kubernetes development)

## Getting Started

### Local Development

1. Clone the repository:

   ```sh
   git clone https://github.com/onlydole/pytorch-keynote-2024.git
   cd pytorch-keynote-2024
   ```

2. Build and run the Docker container:

   ```sh
   docker compose up --build
   ```

3. Open your web browser and navigate to `http://localhost:8080`

### Kubernetes Deployment

1. If you don't have a Kubernetes cluster, you can use [Kind](https://kind.sigs.k8s.io/) to create one locally:

   ```sh
   kind create cluster --config cluster.yml
   ```

2. Apply the Kubernetes configurations:

   ```sh
   kubectl apply -f kubernetes/
   ```

3. Access the application:
   - For Kind: Use port forwarding to access the service

     ```sh
     kubectl port-forward service/pytorch-music-service 8080:8080
     ```

4. Open your web browser and navigate to `http://localhost:8080`

## How It Works

1. The user uploads an image through the React-based web interface.
2. The image is sent to the Flask backend.
3. The image is processed by a custom PyTorch CNN, extracting various features.
4. These features influence different aspects of music generation.
5. The backend generates a unique audio clip.
6. The generated audio is sent back to the user's browser for playback.

## Scripts

- `startup.sh`: Script to start the application
- `shutdown.sh`: Script to shut down the application

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## CI/CD

This project uses GitHub Actions for building and publishing the container image. You can view the latest run status using the badges at the top of this README.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- PyTorch team for their powerful deep learning framework
- Flask team for the lightweight web framework
- React team for the frontend library
- The open source community for various tools and libraries used in this project
