import os # Módulo que fornece funções para interagir com o sistema operacional
import re # Módulo que fornece funções para trabalhar com expressões regulares
import pprint # Módulo que fornece funções para imprimir objetos de forma mais legível
import ast # Módulo que fornece funções para avaliar strings como expressões Python
 
def grava_dados(tabela, dados, qntd):
    """
    Função para gravar os dados encontrados em um arquivo .txt
    Cria um Dicionário com os dados encontrados e a quantidade de cada tipo acrescentando os dados no .txt
    Args:
        tabela: Nome da tabela onde os dados serão gravados
        dado: Dado sensível encontrado
        qntd: Quantidade de vezes que o dado foi encontrado
    Returns:
        None
    """
    dados = f'["{dados}", "{qntd}"]\n' # Formata os dados
    with open('db\\base.txt', 'a+') as py_file: # Abre o arquivo .txt
        py_file.write("\n") # Pula uma linha
        py_file.write(f"{tabela} = {dados}\n") # Escreve os dados no arquivo .txt
    return None

def inicia_dados():
    """
    Função para iniciar o arquivo .txt
    Cria um arquivo .txt vazio
    Args:
        None
    Returns:
        None
    """
    if not os.path.isdir('db'): # Verifica se o diretório db existe
        os.makedirs('db') # Cria o diretório db
    with open('db\\base.txt', 'w') as py_file: # Abre o arquivo .txt para criar o arquivo
        pass # Não faz nada
    return None

def grava_lista_em_arquivo(string, criptografado):
    """
    Função para gravar uma string em uma lista em um arquivo .txt
    Args:
        string: A string a ser gravada
        criptografado: Um booleano que determina em qual lista a string será gravada
    Returns:
        None
    """
    arquivo_nome = 'db\\base.txt' # Nome do arquivo .txt
    if criptografado: # Se a string foi criptografada
        lista_nome = 'criptografados' # Nome da lista
        if string.endswith('.txt'): # Se a string termina com '.txt'
            push_dicionario("quantidade_por_tipo", ".txt", 1) # Adiciona 1 ao valor da chave '.txt' no dicionário 'quantidade_por_tipo'
        elif string.endswith('.docx'): # Se a string termina com '.docx'
            push_dicionario("quantidade_por_tipo", ".docx", 1) # Adiciona 1 ao valor da chave '.docx' no dicionário 'quantidade_por_tipo'
        elif string.endswith('.jpeg'): # Se a string termina com '.jpeg'
            push_dicionario("quantidade_por_tipo", ".jpeg", 1) # Adiciona 1 ao valor da chave '.jpeg' no dicionário 'quantidade_por_tipo'
        elif string.endswith('.jpg'): # Se a string termina com '.jpg'
            push_dicionario("quantidade_por_tipo", ".jpg", 1) # Adiciona 1 ao valor da chave '.jpg' no dicionário 'quantidade_por_tipo'
        elif string.endswith('.png'): # Se a string termina com '.png'
            push_dicionario("quantidade_por_tipo", ".png", 1) # Adiciona 1 ao valor da chave '.png' no dicionário 'quantidade_por_tipo'
        elif string.endswith('.pdf'): # Se a string termina com '.pdf'
            push_dicionario("quantidade_por_tipo", ".pdf", 1) # Adiciona 1 ao valor da chave '.pdf' no dicionário 'quantidade_por_tipo'
        elif string.endswith('.xls'): # Se a string termina com '.xls'
            push_dicionario("quantidade_por_tipo", ".xls", 1) # Adiciona 1 ao valor da chave '.xls' no dicionário 'quantidade_por_tipo'
        elif string.endswith('.xlsx'): # Se a string termina com '.xlsx' 
            push_dicionario("quantidade_por_tipo", ".xlsx", 1) # Adiciona 1 ao valor da chave '.xlsx' no dicionário 'quantidade_por_tipo'
        elif string.endswith('.pst'): # Se a string termina com '.pst'
            push_dicionario("quantidade_por_tipo", ".pst", 1) # Adiciona 1 ao valor da chave '.pst' no dicionário 'quantidade_por_tipo'
    else: # Se a string não foi criptografada
        lista_nome = 'nao_criptografados' # Nome da lista

    # Verifica se o arquivo existe
    if not os.path.exists(arquivo_nome): # Se o arquivo não existe
        raise FileNotFoundError(f"O arquivo {arquivo_nome} não foi encontrado.") # Levanta uma exceção

    # Lê todo o conteúdo do arquivo
    with open(arquivo_nome, 'r') as f: # Abre o arquivo .txt
        conteudo = f.read() # Lê o conteúdo do arquivo

    # Procura pela lista usando regex
    lista_regex = re.compile(rf"({lista_nome} = \[.*?\])", re.DOTALL) # Compila a expressão regular
    lista_match = lista_regex.search(conteudo) # Procura pela lista no conteúdo do arquivo

    # Se a lista foi encontrada
    if lista_match:
        lista_str = lista_match.group(1) # Obtém a string da lista
        nova_lista_str = lista_str[:-1] + f", '{string}']" # Adiciona a nova string à lista
    else: # Se a lista não foi encontrada
        nova_lista_str = f"{lista_nome} = ['{string}']" # Cria uma nova lista com a string

    # Substitui a lista antiga pela nova lista no conteúdo do arquivo
    novo_conteudo = conteudo.replace(lista_str, nova_lista_str) if lista_match else conteudo + '\n' + nova_lista_str

    # Reescreve todo o conteúdo do arquivo
    with open(arquivo_nome, 'w') as f:
        f.write(novo_conteudo)

    return None

