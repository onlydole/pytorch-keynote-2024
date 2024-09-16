import React, { useState, useRef } from 'react';
import { Upload, Music, Loader } from 'lucide-react';

function App() {
  const [image, setImage] = useState(null);
  const [audioSrc, setAudioSrc] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const fileInputRef = useRef(null);
  const audioRef = useRef(null);

  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    if (file && file.type.substr(0, 5) === "image") {
      setImage(URL.createObjectURL(file));
      setAudioSrc(null);
      setError(null);
    } else {
      setError("Please select a valid image file.");
    }
  };

  const generateMusic = async () => {
    if (!image) {
      setError("Please upload an image first.");
      return;
    }

    setIsLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('image', await fetch(image).then(r => r.blob()), 'image.jpg');

    try {
      const response = await fetch('/generate', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Failed to generate music');
      }

      const blob = await response.blob();
      setAudioSrc(URL.createObjectURL(blob));
    } catch (err) {
      setError("An error occurred while generating music. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">
        <div className="md:flex">
          <div className="p-8">
            <div className="uppercase tracking-wide text-sm text-indigo-500 font-semibold mb-1">
              Generative Music App
            </div>
            <p className="block mt-1 text-lg leading-tight font-medium text-black">
              Turn your drawings into music!
            </p>
            <p className="mt-2 text-gray-500">
              Upload an image and we'll generate a unique musical piece based on it.
            </p>
            
            <div className="mt-4">
              <input
                type="file"
                accept="image/*"
                onChange={handleImageUpload}
                ref={fileInputRef}
                className="hidden"
              />
              <button
                onClick={() => fileInputRef.current.click()}
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded inline-flex items-center"
              >
                <Upload className="mr-2" />
                <span>Upload Image</span>
              </button>
            </div>

            {image && (
              <div className="mt-4">
                <img src={image} alt="Uploaded" className="w-full rounded-lg shadow-lg" />
              </div>
            )}

            <button
              onClick={generateMusic}
              disabled={!image || isLoading}
              className={`mt-4 ${
                image && !isLoading
                  ? 'bg-green-500 hover:bg-green-700'
                  : 'bg-gray-300 cursor-not-allowed'
              } text-white font-bold py-2 px-4 rounded inline-flex items-center`}
            >
              {isLoading ? (
                <Loader className="animate-spin mr-2" />
              ) : (
                <Music className="mr-2" />
              )}
              <span>{isLoading ? 'Generating...' : 'Generate Music'}</span>
            </button>

            {audioSrc && (
              <div className="mt-4">
                <audio ref={audioRef} controls src={audioSrc} className="w-full" />
              </div>
            )}

            {error && (
              <div className="mt-4 bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span className="block sm:inline">{error}</span>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;