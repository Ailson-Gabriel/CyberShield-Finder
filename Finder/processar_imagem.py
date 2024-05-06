import os # Módulo que fornece funções para interagir com o sistema operacional
import pytesseract # Módulo para usar a funcionalidade OCR (Optical Character Recognition) do Tesseract
from PIL import Image # Permite abrir, manipular e salvar imagens.
from varredura import varredura # Função que realiza a varredura do texto extraido do arquivo em busca de nomes, CPFs, Etnias e Religiões
from criptografar_arquivo import criptografar_arquivo_caminho # Função que criptografa um arquivo
from print_textbox import print_to_textbox # Função que imprime mensagens em um Textbox

def processar(arquivo, textbox):
    """
    Processa uma imagem usando OCR (Optical Character Recognition) e busca nomes e CPFs no texto extraído.

    Parâmetros:
        arquivo (str): O caminho para o arquivo de imagem a ser processado.
    """

    print_to_textbox(textbox, f"Processando imagem: {os.path.basename(arquivo)}")
    texto_extraido = pytesseract.image_to_string(Image.open(arquivo), lang='por') # Extrai o texto da imagem

    # Verifica se há dados sensíveis no texto extraído da imagem
    dados_sensiveis_encontrados = varredura(textbox, texto_extraido, arquivo)
    if dados_sensiveis_encontrados: # Se houver dados sensíveis
        criptografar_arquivo_caminho(arquivo) # Criptografa o arquivo
        print_to_textbox(textbox, f"\nArquivo {os.path.basename(arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(arquivo+'.criptografado')}")