from openpyxl import workbook

print('Iniciando nosso robô...')
print('Lendo dados do arquivo de texto...')
file_txt = open('gastos.txt','r',encoding='utf-8')

#Ler do arquivo
arquivo = file_txt.read()

lista_dados = arquivo.splitlines()

for i in range(0,len(lista_dados)):
    lista_dados[i] = lista_dados[i].split(',')
    
#Criando arquivo excel

print('Criando arquivo excel...')
wb = workbook()
ws = wb.active

for row in lista_dados:
    ws.append(row)
    
wb.save('gastos.xlsx')
