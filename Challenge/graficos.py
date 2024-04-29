import os
from matplotlib import pyplot as plt
import matplotlib
from grava_resultados import atualizar_dicionario
matplotlib.use('Qt5Agg')

def grafico(encontrados_nomes, encontrados_cpf, encontrados_rostos, encontrados_etnias, encontrados_religioes, encontrados_genero, 
        encontrados_politica, encontrados_orientacao_sexual, encontrados_doencas ,arquivo):
    
    # Cria um dicionário para armazenar a quantidade de cada tipo de dado sensível encontrado
    dados = {}
    # Atualiza o dicionário com a quantidade de cada tipo de dado sensível encontrado
    dados["Nomes"] = len(encontrados_nomes) if encontrados_nomes else 0
    dados["CPFs"] = len(encontrados_cpf) if encontrados_cpf else 0
    #dados["CNPJs"] = len(encontrados_cnpj) if encontrados_cnpj else 0
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

    plt.xlabel('Dados Sensíveis')
    plt.ylabel('Quantidade Encontrada')
    plt.title(f'Arquivo {os.path.basename(arquivo)}')

    # Verifica se o diretório 'graficos' existe
    if not os.path.exists('graficos'):
        # Se não existir, cria o diretório
        os.makedirs('graficos')
    # Salva o gráfico em um arquivo
    plt.savefig(f'graficos/grafico_{os.path.basename(arquivo)}.png')

    atualizar_dicionario("dados_sensiveis_encontrados", dados)