import os
import pytesseract # Módulo para usar a funcionalidade OCR (Optical Character Recognition) do Tesseract
from PIL import Image # Permite abrir, manipular e salvar imagens.
from buscar import encontrar_nomes, encontrar_cpf, encontrar_cnpj
from criptografar_arquivo import criptografar_arquivo_caminho

def processar(arquivo):
    """
    Processa uma imagem usando OCR (Optical Character Recognition) e busca nomes e CPFs no texto extraído.

    Parâmetros:
        arquivo (str): O caminho para o arquivo de imagem a ser processado.
    """

    print("Processando imagem:", os.path.basename(arquivo))

    texto_extraido = pytesseract.image_to_string(Image.open(arquivo), lang='por') # Extrai o texto da imagem

    encontrados_nomes = encontrar_nomes(texto_extraido) # Encontra nomes no texto extraido do arquivo
    encontrados_cpf = encontrar_cpf(texto_extraido) # Encontra CPFs no texto extraido do arquivo
    encontrados_cnpj = encontrar_cnpj(texto_extraido) # Encontra CNPJs no texto extraido do arquivo

    # -------------------------------------- Imprime os resultados -------------------------------------- #
    if encontrados_nomes:
        print(f"Nomes encontrados no arquivo {os.path.basename(arquivo)}\n")
    else:
        print(f"Não foram encontrados nomes no arquivo {os.path.basename(arquivo)}\n")

    if encontrados_cpf:
        print(f"CPF encontrado no arquivo {os.path.basename(arquivo)}\n")
    else:
        print(f"Não encontrado CPFs no arquivo {os.path.basename(arquivo)}\n")

    if encontrados_cnpj:
        print(f"CNPJ encontrado no arquivo {os.path.basename(arquivo)}\n")
    else:
        print(f"Não encontrado CNPJs no arquivo {os.path.basename(arquivo)}\n")
    # -------------------------------------- Imprime os resultados -------------------------------------- #
        
    if encontrados_nomes or encontrados_cpf or encontrados_cnpj:
        criptografar_arquivo_caminho(arquivo)