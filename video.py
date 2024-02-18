from pytube import YouTube

def download_video(url, output_path="."):
    try:
        # Cria um objeto YouTube com a URL do vídeo
        yt = YouTube(url)

        # Pega a stream de vídeo de maior resolução disponível
        video_stream = yt.streams.get_highest_resolution()

        # Baixa o vídeo para o caminho especificado
        video_stream.download(output_path)

        print("Download concluído com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
video_url = "https://www.youtube.com/watch?v=dZu98_pC0kU"
download_video(video_url, "video/")