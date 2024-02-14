# Função para ler os nomes de um arquivo de texto e retornar uma lista
def ler_nomes_txt(caminho_txt):
    """
    Lê os nomes do arquivo de texto.

    Argumentos:
        caminho_txt (str): O caminho para o arquivo de texto.

    Retorno:
        lista: Uma lista contendo os nomes lidos do arquivo de texto.
    """
    with open(caminho_txt, 'r') as file:
        nomes = file.read().splitlines()
    return nomes
