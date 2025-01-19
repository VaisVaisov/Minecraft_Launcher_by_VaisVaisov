import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
from minecraft_launcher_lib.install import install_minecraft_version

class DownloadThread(QThread):
    progress = pyqtSignal(int)

    def run(self):
        # Замените на ваши параметры загрузки
        version = "1.17.1"  # Версия Minecraft
        # Путь к директории, куда будет загружена версия
        directory = "./minecraft"

        # Функция для загрузки версии с обновлением прогресса
        def download_callback(current, total):
            if total > 0:
                self.progress.emit(int((current / total) * 100))

        current_max = 0
        def set_status(status):
            print(status)
        def set_progress(progress):
            if current_max != 0:
                print(f'Progress: {progress}/{current_max}')
                try:
                    self.progress.emit(int((progress/current_max) * 100))
                except Exception as e:
                    print(f'Error updating progress: {str(e)}')
        def set_max(new_max):
            global current_max
            current_max = new_max

        callback = {
            'setStatus': set_status,
            'setProgress': set_progress,
            'setMax': set_max
        }

        # Загружаем версию Minecraft
        install_minecraft_version(version, directory, callback=download_callback)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minecraft Version Downloader")
        self.setGeometry(100, 100, 300, 100)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)

        self.start_button = QPushButton("Start Download", self)
        self.start_button.clicked.connect(self.start_download)

        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.start_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_download(self):
        self.thread = DownloadThread()
        self.thread.progress.connect(self.update_progress)
        self.thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())