from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Defina o caminho para o ChromeDriver
chrome_driver_path = 'D:\Estudo\Outros\Python\Random\automacao\chromedriverWin64\chromedriver.exe'

# Configurações para o Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Inicia o Chrome maximizado
chrome_service = Service(chrome_driver_path)

# Inicializa o navegador
driver = webdriver.Chrome()

# Navega até o site do Google
driver.get("https://registro.br/")
time.sleep(3)

# Localiza a barra de pesquisa
search_box = driver.find_element(By.NAME, "is-avail")

# Digita a consulta de pesquisa
query = "g1"
search_box.send_keys(query)

# Pressiona Enter para realizar a pesquisa
search_box.send_keys(Keys.RETURN)

# Aguarda alguns segundos para carregar os resultados
time.sleep(3)

# Extrai os títulos dos resultados da pesquisa
results = driver.find_elements(By.XPATH, '//h3')
for result in results:
    print(result.text)

time.sleep(3)

contador = 0
try:
    # Encontra todos os elementos com a tag <strong>
    strong_elements = driver.find_elements(By.TAG_NAME, 'strong')

    # Itera pelos elementos encontrados e imprime o texto de cada um
    for element in strong_elements:
        
        if contador == 2:
            print(element.text)
        contador +=1
finally:
    # Fecha o navegador
# Fecha o navegador
    driver.quit()