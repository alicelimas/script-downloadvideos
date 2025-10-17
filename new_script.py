import sys
import yt_dlp
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class DownloaderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Downloader de Vídeos do YouTube")
        self.setGeometry(500, 200, 400, 200)  # Tamanho da janela (largura, altura)
        
        # Layout principal
        self.layout = QVBoxLayout()

        # Título
        self.title_label = QLabel("Baixe seus vídeos do YouTube!", self)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")
        self.layout.addWidget(self.title_label)

        # Campo para inserir a URL
        self.url_label = QLabel("Digite a URL do vídeo do YouTube:", self)
        self.layout.addWidget(self.url_label)

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Cole a URL aqui...")
        self.url_input.setStyleSheet("padding: 5px; font-size: 14px;")
        self.layout.addWidget(self.url_input)

        # Botão para iniciar o download
        self.download_button = QPushButton("Baixar Vídeo", self)
        self.download_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                font-size: 16px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.download_button.clicked.connect(self.baixar_video)
        self.layout.addWidget(self.download_button)

        # Configura o layout da janela
        self.setLayout(self.layout)

    def baixar_video(self):
        url = self.url_input.text()
        if not url:
            self.show_message("Erro", "Por favor, insira a URL do vídeo.")
            return

        try:
            # Diretório de Downloads do sistema
            pasta_downloads = os.path.expanduser("~/Downloads")
            
            # Opções para baixar o vídeo
            ydl_opts = {
                'outtmpl': os.path.join(pasta_downloads, '%(title)s.%(ext)s'),
            }
            
            # Baixar o vídeo
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            self.show_message("Sucesso", "Vídeo baixado com sucesso!")

        except Exception as e:
            self.show_message("Erro", f"Ocorreu um erro: {e}")

    def show_message(self, title, message):
        QMessageBox.information(self, title, message)

# Inicia a aplicação PyQt5
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Estilo moderno para o PyQt
    window = DownloaderApp()
    window.show()
    sys.exit(app.exec_())
