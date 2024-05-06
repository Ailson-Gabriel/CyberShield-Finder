import os # Módulo que fornece funções para interagir com o sistema operacional
from pypff import file # Módulo para ler arquivos PST
from criptografar_arquivo import criptografar_arquivo_caminho # Função que criptografa um arquivo
from print_textbox import print_to_textbox # Função que imprime mensagens em um Textbox

def processar(arquivo, textbox):
    """
    Processa um arquivo PST, procurando por nomes e CPFs.
    Argumentos:
        arquivo_pst (str): O caminho para o arquivo PST a ser processado.
    """

    print_to_textbox(textbox, f"Processando PST: {os.path.basename(arquivo)}")
    # Abre o arquivo PST
    try:
        pst_file = file.open(arquivo) # Abre o arquivo PST
        pst_file.close() # Fecha o arquivo PST
        print_to_textbox(textbox, f"O arquivo {os.path.basename(arquivo)} não está protegido por senha.")
        criptografar_arquivo_caminho(arquivo) # Criptografa o arquivo se não estiver protegido por senha
        print_to_textbox(textbox, f"\nArquivo {os.path.basename(arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(arquivo+'.criptografado')}")
    except Exception as e:
        # Se o arquivo estiver protegido por senha, exibe uma mensagem de erro
        print_to_textbox(textbox, f"O arquivo {os.path.basename(arquivo)} está protegido por senha.")
