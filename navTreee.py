from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# Descendentes - Nível mais baixos
print('---- Descendentes ----')
for child in bs.find('table', {'id':'giftList'}).descendants:
  print(child) 



# Filhos - Nível mais superiores 
print('---- Filhos ----')
for child in bs.find('table', {'id':'giftList'}).children:
  print(child)

# Todo Filho de uma tag é descendente mas nem todo descendente é filho

# Irmãos
print('---- Irmãos ----')
for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
  print(sibling)

# next_siblings - próximos irmãos
# previous_siblings - último irmão

# Pais
print('---- Pais ----')
print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())


# Expressões Regulares
print('---- Expressoes Regulares ----')
Telefones = bs.find_all('', text= re.compile('[0-9]{4}'))

print(Telefones)

# Acessando Atributo
print('\n---- Acessando Atributo ----')

Atr = bs.img.attrs['src']
print(Atr)


# Expressões Lambda
print('\n---- Expressões Lambda ----')

lenTag = bs.find_all(lambda tag: len(tag.attrs) == 2)

for tg in lenTag:
  print(tg)