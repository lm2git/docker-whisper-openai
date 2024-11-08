# Usa una base Python slim per ridurre la dimensione dell'immagine
FROM python:3.9-slim

# Installa dipendenze di sistema come ffmpeg e git
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Installa Whisper e googletrans
RUN pip install --no-cache-dir git+https://github.com/openai/whisper.git \
    googletrans==4.0.0-rc1

# Imposta la cartella di lavoro
WORKDIR /app

# Copia lo script principale, ad esempio main.py, nella cartella di lavoro
COPY main.py /app/main.py

# Comando di default per eseguire lo script
CMD ["python", "main.py"]
