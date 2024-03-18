import os
from cryptography.fernet import Fernet

# Função para gerar uma chave de criptografia usando Fernet
def gerar_chave():
    # Gera uma chave aleatória de criptografia usando Fernet
    return Fernet.generate_key()

# Função para salvar a chave em um arquivo especificado
def salvar_chave(chave, nome_arquivo):
    # Abre o arquivo especificado no modo de escrita binária ('wb') e escreve a chave no arquivo
    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(chave)

# Função para carregar a chave de um arquivo especificado
def carregar_chave(nome_arquivo):
    # Abre o arquivo especificado no modo de leitura binária ('rb') e lê a chave do arquivo
    with open(nome_arquivo, 'rb') as arquivo:
        return arquivo.read()

# Função para criptografar um arquivo especificado e salvar o arquivo criptografado
def criptografar_arquivo(chave, nome_arquivo, nome_arquivo_criptografado):
    # Abre o arquivo especificado no modo de leitura binária ('rb') e lê os dados do arquivo
    with open(nome_arquivo, 'rb') as arquivo:
        dados = arquivo.read()

    # Cria uma instância da classe Fernet usando a chave fornecida
    fernet = Fernet(chave)
    # Criptografa os dados lidos do arquivo
    dados_criptografados = fernet.encrypt(dados)

    # Abre o arquivo criptografado especificado no modo de escrita binária ('wb') e escreve os dados criptografados
    with open(nome_arquivo_criptografado, 'wb') as arquivo:
        arquivo.write(dados_criptografados)

# Função para criptografar um arquivo especificado pelo caminho fornecido
def criptografar_arquivo_caminho(caminho_arquivo):
    # Gera uma nova chave de criptografia
    chave = gerar_chave()
    # Adiciona a extensão ".criptografado" ao nome do arquivo
    nome_arquivo_criptografado = caminho_arquivo + '.criptografado'
    # Adiciona o sufixo "_chave" ao nome do arquivo para armazenar a chave
    nome_arquivo_chave = caminho_arquivo + '_chave'

    # Salva a chave em um arquivo com o nome especificado
    salvar_chave(chave, nome_arquivo_chave)
    # Carrega a chave salva do arquivo
    chave_carregada = carregar_chave(nome_arquivo_chave)

    # Criptografa o arquivo usando a chave carregada e salva o arquivo criptografado
    criptografar_arquivo(chave_carregada, caminho_arquivo, nome_arquivo_criptografado)
    os.remove(caminho_arquivo)

    # Imprime uma mensagem indicando que o arquivo foi criptografado com sucesso e salvo
    print(f"\nArquivo {os.path.basename(caminho_arquivo)} foi criptografado com sucesso e salvo como {os.path.basename(nome_arquivo_criptografado)}.\n")