import os
import re
import pprint
import ast
 
def grava_dados(tabela, dados, qntd):
    """
    Função para gravar os dados encontrados em um arquivo .py
    Cria um Dicionário com os dados encontrados e a quantidade de cada tipo acrescentando os dados no .py
    Args:
        dado: Dado sensível encontrado
        qntd: Quantidade de vezes que o dado foi encontrado
    Returns:
        None
    """
    dados = f'["{dados}", "{qntd}"]\n'
    with open('db\\base.txt', 'a+') as py_file:
        py_file.write("\n")
        py_file.write(f"{tabela} = {dados}\n")
    return None

def inicia_dados():
    """
    Função para iniciar o arquivo .py
    Cria um arquivo .py vazio
    Args:
        None
    Returns:
        None
    """
    if not os.path.isdir('db'):
        os.makedirs('db')

    with open('db\\base.txt', 'w') as py_file:
        pass
    return None

def grava_lista_em_arquivo(string, criptografado):
    """
    Função para gravar uma string em uma lista em um arquivo .py
    Args:
        string: A string a ser gravada
        criptografado: Um booleano que determina em qual lista a string será gravada
    Returns:
        None
    """
    arquivo_nome = 'db\\base.txt'
    if criptografado:
        lista_nome = 'criptografados'
        if string.endswith('.txt'):
            push_dicionario("quantidade_por_tipo", ".txt", 1)
        elif string.endswith('.docx'):
            push_dicionario("quantidade_por_tipo", ".docx", 1)
        elif string.endswith('.jpeg'):
            push_dicionario("quantidade_por_tipo", ".jpeg", 1)
        elif string.endswith('.jpg'):
            push_dicionario("quantidade_por_tipo", ".jpg", 1)
        elif string.endswith('.png'):
            push_dicionario("quantidade_por_tipo", ".png", 1)
        elif string.endswith('.pdf'):
            push_dicionario("quantidade_por_tipo", ".pdf", 1)
        elif string.endswith('.xls'):
            push_dicionario("quantidade_por_tipo", ".xls", 1)
        elif string.endswith('.xlsx'):
            push_dicionario("quantidade_por_tipo", ".xlsx", 1)
        elif string.endswith('.pst'):
            push_dicionario("quantidade_por_tipo", ".pst", 1)
    else:
        lista_nome = 'nao_criptografados'

    # Verifica se o arquivo existe
    if not os.path.exists(arquivo_nome):
        raise FileNotFoundError(f"O arquivo {arquivo_nome} não foi encontrado.")

    # Lê todo o conteúdo do arquivo
    with open(arquivo_nome, 'r') as f:
        conteudo = f.read()

    # Procura pela lista usando regex
    lista_regex = re.compile(rf"({lista_nome} = \[.*?\])", re.DOTALL)
    lista_match = lista_regex.search(conteudo)

    # Se a lista foi encontrada
    if lista_match:
        lista_str = lista_match.group(1)
        # Adiciona a nova string à lista
        nova_lista_str = lista_str[:-1] + f", '{string}']"
    else:
        # Cria uma nova lista com a string
        nova_lista_str = f"{lista_nome} = ['{string}']"

    # Substitui a lista antiga pela nova lista no conteúdo do arquivo
    novo_conteudo = conteudo.replace(lista_str, nova_lista_str) if lista_match else conteudo + '\n' + nova_lista_str

    # Reescreve todo o conteúdo do arquivo
    with open(arquivo_nome, 'w') as f:
        f.write(novo_conteudo)

    return None

def grava_dicionario(nome, dicionario):
    """
    Função para gravar um dicionário em um arquivo .py
    Args:
        nome: O nome do dicionário
        dicionario: O dicionário a ser gravado
    Returns:
        None    
    """
    with open ("db\\base.txt", "a+") as py_file:
        py_file.write(f"{nome} = {{\n")
        # Cria uma lista de strings formatadas
        items = [f'\t"{tipo}": {quantidade}' for tipo, quantidade in dicionario.items()]
        # Combina todas as strings em uma única string, separada por vírgulas
        py_file.write(',\n'.join(items))
        py_file.write("\n}\n")

def atualizar_dicionario(nome_dict, novo_dict):
    caminho_arquivo = "db\\base.txt"
    linhas = []
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    for i, linha in enumerate(linhas):
        if nome_dict in linha:
            dados = eval(linha.split('=')[1].strip())
            for chave, valor in novo_dict.items():
                if chave in dados:
                    dados[chave] += valor
                else:
                    dados[chave] = valor
            linhas[i] = f"{nome_dict} = {str(dados)}\n"
            break
    else:
        linhas.append(f"{nome_dict} = {str(novo_dict)}\n")

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)

def cria_dicionario(nome, chave, valor):
    """
    Função para criar um dicionário vazio em um arquivo .py
    Args:
        None
    Returns:
        None
    """
    with open('db\\base.txt', 'w') as f:
        f.write(f"{nome} = {{\n")
        f.write(f"\t'{chave}': {valor}\n")
        f.write("}\n")
        f.write("\n")
    return None

def push_dicionario(nome, chave, valor):
    """
    Função para adicionar um item a um dicionário em um arquivo .py
    Args:
        nome: O nome do dicionário
        chave: A chave do item a ser adicionado
        valor: O valor do item a ser adicionado
    Returns:
        None
    """
    caminho_arquivo = 'db\\base.txt'
    linhas = []
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    for i, linha in enumerate(linhas):
        if nome in linha:
            dados = eval(linha.split('=')[1].strip())
            if chave in dados:
                novo_dict = {chave: valor}
                atualizar_dicionario(nome, novo_dict)
                return None
            else:
                dados[chave] = valor
                linhas[i] = f"{nome} = " + pprint.pformat(dados, indent=4) + "\n"
                break
    else:
        linhas.append(f"{nome} = {{'{chave}': {valor}}}\n")

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)

    return None

def grava_tabela_de_arquivos(nome_arquivo='db\\base.txt'):
    #from db.base import criptografados, nao_criptografados

    criptografados = load_data_from_txt('db\\base.txt', 'criptografados')
    nao_criptografados = load_data_from_txt('db\\base.txt', 'nao_criptografados')

    tabela_de_arquivos = [[item, 'Sim'] for item in criptografados] + [[item, 'Não'] for item in nao_criptografados]

    with open(nome_arquivo, 'a', encoding='utf-8') as f:
        f.write(f'\ntabela_de_arquivos = {tabela_de_arquivos}\n')


def load_data_from_txt(caminho_arquivo, nome_variavel):
  with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
      if linha.startswith(nome_variavel + ' ='):
        valor = ast.literal_eval(linha.partition('=')[2])
        return valor
  return None  # Retorna None se a variável não for encontrada