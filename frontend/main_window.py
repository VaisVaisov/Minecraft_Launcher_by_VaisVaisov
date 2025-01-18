from PyQt5 import QtWidgets

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from frontend.ui.launcher_ui import Ui_MainWindow

from backend.launcher import version_is_installed, install_loader, launch_loader, check_directory
# from backend.mod_downloader import start_mod_downloader

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.launch_button.clicked.connect(lambda: self.launch_minecraft())
        # self.launch_mod_loader_button.clicked.connect(self.launch_mod_downloader)

    def launch_minecraft(self):
        version = self.get_current_version()
        username = self.get_username()
        directory = self.get_minecraft_directory()
        desired_loader = self.get_current_mod_loader()
        options = {
            'username': username,
            'uuid': '',
            'token': ''
        }
        check_directory(directory)
        if version_is_installed(version, directory):
            print('Launching Minecraft...')
            launch_loader(version, directory, desired_loader, options)
        else:
            print('Installing Minecraft...')
            install_loader(version, directory, desired_loader)
            print('Launching Minecraft...')
            launch_loader(version, directory, desired_loader, options)


    # def launch_mod_downloader(self):
    #     start_mod_downloader()
