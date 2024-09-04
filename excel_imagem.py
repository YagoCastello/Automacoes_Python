from openpyxl import Workbook
from openpyxl.drawing.image import Image
from pathlib import Path

# Criação de uma nova pasta de trabalho e seleção da planilha ativa
wb = Workbook()
ws = wb.active

# Adicionando texto na célula A1
ws['A1'] = 'Você vai ver uma imagem abaixo'

# Carregando a imagem
img_path = Path('pc_imagem.jpg')
if img_path.is_file():
    img = Image(str(img_path))
    
    # Adicionando a imagem na célula A2
    ws.add_image(img, 'A2')
else:
    print(f"Imagem '{img_path}' não encontrada.")

# Salvando a pasta de trabalho em um arquivo Excel
wb.save(filename='logo.xlsx')