# Text-to-Audio Converter

This is a Python script that converts text input into audio using the gTTS (Google Text-to-Speech) library. It allows you to generate audio files from text and save them as MP3 files.

## Requirements

- Python 3.x
- gTTS library

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command in your Python environment:

pip install gTTS


## Usage

1. Open the terminal or command prompt and navigate to the project directory.
2. Run the script by executing the following command:

python file.py


3. Enter the desired text when prompted.
4. The script will generate an audio file with the speech and save it as "output_audio.mp3" in the same directory.
5. The path to the saved audio file will be displayed in the console.

## Example

Here's an example usage:

$ python file.py
Enter the text: welcome in digital world!
Audio saved as output_audio.mp3


This will generate an audio file with the speech "Hello, World!" and save it as "output_audio.mp3" in the project directory.

## Customization

- Language: By default, the script uses English as the language. You can specify a different language by modifying the `lang` parameter when creating the `gTTS` object. Refer to the gTTS documentation for the list of available languages and their language codes.
