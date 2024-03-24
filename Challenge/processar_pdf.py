import os
from PyPDF2 import PdfReader
from buscar import encontrar_nomes, encontrar_cpf, encontrar_cnpj
from criptografar_arquivo import criptografar_arquivo_caminho
from colorama import Fore

def processar(arquivo):
    """
    Processa um arquivo PDF, procurando por nomes e CPFs.

    Argumentos:
        arquivo (str): O caminho para o arquivo PDF a ser processado.
        nomes (list): Lista de nomes para procurar no PDF.
    """

    print(Fore.LIGHTWHITE_EX + "Processando PDF:", os.path.basename(arquivo))

    texto_pdf = extrair_texto(arquivo) 
    encontrados_nomes = encontrar_nomes(texto_pdf) # Encontra nomes no texto extraido do arquivo
    encontrados_cpf = encontrar_cpf(texto_pdf) # Encontra CPFs no texto extraido do arquivo
    encontrados_cnpj = encontrar_cnpj(texto_pdf) # Encontra CNPJs no texto extraido do arquivo

    # -------------------------------------- Imprime os resultados -------------------------------------- #
    if encontrados_nomes:
        print(Fore.RED +  f"Nomes encontrados no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)
    else:
        print(Fore.BLUE + f"Não foram encontrados nomes no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)

    if encontrados_cpf:
        print(Fore.RED + f"CPF encontrado no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)
    else:
        print(Fore.BLUE + f"Não encontrado CPFs no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)

    if encontrados_cnpj:
        print(Fore.RED + f"CNPJ encontrado no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)
    else:
        print(Fore.BLUE + f"Não encontrado CNPJs no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)
    # -------------------------------------- Imprime os resultados -------------------------------------- #
        
    if encontrados_nomes or encontrados_cpf or encontrados_cnpj:
        criptografar_arquivo_caminho(arquivo)
    else:
        print(Fore.CYAN + f"Não encontrado dados sensíveis no arquivo {os.path.basename(arquivo)}")
        print(Fore.RESET)


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