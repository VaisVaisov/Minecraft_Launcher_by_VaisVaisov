# import curseforge
#
# client = curseforge.CurseClient()
#
# minecraft = client.game(432)
# для curseforge

import requests
from bs4 import BeautifulSoup

modrinth = requests.get('https://modrinth.com/mod/create')
print(modrinth.status_code)

modrinth_source = modrinth.text

modrinth_soup = BeautifulSoup(modrinth_source, 'html.parser')