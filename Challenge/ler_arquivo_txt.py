# Função para ler os nomes de um arquivo de texto e retornar uma lista
def ler_arquivo_txt(caminho_txt):
    """
    Lê todo o conteúdo do arquivo de texto.

    Argumentos:
        caminho_txt (str): O caminho para o arquivo de texto.

    Retorno:
        lista: Uma lista contendo todo o conteúdo lido do arquivo de texto.
    """
    with open(caminho_txt, 'r') as file:
        texto = file.read().splitlines()
    return texto
