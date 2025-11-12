from gtts import gTTS
import os

# Read text from a file
with open("python-basics/input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Convert text to speech
tts = gTTS(text=text, lang='en')

# Save as audio file
tts.save("output.mp3")

# Play the audio
os.system("start output.mp3")   # For Windows
# os.system("afplay output.mp3") # For macOS
# os.system("mpg321 output.mp3") # For Linux
