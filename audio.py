import os
from pytube import YouTube
import pandas as pd


def download_audio(url, output_path="."):
    try:
        # Cria um objeto YouTube com a URL do vídeo
        yt = YouTube(url)

        # Pega a stream de áudio de maior resolução disponível
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Baixa o áudio para o caminho especificado
        out_file = audio_stream.download(output_path)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


# Exemplo de uso
if __name__ == '__main__':
    video_url = "https://www.youtube.com/watch?v=TT8p8r9U8OY"
    download_audio(video_url, "audio/")
