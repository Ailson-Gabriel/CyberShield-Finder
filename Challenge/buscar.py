import re
from ler_nomes_txt import ler_nomes_txt
from valida_cpf import valida_cpf

def encontrar_nomes(texto):
    """
    Encontra nomes em um texto.

    Argumentos:
        texto (str): O texto no qual procurar nomes.

    Retorna:
        list: Lista de nomes encontrados.
    """
    print("\nBUSCANDO NOMES")
    caminho_txt = "nomes.txt" # Caminho para o arquivo de texto com os nomes
    nomes = ler_nomes_txt(caminho_txt) # Cria uma lista com os nomes do arquivo
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
    print("\nBUSCANDO POSSÍVEIS CPFs")
    cpfs_validos = []

    cpfs_potenciais = re.findall(r'\b(?:\d{3}\.){2}\d{3}-\d{2}|\b\d{11}\b', texto)
    # Encontra todos os conjuntos de 11 números ou CPFs formatados corretamente usando expressão regular

    # Valida cada CPF potencial
    for cpf in cpfs_potenciais:
        if valida_cpf(cpf):  # Chama a função valida_cpf para validar o CPF
            if cpf not in cpfs_validos:
                cpfs_validos.append(cpf)  # Adiciona o CPF válido à lista de CPFs válidos
                print(f"CPF válido encontrado: {cpf}") #REMOVER ESTA LINHA APÓS VERSÃO DE TESTES
    return cpfs_validos