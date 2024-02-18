import os
import pytesseract # Módulo para usar a funcionalidade OCR (Optical Character Recognition) do Tesseract
from PIL import Image # Permite abrir, manipular e salvar imagens.
from ler_nomes_txt import ler_nomes_txt
from buscar_txt import encontrar_nomes_em_txt, encontrar_cpf

def processar(arquivo):
    """
    Processa uma imagem usando OCR (Optical Character Recognition) e busca nomes e CPFs no texto extraído.

    Parâmetros:
        arquivo (str): O caminho para o arquivo de imagem a ser processado.
    """

    print("Processando imagem:", os.path.basename(arquivo))

    texto_extraido = pytesseract.image_to_string(Image.open(arquivo), lang='por') # Extrai o texto da imagem

    with open('texto_extraido.txt', 'w') as arquivo_texto:
        arquivo_texto.write(texto_extraido) # Escreve o texto extraído em um arquivo de texto

    caminho_txt = "nomes.txt" # Caminho para o arquivo de texto com os nomes
    nomes = ler_nomes_txt(caminho_txt) # Cria uma lista com os nomes do arquivo
    caminho_txt = "texto_extraido.txt" # Redefine o caminho para o arquivo de texto extraido da imagem.
    encontrados_nomes = encontrar_nomes_em_txt(caminho_txt, nomes) # Encontra nomes no arquivo .txt
    encontrados_cpf = encontrar_cpf(caminho_txt) # Encontra CPFs no arquivo .txt

    entrada_usuario = input("Por favor, insira algo e pressione Enter para continuar: ") # Solicita uma entrada do usuário para pausar a execução e verificar o conteúdo do arquivo de texto
    os.remove('texto_extraido.txt') # Remove o arquivo de texto extraído após sua utilização
    print("Arquivo texto_extraido.txt foi excluído.") # Imprime uma mensagem indicando que o arquivo foi excluído (PARA FINS DE DESENVOLVIMENTO APENAS)

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
