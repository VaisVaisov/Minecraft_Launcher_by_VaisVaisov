# import curseforge
#
# client = curseforge.CurseClient()
#
# minecraft = client.game(432)
# для curseforge

import requests
from bs4 import BeautifulSoup

mod = 'TerraFirmaCraft'
version = '1.20.1'

modrinth_mod = requests.get(f'https://modrinth.com/mod/{mod.lower()}/versions')
print(modrinth_mod.status_code)

modrinth_mod_soup = BeautifulSoup(modrinth_mod.text, 'html.parser')

print(*modrinth_mod_soup.find('div', class_='version__supports').find('span'))
#посмотреть, как забрать версию из тега span