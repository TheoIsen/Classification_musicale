from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import os
import librosa
import numpy as np
from pydub import AudioSegment
import io
import tempfile

app = Flask(__name__)

# Charger le modèle CNN
model = load_model("modele_final.h5")

# Mapping des classes prédictes
label_map = {
    0: "hiphop",
    1: "disco",
    2: "metal",
    3: "jazz",
    4: "blues",
    5: "reggae",
    6: "pop",
    7: "classical",
    8: "rock",
    9: "country"
}

# Configuration explicite de FFmpeg pour Pydub
ffmpeg_path = os.path.join(os.getcwd(), "bin", "ffmpeg.exe")
ffprobe_path = os.path.join(os.getcwd(), "bin", "ffprobe.exe")

AudioSegment.converter = ffmpeg_path
AudioSegment.ffprobe = ffprobe_path

# Route principale
@app.route("/", methods=["GET", "POST"])
def upload_file():
    prediction = None

    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename.endswith(".mp3"):
            try:
                # Lire le fichier MP3 en mémoire
                mp3_data = io.BytesIO(file.read())

                # Conversion MP3 -> WAV dans un fichier temporaire
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav:
                    audio = AudioSegment.from_file(mp3_data, format="mp3")
                    audio.export(temp_wav.name, format="wav")

                    # Charger le fichier WAV avec Librosa
                    y, sr = librosa.load(temp_wav.name, sr=None)
                    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
                    S_db = librosa.power_to_db(S, ref=np.max)

                # Redimensionner le mel-spectrogramme à (128, 128)
                if S_db.shape[1] > 128:
                    S_db = S_db[:, :128]
                else:
                    S_db = np.pad(S_db, ((0, 0), (0, 128 - S_db.shape[1])), mode='constant')

                # Normalisation et mise en forme
                S_db = S_db / np.max(S_db)
                input_data = np.expand_dims(S_db, axis=-1)  # Ajouter la dimension du canal
                input_data = np.expand_dims(input_data, axis=0)   # Ajouter la dimension du batch

                # Prédiction du modèle
                predictions = model.predict(input_data)
                predicted_class = np.argmax(predictions, axis=1)[0]
                prediction = label_map.get(predicted_class, "Inconnu")

            finally:
                # Nettoyage du fichier temporaire
                if os.path.exists(temp_wav.name):
                    os.remove(temp_wav.name)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
