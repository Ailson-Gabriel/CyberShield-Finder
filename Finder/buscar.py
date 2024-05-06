import re # Importa o módulo re (regular expressions) para trabalhar com expressões regulares
from ler_arquivo_txt import ler_arquivo_txt # Importa a função ler_arquivo_txt do módulo ler_arquivo_txt
from valida_cpf import valida_cpf # Importa a função valida_cpf do módulo valida_cpf

def encontrar_dados_sensiveis(texto, contexto):
    """
    Encontra dados em um texto.

    Argumentos:
        texto (str): O texto no qual procurar os dados sensíveis
        contexto (str): O contexto no qual procurar os dados sensíveis

    Retorna:
        list: Lista de dados sensíveis encontrados.
    """

    caminho_txt = f"wordlists\{contexto}.txt" # Caminho para o arquivo de texto com os dados que podem ser sensíveis
    lista = ler_arquivo_txt(caminho_txt) # Cria uma lista com os dados do arquivo
    encontrados = [] # Cria uma lista vazia para armazenar os dados sensíveis encontrados
    for elemento in lista: # Repete para cada elemento na lista
        if re.search(r'\b' + re.escape(elemento) + r'\b', texto, re.IGNORECASE): # Verifica se o elemento está presente no texto
            if elemento not in encontrados: # Verifica se o elemento já foi encontrado
                encontrados.append(elemento) # Adiciona o elemento à lista de dados sensíveis encontrados
    return encontrados

def encontrar_cpf(texto):
    """
    Encontra CPFs em um texto.
    Argumento:
        texto (str): O texto no qual procurar CPFs.

    Retorna:
        list: Lista de CPFs encontrados.
    """
    
    cpfs_validos = [] # Cria uma lista vazia para armazenar os CPFs válidos
    # Encontra todos os conjuntos de 11 números ou CPFs formatados corretamente usando expressão regular
    cpfs_potenciais = re.findall(r'\b(?:\d{3}\.){2}\d{3}-\d{2}|\b\d{11}\b', texto) 
    
    # Valida cada CPF potencial
    for cpf in cpfs_potenciais: # Repete para cada CPF potencial
        if valida_cpf(cpf):  # Chama a função valida_cpf para validar o CPF
            if cpf not in cpfs_validos: # Verifica se o CPF já foi encontrado
                cpfs_validos.append(cpf)  # Adiciona o CPF válido à lista de CPFs válidos
    return cpfs_validos

