from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from frontend.ui.launcher_ui import Ui_MainWindow

from backend.launcher import start_launcher
from backend.mod_downloader import start_mod_downloader

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.launch_button.clicked.connect(lambda: self.launch_minecraft())
        # self.launch_mod_loader_button.clicked.connect(self.launch_mod_downloader)

    def launch_minecraft(self):
        print('Minecraft is launching...')
        version = self.get_current_version()
        username = self.get_username()
        directory = self.get_minecraft_directory()
        desired_loader = self.get_current_mod_loader()
        start_launcher(version, username, directory, desired_loader)

    # def launch_mod_downloader(self):
    #     start_mod_downloader()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()