from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search_google(query, num_pages):
    # Inicializa o navegador
    
    
    driver = webdriver.Chrome()  # ou webdriver.Firefox() para o Firefox
    driver.get("https://www.google.com")

    # Localiza a barra de pesquisa e digita a query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    results = []

    for page in range(num_pages):
        # Espera os resultados carregarem
        time.sleep(2)

        # Coleta os resultados da página
        titles = driver.find_elements(By.XPATH, "//h3")
        links = driver.find_elements(By.XPATH, "//h3/ancestor::a")

        for title, link in zip(titles, links):
            result = (title.text, link.get_attribute('href'))
            results.append(result)

        try:
            # Navega para a próxima página de resultados
            next_button = driver.find_element(By.ID, "pnnext")
            next_button.click()
        except Exception as e:
            print("Não há mais páginas disponíveis ou houve um erro:", e)
            break

    # Fecha o navegador
    driver.quit()

    return results

def save_to_file(results, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for title, link in results:
            file.write(f"{title}\n{link}\n\n")

if __name__ == "__main__":
    query = input("Digite a informação que deseja pesquisar no Google: ")
    num_pages = int(input("Digite o número de páginas que deseja extrair os dados: "))

    results = search_google(query, num_pages)
    save_to_file(results, 'resultados_google.txt')

    print(f"Dados salvos em 'resultados_google.txt' com sucesso!")
