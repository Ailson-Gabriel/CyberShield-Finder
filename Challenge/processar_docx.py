import os
from docx import Document
from criptografar_arquivo import criptografar_arquivo_caminho
from varredura import varredura
import tkinter as tk
from print_textbox import print_to_textbox

def processar(arquivo, textbox):
    """
    Processa um arquivo .docx, procurando por nomes e CPFs.

    Argumento:
        arquivo (str): O caminho para o arquivo .docx a ser processado.
    """
    
    print_to_textbox(textbox, f"Processando DOCX: {os.path.basename(arquivo)}",)    
    
    texto_docx = extrair_texto(arquivo)

    dados_sensiveis_encontrados = varredura(textbox, texto_docx) # Verifica se há dados sensíveis no texto extraído do arquivo Excel
    if dados_sensiveis_encontrados:
        criptografar_arquivo_caminho(arquivo)
        print_to_textbox(textbox, f"\nArquivo {os.path.basename(arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(arquivo+'.criptografado')}")
    else:
        print_to_textbox(textbox, f"Não encontrado dados sensíveis que possam ser associados a algum individuo no arquivo {os.path.basename(arquivo)}")
        
def extrair_texto(arquivo):
    """
    Extrai texto de um arquivo DOCX.

    Argumento:
        arquivo (str): O caminho para o arquivo DOCX a ser processado.

    Retorna:
        str: O texto extraído do arquivo DOCX.
    """
    document = Document(arquivo) # Abre o arquivo .docx e extrai o texto
    texto = ""
    for paragraph in document.paragraphs: # Repete sobre os parágrafos do documento e concatena seus textos
        texto += paragraph.text + "\n"
    return texto