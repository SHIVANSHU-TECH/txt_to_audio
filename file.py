from gtts import gTTS

# Define the text to be converted to audio
text = input("Enter the text:")

# Create a gTTS object with the text and language
tts = gTTS(text=text, lang="en")

# Specify the path to save the audio file
audio_file_path = "output_audio.mp3"

# Save the audio file
tts.save(audio_file_path)
print(f"Audio saved as {audio_file_path}")
