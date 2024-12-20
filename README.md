# Analyse de Genre Musical
## Description
Ce projet est une application web qui utilise un modèle CNN pour prédire le genre musical d'un fichier audio MP3 parmi 10 genres (hiphop, disco, metal, jazz, blues, reggae, pop, classical, rock et country).
L'application convertit les fichiers MP3 en format WAV, génère un melspectrogramme, et utilise un modèle CNN pré-entraîné pour analyser les motifs audio et fournir une prédiction.

## Structure du Projet
```plaintext
Classification_musicale/
├── bin/
│   ├── ffmpeg.exe
│   ├── ffplay.exe
│   └── ffprobe.exe
├── templates/
│   └── index.html
├── app.py
├── modele_final.h5
├── README.md
├── test_conversion.py
└── test_audio.mp3
```

## Description des Fichiers
#### app.py :
Fichier principal contenant le serveur Flask.
Charge le modèle de classification et traite les fichiers MP3.
#### index.html :
Interface utilisateur pour l'application web.
#### modele_final.h5 :
Modèle CNN pré-entraîné pour la classification des genres musicaux.
#### bin/ :
Contient les exécutables FFmpeg nécessaires pour traiter les fichiers audio.

## Installation
Exécutez la commande suivante pour cloner le dépôt :

```bash
git clone https://github.com/votre-utilisateur/Classification_musicale.git
```
Créer un environnement virtuel :

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

Installer les dépendances nécessaires : 
```bash
pip install flask tensorflow librosa numpy pydub
```

Assurez-vous que FFmpeg fonctionne correctement en exécutant le script suivant: 
```bash
python test_ffmpeg.py
```

Puis lancer l'application web :
```bash
python app.py
```
 Ouvrez votre navigateur et accédez à http://127.0.0.1:5000.



