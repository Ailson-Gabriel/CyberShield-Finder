import os
import re
from valida_cpf import valida_cpf

def encontrar_nomes_em_txt(caminho_arquivo, nomes):
    """
    Procura pelos nomes nos arquivos .txt em um diretório especificado.
    
    Argumentos:
        caminho_arquivo (str): O caminho para o diretório contendo os arquivos .txt
        nomes (lista): Uma lista de nomes a serem procurados nos arquivos .txt
    Retorno:
        lista: Uma lista dos nomes encontrados nos arquivos .txt.
    """

    nomes_encontrados = [] # Inicializa uma lista para armazenar os nomes encontrados
    with open(caminho_arquivo, 'r') as file: # Abre o arquivo .txt no modo de leitura ('r')
        texto = file.read().lower() # Armazena todo o conteúdo do arquivo e converte para minúsculo
        for nome in nomes: # Repete para cada nome na lista de nomes fornecida
            if nome.lower() in texto: # Verifica se o nome (em minúsculo) está presente no texto do arquivo
                nomes_encontrados.append(nome) # Adiciona à lista de nomes encontrados
                #print(f"Nome encontrado: {nome} - Arquivo: {arquivo}") # Imprime mensagem indicando o nome encontrado e o arquivo onde foi encontrado
    return nomes_encontrados


def encontrar_cpf(caminho_arquivo):
    """
    Procura por cadeias de 11 números (supostos CPFs) em arquivos .txt em um diretório especificado.
    Valida cada CPF encontrado usando a função valida_cpf de outro arquivo .py.

    Argmuentos:
        caminho_arquivo (str): O caminho para o diretório contendo os arquivos .txt.

    Retorno:
        lista: Uma lista dos CPFs válidos encontrados nos arquivos .txt.
    """
    
    cpfs_validos = [] # Inicializa uma lista para armazenar os CPFs válidos
    with open(caminho_arquivo, 'r') as file:
        texto = file.read() # Lê o conteúdo do arquivo
        texto = re.sub(r'\D', '', texto) # Remove todos os caracteres não numéricos (exceto dígitos)
        # Procura por cadeias de 11 números (supostos CPFs)
        for i in range(len(texto) - 10): # Repete sobre o texto, considerando todas as sequências de 11 dígitos
            possivel_cpf = texto[i:i+11]  # Obtém uma sequência de 11 dígitos
            if valida_cpf(possivel_cpf):  # Chama a função valida_cpf para validar o CPF
                cpfs_validos.append(possivel_cpf) # Adiciona o CPF válido à lista de CPFs válidos
                print(f"CPF válido encontrado: {possivel_cpf} - Arquivo: {os.path.basename(caminho_arquivo)}") #REMOVER ESTA LINHA APÓS VERSÃO DE TESTES
    return cpfs_validos
