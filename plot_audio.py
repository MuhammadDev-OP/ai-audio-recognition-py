import wave
import numpy as np
import matplotlib.pyplot as plt
import speech_recognition as sr
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import speech_recognition as sr
import tkinter as tk
from tkinter import ttk
import pickle
import os

wav_obj = wave.open('new_file.wav', 'r')

sample_freq = wav_obj.getframerate()
print(sample_freq)

n_samples = wav_obj.getnframes()
print(n_samples)

t_audio = n_samples/sample_freq
print(t_audio, "seconds")

signal_wave = wav_obj.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
print(signal_array.shape)

# for stereo:
#l_channel = signal_array[0::2]
#r_channel = signal_array[1::2]

times = np.linspace(0, n_samples/sample_freq, num=n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title('Audio')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()


plt.figure(figsize=(15, 5))
plt.specgram(signal_array, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()

wav_obj = wave.open('output2.wav', 'r')

sample_freq = wav_obj.getframerate()
print(sample_freq)

n_samples = wav_obj.getnframes()
print(n_samples)

t_audio = n_samples/sample_freq
print(t_audio, "seconds")

signal_wave = wav_obj.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
print(signal_array.shape)

# for stereo:
#l_channel = signal_array[0::2]
#r_channel = signal_array[1::2]

times = np.linspace(0, n_samples/sample_freq, num=n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title('Audio')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()


plt.figure(figsize=(15, 5))
plt.specgram(signal_array, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()


'''

class AudioComparisonGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # set up the GUI
        self.title("Audio Comparison")
        self.geometry("600x400")
        self.resizable(False, False)

        # create the widgets
        self.intro_label = tk.Label(self, text="Enter the file paths for the two audio files you want to compare:")
        self.intro_label.pack(pady=10)

        self.file1_entry = tk.Entry(self)
        self.file1_entry.pack()

        self.file2_entry = tk.Entry(self)
        self.file2_entry.pack()

        self.compare_button = tk.Button(self, text="Compare", command=self.compare_audio_files)
        self.compare_button.pack(pady=10)

        self.result_label = tk.Label(self)
        self.result_label.pack(pady=10)

        self.transcription1_label = tk.Label(self)
        self.transcription1_label.pack()

        self.transcription2_label = tk.Label(self)
        self.transcription2_label.pack()

    def transcribe_audio_file(self, audio_file):
        # set up the recognizer
        r = sr.Recognizer()

        # read the audio file
        with sr.AudioFile(audio_file) as source:
            audio_data = r.record(source)

        # recognize the speech in the audio file
        transcription = r.recognize_google(audio_data)
        return transcription

    def compare_transcriptions(self, transcription1, transcription2):
        # compare the transcriptions and return True if they match, False otherwise
        return transcription1 == transcription2

    def open_door(self):
        # code to open the door goes here
        print("Opening the door!")

    def compare_audio_files(self):
        # get the file paths for the two audio files
        file1 = self.file1_entry.get()
        file2 = self.file2_entry.get()

        # transcribe the audio files
        transcription1 = self.transcribe_audio_file(file1)
        transcription2 = self.transcribe_audio_file(file2)

        # compare the transcriptions
        if self.compare_transcriptions(transcription1, transcription2):
            result = "Transcriptions match! Opening the door."
            self.open_door()
        else:
            result = "Transcriptions do not match. Door will not be opened."

        # update the labels with the transcript
                # update the labels with the transcriptions and result
        self.result_label.config(text=result)
        self.transcription1_label.config(text="Transcription 1: " + transcription1)
        self.transcription2_label.config(text="Transcription 2: " + transcription2)

if __name__ == "__main__":
    gui = AudioComparisonGUI()
    gui.mainloop()

'''

'''
import speech_recognition as sr
from tkinter import ttk

class AudioComparisonGUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # set up the GUI
        self.parent = parent
        self.parent.title("Audio Comparison")
        self.parent.geometry("600x400")
        self.parent.resizable(False, False)
        self.parent.configure(background="#333333")

        # create the widgets
        self.intro_label = ttk.Label(self, text="Enter the file paths for the two audio files you want to compare:",
                                     font=("Arial", 14), foreground="#FFFFFF", background="#333333")
        self.intro_label.pack(pady=10)

        self.file1_entry = ttk.Entry(self, font=("Arial", 14), foreground="#000000", background="#FFFFFF")
        self.file1_entry.pack()

        self.file2_entry = ttk.Entry(self, font=("Arial", 14), foreground="#000000", background="#FFFFFF")
        self.file2_entry.pack()

        self.compare_button = ttk.Button(self, text="Compare", style="Custom.TButton",
                                         command=self.compare_audio_files)
        self.compare_button.pack(pady=10)

        self.result_label = ttk.Label(self, font=("Arial", 16), foreground="#FFFFFF", background="#333333")
        self.result_label.pack(pady=10)

        self.transcription1_label = ttk.Label(self, font=("Arial", 14), foreground="#FFFFFF", background="#333333")
        self.transcription1_label.pack()

        self.transcription2_label = ttk.Label(self, font=("Arial", 14), foreground="#FFFFFF", background="#333333")
        self.transcription2_label.pack()

        # set up the styling
        self.style = ttk.Style()
        self.style.configure("Custom.TButton", font=("Arial", 14), foreground="#FFFFFF", background="#333333",
                             relief="flat", padding=10)
        self.style.map("Custom.TButton", background=[("active", "#444444")])

    def transcribe_audio_file(self, audio_file):
        # set up the recognizer
        r = sr.Recognizer()

        # read the audio file
        with sr.AudioFile(audio_file) as source:
            audio_data = r.record(source)

        # recognize the speech in the audio file
        transcription = r.recognize_google(audio_data)
        return transcription

    def compare_transcriptions(self, transcription1, transcription2):
                # compare the transcriptions and return True if they match, False otherwise
        return transcription1 == transcription2

    def open_door(self):
        # code to open the door goes here
        print("Opening the door!")

    def compare_audio_files(self):
        # get the file paths for the two audio files
        file1 = self.file1_entry.get()
        file2 = self.file2_entry.get()

        # transcribe the audio files
        transcription1 = self.transcribe_audio_file(file1)
        transcription2 = self.transcribe_audio_file(file2)

        # compare the transcriptions
        if self.compare_transcriptions(transcription1, transcription2):
            result = "Transcriptions match! Opening the door."
            self.open_door()
        else:
            result = "Transcriptions do not match. Door will not be opened."

        # update the labels with the transcriptions and result
        self.result_label.config(text=result)
        self.transcription1_label.config(text="Transcription 1: " + transcription1)
        self.transcription2_label.config(text="Transcription 2: " + transcription2)

if __name__ == "__main__":
    root = tk.Tk()
    gui = AudioComparisonGUI(root)
    gui.pack()
    root.mainloop()


'''


class WelcomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # set up the welcome page
        self.parent = parent
        self.parent.title("Audio Comparison")
        self.parent.geometry("800x1000")
        self.parent.resizable(False, False)
        self.parent.configure(background="#333333")

        # create the widgets
        self.hero_title = tk.Label(self, text="Welcome to the Audio Comparison Tool!", font=("Arial", 24),
                                    foreground="#FFFFFF", background="#333333")
        self.hero_title.pack(pady=20)

        self.intro_label = tk.Label(self, text="This tool allows you to compare two audio files and see if they match.",
                                     font=("Arial", 14), foreground="#FFFFFF", background="#333333")
        self.intro_label.pack(pady=10)

        self.start_button = tk.Button(self, text="Start", font=("Arial", 14), foreground="#FFFFFF",
                                      background="#333333", activebackground="#444444", relief="flat",
                                      command=self.start)
        self.start_button.pack(pady=10)

    def start(self):
        # switch to the main page
        self.parent.switch_frame(MainPage)

class MainPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # set up the main page
        self.parent = parent
        self.parent.title("Audio Comparison")
        self.parent.geometry("800x1000")
        self.parent.resizable(False, False)
        self.parent.configure(background="#333333")

        # create the widgets
        self.intro_label = tk.Label(self, text="Enter the file paths for the two audio files you want to compare:",
                                     font=("Arial", 14), foreground="#FFFFFF", background="#333333")
        self.intro_label.pack(pady=10)

        self.file1_entry = tk.Entry(self, font=("Arial", 14), foreground="#000000", background="#FFFFFF")
        self.file1_entry.pack()
        self.file2_entry = tk.Entry(self, font=("Arial", 14), foreground="#000000", background="#FFFFFF")
        self.file2_entry.pack()

        self.compare_button = tk.Button(self, text="Compare", font=("Arial", 14), foreground="#FFFFFF",
                                        background="#333333", activebackground="#444444", relief="flat",
                                        command=self.compare_audio_files)
        self.compare_button.pack(pady=10)

        self.result_label = tk.Label(self, font=("Arial", 16), foreground="#FFFFFF", background="#333333")
        self.result_label.pack(pady=10)

        self.transcription1_label = tk.Label(self, font=("Arial", 14), foreground="#FFFFFF", background="#333333")
        self.transcription1_label.pack()

        self.transcription2_label = tk.Label(self, font=("Arial", 14), foreground="#FFFFFF", background="#333333")
        self.transcription2_label.pack()

        self.back_button = tk.Button(self, text="Back", font=("Arial", 14), foreground="#FFFFFF",
                                     background="#333333", activebackground="#444444", relief="flat",
                                     command=self.back)
        self.back_button.pack(pady=10)

    def transcribe_audio_file(self, audio_file):
        # set up the recognizer
        r = sr.Recognizer()

        # read the audio file
        with sr.AudioFile(audio_file) as source:
            audio_data = r.record(source)

        # recognize the speech in the audio file
        transcription = r.recognize_google(audio_data)
        return transcription

    def compare_transcriptions(self, transcription1, transcription2):
        # compare the transcriptions and return True if they match, False otherwise
        return transcription1 == transcription2

    def open_door(self):
        # code to open the door goes here
        print("Opening the door!")

    def compare_audio_files(self):
        # get the file paths for the two audio files
        file1 = self.file1_entry.get()
        file2 = self.file2_entry.get()

        # transcribe the audio files
        transcription1 = self.transcribe_audio_file(file1)
        transcription2 = self.transcribe_audio_file(file2)

        # compare the transcriptions
        if self.compare_transcriptions(transcription1, transcription2):
            result = "Transcriptions match! Opening the door."
            self.open_door()
        else:
            result = "Transcriptions do not match. Door will not be opened."

        # update the labels with the transcriptions and result
        self.result_label.config(text=result)
        self.transcription1_label.config(text="Transcription 1: " + transcription1)
        self.transcription2_label.config(text="Transcription 2: " + transcription2)

    def back(self):
        # switch back to the welcome page
        self.parent.switch_frame(WelcomePage)

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Audio Comparison")
        self.geometry("600x400")
        self.resizable(False, False)
        self.configure(background="#333333")
        self.switch_frame(WelcomePage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if hasattr(self, "current_frame"):
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()


