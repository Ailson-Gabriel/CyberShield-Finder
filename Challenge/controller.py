import os
from processar_imagem import processar as processar_imagem
from processar_texto import processar as processar_texto
from processar_docx import processar as processar_docx
from processar_pdf import processar as processar_pdf
from processar_excel import processar as processar_excel
from processar_pst import processar as processar_pst
from print_textbox import print_to_textbox
from grava_resultados import grava_dados, grava_dicionario, grava_tabela_de_arquivos

def varrer_diretorio(diretorio, textbox):
    print_to_textbox(textbox, f"Varrendo o diretório: {os.path.basename(diretorio)}")

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

    for arquivo in os.listdir(diretorio):
        if os.path.isdir(os.path.join(diretorio, arquivo)):  # Se for um diretório
            print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
            print_to_textbox(textbox, f"Acessando o subdiretório: {arquivo}")
            varrer_diretorio(os.path.join(diretorio, arquivo), textbox)
        else:
            # Adiciona o arquivo à lista de arquivos varridos
            arquivos_varridos.append(arquivo)

            if arquivo.endswith(('.jpg', '.jpeg', '.png')):
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_imagem(os.path.join(diretorio, arquivo), textbox)
                if arquivo.endswith('.jpg'):
                    qntd_jpg += 1
                elif arquivo.endswith('.jpeg'):
                    qntd_jpeg += 1
                elif arquivo.endswith('.png'):
                    qntd_png += 1

            elif arquivo.endswith('.txt'):
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_texto(os.path.join(diretorio, arquivo), textbox)
                qntd_txt += 1
                
            elif arquivo.endswith('.docx'):
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_docx(os.path.join(diretorio, arquivo), textbox)
                qntd_docx += 1

            elif arquivo.endswith('.pdf'):
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_pdf(os.path.join(diretorio, arquivo), textbox)
                qntd_pdf += 1

            elif arquivo.endswith(('.xls', '.xlsx')):
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_excel(os.path.join(diretorio, arquivo), textbox)
                if arquivo.endswith('.xls'):
                    qntd_xls += 1
                elif arquivo.endswith('.xlsx'):
                    qntd_xlsx += 1
            
            elif arquivo.endswith('.pst'):
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_pst(os.path.join(diretorio, arquivo), textbox)
                qntd_pst += 1

    # Se nenhum arquivo foi processado, imprima uma mensagem
    if not arquivos_varridos:
        print_to_textbox(textbox, f"Nenhum arquivo encontrado para varrer em {os.path.basename(diretorio)}")
    
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

    grava_dados("qntd_total" ,f"{os.path.basename(diretorio)}", f"{len(arquivos_varridos)}")
    grava_dicionario("quantidade_de_arquivos", contagem)
    grava_tabela_de_arquivos()
