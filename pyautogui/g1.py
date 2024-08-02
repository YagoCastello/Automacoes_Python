import requests
from bs4 import BeautifulSoup

page = requests.get("https://g1.globo.com/trabalho-e-carreira/noticia/2024/07/18/clt-premium-entenda-termo-usado-em-trend-que-ostenta-luxos-trabalhistas.ghtml")

if page.status_code == 200:
    soup = BeautifulSoup(page.text)

    for link in soup.find_all("a"):
        print(link.get("href", ""))
else:
    print("HTTP error ", page.status_code)


