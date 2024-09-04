import PyPDF2
from openpyxl import workbook


print('iniciando o nosso robô...')
pdf_file = open("Produto","rb")

read_pdf = PyPDF2.PdfFileReader(pdf_file)

number_of_pages = read_pdf.getNumPages()

page = read_pdf.get_object(0)

print('Lendo dados do arquivo PDF...')


page_content = page.extractText()

parsed = page_content.splitlines()

while ' ' in parsed:
    parsed.remove(' ')

lista_dados = []
for i in range(0,len(parsed)-3,3):
    lista_dados.append(parsed[i],parsed[i+1],parsed[i+2])

wb = workbook()
ws = wb.active

for row in lista_dados:
     ws.append(row)
     
wb.save(filename = 'lista_de_produtos.xlsx') 
