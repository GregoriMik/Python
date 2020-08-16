import requests
from bs4 import BeautifulSoup
url = 'https://www.pracuj.pl/praca/python;kw?rd=0'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title)
# <span class="results-header__offer-count-text-number">256</span>
element = soup.find('span', class_="results-header__offer-count-text-number")
print('Pokaż kochany pythonie ile mamy obecnie pracy?\nWąż: Mój drogi, obecnie mamy w Pythonie',
      element.text, 'aktualnych ofert')
