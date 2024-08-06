from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

print("Iniciando nosso robô...\n")
try:
    with open("resultado.txt", "w") as arq:
        dominios = []
        
        # Lendo do Excel usando pandas
        df = pd.read_excel('Sites.xlsx', header=None)
        dominios = df[0].tolist()[:10]  # Lendo os primeiros 10 domínios

        # Caminho para o ChromeDriver manualmente baixado
        chrome_driver_path = "D:\Programacao\Python\Automacoes_Python\chromedriverWin64\chromedriver.exe"
        
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Inicia o Chrome maximizado
        chrome_service = Service(chrome_driver_path)
        # Inicializando o driver do Chrome
        driver = webdriver.Chrome()

        driver.get("https://registro.br/")
        time.sleep(3)

        for dominio in dominios:
            pesquisa = driver.find_element(By.ID, "is-avail-field")
            pesquisa.clear()  # Limpando a barra de pesquisa
            pesquisa.send_keys(dominio)
            pesquisa.send_keys(Keys.RETURN)
            time.sleep(2)
            resultados = driver.find_elements(By.TAG_NAME, "strong")
            
            if len(resultados) > 4:
                texto = "Domínio %s, situação atual: %s\n" % (dominio, resultados[2].text)
                arq.write(texto)
            else:
                arq.write(f"Domínio {dominio} não encontrou resultados suficientes.\n")

        driver.quit()
except Exception as e:
    print(f"Ocorreu um erro: {e}")
