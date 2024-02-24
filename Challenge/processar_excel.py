import os
import xlrd
import openpyxl
from buscar import encontrar_nomes, encontrar_cpf

def processar(arquivo):
    """
    Processa um arquivo .xls ou .xlsx, procurando por nomes e CPFs.

    Argumento:
        arquivo (str): O caminho para o arquivo .xls ou .xlsx a ser processado.
    """

    print("Processando Excel:", os.path.basename(arquivo))
    
    # Extrai texto das colunas 'nome', 'cpf' e o texto completo do arquivo Excel
    texto_nomes, texto_cpf, texto_completo = extrair_texto(arquivo)
    
    # Chama as funções 'encontrar_nomes' e 'encontrar_cpf' com os textos extraídos
    encontrados_nomes = encontrar_nomes(texto_nomes) if texto_nomes else encontrar_nomes(texto_completo)
    encontrados_cpf = encontrar_cpf(texto_cpf) if texto_cpf else encontrar_cpf(texto_completo)
    
    # -------------------------------------- Imprime os resultados -------------------------------------- #
    if encontrados_nomes:
        print(f"Nomes encontrados no arquivo {os.path.basename(arquivo)}\n")
        print(encontrados_nomes,"\n")
    else:
        print(f"Não foram encontrados nomes no arquivo {os.path.basename(arquivo)}\n")

    if encontrados_cpf:
        print(f"CPF encontrado no arquivo {os.path.basename(arquivo)}\n")
    else:
        print(f"Não encontrado CPFs no arquivo {os.path.basename(arquivo)}\n")
    # -------------------------------------- Imprime os resultados -------------------------------------- #

def extrair_texto(arquivo):
    """
    Extrai texto de um arquivo Excel (.xls ou .xlsx).

    Argumento:
        arquivo (str): O caminho para o arquivo Excel a ser processado.

    Retorna:
        str: O texto extraído da coluna 'nome', se encontrada.
        str: O texto extraído da coluna 'cpf', se encontrada.
        str: O texto extraído do arquivo Excel completo, se nenhuma das colunas for encontrada.
    """
    texto_nomes = ""  # Inicializa a variável para armazenar o texto da coluna 'nome'
    texto_cpf = ""    # Inicializa a variável para armazenar o texto da coluna 'cpf'
    texto_completo = ""  # Inicializa a variável para armazenar o texto completo do arquivo

    if arquivo.endswith('.xls'):  # Para arquivos .xls
        workbook = xlrd.open_workbook(arquivo)  # Abre o arquivo Excel usando a biblioteca xlrd
        for sheet in workbook.sheets():  # Repete para as planilhas no arquivo Excel
            for col_idx in range(sheet.ncols):  # Repete para as colunas na planilha
                col_name = str(sheet.cell_value(0, col_idx)).lower()  # Obtém o nome da coluna e converte para minúsculas
                if 'nome' in col_name:  # Verifica se a coluna 'nome' está presente no nome da coluna
                    for row_idx in range(1, sheet.nrows):  # Repete para as linhas na coluna
                        texto_nomes += str(sheet.cell_value(row_idx, col_idx)) + "\n"  # Adiciona o texto à variável
                elif 'cpf' in col_name:  # Verifica se a coluna 'cpf' está presente no nome da coluna
                    for row_idx in range(1, sheet.nrows):  # Repete para as linhas na coluna
                        texto_cpf += str(sheet.cell_value(row_idx, col_idx)) + "\n"  # Adiciona o texto à variável
                else:  # Se nenhuma das colunas for encontrada, extrai todo o texto do arquivo Excel
                    for row_idx in range(sheet.nrows):
                        for col in range(sheet.ncols):
                            texto_completo += str(sheet.cell_value(row_idx, col)) + " "
                        texto_completo += "\n"
        return texto_nomes, texto_cpf, texto_completo

    elif arquivo.endswith('.xlsx'):  # Para arquivos .xlsx
        workbook = openpyxl.load_workbook(arquivo)  # Abre o arquivo Excel usando a biblioteca openpyxl
        for sheet_name in workbook.sheetnames:  # Repete para os nomes das planilhas no arquivo Excel
            worksheet = workbook[sheet_name]  # Obtém a planilha atual
            for col in worksheet.iter_cols(max_row=1, values_only=True):  # Repete para as colunas na primeira linha
                for cell in col:  # Repete para as células na coluna
                    col_name = str(cell).lower()  # Obtém o nome da coluna e converte para minúsculas
                    if 'nome' in col_name:  # Verifica se a coluna 'nome' está presente no nome da coluna
                        for row_idx, row in enumerate(worksheet.iter_rows(min_row=2, min_col=cell.column, max_col=cell.column, values_only=True), start=2):
                            texto_nomes += str(row[0]) + "\n"  # Adiciona o texto à variável
                    elif 'cpf' in col_name:  # Verifica se a coluna 'cpf' está presente no nome da coluna
                        for row_idx, row in enumerate(worksheet.iter_rows(min_row=2, min_col=cell.column, max_col=cell.column, values_only=True), start=2):
                            texto_cpf += str(row[0]) + "\n"  # Adiciona o texto à variável
                    else:  # Se nenhuma das colunas for encontrada, extrai todo o texto do arquivo Excel
                        for row in worksheet.iter_rows(values_only=True):
                            texto_completo += ' '.join(str(cell) for cell in row) + '\n'
        return texto_nomes, texto_cpf, texto_completo
