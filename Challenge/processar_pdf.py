import os
from PyPDF2 import PdfReader
from varredura import varredura
from criptografar_arquivo import criptografar_arquivo_caminho
import tkinter as tk
from print_textbox import print_to_textbox

def processar(arquivo, textbox):
    """
    Processa um arquivo PDF, procurando por nomes e CPFs.

    Argumentos:
        arquivo (str): O caminho para o arquivo PDF a ser processado.
        nomes (list): Lista de nomes para procurar no PDF.
    """

    print_to_textbox(textbox, f"Processando PDF: {os.path.basename(arquivo)}",)
    texto_pdf = extrair_texto(arquivo) 
    
    dados_sensiveis_encontrados = varredura(textbox, texto_pdf) # Verifica se há dados sensíveis no texto extraído do arquivo Excel
    if dados_sensiveis_encontrados:
        criptografar_arquivo_caminho(arquivo)
        print_to_textbox(textbox, f"\nArquivo {os.path.basename(arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(arquivo+'.criptografado')}")
    else:
        print_to_textbox(textbox, f"Não encontrado dados sensíveis que possam ser associados a algum individuo no arquivo {os.path.basename(arquivo)}")

def extrair_texto(arquivo):
    """
    Extrai texto de um arquivo PDF.

    Argumento:
        arquivo (str): O caminho para o arquivo PDF a ser processado.

    Retorna:
        str: O texto extraído do arquivo PDF.
    """
    texto = ""
    with open(arquivo, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            texto += page.extract_text()
    return texto