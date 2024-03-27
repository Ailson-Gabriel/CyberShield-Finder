from curses.textpad import Textbox
import os
from processar_imagem import processar as processar_imagem
from processar_texto import processar as processar_texto
from processar_docx import processar as processar_docx
from processar_pdf import processar as processar_pdf
from processar_excel import processar as processar_excel
import tkinter as tk
from tkinter import filedialog
import customtkinter
from print_textbox import print_to_textbox

def varrer_diretorio(diretorio, textbox):
    print_to_textbox(textbox, f"Varrendo o diretório: {os.path.basename(diretorio)}")
    
    # Variável de controle para verificar se algum arquivo foi processado
    arquivo_processado = False

    for arquivo in os.listdir(diretorio):
        if os.path.isdir(os.path.join(diretorio, arquivo)):  # Se for um diretório
            print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
            print_to_textbox(textbox, f"Acessando o subdiretório: {arquivo}")
            varrer_diretorio(os.path.join(diretorio, arquivo), textbox)
        else:
            if arquivo.endswith('.jpg') or arquivo.endswith('.jpeg') or arquivo.endswith('.png'):
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_imagem(os.path.join(diretorio, arquivo), textbox)
                arquivo_processado = True

            elif arquivo.endswith('.txt'):
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_texto(os.path.join(diretorio, arquivo), textbox)
                arquivo_processado = True

            elif arquivo.endswith('.docx'):
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_docx(os.path.join(diretorio, arquivo), textbox)
                arquivo_processado = True

            elif arquivo.endswith('.pdf'):
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_pdf(os.path.join(diretorio, arquivo), textbox)
                arquivo_processado = True

            elif arquivo.endswith('.xls') or arquivo.endswith('.xlsx'):
                print_to_textbox(textbox, "-----------------------------------------------------------------------------------------------------------------")
                processar_excel(os.path.join(diretorio, arquivo), textbox)
                arquivo_processado = True

    # Se nenhum arquivo foi processado, imprima uma mensagem
    if not arquivo_processado:
        print_to_textbox(textbox, f"Nenhum arquivo encontrado para varrer em {os.path.basename(diretorio)}")