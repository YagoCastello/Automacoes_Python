import PyPDF2
from openpyxl import Workbook

print('Iniciando o nosso robô...')

# Abrindo o arquivo PDF
with open("Produto.pdf", "rb") as pdf_file:
    # Criando um leitor de PDF
    read_pdf = PyPDF2.PdfReader(pdf_file)
    
    # Obtendo o número de páginas
    number_of_pages = len(read_pdf.pages)
    
    # Lendo a primeira página do PDF
    page = read_pdf.pages[0]
    
    print('Lendo dados do arquivo PDF...')
    
    # Extraindo o texto da página
    page_content = page.extract_text()
    print(page_content)
    # Dividindo o conteúdo do texto em linhas
    parsed = page_content.splitlines()
    print(parsed)
# Removendo linhas vazias ou espaços em branco
parsed = [line for line in parsed if line.strip()]
print(parsed)
# Criando a lista de dados
lista_dados = []
for i in range(0, len(parsed) - 2, 3):
    lista_dados.append([parsed[i], parsed[i+1], parsed[i+2]])

# Criando uma nova planilha Excel
wb = Workbook()
ws = wb.active

# Adicionando os dados à planilha
for row in lista_dados:
    ws.append(row)

# Salvando a planilha em um arquivo Excel
wb.save(filename='lista_de_produtos.xlsx')

print('Processo concluído, a planilha foi salva como lista_de_produtos.xlsx')
