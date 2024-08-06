from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

pesquisa = input("Digite a pesquisa: ")
n_paginas = int(input('Digite um número positivo maior que 1, que represente até qual página do google, você deseja extrair os dados: '))


# Caminho para o ChromeDriver manualmente baixado
chrome_driver_path = "D:\Estudo\Outros\Python\Random\automacao\chromedriverWin64\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Inicia o Chrome maximizado
chrome_service = Service(chrome_driver_path)
        # Inicializando o driver do Chrome
# Configuração do driver
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Encontrar o campo de pesquisa e realizar a pesquisa
campo = driver.find_element(By.NAME, "q")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)


# Espera para os resultados carregarem
time.sleep(2)

# Coletar os links das páginas de resultados
pagina_atual = 0
start = 0
lista_resultados = []

while pagina_atual < n_paginas:
    if pagina_atual > 0:
        url_pagina = f"https://www.google.com/search?q={pesquisa}&start={start}"
        driver.get(url_pagina)
        time.sleep(2)  # Espera para os resultados carregarem

    divs = driver.find_elements(By.XPATH, "//div[@class='g']")
    for div in divs:
        nomes = driver.find_elements(By.XPATH, "//h3")
        links = driver.find_elements(By.XPATH, "//h3/ancestor::a")
        for title, link in zip(nomes, links):
            if title.text !='':
                resultado = (title.text, link.get_attribute('href'))
                lista_resultados.append(resultado)
    
    pagina_atual += 1
    start += 10

# Salvar os resultados em um arquivo
with open("resultados.txt", "w") as arquivo:
    for resultado in lista_resultados:
        arquivo.write(f"{resultado}\n")

print(f"{len(lista_resultados)} resultados encontrados no Google e salvos no arquivo resultados.txt")

# Fechar o driver
driver.quit()