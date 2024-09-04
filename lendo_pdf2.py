import PyPDF2
from openpyxl import Workbook

# Abrindo o arquivo PDF
with open("Produto.pdf", "rb") as pdf_file:
    # Criando um leitor de PDF
    read_pdf = PyPDF2.PdfReader(pdf_file)
    
    # Obtendo o número de páginas
    number_of_pages = len(read_pdf.pages)
    
    # Extraindo texto da primeira página
    page = read_pdf.pages[0]
    page_content = page.extract_text()
    
    # Exibindo o conteúdo da primeira página
    print(page_content)

# Exemplo de como você pode usar openpyxl para criar uma nova planilha (caso precise)
wb = Workbook()
ws = wb.active
ws.title = "Dados do PDF"
ws['A1'] = page_content

# Salvando a planilha em um arquivo Excel
wb.save("Dados_do_PDF.xlsx")
