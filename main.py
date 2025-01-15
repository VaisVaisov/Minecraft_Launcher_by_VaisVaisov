import minecraft_launcher_lib
import subprocess

version = '1.12.2'
username = 'Vais55'
directory = '.launcher'

options = {
    'username': username,
    'uuid': '',
    'token': ''
}


def launch():
    minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=directory)

    if input('Would you like to install Forge? (y/n): ') == 'y':
        minecraft_launcher_lib.forge.forge_to_installed_version(forge_version=version)

    subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=directory, options=options))
