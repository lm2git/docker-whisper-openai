import whisper
import os
from datetime import datetime
from googletrans import Translator  # Importa il traduttore di Google

# Carica il modello di Whisper
model = whisper.load_model("base")
translator = Translator()

# Cartelle per i video da trascrivere e i file di output
media_folder = "/app/media/"
output_folder = "/app/output/"

# Verifica se le cartelle esistono
if not os.path.exists(media_folder):
    print(f"La cartella {media_folder} non esiste.")
    exit(1)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop sui file .mp4 nella cartella
for video_file in os.listdir(media_folder):
    if video_file.endswith(".mp4"):
        video_path = os.path.join(media_folder, video_file)
        video_name = os.path.splitext(video_file)[0]
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Trascrizione nella lingua originale
        print(f"Inizio trascrizione di {video_path}...")
        result = model.transcribe(video_path)
        transcript_text = result["text"]
        
        # Salva trascrizione
        transcription_filename = os.path.join(output_folder, f"{video_name}_{timestamp}_transcription.txt")
        with open(transcription_filename, "w") as f:
            f.write(transcript_text)
        print(f"Trascrizione completata per {video_file}, salvata in {transcription_filename}")

        # Traduzione in italiano
        print(f"Inizio traduzione di {video_file} in italiano...")
        translation = translator.translate(transcript_text, dest="it").text
        
        # Salva traduzione
        translation_filename = os.path.join(output_folder, f"{video_name}_{timestamp}_translation_it.txt")
        with open(translation_filename, "w") as f:
            f.write(translation)
        print(f"Traduzione in italiano completata per {video_file}, salvata in {translation_filename}")

print("Tutte le trascrizioni e traduzioni sono state completate.")
