import pandas as pd
import PyPDF2

# Função para extrair o texto da tabela do PDF
def extrair_tabela_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        page = reader.pages[0]
        texto = page.extract_text()

    # Separando linhas e colunas da tabela
    linhas = texto.strip().split('\n')
    dados = [linha.split() for linha in linhas]

    return dados

# Caminho para o arquivo PDF
pdf_path = "D:/Programacao/Python/Automacoes_Python/Produto.pdf"

# Extrair dados da tabela
dados_tabela = extrair_tabela_pdf(pdf_path)

# Criar um DataFrame com os dados extraídos
colunas = dados_tabela[0]  # Primeira linha como cabeçalho
tabela_df = pd.DataFrame(dados_tabela[1:], columns=colunas)

# Caminho para salvar o arquivo Excel
xlsx_path = "D:/Programacao/Python/Automacoes_Python/arquivo.xlsx"

# Salvar os dados em um arquivo Excel
tabela_df.to_excel(xlsx_path, index=False)

print(f"Os dados foram convertidos e salvos em {xlsx_path}")
