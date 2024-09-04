import pandas as pd
from tabula import read_pdf

# Caminho para o arquivo PDF
pdf_path = "D:/Programacao/Python/Automacoes_Python/Produto.pdf"

# Ler as tabelas do PDF (retorna uma lista de DataFrames)
tabelas = read_pdf(pdf_path, pages='all', multiple_tables=True)

# Verificar se encontrou tabelas
if tabelas:
    # Caminho para salvar o arquivo Excel
    xlsx_path = "D:/Programacao/Python/Automacoes_Python/arquivo.xlsx"
    
    # Criar um objeto ExcelWriter
    with pd.ExcelWriter(xlsx_path, engine='openpyxl') as writer:
        for i, tabela in enumerate(tabelas):
            # Escrever cada tabela em uma aba diferente
            tabela.to_excel(writer, sheet_name=f'Tabela_{i+1}', index=False)
    print(f"Tabelas convertidas e salvas em {xlsx_path}")
else:
    print("Nenhuma tabela encontrada no PDF.")
