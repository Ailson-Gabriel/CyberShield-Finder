def ler_arquivo_txt(caminho_txt):
    """
    Lê todo o conteúdo do arquivo de texto.
    Argumentos:
        caminho_txt (str): O caminho para o arquivo de texto.
    Retorno:
        lista: Uma lista contendo todo o conteúdo lido do arquivo de texto.
    """
    with open(caminho_txt, 'r', encoding='utf-8') as file: # Abre o arquivo em modo de leitura
        texto = file.read().splitlines() # Lê o conteúdo do arquivo e divide em linhas
    return texto # Retorna o texto extraído do arquivo