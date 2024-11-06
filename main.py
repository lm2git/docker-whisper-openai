import whisper
import os
from datetime import datetime

# Load the Whisper model
model = whisper.load_model("base")

# Folder containing the videos to transcribe
media_folder = "/app/media/"

# Check if the folder exists
if not os.path.exists(media_folder):
    print(f"The folder {media_folder} does not exist.")
    exit(1)

# Loop through all .mp4 files in the folder
for video_file in os.listdir(media_folder):
    if video_file.endswith(".mp4"):
        video_path = os.path.join(media_folder, video_file)

        # Transcribe the video
        print(f"Starting transcription of {video_path}...")
        result = model.transcribe(video_path)

        # Extract the file name without extension
        video_name = os.path.splitext(os.path.basename(video_path))[0]

        # Create a name for the transcription file with video name and timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        transcription_filename = f"/app/output/{video_name}_{timestamp}_transcription.txt"

        # Save the transcription to a file with the generated name
        with open(transcription_filename, "w") as f:
            f.write(result["text"])

        print(f"Transcription completed for {video_file}, saved to {transcription_filename}")

print("All transcriptions are completed.")
