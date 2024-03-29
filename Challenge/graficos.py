import os
import tkinter as tk
from tkinter import messagebox
from matplotlib import pyplot as plt


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

    # Cria uma janela tkinter invisível
    root = tk.Tk()
    root.withdraw()

    # Pergunta ao usuário se ele deseja abrir o gráfico
    if messagebox.askyesno('Abrir gráfico', f'Deseja abrir o gráfico do arquivo {os.path.basename(arquivo)}?'):
        # Cria uma figura com um tamanho específico
        plt.figure(figsize=(11, 7))

        # Cria um gráfico de barras
        plt.bar(dados.keys(), dados.values())

        plt.xlabel('Dados Sensíveis')
        plt.ylabel('Quantidade Encontrada')
        plt.title(f'Arquivo {os.path.basename(arquivo)}')

        # Exibe o gráfico sem bloquear a execução do código
        plt.show()
        pass
    else:
        # Finaliza a função
        root.destroy()  # Ensure the Tkinter application is properly closed
        return