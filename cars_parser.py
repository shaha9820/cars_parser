import requests
from bs4 import BeautifulSoup as bs
import lxml
import json
import os
from pathlib import Path 

url = 'https://turbo.kg/'
html = requests.get(url).content
soup = bs(html,'lxml')
cars = soup.find_all('div', class_='car col-12 col-sm-6 col-lg-4 col-xl-3 mb-4')
list_ = []
for car in cars:
    title = car.find('h3', class_ = 'text-truncate h6 mb-1').text
    price_text = car.find('b', class_ = 'float-right').text
    price = price_text if 'сом' in price_text else int(price_text.replace('$', '')) * 87.5
    img = car.find('img').get('src')
    year = car.find('p', class_ = 'mb-1').find('b').text
    list_.append({"title":title,
                 "price": price,
                 "img":img,
                 "yesr":year})
with open('db.json','w', encoding= 'utf-8') as f:
    json.dump(list_, f, ensure_ascii= False, indent= 4)