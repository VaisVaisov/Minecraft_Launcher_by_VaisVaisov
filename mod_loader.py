import requests
from bs4 import BeautifulSoup

mod = 'TerraFirmaCraft'
minecraft_version = '1.12.2'

modrinth = requests.get(f'https://modrinth.com/mod/{mod.lower()}/versions?g={minecraft_version}')

modrinth_soup = BeautifulSoup(modrinth.text, 'html.parser')

mod_div = modrinth_soup.find('div', class_='version-button button-transparent')
mod_div_text = mod_div.get_text()

mod_version = modrinth_soup.find('div', class_='version__metadata')
mod_version_text = mod_version.get_text().replace(' Release', '')

mod_link = f'https://modrinth.com/mod/{mod.lower()}/version/{mod_version_text}'

mod_page = requests.get(mod_link)
print(mod_page.status_code)

mod_page_soup = BeautifulSoup(mod_page.text, 'html.parser')

mod_page_div = mod_page_soup.find('div',
                                  class_='version-page__title universal-card').find('div', class_='input-group')

mod_download_link = mod_page_div.find('a')['href']

mod_requirements = mod_page_soup.find('div', class_='version-page__dependencies universal-card')

mod_requirement = mod_requirements.find('div', class_='button-transparent dependency')

print(mod_requirements)