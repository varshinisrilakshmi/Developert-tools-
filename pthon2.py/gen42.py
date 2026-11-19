
import sounddevice as sd
import numpy as np
import wave
import os
from google import genai
from getpass import getpass

# Enter Gemini API key
api_key = getpass("Enter your Gemini API key: ")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Audio settings
duration = 5
fs = 16000
filename = "voice_input.wav"

print("\nVoice Input Speech-to-Text Assistant")

try:
    # Record voice
    print("\nSpeak now (recording for 5 seconds)...")

    audio = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype=np.int16
    )

    sd.wait()
    print("Recording completed!")

    # Save audio as WAV file
    with wave.open(filename, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(fs)
        f.writeframes(audio.tobytes())

    print("\nUploading audio to Gemini...")

    # Upload audio file
    uploaded_file = client.files.upload(file=filename)
    print("Audio uploaded successfully!")

    # Generate response
    print("\nProcessing audio with Gemini...")

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=[
            "Listen to this voice input. First write the exact "
            "words spoken, then respond to what was said:",
            uploaded_file
        ]
    )

    print("\nGemini Response:")
    print(response.text or "No response received.")

except Exception as e:
    print("\nError:", e)

finally:
    # Delete temporary audio file
    if os.path.exists(filename):
        os.remove(filename)
