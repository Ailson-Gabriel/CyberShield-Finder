import os
from PyPDF2 import PdfReader
from buscar import encontrar_nomes, encontrar_cpf

def processar(arquivo):
    """
    Processa um arquivo PDF, procurando por nomes e CPFs.

    Argumentos:
        arquivo (str): O caminho para o arquivo PDF a ser processado.
        nomes (list): Lista de nomes para procurar no PDF.
    """

    print("Processando PDF:", os.path.basename(arquivo))

    texto_pdf = extrair_texto(arquivo) 
    encontrados = encontrar_nomes(texto_pdf)
    encontrados_cpf = encontrar_cpf(texto_pdf)

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


def extrair_texto(arquivo):
    """
    Extrai texto de um arquivo PDF.

    Argumento:
        arquivo (str): O caminho para o arquivo PDF a ser processado.

    Retorna:
        str: O texto extraído do arquivo PDF.
    """
    texto = ""
    with open(arquivo, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            texto += page.extract_text()
    return texto