from openpyxl import load_workbook

#Escolhendo o arquivo
dest_filename = 'bookao.xlsx'
wb = load_workbook(filename=dest_filename)
ws = wb['Data']

#Move a linha  2 (DE a até z) uma para cima

ws.move_range("A2:Z2",rows=-1)

#Move f8 duas colunas para a direita
ws.move_range('F8:F8',cols=2)

#move f10 duas colunas para a esquerda
ws.move_range('F10:F10',cols=-2)

ws.move_range('C13:E15',cols=-2,rows=-1)

wb.save(filename=dest_filename)