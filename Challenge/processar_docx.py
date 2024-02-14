import os
from docx import Document
from buscar_docx import encontrar_nomes, encontrar_cpf
from ler_nomes_txt import ler_nomes_txt

def processar(arquivo):
    """
    Processa um arquivo .docx, procurando por nomes e CPFs.

    Argumento:
        arquivo (str): O caminho para o arquivo .docx a ser processado.
    """

    print("Processando docx:", os.path.basename(arquivo))
    
    caminho_txt = "nomes.txt" # Caminho para o arquivo de texto com os nomes

    nomes = ler_nomes_txt(caminho_txt) # Cria uma lista com os nomes do arquivo

    encontrados = encontrar_nomes(arquivo, nomes) # Encontrar nomes nos arquivos .docx
    encontrados_cpf = encontrar_cpf(arquivo) # Encontrar CPFs no arquivo .docx

    # -------------------------------------- Imprime os resultados -------------------------------------- #
    if encontrados:
        print(f"Nomes encontrados no arquivo {os.path.basename(arquivo)}\n")
        print(encontrados)
        print("\n")
    else:
        print(f"Não foram encontrados nomes no arquivo {os.path.basename(arquivo)}\n")

    if encontrados_cpf:
        print(f"CPF encontrado no arquivo {os.path.basename(arquivo)}\n")
    else:
        print(f"Não encontrado CPFs no arquivo {os.path.basename(arquivo)}\n")
    # -------------------------------------- Imprime os resultados -------------------------------------- #