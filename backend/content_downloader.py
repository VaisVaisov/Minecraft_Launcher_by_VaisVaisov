import requests
import json
import os


def check_directory(content_type):
    if not os.path.isdir(content_type + 's'):
        os.mkdir(content_type + 's')
        os.chdir(content_type + 's')
    else:
        os.chdir(content_type + 's')


def get_project_files(project_id, download_optional_dependencies_flag, game_version, latest_version_flag, loader):
    project = requests.get(f'https://api.modrinth.com/v2/project/{project_id}').text
    project_json = json.loads(project)
    project_versions = project_json['versions']
    project_versions_codes = []
    project_versions_numbers = []
    if len(project_versions) == 0:
        print(f'Versions not found.')
        exit(1)
    if latest_version_flag:
        desired_project_version = 0
    else:
        for project_version_code in project_versions:
                version = requests.get(f'https://api.modrinth.com/v2/project/{project_id}/version/{project_version_code}').text
                version_json = json.loads(version)
                if game_version in version_json['game_versions']:
                    project_versions_codes.append(project_version_code)
                    project_version = version_json['version_number']
                    project_versions_numbers.append(project_version)
        project_versions = dict(zip(project_versions_numbers, project_versions_codes))
        print(*(list(project_versions.keys())))
        desired_project_version = input('Enter the desired version from list above: ')
    version = requests.get(
        f'https://api.modrinth.com/v2/project/{project_id}/version/{project_versions[desired_project_version]}').text
    version_json = json.loads(version)
    project_dependencies = version_json['dependencies']
    project_file_link = version_json['files'][0]['url']
    project_file_name = version_json['files'][0]['filename']
    project_file = requests.get(project_file_link).content
    if project_json['project_type'] == 'mod' and (loader == 'bukkit' or loader == 'spigot' or loader == 'paper'):
        project_type = 'plugin'
    else:
        project_type = project_json['project_type']
    download_project_files(project_file, project_file_name, project_type)
    if len(project_dependencies) > 0:
        download_dependencies(project_dependencies, download_optional_dependencies_flag, game_version, latest_version_flag, loader)


def download_project_files(project_file, project_file_name, project_type):
    check_directory(project_type)
    with open(f'{project_file_name}', 'wb') as file:
        file.write(project_file)
    print(f'Downloading and installing {project_file_name}')


def download_dependencies(project_dependencies, download_optional_dependencies_flag, game_version, latest_version_flag, loader):
    for dependency in project_dependencies:
        match dependency['dependency_type']:
            case 'required':
                get_project_files(dependency['project_id'], download_optional_dependencies_flag, game_version, latest_version_flag, loader)
            case 'optional':
                if download_optional_dependencies_flag:
                    get_project_files(dependency['project_id'], download_optional_dependencies_flag, game_version, latest_version_flag, loader)
                else:
                    print(f'Skipped installing {dependency['project_id']}')


def search_project(project_name, loader, game_version, download_optional_dependencies_flag, latest_version_flag):
    project_id = ''
    search = requests.get('https://api.modrinth.com/v2/search', params={'query': project_name,
                                                                        'categories': loader,
                                                                        'versions': game_version}).text
    search_json = json.loads(search)['hits']
    for search_result in range(len(search_json)):
        if search_json[search_result]['title'] == project_name:
            project_id = search_json[search_result]['project_id']
            break


    if project_id == '':
        print(f'Project {project_name} not found.')
        exit(1)

    get_project_files(project_id, download_optional_dependencies_flag, game_version, latest_version_flag, loader)


def start_content_downloader():
    project_name = input('Enter the project name: ')
    game_version = input('Enter the game version: ')
    loader = input('Enter the loader (Forge, Fabric, NeoForge, Spigot, Paper, Bukkit, OptiFine, Iris, Minecraft(for resourcepacks), etc): ').lower()
    if input('Would you like to download optional dependencies? (y/n): ').lower() == 'y':
        download_optional_dependencies_flag = True
    else:
        download_optional_dependencies_flag = False

    if input('Would you like to download latest version? (y/n): ').lower() == 'y':
        latest_version_flag = True
    else:
        latest_version_flag = False

    search_project(project_name, loader, game_version, download_optional_dependencies_flag, latest_version_flag)

start_content_downloader()
