import os
from buscar import encontrar_nomes, encontrar_cpf, encontrar_cnpj, encontrar_etnias, encontrar_religiao
from criptografar_arquivo import criptografar_arquivo_caminho
from colorama import Fore

def processar(arquivo):
    """
    Processa um arquivo de texto, procurando por nomes e CPFs.

    Argumento:
        arquivo (str): O caminho para o arquivo de texto a ser processado.
    """

    print(Fore.LIGHTWHITE_EX + "Processando texto:", os.path.basename(arquivo))

    texto_txt = extrair_texto(arquivo) 

    encontrados_nomes = encontrar_nomes(texto_txt) # Encontra nomes no texto extraido do arquivo
    encontrados_cpf = encontrar_cpf(texto_txt) # Encontra CPFs no texto extraido do arquivo
    encontrados_cnpj = encontrar_cnpj(texto_txt) # Encontra CNPJs no texto extraido do arquivo
    encontrados_etnias = encontrar_etnias(texto_txt) # Encontra Etnias no texto extraido do arquivo

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

    if encontrados_etnias:
        print(Fore.RED + f"Etnia encontrada no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)
    else:
        print(Fore.BLUE + f"Não encontrada etnia no arquivo {os.path.basename(arquivo)}\n")
        print(Fore.RESET)
    # -------------------------------------- Imprime os resultados -------------------------------------- #

    if encontrados_nomes or encontrados_cpf or encontrados_cnpj or encontrados_etnias:
        criptografar_arquivo_caminho(arquivo)
    else:
        print(Fore.CYAN + f"Não encontrado dados sensíveis no arquivo {os.path.basename(arquivo)}")
        print(Fore.RESET)


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