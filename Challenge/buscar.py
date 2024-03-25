import re
from ler_arquivo_txt import ler_arquivo_txt
from valida_cpf import valida_cpf
from valida_cnpj import valida_cnpj
from colorama import Fore

def encontrar_nomes(texto):
    """
    Encontra nomes em um texto.

    Argumentos:
        texto (str): O texto no qual procurar nomes.

    Retorna:
        list: Lista de nomes encontrados.
    """
    print(Fore.YELLOW + "\nBUSCANDO NOMES")
    caminho_txt = "nomes.txt" # Caminho para o arquivo de texto com os nomes
    nomes = ler_arquivo_txt(caminho_txt) # Cria uma lista com os nomes do arquivo
    encontrados = []
    for nome in nomes:
        if re.search(r'\b' + re.escape(nome) + r'\b', texto, re.IGNORECASE):
            if nome not in encontrados:    
                encontrados.append(nome)
                #print(f"Nome encontrado: {nome}")
    return encontrados

def encontrar_cpf(texto):
    """
    Encontra CPFs em um texto.
    Argumento:
        texto (str): O texto no qual procurar CPFs.

    Retorna:
        list: Lista de CPFs encontrados.
    """
    print(Fore.YELLOW + "BUSCANDO POSSÍVEIS CPFs")
    cpfs_validos = []

    cpfs_potenciais = re.findall(r'\b(?:\d{3}\.){2}\d{3}-\d{2}|\b\d{11}\b', texto)
    # Encontra todos os conjuntos de 11 números ou CPFs formatados corretamente usando expressão regular

    # Valida cada CPF potencial
    for cpf in cpfs_potenciais:
        if valida_cpf(cpf):  # Chama a função valida_cpf para validar o CPF
            if cpf not in cpfs_validos:
                cpfs_validos.append(cpf)  # Adiciona o CPF válido à lista de CPFs válidos
                #print(f"CPF válido encontrado: {cpf}") #REMOVER ESTA LINHA APÓS VERSÃO DE TESTES
    return cpfs_validos

def encontrar_cnpj(texto):
    """
    Encontra CNPJs em um texto.
    Argumento:
        texto (str): O texto no qual procurar CNPJs.

    Retorna:
        list: Lista de CNPJs encontrados.
    """
    print(Fore.YELLOW + "BUSCANDO POSSÍVEIS CNPJs\n")
    print(Fore.RESET)
    cnpjs_validos = []

    # Encontra todos os conjuntos de 14 números ou CNPJs formatados corretamente usando expressão regular
    cnpjs_potenciais = re.findall(r'(?<!\d)(?:\d{1,2}\.)?\d{3}\.\d{3}/\d{4}-\d{2}(?!\d)|\b\d{14}\b', texto)

    # Valida cada CNPJ potencial
    for cnpj in cnpjs_potenciais:
        if valida_cnpj(cnpj):  # Chama a função valida_cnpj para validar o CNPJ
            if cnpj not in cnpjs_validos:
                cnpjs_validos.append(cnpj)  # Adiciona o CNPJ válido à lista de CNPJs válidos
                #print(f"CNPJ válido encontrado: {cnpj}") #REMOVER ESTA LINHA APÓS VERSÃO DE TESTES
    return cnpjs_validos

def encontrar_etnias(texto):
    """
    Encontra nomes em um texto.

    Argumentos:
        texto (str): O texto no qual procurar etnias.

    Retorna:
        list: Lista de etnias encontradas.
    """
    print(Fore.YELLOW + "\nBUSCANDO ETNIAS")
    caminho_txt = "etnias.txt" # Caminho para o arquivo de texto com os etnias
    etnias = ler_arquivo_txt(caminho_txt) # Cria uma lista com as etnias do arquivo
    encontrados = []
    for etnia in etnias:
        if re.search(r'\b' + re.escape(etnia) + r'\b', texto, re.IGNORECASE):
            if etnia not in encontrados:    
                encontrados.append(etnia)
    return encontrados

def encontrar_religiao(texto):
    """
    Encontra religioes em um texto.

    Argumentos:
        texto (str): O texto no qual procurar religioes.

    Retorna:
        list: Lista de religioes encontradas.
    """
    print(Fore.YELLOW + "\nBUSCANDO RELIGIOES")
    caminho_txt = "religiao.txt" # Caminho para o arquivo de texto com os religioes
    religioes = ler_arquivo_txt(caminho_txt) # Cria uma lista com as religioes do arquivo
    encontrados = []
    for religiao in religioes:
        if re.search(r'\b' + re.escape(religiao) + r'\b', texto, re.IGNORECASE):
            if religiao not in encontrados:    
                encontrados.append(religiao)
    return encontrados
