import os
from matplotlib import pyplot as plt
import ctypes
import matplotlib
matplotlib.use('Qt5Agg')

def grafico(encontrados_nomes, encontrados_cpf, encontrados_cnpj, encontrados_rostos, encontrados_etnias, encontrados_religioes, encontrados_genero, 
        encontrados_politica, encontrados_orientacao_sexual, arquivo):
    
    # Cria um dicionário para armazenar a quantidade de cada tipo de dado sensível encontrado
    dados = {}
    # Atualiza o dicionário com a quantidade de cada tipo de dado sensível encontrado
    dados["Nomes"] = len(encontrados_nomes) if encontrados_nomes else 0
    dados["CPFs"] = len(encontrados_cpf) if encontrados_cpf else 0
    dados["CNPJs"] = len(encontrados_cnpj) if encontrados_cnpj else 0
    dados["Rostos"] = 1 if encontrados_rostos else 0
    dados["Etnias"] = len(encontrados_etnias) if encontrados_etnias else 0
    dados["Religiões"] = len(encontrados_religioes) if encontrados_religioes else 0
    dados["Gênero"] = len(encontrados_genero) if encontrados_genero else 0
    dados["Ideologia\npolítica"] = len(encontrados_politica) if encontrados_politica else 0
    dados["Sexualidade"] = len(encontrados_orientacao_sexual) if encontrados_orientacao_sexual else 0

    # Cria uma figura com um tamanho específico
    plt.figure(figsize=(11, 7))

    # Cria um gráfico de barras
    plt.bar(dados.keys(), dados.values())

    plt.xlabel('Dados Sensíveis')
    plt.ylabel('Quantidade Encontrada')
    plt.title(f'Arquivo {os.path.basename(arquivo)}')

    # Salva o gráfico em um arquivo
    plt.savefig(f'graficos/grafico_{os.path.basename(arquivo)}.png')
    plt.savefig(f'graficos/grafico_{os.path.basename(arquivo)}.svg')

    # Cria uma caixa de mensagem
    MessageBox = ctypes.windll.user32.MessageBoxW
    result = MessageBox(None, 'Deseja abrir o gráfico do arquivo {}?'.format(os.path.basename(arquivo)), 'Abrir gráfico', 4)

    # Se o usuário clicar em 'OK', exibe o gráfico
    if result == 6:
        plt.show()
