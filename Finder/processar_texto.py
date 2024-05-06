import os # Módulo que fornece funções para interagir com o sistema operacional
from varredura import varredura # Função que realiza a varredura do texto extraido do arquivo em busca de nomes, CPFs, Etnias e Religiões
from criptografar_arquivo import criptografar_arquivo_caminho # Função que criptografa um arquivo
from print_textbox import print_to_textbox # Função que imprime mensagens em um Textbox

def processar(arquivo, textbox):
    """
    Processa um arquivo de texto, procurando por nomes e CPFs.

    Argumento:
        arquivo (str): O caminho para o arquivo de texto a ser processado.
        textbox (CTkTextbox): O objeto CTkTextbox onde as mensagens devem ser exibidas.
    """

    print_to_textbox(textbox, f"Processando TXT: {os.path.basename(arquivo)}",)
    texto_txt = extrair_texto(arquivo) # Extrai o texto do arquivo TXT

    dados_sensiveis_encontrados = varredura(textbox, texto_txt, arquivo) # Verifica se há dados sensíveis no texto extraído do arquivo Excel
    if dados_sensiveis_encontrados:
        criptografar_arquivo_caminho(arquivo) # Criptografa o arquivo se houver dados sensíveis
        print_to_textbox(textbox, f"\nArquivo {os.path.basename(arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(arquivo+'.criptografado')}")

def extrair_texto(arquivo):
    """
    Extrai texto de um arquivo TXT.

    Argumento:
        arquivo (str): O caminho para o arquivo TXT a ser processado.

    Retorna:
        str: O texto extraído do arquivo TXT.
    """

    # Abre o arquivo em modo de leitura
    with open(arquivo, 'r') as file:
        texto = file.read() # Lê o conteúdo do arquivo
    return texto # Retorna o texto extraído do arquivo