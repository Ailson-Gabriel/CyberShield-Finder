import os # Módulo que fornece funções para interagir com o sistema operacional
from docx import Document # Módulo para ler arquivos DOCX
from criptografar_arquivo import criptografar_arquivo_caminho # Função que criptografa um arquivo
from varredura import varredura # Função que realiza a varredura do texto extraido do arquivo em busca de nomes, CPFs, Etnias e Religiões
from print_textbox import print_to_textbox # Função que imprime mensagens em um Textbox

def processar(arquivo, textbox):
    """
    Processa um arquivo .docx, procurando por nomes e CPFs.

    Argumento:
        arquivo (str): O caminho para o arquivo .docx a ser processado.
        textbox (CTkTextbox): O objeto CTkTextbox onde as mensagens devem ser exibidas.
    """
    
    print_to_textbox(textbox, f"Processando DOCX: {os.path.basename(arquivo)}",)    
    texto_docx = extrair_texto(arquivo)# Extrai texto do arquivo DOCX
    
    # Verifica se há dados sensíveis no texto extraído do arquivo Excel
    dados_sensiveis_encontrados = varredura(textbox, texto_docx, arquivo)
    if dados_sensiveis_encontrados: # Se houver dados sensíveis
        criptografar_arquivo_caminho(arquivo) # Criptografa o arquivo
        print_to_textbox(textbox, f"\nArquivo {os.path.basename(arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(arquivo+'.criptografado')}")
        
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
        texto += paragraph.text + "\n" # Adiciona o texto do parágrafo à variável texto
    return texto