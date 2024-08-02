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
driver.get("https://www.youtube.com/")
time.sleep(3)

# Localiza a barra de pesquisa
search_box = driver.find_element(By.NAME, "search_query")

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

# Fecha o navegador
driver.quit()
