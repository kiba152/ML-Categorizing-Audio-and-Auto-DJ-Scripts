import tensorflow.keras as keras
import numpy as np
from pydub import AudioSegment
import librosa, os, glob 
# Now you can place the following block in another program to load saved model to that program
MODEL_PATH = 'model.h5'
NUMBER_SAMPLES_TO_CONSIDER = 22050 #1 sec
class _GenreClassifier:
    model = None
    _mappings = [
         "blues",
        "classical",
        "classics",
        "country",
        "disco",
        "hiphop",
        "jazz",
        "metal",
        "pop",
        "reggae",
        "rock",
        "trap"
    ]
    _instance = None
    def predict(self, file_path):
        # extract MFCCs using the preprocess function below 
        MFCCs = self.preprocess(file_path)#Shape of 2Darray is number of (segments/snapshots,coefficients)
        # convert 2D to 4D
        MFCCs = MFCCs[np.newaxis, ..., np.newaxis]#Creates a new axis at beginning and end for (samples,...,channels) 
                                    # thus making a 4D array of (samples,segments,coefficients,channels)
        # make prediction
        predictions = self.model.predict(MFCCs)
        predicted_index = np.argmax(predictions)
        predicted_keyword = self._mappings[predicted_index]
        return predicted_keyword

        # To preprocess audio file
    def preprocess(self, file_path, n_mfcc=13, n_fft=2048, hop_length=512):
        # Load file
        signal, sr = librosa.load(file_path)
        # Ensure consistency in audio length
        if len(signal) > NUMBER_SAMPLES_TO_CONSIDER:
            signal = signal[:NUMBER_SAMPLES_TO_CONSIDER]
        
        # Extract MFCCs
        MFCCs = librosa.feature.mfcc(signal,n_mfcc=n_mfcc, n_fft=n_fft,hop_length=hop_length)
        return MFCCs.T

# Ensure you have singleton aclss/one instance of genre classifier
def Genre_Classifier():
    if _GenreClassifier._instance is None:
        _GenreClassifier._instance = _GenreClassifier()
        _GenreClassifier.model = keras.models.load_model(MODEL_PATH)
    return _GenreClassifier._instance

# song_path = r"C:\Users\Kariuki\Documents\Python\Audio\Data\genres_original\hiphop\hiphop.00002.wav"
# song = "BUTTERFLY EFFECT"
# song_mp3 = song+'.mp3'
# song_wav = song+'.wav'

song_category = []

path = r"C:\Users\Kariuki\Music"
output = r"C:\Users\Kariuki\Documents\Python\Audio\Categorized\\"
def categorize_loop(path):
    g = glob.glob(path+'\*.mp3')
# print(g)
    for f in g:
        song_category.append(f)
    while song_category != 0:
        for song in song_category:
            AUDIO_FILE1 = song_category[0]
            slash = path + '\\'
            AUDIO_FILE_EXTENSION1 = AUDIO_FILE1.replace(slash,'')
            AUDIO_FILE_EXTENSION2  = AUDIO_FILE_EXTENSION1.replace('.mp3','.wav')
            song_audio = AudioSegment.from_file(song_category[0])
            song_audio.export(AUDIO_FILE_EXTENSION1, format="wav")
            gc = Genre_Classifier()
            first= gc.predict(song_category[0])
            print(f'Predicted keyword: {first}')
            predicted_song = first+AUDIO_FILE_EXTENSION2
            song_audio.export(output+predicted_song, format="wav")
            song_category.pop(0)
    else:
        print('Done')
       

        # os.remove(AUDIO_FILE_EXTENSION1+'.wav')
# x = song_audio[25000:90000]
# song_audio.export(song_wav, format='wav')
# song_path = "montero.wav"
if __name__ == '__main__':
    categorize_loop(path=path)
    

