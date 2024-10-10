
import requests 
from bs4 import BeautifulSoup

url = 'https:www.pichau.com.br/hardware/placa-de-video'

headers = {
        'Super-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)        
soup = BeautifulSoup(site.content, 'html.parser')
placas = soup.find_all('div', class)