import os
from cryptography.fernet import Fernet

# Função para descriptografar um arquivo criptografado
def descriptografar_arquivo(caminho_arquivo_chave, nome_arquivo_criptografado, nome_arquivo_descriptografado):
    # Abre o arquivo criptografado no modo de leitura binária ('rb') e lê os dados criptografados
    with open(nome_arquivo_criptografado, 'rb') as arquivo:
        dados_criptografados = arquivo.read()

    # Abre o arquivo da chave no modo de leitura binária ('rb') e lê a chave de criptografia
    with open(caminho_arquivo_chave, 'rb') as arquivo:
        chave = arquivo.read()

    fernet = Fernet(chave) # Cria uma instância da classe Fernet usando a chave fornecida
    dados_descriptografados = fernet.decrypt(dados_criptografados) # Descriptografa os dados criptografados usando a chave

    # Abre o arquivo especificado no modo de escrita binária ('wb') e escreve os dados descriptografados
    with open(nome_arquivo_descriptografado, 'wb') as arquivo:
        arquivo.write(dados_descriptografados)

# Função para descriptografar arquivos em um diretório especificado
def descriptografar_arquivos_em_diretorio(diretorio):
    for arquivo in os.listdir(diretorio): # Repete para os arquivos no diretório

        if os.path.isdir(os.path.join(diretorio, arquivo)):  # Se for um diretório
            print(f"Entrando no diretório: {arquivo}")
            descriptografar_arquivos_em_diretorio(os.path.join(diretorio, arquivo))  # Chama a função de varredura novamente para o subdiretório
        else:
            if arquivo.endswith('.criptografado'): # Verifica se o arquivo tem a extensão ".criptografado"
                caminho_arquivo_criptografado = os.path.join(diretorio, arquivo) # Obtém o caminho completo do arquivo criptografado
                caminho_arquivo_original = caminho_arquivo_criptografado[:-len('.criptografado')] # Remove a extensão ".criptografado" para obter o caminho do arquivo original
                caminho_arquivo_chave = caminho_arquivo_original + '_chave' # Obtém o caminho do arquivo da chave correspondente
                
                # Descriptografa o arquivo criptografado e salva o arquivo descriptografado
                descriptografar_arquivo(caminho_arquivo_chave, caminho_arquivo_criptografado, caminho_arquivo_original) 
                
                # Remove os arquivos criptografado e de chave após a descriptografia
                os.remove(caminho_arquivo_criptografado)
                os.remove(caminho_arquivo_chave)

# Diretório onde os arquivos criptografados estão localizados
diretorio = r'C:\Users\Gabriel\Desktop\FIAP - CyberSec\Primeiro_Ano\Nuclea\TESTES' #ALTERAR AQUI O CAMINHO DA PASTA DE TESTE DE VARREDURA
descriptografar_arquivos_em_diretorio(diretorio) # Chama a função para descriptografar os arquivos no diretório especificado
