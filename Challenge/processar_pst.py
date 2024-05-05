import os
from pypff import file
import pypff
from criptografar_arquivo import criptografar_arquivo_caminho
from print_textbox import print_to_textbox

def processar(arquivo, textbox):
    """
    Processa um arquivo PST, procurando por nomes e CPFs.
    Argumentos:
        arquivo_pst (str): O caminho para o arquivo PST a ser processado.
    """
    print_to_textbox(textbox, f"Processando PST: {os.path.basename(arquivo)}")
    try:
        pst_file = file.open(arquivo)
        pst_file.close()
        print_to_textbox(textbox, f"O arquivo {os.path.basename(arquivo)} não está protegido por senha.")
        criptografar_arquivo_caminho(arquivo)
        print_to_textbox(textbox, f"\nArquivo {os.path.basename(arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(arquivo+'.criptografado')}")
    except Exception as e:
        print_to_textbox(textbox, f"O arquivo {os.path.basename(arquivo)} está protegido por senha.")


def extrair_texto(arquivo):
    """
    Extrai texto de um arquivo PST.
 
    Argumento:
        arquivo (str): O caminho para o arquivo PST a ser processado.
 
    Retorna:
        str: O texto extraído do arquivo PST.
    """
    pst_file = pypff.file()  # Correção: usar PSTFile de libpff-python
    pst_file.open(arquivo)
    textos = []
    
    # Iterar sobre as pastas
    for folder in pst_file.root_folder.sub_folders:
        for message in folder.sub_messages:
            if message.message_class == "IPM.Note":
                # Extrair o corpo da mensagem
                try:
                    # Code to handle the AttributeError
                    pass
                except AttributeError:
                    body = ""  # Lidar com mensagens sem corpo de texto simples
                textos.append(body)

                # Extrair e salvar anexos
                for attachment in message.attachments:
                    filename = attachment.long_filename

                    # Cria um novo diretório para os anexos
                    anexos_dir = os.path.join(os.path.dirname(arquivo), f"{os.path.basename(arquivo)}_anexos")
                    os.makedirs(anexos_dir, exist_ok=True)

                    # Salvar o anexo no novo diretório
                    with open(os.path.join(anexos_dir, filename), "wb") as f:
                        f.write(attachment.read_stream())
    return textos
