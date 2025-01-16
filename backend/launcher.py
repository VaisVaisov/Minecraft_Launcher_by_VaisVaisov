import minecraft_launcher_lib
import subprocess
import os

def install_loader(loader, version, directory):
    match loader:
        case 'forge':
            minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=directory)
            forge_version = minecraft_launcher_lib.forge.find_forge_version(version)
            minecraft_launcher_lib.forge.install_forge_version(forge_version, directory)
        case 'fabric':
            minecraft_launcher_lib.fabric.install_fabric(minecraft_version=version, minecraft_directory=directory)
        case 'vanilla':
            minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=directory)


def launch_loader(loader, version, directory, options):
    match loader:
        case 'forge':
            forge_version = minecraft_launcher_lib.forge.find_forge_version(version)
            forge_version = version + '-forge' + forge_version[forge_version.find('-'):]
            subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=forge_version, minecraft_directory=directory, options=options))
        case 'fabric':
            subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=directory, options=options))
        case 'vanilla':
            subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=directory, options=options))    
   

def start_launcher(version, username, directory, desired_loader):

    if not os.path.isdir(directory):
        os.mkdir(directory)
    
    options = {
        'username': username,
        'uuid': '',
        'token': ''
        }

    try:
        launch_loader(desired_loader, version, directory, options)
    except minecraft_launcher_lib.exceptions.VersionNotFound:
        install_loader(desired_loader, version, directory)
        launch_loader(desired_loader, version, directory, options)
    