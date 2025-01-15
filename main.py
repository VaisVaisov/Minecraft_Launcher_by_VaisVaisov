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


def forge_install():
    forge_version = minecraft_launcher_lib.forge.find_forge_version(vanilla_version=version)
    minecraft_launcher_lib.forge.forge_to_installed_version(forge_version=forge_version)


def launch():
    minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=directory)

    if input('Would you like to install Forge? (y/n): ') == 'y':
        forge_install()

    subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=directory, options=options))

if __name__ == '__main__':
    launch()
    