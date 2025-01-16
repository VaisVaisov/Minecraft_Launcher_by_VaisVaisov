import minecraft_launcher_lib
import subprocess
import os

import minecraft_launcher_lib.install

version = input('Which Minecraft version you desire to download? (e.g. 1.12.2): ')
username = input('Which your username? ')

if not os.path.isdir('.launcher'):
    os.mkdir('.launcher')
directory = '.launcher'

options = {
    'username': username,
    'uuid': '',
    'token': ''
}


def forge_install(version, directory):
    forge_version = minecraft_launcher_lib.forge.find_forge_version(version)
    minecraft_launcher_lib.forge.install_forge_version(forge_version, directory)
    forge_version = version + '-forge' + forge_version[forge_version.find('-'):]
    subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=forge_version, minecraft_directory=directory, options=options))

def fabric_install(version, directory):
    minecraft_launcher_lib.fabric.install_fabric(minecraft_version=version, minecraft_directory=directory)
    subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=directory, options=options))


def vanilla_install(version, directory):
    minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=directory)
    subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=directory, options=options))
   

def launch():
    desired_loader = input('Which mod loader you desire to download? (Forge, Fabric, Vanilla): ').lower()    
    match desired_loader:
        case 'forge':
            forge_install(version, directory)
        case 'fabric':
            fabric_install(version, directory)
        case 'vanilla':
            vanilla_install(version, directory)



if __name__ == '__main__':
    launch()
    