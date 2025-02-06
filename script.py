import yt_dlp
import os

# Função para baixar o vídeo
def baixar_video(url):
    try:
        # Diretório de Downloads do sistema
        pasta_downloads = os.path.expanduser("~/Downloads")
        
        # Opções para baixar o vídeo
        ydl_opts = {
            'outtmpl': os.path.join(pasta_downloads, '%(title)s.%(ext)s'),
        }
        
        # Baixar o vídeo
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Baixando o vídeo: {url}")
            ydl.download([url])
            print("Vídeo baixado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Solicita o link do vídeo
url_video = input("Digite a URL do vídeo do YouTube: ")
baixar_video(url_video)
