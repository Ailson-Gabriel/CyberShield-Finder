import os # Módulo que fornece funções para interagir com o sistema operacional
from processar_imagem import processar as processar_imagem # Função que processa uma imagem
from processar_texto import processar as processar_texto # Função que processa um arquivo de texto
from processar_docx import processar as processar_docx # Função que processa um arquivo docx
from processar_pdf import processar as processar_pdf # Função que processa um arquivo pdf
from processar_excel import processar as processar_excel # Função que processa um arquivo excel
from processar_pst import processar as processar_pst # Função que processa um arquivo pst
from print_textbox import print_to_textbox # Função que imprime mensagens em um Textbox
from grava_resultados import grava_dados, grava_dicionario, grava_tabela_de_arquivos # Função que grava os resultados em um arquivo

def varrer_diretorio(diretorio, textbox):
    """
    Varre um diretório em busca de arquivos e processa cada arquivo encontrado.
    Argumentos:
        diretorio (str): O caminho para o diretório a ser varrido.
        textbox (Tkinter.Text): O objeto Textbox onde as mensagens devem ser exibidas.
    """
    print_to_textbox(textbox, f"Varrendo o diretório: {os.path.basename(diretorio)}")
    # Lista para armazenar os arquivos varridos
    arquivos_varridos = []
    qntd_txt = 0
    qntd_docx = 0
    qntd_jpg = 0
    qntd_jpeg = 0
    qntd_png = 0
    qntd_pdf = 0
    qntd_xls = 0
    qntd_xlsx = 0
    qntd_pst = 0

    for arquivo in os.listdir(diretorio): # Repete para os arquivos no diretório
        if os.path.isdir(os.path.join(diretorio, arquivo)):  # Se for um diretório
            print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
            print_to_textbox(textbox, f"Acessando o subdiretório: {arquivo}")
            varrer_diretorio(os.path.join(diretorio, arquivo), textbox)
        else:
            # Adiciona o arquivo à lista de arquivos varridos
            arquivos_varridos.append(arquivo)

            if arquivo.endswith(('.jpg', '.jpeg', '.png')): # Verifica se o arquivo é uma imagem
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_imagem(os.path.join(diretorio, arquivo), textbox)
                if arquivo.endswith('.jpg'): # Verifica se o arquivo é um arquivo .jpg
                    qntd_jpg += 1  # Incrementa a contagem de arquivos .jpg
                elif arquivo.endswith('.jpeg'): # Verifica se o arquivo é um arquivo .jpeg
                    qntd_jpeg += 1 # Incrementa a contagem de arquivos .jpeg
                elif arquivo.endswith('.png'): # Verifica se o arquivo é um arquivo .png
                    qntd_png += 1 # Incrementa a contagem de arquivos .png

            elif arquivo.endswith('.txt'): # Verifica se o arquivo é um arquivo de texto
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_texto(os.path.join(diretorio, arquivo), textbox)
                qntd_txt += 1 # Incrementa a contagem de arquivos .txt
                
            elif arquivo.endswith('.docx'): # Verifica se o arquivo é um arquivo docx
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_docx(os.path.join(diretorio, arquivo), textbox)
                qntd_docx += 1 # Incrementa a contagem de arquivos .docx

            elif arquivo.endswith('.pdf'): # Verifica se o arquivo é um arquivo pdf
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_pdf(os.path.join(diretorio, arquivo), textbox)
                qntd_pdf += 1 # Incrementa a contagem de arquivos .pdf

            elif arquivo.endswith(('.xls', '.xlsx')): # Verifica se o arquivo é um arquivo excel
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_excel(os.path.join(diretorio, arquivo), textbox)
                if arquivo.endswith('.xls'): # Verifica se o arquivo é um arquivo excel .xls
                    qntd_xls += 1 # Incrementa a contagem de arquivos .xls
                elif arquivo.endswith('.xlsx'): # Verifica se o arquivo é um arquivo excel .xlsx
                    qntd_xlsx += 1 # Incrementa a contagem de arquivos .xlsx
            
            elif arquivo.endswith('.pst'): # Verifica se o arquivo é um arquivo pst
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_pst(os.path.join(diretorio, arquivo), textbox)
                qntd_pst += 1 # Incrementa a contagem de arquivos .pst

    # Se nenhum arquivo foi processado, imprima uma mensagem
    if not arquivos_varridos:
        print_to_textbox(textbox, f"Nenhum arquivo encontrado para varrer em {os.path.basename(diretorio)}")
    
    # Dicionário para armazenar a quantidade de cada tipo de arquivo
    contagem = {
    ".txt": qntd_txt,
    ".docx": qntd_docx,
    ".jpeg": qntd_jpeg,
    ".jpg": qntd_jpg,
    ".png": qntd_png,
    ".pdf": qntd_pdf,
    ".xls": qntd_xls,
    ".xlsx": qntd_xlsx,
    ".pst": qntd_pst
    }

    grava_dados("qntd_total" ,f"{os.path.basename(diretorio)}", f"{len(arquivos_varridos)}") # Grava a quantidade total de arquivos
    grava_dicionario("quantidade_de_arquivos", contagem) # Grava a quantidade de cada tipo de arquivo
    grava_tabela_de_arquivos() # Grava a tabela de arquivos
