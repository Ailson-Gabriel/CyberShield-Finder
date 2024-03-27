import os
from buscar import encontrar_nomes, encontrar_cpf, encontrar_cnpj, encontrar_etnias, encontrar_religiao
from criptografar_arquivo import criptografar_arquivo_caminho
import tkinter as tk
from print_textbox import print_to_textbox
from colorama import init, Fore
init()

def processar(arquivo, textbox):
    """
    Processa um arquivo de texto, procurando por nomes e CPFs.

    Argumento:
        arquivo (str): O caminho para o arquivo de texto a ser processado.
    """

    print_to_textbox(textbox, f"Processando texto: {os.path.basename(arquivo)}",)
    #print(Fore.LIGHTWHITE_EX + "Processando texto:", os.path.basename(arquivo))

    texto_txt = extrair_texto(arquivo) 

    encontrados_nomes = encontrar_nomes(texto_txt, textbox) # Encontra nomes no texto extraido do arquivo
    encontrados_cpf = encontrar_cpf(texto_txt, textbox) # Encontra CPFs no texto extraido do arquivo
    encontrados_cnpj = encontrar_cnpj(texto_txt, textbox) # Encontra CNPJs no texto extraido do arquivo

    if encontrados_nomes or encontrados_cpf or encontrados_cnpj:
        encontrados_etnias = encontrar_etnias(texto_txt, textbox) # Encontra Etnias no texto extraido do arquivo
        encontrados_religioes = encontrar_religiao(texto_txt, textbox) # Encontra Religioes no texto extraido do arquivo

    # -------------------------------------- Imprime os resultados -------------------------------------- #
    if encontrados_nomes:
        print_to_textbox(textbox, f"Nomes encontrados no arquivo {os.path.basename(arquivo)}")
        #print(Fore.RED +  f"Nomes encontrados no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    else:
        print_to_textbox(textbox, f"Não foram encontrados nomes no arquivo {os.path.basename(arquivo)}")
        #print(Fore.BLUE + f"Não foram encontrados nomes no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    #
    if encontrados_cpf:
        print_to_textbox(textbox, f"CPF encontrado no arquivo {os.path.basename(arquivo)}")
        #print(Fore.RED + f"CPF encontrado no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    else:
        print_to_textbox(textbox, f"Não encontrado CPFs no arquivo {os.path.basename(arquivo)}")
        #print(Fore.BLUE + f"Não encontrado CPFs no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    #
    if encontrados_cnpj:
        print_to_textbox(textbox, f"CNPJ encontrado no arquivo {os.path.basename(arquivo)}")
        #print(Fore.RED + f"CNPJ encontrado no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    else:
        print_to_textbox(textbox, f"Não encontrado CNPJs no arquivo {os.path.basename(arquivo)}")
        #print(Fore.BLUE + f"Não encontrado CNPJs no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)

    if encontrados_etnias:
        print_to_textbox(textbox, f"Etnia encontrada no arquivo {os.path.basename(arquivo)}")
        #print(Fore.RED + f"Etnia encontrada no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    else:
        print_to_textbox(textbox, f"Não encontrada etnia no arquivo {os.path.basename(arquivo)}")
        #print(Fore.BLUE + f"Não encontrada etnia no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)

    if encontrados_religioes:
        print_to_textbox(textbox, f"Religiao encontrada no arquivo {os.path.basename(arquivo)}")
        #print(Fore.RED + f"Religiao encontrada no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    else:
        print_to_textbox(textbox, f"Não encontrada Religiao no arquivo {os.path.basename(arquivo)}")
        #print(Fore.BLUE + f"Não encontrada Religiao no arquivo {os.path.basename(arquivo)}\n")
        #print(Fore.RESET)
    # -------------------------------------- Imprime os resultados -------------------------------------- #

    if (encontrados_nomes or encontrados_cpf or encontrados_cnpj) and (encontrados_etnias or encontrados_religioes):
        criptografar_arquivo_caminho(arquivo)
        print_to_textbox(textbox, f"\nArquivo {os.path.basename(arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(arquivo+'.criptografado')}.")
    else:
        print_to_textbox(textbox, f"Não encontrado dados sensíveis que possam ser associados a algum individuo no arquivo {os.path.basename(arquivo)}")
        #print(Fore.CYAN + f"Não encontrado dados sensíveis no arquivo {os.path.basename(arquivo)}")
        #print(Fore.RESET)

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