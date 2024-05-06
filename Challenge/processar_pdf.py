import os # Módulo que fornece funções para interagir com o sistema operacional
from PyPDF2 import PdfReader # Módulo para ler arquivos PDF
from varredura import varredura # Função que realiza a varredura do texto extraido do arquivo em busca de nomes, CPFs, Etnias e Religiões
from criptografar_arquivo import criptografar_arquivo_caminho # Função que criptografa um arquivo
from print_textbox import print_to_textbox # Função que imprime mensagens em um Textbox

def processar(arquivo, textbox):
    """
    Processa um arquivo PDF, procurando por nomes e CPFs.

    Argumentos:
        arquivo (str): O caminho para o arquivo PDF a ser processado.
        nomes (list): Lista de nomes para procurar no PDF.
    """

    print_to_textbox(textbox, f"Processando PDF: {os.path.basename(arquivo)}",)
    texto_pdf = extrair_texto(arquivo) # Extrai texto do arquivo PDF
    
    dados_sensiveis_encontrados = varredura(textbox, texto_pdf, arquivo) # Verifica se há dados sensíveis no texto extraído do arquivo Excel
    if dados_sensiveis_encontrados:
        criptografar_arquivo_caminho(arquivo) # Criptografa o arquivo se houver dados sensíveis
        print_to_textbox(textbox, f"\nArquivo {os.path.basename(arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(arquivo+'.criptografado')}")

def extrair_texto(arquivo):
    """
    Extrai texto de um arquivo PDF.

    Argumento:
        arquivo (str): O caminho para o arquivo PDF a ser processado.

    Retorna:
        str: O texto extraído do arquivo PDF.
    """
    texto = "" # Inicializa a variável texto
    with open(arquivo, "rb") as f: # Abre o arquivo PDF em modo de leitura binária
        reader = PdfReader(f) # Cria um objeto PdfReader
        for page in reader.pages: # Repete sobre as páginas do arquivo PDF
            texto += page.extract_text() # Extrai o texto de cada página do arquivo PDF
    return texto