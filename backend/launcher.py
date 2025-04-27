from PyQt5.QtCore import QThread, pyqtSignal
import minecraft_launcher_lib
import subprocess
import os

class InstallThread(QThread):
    progress = pyqtSignal(int)
    max_value = pyqtSignal(int)
    status = pyqtSignal(str)

    def __init__(self, version, directory, loader):
        super().__init__()
        self.version = version
        self.directory = directory
        self.loader = loader

    def run(self):
        current_max = 0

        def set_status(status):
            self.status.emit(status)

        def set_progress(progress):
            if current_max != 0:
                value = int((progress / current_max) * 100)
                self.progress.emit(value)

        def set_max(new_max):
            nonlocal current_max
            current_max = new_max
            self.max_value.emit(current_max)

        callback = {
            'setStatus': set_status,
            'setProgress': set_progress,
            'setMax': set_max
        }

        match self.loader:
            case 'forge':
                minecraft_launcher_lib.install.install_minecraft_version(versionid=self.version,
                                                                        minecraft_directory=self.directory,
                                                                        callback=callback)
                forge_version = minecraft_launcher_lib.forge.find_forge_version(self.version)
                minecraft_launcher_lib.forge.install_forge_version(forge_version, self.directory)
            case 'fabric':
                minecraft_launcher_lib.fabric.install_fabric(minecraft_version=self.version,
                                                             minecraft_directory=self.directory,
                                                             callback=callback)
            case 'vanilla':
                minecraft_launcher_lib.install.install_minecraft_version(versionid=self.version,
                                                                         minecraft_directory=self.directory,
                                                                         callback=callback)


def launch_loader(version, directory, loader, options):
    match loader:
        case 'forge':
            forge_version = minecraft_launcher_lib.forge.find_forge_version(version)
            forge_version = version + '-forge' + forge_version[forge_version.find('-'):]
            subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=forge_version,
                                                                                 minecraft_directory=directory,
                                                                                 options=options))
        case 'fabric':
            subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version,
                                                                                 minecraft_directory=directory,
                                                                                 options=options))
        case 'vanilla':
            subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version,
                                                                                 minecraft_directory=directory,
                                                                                 options=options))
    return True


def version_is_installed(version, directory):
    installed_versions = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory=directory)
    for installing_version in installed_versions:
        if installing_version['id'] == version:
            return True
    return False


def check_directory(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)
