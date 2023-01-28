from cProfile import label
import pickle
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import speech_recognition as sr

# Set the directories for the audio files and transcriptions
audio_dir = 'f:/UNI cource/Sem 5/Ai Speech Recognition TEST/python-speech-recognition-course-main/ProjectAudio/Dataset/audio' # directory containing the audio files
transcription_dir = 'f:/UNI cource/Sem 5/Ai Speech Recognition TEST/python-speech-recognition-course-main/ProjectAudio/Dataset/transcriptions' # directory containing the transcriptions

# Load the dataset of audio files and transcriptions
audio_files = ['response_1.wav','response_2.wav',...] # list of audio files
transcriptions = ['response_1.txt','response_2.txt',...] # list of transcriptions for the audio files
labels = [0,1,2,3,4,5,6,7,8,9] # list of labels for the audio files (0 for speaker 1, 1 for speaker 2, etc.)
features = ['names','cities','happy','overwhelming','joy','charming','greeting','scolding','sad','yellow'] # list of feature vectors for the audio files

# Extract features from the transcriptions
def extract_features(transcriptions):
    # Extract features from the transcription
    # You can add any desired features here
    features = ['names','numbers',...]
    return features

# Load the audio files and transcriptions from the directories
for filename in os.listdir(audio_dir):
    if filename.endswith('.wav'):
        # Load the audio file
        audio_file = sr.AudioFile(os.path.join(audio_dir, filename))
        # Load the corresponding transcription
        transcription_filename = filename.replace('.wav', '.txt')
        with open(os.path.join(transcription_dir, transcription_filename), 'r') as f:
            transcription = f.read()
        # Extract features from the transcription
        features = extract_features(transcription)
        # Add the audio file, transcription, and features to the dataset
        audio_files.append(audio_file)
        transcriptions.append(transcription)
        features.append(features)
        labels.append(label)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

# Train the SVM model on the training set
svm = SVC()
svm.fit(X_train, y_train)

# Evaluate the model's performance on the test set
y_pred = svm.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save the trained model to a file
with open('svm.pkl', 'wb') as f:
    pickle.dump(svm, f)
