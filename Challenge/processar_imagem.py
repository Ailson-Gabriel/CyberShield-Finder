import os
import pytesseract # Módulo para usar a funcionalidade OCR (Optical Character Recognition) do Tesseract
from PIL import Image # Permite abrir, manipular e salvar imagens.
import cv2
from buscar import encontrar_nomes, encontrar_cpf, encontrar_cnpj, encontrar_etnias, encontrar_religiao
from criptografar_arquivo import criptografar_arquivo_caminho
import tkinter as tk
from print_textbox import print_to_textbox
from colorama import init, Fore
init()

def processar(arquivo, textbox):
    """
    Processa uma imagem usando OCR (Optical Character Recognition) e busca nomes e CPFs no texto extraído.

    Parâmetros:
        arquivo (str): O caminho para o arquivo de imagem a ser processado.
    """
    print_to_textbox(textbox, f"Processando imagem: {os.path.basename(arquivo)}")
    #print(Fore.LIGHTWHITE_EX + "Processando imagem:", os.path.basename(arquivo))
    
    texto_extraido = pytesseract.image_to_string(Image.open(arquivo), lang='por') # Extrai o texto da imagem

    encontrados_nomes = encontrar_nomes(texto_extraido, textbox) # Encontra nomes no texto extraido do arquivo
    encontrados_cpf = encontrar_cpf(texto_extraido, textbox) # Encontra CPFs no texto extraido do arquivo
    encontrados_cnpj = encontrar_cnpj(texto_extraido, textbox) # Encontra CNPJs no texto extraido do arquivo
    rosto_reconhecido = reconhecimento_facial(arquivo, textbox) # Encontra rostos no arquivo da imagem

    if encontrados_nomes or encontrados_cpf or encontrados_cnpj or rosto_reconhecido:
        encontrados_etnias = encontrar_etnias(texto_extraido, textbox) # Encontra Etnias no texto extraido do arquivo
        encontrados_religioes = encontrar_religiao(texto_extraido, textbox) # Encontra Religioes no texto extraido do arquivo

    # -------------------------------------- Imprime os resultados -------------------------------------- #
    if encontrados_nomes:
        print_to_textbox(textbox, f"Nomes encontrados no arquivo {os.path.basename(arquivo)}")
        #print(Fore.RED +  f"Nomes encontrados no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    else:
        print_to_textbox(textbox, f"Não foram encontrados nomes no arquivo {os.path.basename(arquivo)}")
        #print(Fore.BLUE + f"Não foram encontrados nomes no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    #
    if encontrados_cpf:
        print_to_textbox(textbox, f"CPF encontrado no arquivo {os.path.basename(arquivo)}")
        #print(Fore.RED + f"CPF encontrado no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    else:
        print_to_textbox(textbox, f"Não encontrado CPFs no arquivo {os.path.basename(arquivo)}")
        #print(Fore.BLUE + f"Não encontrado CPFs no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    #
    if encontrados_cnpj:
        print_to_textbox(textbox, f"CNPJ encontrado no arquivo {os.path.basename(arquivo)}")
        #print(Fore.RED + f"CNPJ encontrado no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    else:
        print_to_textbox(textbox, f"Não encontrado CNPJs no arquivo {os.path.basename(arquivo)}")
        #print(Fore.BLUE + f"Não encontrado CNPJs no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    #
    if rosto_reconhecido:
        print_to_textbox(textbox, f"Rosto detectado!")
        #print(Fore.RED + f"Rosto detectado!")
        #print(Fore.RESET)
    else:
        print_to_textbox(textbox, f"Nenhum rosto detectado")
        #print(Fore.BLUE + f"Nenhum rosto detectado")
        #print(Fore.RESET)

    if encontrados_etnias:
        print_to_textbox(textbox, f"Etnia encontrada no arquivo {os.path.basename(arquivo)}")
        #print(Fore.RED + f"Etnia encontrada no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    else:
        print_to_textbox(textbox, f"Não encontrada etnia no arquivo {os.path.basename(arquivo)}")
        #print(Fore.BLUE + f"Não encontrada etnia no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)

    if encontrados_religioes:
        print_to_textbox(textbox, f"Religiao encontrada no arquivo {os.path.basename(arquivo)}")
        #print(Fore.RED + f"Religiao encontrada no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    else:
        print_to_textbox(textbox, f"Não encontrada Religiao no arquivo {os.path.basename(arquivo)}")
        #print(Fore.BLUE + f"Não encontrada Religiao no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    # -------------------------------------- Imprime os resultados -------------------------------------- #
        
    if (encontrados_nomes or encontrados_cpf or encontrados_cnpj or rosto_reconhecido) and (encontrados_etnias or encontrados_religioes):
        criptografar_arquivo_caminho(arquivo)
        print_to_textbox(textbox, f"\nArquivo {os.path.basename(arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(arquivo+'.criptografado')}.")
        #print(f"\nArquivo {os.path.basename(arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(arquivo+".criptografado")}.\n")
    else:
        print_to_textbox(textbox, f"Não encontrado dados sensíveis que possam ser associados a algum individuo no arquivo {os.path.basename(arquivo)}")
        #print(Fore.CYAN + f"Não encontrado dados sensíveis no arquivo {os.path.basename(arquivo)}")
        #print(Fore.RESET)


def reconhecimento_facial(caminho_imagem):
    """
    Processa uma imagem usando OpenCV e busca por Rostos.

    Parâmetros:
        arquivo (str): O caminho para o arquivo de imagem a ser processada.
    Retorna:
        bool: True ou False se encontrou ou não.
    """
    print(Fore.YELLOW + "BUSCANDO ROSTOS")
    print(Fore.RESET)
    # Carrega o classificador pré-treinado para detecção de faces
    classificador_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    imagem = cv2.imread(caminho_imagem) # Carrega a imagem

    # Verifica se a imagem foi carregada corretamente
    if imagem is None:
        print("Erro: Não foi possível carregar a imagem.")
        return False

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # Converte a imagem para escala de cinza

    # Detecta rostos na imagem
    faces = classificador_face.detectMultiScale(imagem_cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Retorna True se pelo menos um rosto for detectado
    if len(faces) > 0:
        return True
    else:
        return False
