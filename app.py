import torch
import torch.nn as nn
import torchvision.transforms as transforms
from flask import Flask, request, send_file, send_from_directory
from flask_cors import CORS
from PIL import Image
import io
import numpy as np
from scipy.io import wavfile
import os

app = Flask(__name__, static_folder='build')
CORS(app)

class ImageAnalyzer(nn.Module):
    def __init__(self):
        super(ImageAnalyzer, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.AdaptiveAvgPool2d((1, 1))
        )
        self.fc = nn.Linear(128, 3)

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)
        return torch.sigmoid(x)

model = ImageAnalyzer()

def create_sine_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    return np.sin(2 * np.pi * freq * t)

def get_image_brightness(image):
    # Convert image to grayscale and calculate average pixel value
    gray_image = image.convert('L')
    return np.mean(np.array(gray_image)) / 255.0  # Normalize to 0-1

def image_to_melodic_sound(image):
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
    ])
    image_tensor = transform(image).unsqueeze(0)
    
    with torch.no_grad():
        features = model(image_tensor).squeeze().numpy()
    
    duration = 10  # 10 seconds of music
    sample_rate = 44100
    samples = int(sample_rate * duration)
    
    # Use features to determine musical parameters
    base_freq = 220 + (features[0] * 440)  # 220Hz (A3) to 660Hz (E5)
    rhythm_complexity = features[1]
    harmony_complexity = features[2]
    
    # Determine tempo based on image brightness
    brightness = get_image_brightness(image)
    tempo = 160 - int(brightness * 80)  # 80 to 160 BPM, inverted so darker is faster
    
    # Create a simple melody
    melody_notes = [base_freq, base_freq * 2**(2/12), base_freq * 2**(4/12), base_freq * 2**(5/12), base_freq * 2**(7/12)]
    melody = np.zeros(samples)
    note_duration = 60 / tempo  # duration of each note in seconds
    for i in range(int(duration / note_duration)):
        note_samples = int(sample_rate * note_duration)
        start = i * note_samples
        end = start + note_samples
        note = create_sine_wave(np.random.choice(melody_notes), note_duration, sample_rate)
        melody[start:end] += note
    
    # Create harmony
    harmony_notes = [base_freq / 2, base_freq * 2**(4/12), base_freq * 2**(7/12)]
    harmony = np.zeros(samples)
    for note in harmony_notes:
        harmony += create_sine_wave(note, duration, sample_rate)
    
    # Create rhythm
    rhythm = np.random.rand(samples) * rhythm_complexity
    rhythm[::int(sample_rate * 60 / tempo)] = 1  # Strong beat on the 1
    
    # Combine all elements
    audio = melody * 0.5 + harmony * 0.3 * harmony_complexity + rhythm * 0.2
    
    # Normalize and convert to 16-bit PCM
    audio = np.int16(audio / np.max(np.abs(audio)) * 32767)
    return audio, sample_rate

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/generate', methods=['POST'])
def generate_music():
    if 'image' not in request.files:
        return {'error': 'No image file provided'}, 400

    image_file = request.files['image']
    image = Image.open(io.BytesIO(image_file.read())).convert('RGB')
    
    audio, sample_rate = image_to_melodic_sound(image)
    
    output_file = 'generated_music.wav'
    wavfile.write(output_file, sample_rate, audio)

    return send_file(output_file, mimetype='audio/wav')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)