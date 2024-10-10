import requests
from bs4 import BeautifulSoup

# URL do site que você deseja fazer o scraping
url = 'https://www.infomoney.com.br/mercados/'

# Fazer a requisição HTTP
response = requests.get(url)

# Se o status da resposta for 200 (OK), continue
if response.status_code == 200:
    # Criar um objeto BeautifulSoup para analisar o conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Exemplo: Encontrar todos os títulos de artigos
    titulos = soup.find_all('h2', class_='titulo-artigo')
    
    # Exibir os títulos no terminal
    for idx, titulo in enumerate(titulos, 1):
        print(f"{idx}. {titulo.get_text(strip=True)}")
else:
    print(f"Erro ao acessar o site: {response.status_code}")
