import os
from docx import Document
from ler_nomes_txt import ler_nomes_txt
from buscar import encontrar_nomes, encontrar_cpf

def processar(arquivo):
    """
    Processa um arquivo .docx, procurando por nomes e CPFs.

    Argumento:
        arquivo (str): O caminho para o arquivo .docx a ser processado.
    """

    print("Processando docx:", os.path.basename(arquivo))
    
    caminho_txt = "nomes.txt" # Caminho para o arquivo de texto com os nomes
    nomes = ler_nomes_txt(caminho_txt) # Cria uma lista com os nomes do arquivo
    texto_docx = extrair_texto(arquivo)

    encontrados_nomes = encontrar_nomes(texto_docx, nomes) # Encontrar nomes nos arquivos .docx
    encontrados_cpf = encontrar_cpf(texto_docx) # Encontrar CPFs no arquivo .docx

    # -------------------------------------- Imprime os resultados -------------------------------------- #
    if encontrados_nomes:
        print(f"Nomes encontrados no arquivo {os.path.basename(arquivo)}\n")
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
    Extrai texto de um arquivo DOCX.

    Argumento:
        arquivo (str): O caminho para o arquivo DOCX a ser processado.

    Retorna:
        str: O texto extraído do arquivo DOCX.
    """
    document = Document(arquivo) # Abre o arquivo .docx e extrai o texto
    texto = ""
    for paragraph in document.paragraphs: # Repete sobre os parágrafos do documento e concatena seus textos
        texto += paragraph.text + "\n"
    return texto