
# Whisper Docker - Video Transcription

This project uses OpenAI's Whisper to transcribe video files into text. The system is built with Docker and Whisper, with the ability to mount volumes for input (video) and output (transcription).

## Prerequisites

Make sure you have the following tools installed:

- **Docker**: To run the containers.
  - [docker on Windows](docs/win-README.md)
  - [docker on Linux](docs/linux-README.md)
- **git**: To clone repository  
  - [git setup](https://git-scm.com/book/it/v2/Per-Iniziare-Installing-Git)

## Steps for Installation and Execution

Clone repository

```bash
git clone https://github.com/lm2git/docker-whisper-openai.git
cd docker-whisper-openai
```
### 1. **Build the Docker Image**

Navigate to the main folder of the project where `Dockerfile` and `main.py` are located, then build the Docker image with the following command:

on your terminal:
```bash
docker build -t whisper-container .
```
This command will build a Docker image named whisper-container.

### 2. Run the Container with Mounted Volumes

To run the container and transcribe all .mp4 video files, use the `docker run` command by mounting the folder containing the videos (media folder) and the output folder for the transcription files. Be sure to replace the paths with those that are correct for your system.

Example command on Windows on command propt :
```bash
docker run --rm -v C:\path\to\media:/app/media -v C:\path\to\output:/app/output whisper-container
```

Example command on macOS/Linux on your terminal:
```bash
docker run --rm -v /path/to/media:/app/media -v /path/to/output:/app/output whisper-container
```

#### Example paths
/path/to/media: The path to the folder containing the .mp4 video files you want to transcribe (local).
/path/to/output: The folder where you want to save the transcription files (the generated .txt files).

### 3. Check the Transcription
After the container has completed execution, you will find the transcription files in the output folder you specified. Each transcription file will be named after the video and the date/time when the transcription was done, for example:

```lua
/path/to/output/video1_2024-11-06_14-30-00_transcription.txt
/path/to/output/video2_2024-11-06_14-45-00_transcription.txt
```

## Common Issues and Solutions
Error on FP16 not supported on CPU:
This warning is normal if you are running the code on a CPU. Whisper will automatically switch to FP32 without any issues.

torch.load security warning:
This warning concerns a future change in PyTorch libraries. Currently, you don't need to modify anything, but be aware when updating libraries in the future.
