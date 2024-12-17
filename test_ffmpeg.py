from pydub import AudioSegment
import os

# Chemins explicites vers FFmpeg et FFprobe
ffmpeg_path = os.path.join(os.getcwd(), "bin", "ffmpeg.exe")
ffprobe_path = os.path.join(os.getcwd(), "bin", "ffprobe.exe")

# Configuration Pydub
AudioSegment.converter = ffmpeg_path
AudioSegment.ffprobe = ffprobe_path

try:
    print("Test de conversion avec FFmpeg...")
    # Test de conversion d'un fichier MP3
    mp3_file = "test_audio.mp3"  # Assurez-vous que ce fichier existe dans le dossier
    wav_file = "test_output.wav"

    audio = AudioSegment.from_file(mp3_file, format="mp3")
    audio.export(wav_file, format="wav")
    print("Conversion réussie ! Fichier WAV créé :", wav_file)
except Exception as e:
    print(f"Erreur lors de la conversion : {e}")
