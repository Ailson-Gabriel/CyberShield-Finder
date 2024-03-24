import os
import pytesseract # Módulo para usar a funcionalidade OCR (Optical Character Recognition) do Tesseract
from PIL import Image # Permite abrir, manipular e salvar imagens.
import cv2
from buscar import encontrar_nomes, encontrar_cpf, encontrar_cnpj
from criptografar_arquivo import criptografar_arquivo_caminho
from colorama import Fore

def processar(arquivo):
    """
    Processa uma imagem usando OCR (Optical Character Recognition) e busca nomes e CPFs no texto extraído.

    Parâmetros:
        arquivo (str): O caminho para o arquivo de imagem a ser processado.
    """

    print(Fore.LIGHTWHITE_EX + "Processando imagem:", os.path.basename(arquivo))
    
    rosto_reconhecido = reconhecimento_facial(arquivo)
    texto_extraido = pytesseract.image_to_string(Image.open(arquivo), lang='por') # Extrai o texto da imagem

    encontrados_nomes = encontrar_nomes(texto_extraido) # Encontra nomes no texto extraido do arquivo
    encontrados_cpf = encontrar_cpf(texto_extraido) # Encontra CPFs no texto extraido do arquivo
    encontrados_cnpj = encontrar_cnpj(texto_extraido) # Encontra CNPJs no texto extraido do arquivo

    # -------------------------------------- Imprime os resultados -------------------------------------- #
    if encontrados_nomes:
        print(Fore.RED +  f"Nomes encontrados no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)
    else:
        print(Fore.BLUE + f"Não foram encontrados nomes no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)
    #
    if encontrados_cpf:
        print(Fore.RED + f"CPF encontrado no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)
    else:
        print(Fore.BLUE + f"Não encontrado CPFs no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)
    #
    if encontrados_cnpj:
        print(Fore.RED + f"CNPJ encontrado no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)
    else:
        print(Fore.BLUE + f"Não encontrado CNPJs no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)
    #
    if rosto_reconhecido:
        print(Fore.RED + f"Rosto detectado!")
        print(Fore.RESET)
    else:
        print(Fore.BLUE + f"Nenhum rosto detectado")
        print(Fore.RESET)
    # -------------------------------------- Imprime os resultados -------------------------------------- #
        
    if encontrados_nomes or encontrados_cpf or encontrados_cnpj:
        criptografar_arquivo_caminho(arquivo)
    else:
        print(Fore.CYAN + f"Não encontrado dados sensíveis no arquivo {os.path.basename(arquivo)}")
        print(Fore.RESET)


def reconhecimento_facial(caminho_imagem):
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
