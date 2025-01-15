import requests
import json
import os

os.chdir('.launcher')

def check_directory():
    if not os.path.isdir('mods'):
        os.mkdir('mods')
        os.chdir('mods')
    else:
        os.chdir('mods') 


def get_project_files(project_name, project_id, download_optional_dependencies_flag, game_version):
    project = requests.get(f'https://api.modrinth.com/v2/project/{project_id}').text
    project_json = json.loads(project)
    project_versions = project_json['versions']
    project_versions_codes = []
    project_versions_numbers = []
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
    download_project_files(project_file, project_file_name)
    if len(project_dependencies) > 0:
        download_dependencies(project_dependencies, download_optional_dependencies_flag, game_version)


def download_project_files(project_file, project_file_name):
    with open(f'{project_file_name}', 'wb') as file:
        file.write(project_file)
    print(f'Downloading and installing {project_file_name}')
    exit(0)


def download_dependencies(project_dependencies, download_optional_dependencies_flag, game_version):
    for dependency in project_dependencies:
        match dependency['dependency_type']:
            case 'required':
                get_project_files(dependency['project_id'], download_optional_dependencies_flag, game_version)
            case 'optional':
                if download_optional_dependencies_flag:
                    get_project_files(dependency['project_id'], download_optional_dependencies_flag, game_version)
                else:
                    print(f'Skipped installing {dependency['project_id']}')


def search_project(project_name, loader, game_version, download_optional_dependencies_flag):
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

    get_project_files(project_name, project_id, download_optional_dependencies_flag, game_version)


def main():
    check_directory()
    project_name = input('Enter the project name: ')
    game_version = input('Enter the game version: ')
    download_optional_dependencies_flag = True if input('Do you want to download optional dependencies? (y/n): ') else download_optional_dependencies_flag = False
    loader = input('Enter the loader (Forge, Fabric, etc): ').lower()
    search_project(project_name, loader, game_version, download_optional_dependencies_flag)


if __name__ == '__main__':
    main()
