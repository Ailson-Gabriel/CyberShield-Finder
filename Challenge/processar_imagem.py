import os
import pytesseract # Módulo para usar a funcionalidade OCR (Optical Character Recognition) do Tesseract
from PIL import Image # Permite abrir, manipular e salvar imagens.
from ler_nomes_txt import ler_nomes_txt
from buscar import encontrar_nomes, encontrar_cpf

def processar(arquivo):
    """
    Processa uma imagem usando OCR (Optical Character Recognition) e busca nomes e CPFs no texto extraído.

    Parâmetros:
        arquivo (str): O caminho para o arquivo de imagem a ser processado.
    """

    print("Processando imagem:", os.path.basename(arquivo))

    texto_extraido = pytesseract.image_to_string(Image.open(arquivo), lang='por') # Extrai o texto da imagem

    caminho_txt = "nomes.txt" # Caminho para o arquivo de texto com os nomes
    nomes = ler_nomes_txt(caminho_txt) # Cria uma lista com os nomes do arquivo
    encontrados_nomes = encontrar_nomes(texto_extraido, nomes) # Encontra nomes no texto extraido do arquivo
    encontrados_cpf = encontrar_cpf(texto_extraido) # Encontra CPFs no texto extraido do arquivo

    # -------------------------------------- Imprime os resultados -------------------------------------- #
    if encontrados_nomes:
        print(f"Nomes encontrados no arquivo {os.path.basename(arquivo)}:\n")
        print(encontrados_nomes)
        print("\n")
    else:
        print(f"Não foram encontrados nomes no arquivo {os.path.basename(arquivo)}\n")

    if encontrados_cpf:
        print(f"CPF encontrado no arquivo {os.path.basename(arquivo)}\n")
    else:
        print(f"Não encontrado CPFs no arquivo {os.path.basename(arquivo)}\n")
    # -------------------------------------- Imprime os resultados -------------------------------------- #