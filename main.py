from uu import encode
import requests
from bs4 import BeautifulSoup
import csv

header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Mobile Safari/537.36 '
}

url = 'https://store.steampowered.com/explore/new/'

r = requests.get(url, header)

soup = BeautifulSoup(r.text, "html.parser")
popular = soup.findAll('a', attrs={'class': 'tab_item'})
file = open('steam.csv', 'w', newline='')
writer =csv.writer(file)
writer.writerow(['title','priece','tag'])
for pop in popular:
    if(pop.find('div',{'class':'tab_item_name'})!=None):
        title = pop.find('div',{'class':'tab_item_name'}).text
    else:
        title =''

    if (pop.find('div', {'class': 'discount_original_price'}) != None):
        priece = pop.find('div', {'class': 'discount_original_price'}).text
    else:
        priece = ''

    if (pop.find('div', {'class': 'tab_item_top_tags'}) != None):
        tag = pop.find('div', {'class': 'tab_item_top_tags'}).text
    else:
        title = ''

    file = open('steam.csv','a',newline='',encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([title, priece, tag])
    file.close()