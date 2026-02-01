# ============================================================================
# Voice Assistant - Basic Speech Recognition Program
# ============================================================================
# Install required library: 
# pip install SpeechRecognition (not recommended version 3.14+)
'''
So here's the thing we can install 3.14+ but it messes up the recognize_google function.
Plus it will ask for some stupid api ? and it will slow you down , so we need to downgrade to a stable version
that works perfectly fine without any api key or anything.

🧠 Why I’m Suggesting Downgrade

Version 3.14+ introduced a new API system that requires different setup.

For learning + building your first assistant:

👉 3.10.0 is simpler
👉 Tons of tutorials use it
👉 Less headache

'''
# Install this instead:
# pip install SpeechRecognition==3.10.0
# This program captures audio from microphone and converts it to text using Google's speech recognition API.

# 🛠️ Fixing recognize_google Issue in SpeechRecognition Library
# pip uninstall SpeechRecognition( if you have 3.14+ installed )
# pip install SpeechRecognition==3.10.0


# Then we need to install the following dependencies for Voice recognize to work:
# pip install pocketsphinx (If you want offline recognition)
'''
A important note here is that pocketsphinx is used for offline speech recognition.
But but ...........
It have bad recognition accuracy compared to online services like Google.
So if you want better accuracy use google recognize function. Which is inbuild and you have to install nothing.
But if you want to use it offline then you need to install pocketsphinx.( not recommended from my side)

'''
# Then install pyaudio for microphone access:
# pip install PyAudio

# ----------------------------------------------------------

'''

🎯 After Downgrade Test This:
import speech_recognition as sr
print("recognize_google" in dir(sr.Recognizer()))
print("recognize_sphinx" in dir(sr.Recognizer()))

If both print True → you’re locked in 🔥 → you’re good to go 🚀

It means:

✅ recognize_google exists
✅ recognize_sphinx exists
✅ You are now using the correct version (3.10.0)
✅ Your environment is finally clean

'''

# ----------------------------------------------------------
# CODES

# Import the speech_recognition library for audio capture and processing
import speech_recognition as sr

# Create a Recognizer object - this will process the audio and recognize speech
recognizer = sr.Recognizer()

# Use Microphone as the audio source within a context manager
with sr.Microphone() as source:
    print("Say something...")

    # Adjust for ambient noise to improve recognition accuracy
    # This samples the background noise for 1 second
    recognizer.adjust_for_ambient_noise(source, duration=1)

    # Listen to microphone input and capture audio until silence is detected
    audio = recognizer.listen(source)

# Try to process the audio and recognize speech
try:
    # Attempt speech recognition using Google's API
    text = recognizer.recognize_google(audio)
    print("You said:", text)

    # Check if the recognized text starts with "print" command
    if text.lower().startswith("print"):
        # Print the rest of the text after the "print" command (skip first 5 chars)
        print(text[6:])

# Exception handling for cases where audio could not be understood
except sr.UnknownValueError:
    print("Error: Could not understand the audio. Please speak clearly.")

# Exception handling for speech recognition service errors
except sr.RequestError as e:
    print(f"Error: Problem with the speech recognition service - {e}")
