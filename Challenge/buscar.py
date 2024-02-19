import re
from valida_cpf import valida_cpf

def encontrar_nomes(texto, nomes):
    """
    Encontra nomes em um texto.

    Argumentos:
        texto (str): O texto no qual procurar nomes.
        nomes (list): Lista de nomes para procurar no texto.

    Retorna:
        list: Lista de nomes encontrados.
    """
    encontrados = []
    for nome in nomes:
        if re.search(r'\b' + re.escape(nome) + r'\b', texto, re.IGNORECASE):
            encontrados.append(nome)
    return encontrados

def encontrar_cpf(texto):
    """
    Encontra CPFs em um texto.
    Argumento:
        texto (str): O texto no qual procurar CPFs.

    Retorna:
        list: Lista de CPFs encontrados.
    """
    cpfs_validos = []

    cpfs_potenciais = re.findall(r'\b(?:\d{3}\.){2}\d{3}-\d{2}|\b\d{11}\b', texto)
    # Encontra todos os conjuntos de 11 números ou CPFs formatados corretamente usando expressão regular

    # Valida cada CPF potencial
    for cpf in cpfs_potenciais:
        if valida_cpf(cpf):  # Chama a função valida_cpf para validar o CPF
            cpfs_validos.append(cpf)  # Adiciona o CPF válido à lista de CPFs válidos
            print(f"CPF válido encontrado: {cpf}") #REMOVER ESTA LINHA APÓS VERSÃO DE TESTES
    return cpfs_validos