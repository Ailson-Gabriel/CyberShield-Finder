import os # Módulo que fornece funções para interagir com o sistema operacional
from matplotlib import pyplot as plt # Módulo para criar gráficos
import matplotlib # Módulo para criar gráficos
from grava_resultados import atualizar_dicionario # Função que atualiza o dicionário de resultados
matplotlib.use('Qt5Agg') # Define o backend do matplotlib para Qt5Agg

def grafico(encontrados_nomes, encontrados_cpf, encontrados_rostos, encontrados_etnias, encontrados_religioes, encontrados_genero, 
        encontrados_politica, encontrados_orientacao_sexual, encontrados_doencas ,arquivo):
    """
    Cria um gráfico de barras com a quantidade de cada tipo de dado sensível encontrado.
    Argumentos:
        encontrados_nomes (list): Lista de nomes encontrados no arquivo.
        encontrados_cpf (list): Lista de CPFs encontrados no arquivo.
        encontrados_rostos (list): Lista de rostos encontrados no arquivo.
        encontrados_etnias (list): Lista de etnias encontradas no arquivo.
        encontrados_religioes (list): Lista de religiões encontradas no arquivo.
        encontrados_genero (list): Lista de gêneros encontrados no arquivo.
        encontrados_politica (list): Lista de visões políticas encontradas no arquivo.
        encontrados_orientacao_sexual (list): Lista de orientações sexuais encontradas no arquivo.
        encontrados_doencas (list): Lista de doenças encontradas no arquivo.
        arquivo (str): O caminho para o arquivo processado.
    """
    dados = {} # Cria um dicionário para armazenar a quantidade de cada tipo de dado sensível encontrado
    # Atualiza o dicionário com a quantidade de cada tipo de dado sensível encontrado
    dados["Nomes"] = len(encontrados_nomes) if encontrados_nomes else 0
    dados["CPFs"] = len(encontrados_cpf) if encontrados_cpf else 0
    dados["Rostos"] = 1 if encontrados_rostos else 0
    dados["Etnias"] = len(encontrados_etnias) if encontrados_etnias else 0
    dados["Religioes"] = len(encontrados_religioes) if encontrados_religioes else 0
    dados["Genero"] = len(encontrados_genero) if encontrados_genero else 0
    dados["Visao_politica"] = len(encontrados_politica) if encontrados_politica else 0
    dados["Sexualidade"] = len(encontrados_orientacao_sexual) if encontrados_orientacao_sexual else 0
    dados["Doencas"] = len(encontrados_doencas) if encontrados_doencas else 0

    # Cria uma figura com um tamanho específico
    plt.figure(figsize=(12, 7))

    # Cria um gráfico de barras
    plt.bar(dados.keys(), dados.values())

    plt.xlabel('Dados Sensíveis') # Adiciona rótulo ao eixo x
    plt.ylabel('Quantidade Encontrada') # Adiciona rótulo ao eixo y
    plt.title(f'Arquivo {os.path.basename(arquivo)}') # Adiciona título ao gráfico

    # Verifica se o diretório 'graficos' existe
    if not os.path.exists('graficos'):
        # Se não existir, cria o diretório
        os.makedirs('graficos')
    # Salva o gráfico em um arquivo
    plt.savefig(f'graficos/grafico_{os.path.basename(arquivo)}.png')

    atualizar_dicionario("dados_sensiveis_encontrados", dados) # Atualiza o dicionário com a quantidade de cada tipo de dado sensível encontrado