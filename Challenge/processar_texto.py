import os
from buscar_txt import encontrar_nomes_em_txt, encontrar_cpf
from ler_nomes_txt import ler_nomes_txt

def processar(arquivo):
    """
    Processa um arquivo de texto, procurando por nomes e CPFs.

    Argumento:
        arquivo (str): O caminho para o arquivo de texto a ser processado.
    """

    print("Processando texto:", os.path.basename(arquivo))

    caminho_txt = "nomes.txt" # Caminho para o arquivo de texto com os nomes

    nomes = ler_nomes_txt(caminho_txt) # Cria uma lista com os nomes do arquivo

    encontrados_nomes = encontrar_nomes_em_txt(arquivo, nomes) # Encontra nomes no arquivo .txt
    encontrados_cpf = encontrar_cpf(arquivo) # Encontra CPFs no arquivo .txt

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
