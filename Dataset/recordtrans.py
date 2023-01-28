import speech_recognition as sr
import os
import wave

# Set up the microphone
r = sr.Recognizer()
mic = sr.Microphone()

# Create a directory for the audio files and transcriptions
if not os.path.exists('audio'):
    os.makedirs('audio')
if not os.path.exists('transcriptions'):
    os.makedirs('transcriptions')

# Record and transcribe audio from the microphone
for i in range(10):
    print(f"Recording response {i+1}...")
    with mic as source:
        audio = r.record(source, duration=5)
    transcription = r.recognize_google(audio)

    # Save the recorded audio to a WAV file
    filename = f"audio/response_{i+1}.wav"
    with wave.open(filename, 'wb') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(16000)
        f.writeframes(audio.get_wav_data())

    # Save the transcription to a text file
    filename = f"transcriptions/response_{i+1}.txt"
    with open(filename, 'w') as f:
        f.write(transcription)

print("Transcriptions saved to text files.")
