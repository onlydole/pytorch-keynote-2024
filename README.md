# PyTorch Image-to-Music Generator

## Overview

This project is a unique demonstration of PyTorch's capabilities, created for the PyTorch Conference. It combines computer vision and audio synthesis to generate electronic music based on input images. The application uses a PyTorch neural network to process images and extract features, which are then used to create varied, electronic-style music.

## Features

- Upload any image and receive a unique musical composition based on that image
- PyTorch-powered image processing
- Dynamic music generation influenced by image features
- Web-based interface for easy interaction
- Dockerized application for simple deployment

## Tech Stack

- Frontend: React
- Backend: Flask
- ML Framework: PyTorch
- Audio Processing: Numpy, SciPy
- Containerization: Docker

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/pytorch-image-to-music.git
   cd pytorch-image-to-music
   ```

2. Build and run the Docker container:

   ```
   docker-compose up --build
   ```

3. Open your web browser and navigate to `http://localhost:5000`

4. Upload an image and listen to the generated music!

## How It Works

1. The user uploads an image through the web interface.
2. The image is processed by a PyTorch neural network, extracting various features.
3. These features are used to influence different aspects of music generation, including:
   - Base frequency
   - Scale type (major or minor)
   - Tempo
   - Note selection and amplitude
   - Waveform types
   - Rhythm patterns
4. The generated audio is sent back to the user's browser for playback.

## Project Structure

- `app.py`: Main Flask application and PyTorch model
- `Dockerfile`: Instructions for building the Docker image
- `docker-compose.yml`: Docker Compose configuration
- `requirements.txt`: Python dependencies
- `src/`: React frontend source code

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- PyTorch team for their amazing framework
- Flask team for the lightweight web framework
- React team for the frontend library

---

Enjoy turning your images into music with PyTorch!