def grava_dicionario(nome, dicionario):
    """
    Função para gravar um dicionário em um arquivo .txt
    Args:
        nome: O nome do dicionário
        dicionario: O dicionário a ser gravado
    Returns:
        None    
    """
    with open ("db\\base.txt", "a+") as py_file: # Abre o arquivo .txt
        py_file.write(f"{nome} = {{\n") # Escreve o nome do dicionário
        # Cria uma lista de strings formatadas
        items = [f'\t"{tipo}": {quantidade}' for tipo, quantidade in dicionario.items()]
        # Combina todas as strings em uma única string, separada por vírgulas
        py_file.write(',\n'.join(items))
        py_file.write("\n}\n")

def atualizar_dicionario(nome_dict, novo_dict): 
    """
    Função para atualizar um dicionário em um arquivo .txt
    Args:
        nome_dict: O nome do dicionário
        novo_dict: O dicionário com os novos valores
    Returns:
        None
    """

    caminho_arquivo = "db\\base.txt" # Caminho do arquivo .txt
    linhas = [] # Lista para armazenar as linhas do arquivo
    with open(caminho_arquivo, 'r') as arquivo: # Abre o arquivo .txt
        linhas = arquivo.readlines() # Lê as linhas do arquivo

    for i, linha in enumerate(linhas): # Para cada linha do arquivo
        if nome_dict in linha: # Se o nome do dicionário está na linha
            dados = eval(linha.split('=')[1].strip()) # Obtém os dados do dicionário
            for chave, valor in novo_dict.items(): # Para cada chave e valor do novo dicionário
                if chave in dados: # Se a chave já existe no dicionário
                    dados[chave] += valor # Adiciona o valor ao valor existente
                else: # Se a chave não existe no dicionário
                    dados[chave] = valor # Adiciona a chave e o valor ao dicionário
            linhas[i] = f"{nome_dict} = {str(dados)}\n" # Atualiza a linha com os novos dados
            break # Sai do loop
    else: # Se o loop terminar sem encontrar o nome do dicionário
        linhas.append(f"{nome_dict} = {str(novo_dict)}\n") # Adiciona o novo dicionário ao final do arquivo

    with open(caminho_arquivo, 'w') as arquivo: # Abre o arquivo .txt
        arquivo.writelines(linhas) # Escreve as linhas no arquivo

def cria_dicionario(nome, chave, valor):
    """
    Função para criar um dicionário vazio em um arquivo .txt
    Args:
        None
    Returns:
        None
    """
    with open('db\\base.txt', 'w') as f: # Abre o arquivo .txt
        f.write(f"{nome} = {{\n") # Escreve o nome do dicionário
        f.write(f"\t'{chave}': {valor}\n") # Escreve a chave e o valor
        f.write("}\n") # Fecha o dicionário
        f.write("\n") # Pula uma linha
    return None

def push_dicionario(nome, chave, valor):
    """
    Função para adicionar um item a um dicionário em um arquivo .txt
    Args:
        nome: O nome do dicionário
        chave: A chave do item a ser adicionado
        valor: O valor do item a ser adicionado
    Returns:
        None
    """
    caminho_arquivo = 'db\\base.txt' # Caminho do arquivo .txt
    linhas = [] # Lista para armazenar as linhas do arquivo
    with open(caminho_arquivo, 'r') as arquivo: # Abre o arquivo .txt
        linhas = arquivo.readlines() # Lê as linhas do arquivo

    for i, linha in enumerate(linhas): # Para cada linha do arquivo
        if nome in linha: # Se o nome do dicionário está na linha
            dados = eval(linha.split('=')[1].strip()) # Obtém os dados do dicionário
            if chave in dados: # Se a chave já existe no dicionário
                novo_dict = {chave: valor} # Cria um novo dicionário com a chave e o valor
                atualizar_dicionario(nome, novo_dict) # Atualiza o dicionário
                return None 
            else: # Se a chave não existe no dicionário
                dados[chave] = valor # Adiciona a chave e o valor ao dicionário
                linhas[i] = f"{nome} = " + pprint.pformat(dados, indent=4) + "\n" # Atualiza a linha com os novos dados
                break # Sai do loop
    else: # Se o loop terminar sem encontrar o nome do dicionário
        linhas.append(f"{nome} = {{'{chave}': {valor}}}\n") # Adiciona o novo item ao final do arquivo

    with open(caminho_arquivo, 'w') as arquivo: # Abre o arquivo .txt
        arquivo.writelines(linhas) # Escreve as linhas no arquivo

    return None

def grava_tabela_de_arquivos(nome_arquivo='db\\base.txt'):
    """
    Grava a tabela de arquivos em um arquivo .txt
    Args:
        nome_arquivo: O nome do arquivo .txt
    Returns:
        None
    """

    criptografados = load_data_from_txt('db\\base.txt', 'criptografados') # Carrega os arquivos criptografados
    nao_criptografados = load_data_from_txt('db\\base.txt', 'nao_criptografados') # Carrega os arquivos não criptografados

    # Cria a tabela de arquivos
    tabela_de_arquivos = [[item, 'Sim'] for item in criptografados] + [[item, 'Não'] for item in nao_criptografados]

    with open(nome_arquivo, 'a', encoding='utf-8') as f: # Abre o arquivo .txt
        f.write(f'\ntabela_de_arquivos = {tabela_de_arquivos}\n') # Escreve a tabela de arquivos no arquivo .txt


def load_data_from_txt(caminho_arquivo, nome_variavel): # Função para carregar dados de um arquivo .txt
  with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: # Abre o arquivo .txt
    for linha in arquivo: # Para cada linha do arquivo
      if linha.startswith(nome_variavel + ' ='): # Se a linha começa com o nome da variável
        valor = ast.literal_eval(linha.partition('=')[2]) # Obtém o valor da variável
        return valor # Retorna o valor da variável
  return None  # Retorna None se a variável não for encontrada