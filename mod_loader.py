import modrinth
import requests
import os

mod_name = 'NEI'
mod = modrinth.Projects.ModrinthProject(mod_name)
mod_name = mod.name
mod_id = mod.id
mod_version = mod.getVersion(mod.versions[-1])
mod_link = mod_version.getDownload(mod_version.getFiles()[0])

mod_file = requests.get(mod_link)
mod_file_name = mod_version.name + '.jar'
with open(f'{mod_file_name}', 'wb') as file:
    file.write(mod_file.content)