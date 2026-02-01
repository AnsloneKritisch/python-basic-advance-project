# ============================================================================
# Voice Assistant - Text-to-Speech (TTS) Program
# ============================================================================
# Install required library: pip install pyttsx3
# This program uses pyttsx3 to give the assistant a voice

# Import the pyttsx3 library for text-to-speech functionality
import pyttsx3

# Initialize the TTS (Text-to-Speech) engine
# pyttsx3.init() sets up the speech engine and returns an engine object
engine = pyttsx3.init()

# Use the engine to speak a greeting message
# engine.say() queues the text to be spoken
engine.say("I'm ready for your command!")

# Process and play the queued speech
# runAndWait() executes the speech and waits until it's finished
engine.runAndWait() 
