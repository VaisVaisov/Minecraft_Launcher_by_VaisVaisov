from PyQt5 import QtWidgets

import os
import sys

from minecraft_launcher_lib import utils

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from frontend.ui.launcher_ui import Ui_MainWindow
from backend.launcher import InstallThread, launch_loader, version_is_installed, check_directory

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.launch_button.clicked.connect(self.launch_minecraft)
        self.browse_button.clicked.connect(self.browse_directory)

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
            self.hide()
            launch_loader(version, directory, desired_loader, options)
            self.show()
        else:
            print('Installing Minecraft...')
            self.install_thread = InstallThread(version, directory, desired_loader)
            self.install_thread.progress.connect(self.update_progress)
            self.install_thread.max_value.connect(self.update_max_progress)
            self.install_thread.status.connect(self.update_status)
            self.install_thread.finished.connect(self.on_install_finished)
            self.install_thread.start()

    def on_install_finished(self):
        version = self.get_current_version()
        username = self.get_username()
        directory = self.get_minecraft_directory()
        desired_loader = self.get_current_mod_loader()
        options = {
            'username': username,
            'uuid': '',
            'token': ''
        }
        print('Launching Minecraft...')
        self.hide()
        launch_loader(version, directory, desired_loader, options)
        self.show()

    def update_progress(self, value):
        self.loading_progressbar.setValue(value)

    def update_max_progress(self, max_value):
        self.loading_progressbar.setMaximum(max_value)

    def update_status(self, status):
        self.launch_status.setText(status)

    def browse_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Installation Directory for Minecraft')
        if directory:
            self.minecraft_directory_field.setText(directory)

    def get_username(self):
        return self.username_field.text()

    def get_current_version(self):
        return self.version_list.currentText()

    def get_current_mod_loader(self):
        if self.forge_flag.isChecked():
            return 'forge'
        elif self.fabric_flag.isChecked():
            return 'fabric'
        elif self.vanilla_flag.isChecked():
            return 'vanilla'
        return None

    def get_minecraft_directory(self):
        if self.standard_directory_flag.isChecked():
            return utils.get_minecraft_directory()
        else:
            return self.minecraft_directory_field.text()

    # def launch_content_downloader(self):
    #     start_content_downloader()
