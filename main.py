import minecraft_launcher_lib
import subprocess

version = 'rd-132328'
username = 'Vais55'
directory = '.launcher'

minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=directory)

options = {
    'username': username,
    'uuid': '',
    'token': ''
}

subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=directory, options=options))
