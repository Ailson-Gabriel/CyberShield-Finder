import os
import re
from buscar import encontrar_nomes, encontrar_cpf

def processar(arquivo):
    """
    Processa um arquivo de texto, procurando por nomes e CPFs.

    Argumento:
        arquivo (str): O caminho para o arquivo de texto a ser processado.
    """

    print("Processando texto:", os.path.basename(arquivo))

    texto_txt = extrair_texto(arquivo) 

    encontrados_nomes = encontrar_nomes(texto_txt) # Encontra nomes no texto extraido do arquivo
    encontrados_cpf = encontrar_cpf(texto_txt) # Encontra CPFs no texto extraido do arquivo

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


def extrair_texto(arquivo):
    """
    Extrai texto de um arquivo TXT.

    Argumento:
        arquivo (str): O caminho para o arquivo TXT a ser processado.

    Retorna:
        str: O texto extraído do arquivo TXT.
    """
    with open(arquivo, 'r') as file:
        texto = file.read() # Lê o conteúdo do arquivo
    return texto