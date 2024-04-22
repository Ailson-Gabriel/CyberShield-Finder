import os
import pytesseract # Módulo para usar a funcionalidade OCR (Optical Character Recognition) do Tesseract
from PIL import Image # Permite abrir, manipular e salvar imagens.
import cv2 # OpenCV - Biblioteca de visão computacional e processamento de imagens e vídeos.
from varredura import varredura
from criptografar_arquivo import criptografar_arquivo_caminho
import tkinter as tk
from print_textbox import print_to_textbox

def processar(arquivo, textbox):
    """
    Processa uma imagem usando OCR (Optical Character Recognition) e busca nomes e CPFs no texto extraído.

    Parâmetros:
        arquivo (str): O caminho para o arquivo de imagem a ser processado.
    """

    print_to_textbox(textbox, f"Processando imagem: {os.path.basename(arquivo)}")
    texto_extraido = pytesseract.image_to_string(Image.open(arquivo), lang='por') # Extrai o texto da imagem

    dados_sensiveis_encontrados = varredura(textbox, texto_extraido, arquivo)
    if dados_sensiveis_encontrados:    
        criptografar_arquivo_caminho(arquivo)
        print_to_textbox(textbox, f"\nArquivo {os.path.basename(arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(arquivo+'.criptografado')}")