import requests
import json
import os

project_name = input('Введи название проекта: ')
project_id = ''
game_version = input('Введи версию игры: ')
loader = input('Введи название загрузчика модов(Forge, Fabric, и т. д.): ').lower()
search = requests.get('https://api.modrinth.com/v2/search', params={'query': project_name,
                                                                        'categories': loader,
                                                                        'versions': game_version}).text
search_json = json.loads(search)['hits']
for i in range(len(search_json)):
    if search_json[i]['title'] == project_name:
        project_id = search_json[i]['project_id']
        break

if project_id == '':
    print(f'Project {project_name} not found.')
    exit(1)
project = requests.get(f'https://api.modrinth.com/v2/project/{project_id}').text
project_json = json.loads(project)
project_versions = project_json['versions']
mod_versions_codes = []
mod_versions_numbers = []
for i in project_versions:
    version = requests.get(f'https://api.modrinth.com/v2/project/{project_id}/version/{i}').text
    version_json = json.loads(version)
    if game_version in version_json['game_versions']:
        mod_versions_codes.append(i)
        mod_version = version_json['version_number']
        mod_versions_numbers.append(mod_version)
mod_versions = dict(zip(mod_versions_numbers, mod_versions_codes))
print(*(list(mod_versions.keys())))
requred_mod_version = input('Выбери(напиши в консоль) нужную тебе версию мода из списка выше: ')
version = requests.get(f'https://api.modrinth.com/v2/project/{project_id}/version/{mod_versions[requred_mod_version]}').text
version_json = json.loads(version)
mod_file_link = version_json['files'][0]['url']
mod_file_name = version_json['files'][0]['filename']
mod_file = requests.get(mod_file_link).content
if not os.path.isdir('mods'):
    os.makedirs('mods')
with open(f'{mod_file_name}', 'wb') as file:
    file.write(mod_file)
os.replace(f'{mod_file_name}', f'mods/{mod_file_name}')
