import minecraft_launcher_lib
import subprocess
import os
from frontend.ui.launcher_ui import Ui_MainWindow




def install_loader(version, directory, loader, callback):

    match loader:
        case 'forge':
            minecraft_launcher_lib.install.install_minecraft_version(versionid=version,
                                                                     minecraft_directory=directory,
                                                                     callback=callback)
            forge_version = minecraft_launcher_lib.forge.find_forge_version(version)
            minecraft_launcher_lib.forge.install_forge_version(forge_version, directory)
        case 'fabric':
            minecraft_launcher_lib.fabric.install_fabric(minecraft_version=version,
                                                         minecraft_directory=directory,
                                                         callback=callback)
        case 'vanilla':
            minecraft_launcher_lib.install.install_minecraft_version(versionid=version,
                                                                     minecraft_directory=directory,
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
        else:
            return False

def check_directory(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)
