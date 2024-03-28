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
    
    dados_sensiveis_encontrados = varredura(textbox, texto_extraido)
    # -------------------------------------- REVER LÓGICA DE DADOS SENSÍVEIS -------------------------------------- #
    if dados_sensiveis_encontrados or reconhecimento_facial(arquivo, textbox):
        criptografar_arquivo_caminho(arquivo)
        print_to_textbox(textbox, f"\nArquivo {os.path.basename(arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(arquivo+'.criptografado')}")
    else:
        print_to_textbox(textbox, f"Não encontrado dados sensíveis que possam ser associados a algum individuo no arquivo {os.path.basename(arquivo)}")

def reconhecimento_facial(caminho_imagem, textbox):
    """
    Processa uma imagem usando OpenCV e busca por Rostos.

    Parâmetros:
        arquivo (str): O caminho para o arquivo de imagem a ser processada.
    Retorna:
        bool: True ou False se encontrou ou não.
    """
    print_to_textbox(textbox, f"BUSCANDO ROSTOS")
    # Carrega o classificador pré-treinado para detecção de faces
    classificador_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    imagem = cv2.imread(caminho_imagem) # Carrega a imagem

    # Verifica se a imagem foi carregada corretamente
    if imagem is None:
        print_to_textbox(textbox, f"Erro: Não foi possível carregar a imagem.")
        return False

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # Converte a imagem para escala de cinza

    # Detecta rostos na imagem
    faces = classificador_face.detectMultiScale(imagem_cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Retorna True se pelo menos um rosto for detectado
    if len(faces) > 0:
        print_to_textbox(textbox, f"Rosto detectado no arquivo {os.path.basename(caminho_imagem)}")
        return True
    else:
        print_to_textbox(textbox, f"Nenhum rosto detectado no arquivo {os.path.basename(caminho_imagem)}")
        return False
