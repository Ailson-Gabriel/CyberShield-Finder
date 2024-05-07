import cv2 # OpenCV - Biblioteca de visão computacional e processamento de imagens e vídeos.
import os # Módulo que fornece funções para interagir com o sistema operacional.
import tkinter as tk # Módulo que fornece funções para criar interfaces gráficas.
from tkinter import messagebox # Módulo que fornece caixas de diálogo para exibir mensagens.
from graficos import grafico # Função que gera gráficos
from print_textbox import print_to_textbox # Função que imprime mensagens em um Textbox
from buscar import encontrar_dados_sensiveis, encontrar_cpf # Função que busca por dados sensiveis
from grava_resultados import grava_lista_em_arquivo # Função que grava os resultados em um arquivo


def varredura(textbox, texto, arquivo):
    '''
    Função que realiza a varredura do texto extraido do arquivo em busca de nomes, CPFs, CNPJs, Etnias e Religiões
        Args:  
            textbox (CTkTextbox): O objeto CTkTextbox onde as mensagens devem ser exibidas.
            texto: Texto extraido do arquivo
            arquivo: Nome do arquivo
        Returns:
            True: Se encontrar dados sensiveis que possa ser associados a algum individuo
            False: Se não encontrar dados sensiveis que possa ser associados a algum individuo
    '''
    print_to_textbox(textbox, "INICIANDO VARREDURA")
    check = busca_por_individuos(textbox, texto, arquivo)
    grava_lista_em_arquivo(os.path.basename(arquivo), check)
    if not check:
        root = tk.Tk()
        root.withdraw() 
        messagebox.showinfo("Varredura concluída", "Nenhum dado sensível que possa ser associado encontrado.")
        root.destroy()
    return check
    
def reconhecimento_facial(textbox, caminho_imagem):
    """
    Processa uma imagem usando OpenCV e busca por Rostos.

    Parâmetros:
        arquivo (str): O caminho para o arquivo de imagem a ser processada.
    Retorna:
        bool: True ou False se encontrou ou não.
    """
    print_to_textbox(textbox, f"BUSCANDO ROSTOS")

    # Carrega o classificador pré-treinado para detecção de faces
    classificador_face = cv2.CascadeClassifier('assets\\haarcascade_frontalface_default.xml')

    imagem = cv2.imread(caminho_imagem) # Carrega a imagem

    # Verifica se a imagem foi carregada corretamente
    if imagem is None:
        print_to_textbox(textbox, f"\tErro: Não foi possível carregar a imagem.")
        return False
    
    # Converte a imagem para escala de cinza
    try:
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    except Exception as e:
        print_to_textbox(textbox, f"Erro na conversão para escala de cinza: {e}")
    
    # Detecta rostos na imagem
    try:
        faces = classificador_face.detectMultiScale(imagem_cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    except Exception as e:
        print_to_textbox(textbox, f"Erro em detectMultiScale: {e}")

    # Retorna True se pelo menos um rosto for detectado
    if len(faces) > 0:
        print_to_textbox(textbox, f"\tROSTO detectado no arquivo {os.path.basename(caminho_imagem)}")
        return True
    else:
        print_to_textbox(textbox, f"\tNenhum ROSTO detectado no arquivo {os.path.basename(caminho_imagem)}")
        return False

def busca_por_individuos(textbox, texto, arquivo):
    """
    Função que busca por individuos no texto extraido do arquivo
    Args:
        textbox: Objeto Textbox onde será impresso o resultado da varredura
        texto: Texto extraido do arquivo
    Returns:
        True: Se encontrar individuos
        False: Se não encontrar individuos
    """

    print_to_textbox(textbox, "BUSCANDO POR NOMES")
    # Busca por nomes no texto
    encontrados_nomes = encontrar_dados_sensiveis(texto, "nomes") # Encontra nomes no texto extraido do arquivo
    if encontrados_nomes:
        print_to_textbox(textbox, f"\tNomes encontrados no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão foram encontrados nomes no arquivo")

    # Busca por CPFs no texto
    print_to_textbox(textbox, "BUSCANDO POR CPF")
    encontrados_cpf = encontrar_cpf(texto) # Encontra CPFs no texto extraido do arquivo
    if encontrados_cpf:
        print_to_textbox(textbox, f"\tCPF encontrado no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrado CPF no arquivo")

    # Se o arquivo for uma imagem, realiza o reconhecimento facial
    encontrados_rostos = False
    if arquivo.endswith('.jpg') or arquivo.endswith('.png') or arquivo.endswith('.jpeg'):
        encontrados_rostos = reconhecimento_facial(textbox, arquivo)

    # Se encontrou nomes, CPFs ou rostos, realiza a busca por dados sensíveis
    if encontrados_nomes or encontrados_cpf or encontrados_rostos:
        if busca_por_dados_sensiveis(textbox, texto, encontrados_nomes, encontrados_cpf, encontrados_rostos, arquivo) or encontrados_rostos:
            return True
    else:
        print_to_textbox(textbox, f"\nNão foram encontrados individuos que possam ser associados a dados sensíveis")
        return False
        

def busca_por_dados_sensiveis(textbox, texto, encontrados_nomes, encontrados_cpf,encontrados_rostos, arquivo):
    """
    Função que busca por dados sensiveis no texto extraido do arquivo
    Args:
        textbox: Objeto Textbox onde será impresso o resultado da varredura
        texto: Texto extraido do arquivo
        encontrados_nomes: Nomes encontrados no texto
        encontrados_cpf: CPFs encontrados no texto
        encontrados_rostos: Rostos encontrados no arquivo
        arquivo: Nome do arquivo
    Returns:
        True: Se encontrar dados sensiveis que possa ser associados a algum individuo
        False: Se não encontrar dados sensiveis que possa ser associados a algum individuo
    """

     # Busca por etnias no texto
    print_to_textbox(textbox, "BUSCANDO POR ETNIAS")
    encontrados_etnias = encontrar_dados_sensiveis(texto, "etnias") # Encontra Etnias no texto extraido do arquivo
    if encontrados_etnias:
        print_to_textbox(textbox, f"\tEtnia encontrada no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrada etnia no arquivo")

     # Busca por religiões no texto
    print_to_textbox(textbox, "BUSCANDO POR RELIGIÕES")
    encontrados_religioes = encontrar_dados_sensiveis(texto, "religiao") # Encontra Religiões no texto extraido do arquivo
    if encontrados_religioes:
        print_to_textbox(textbox, f"\tReligião encontrada no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrada Religião no arquivo")


    # Busca por gênero no texto
    print_to_textbox(textbox, "BUSCANDO POR GENERO")
    encontrados_genero = encontrar_dados_sensiveis(texto, "genero")
    if encontrados_genero:
        print_to_textbox(textbox, f"\tGenero encontrado no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrado Genero no arquivo")

    # Busca por posições políticas no texto
    print_to_textbox(textbox, "BUSCANDO POR POSIÇÕES POLÍTICAS")
    encontrados_politica = encontrar_dados_sensiveis(texto, "politica")
    if encontrados_politica:
        print_to_textbox(textbox, f"\tPosição politica encontrada no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrada Posição politica no arquivo")
    
    # Busca por orientação sexual no texto
    print_to_textbox(textbox, "BUSCANDO POR ORIENTAÇÃO SEXUAL")
    encontrados_orientacao_sexual = encontrar_dados_sensiveis(texto, "orientacao_sexual")
    if encontrados_orientacao_sexual:
        print_to_textbox(textbox, f"\tOrientação sexual encontrada no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrada Orientação sexual no arquivo")

    # Busca por doenças no texto
    print_to_textbox(textbox, "BUSCANDO POR DOENÇAS")
    encontrados_doencas = encontrar_dados_sensiveis(texto, "doencas")
    if encontrados_doencas:
        print_to_textbox(textbox, f"\tDoenças encontradas no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrada Doenças no arquivo")

    # Se encontrou algum dado sensível, gera um gráfico e retorna True
    if (encontrados_etnias or encontrados_religioes or encontrados_genero or 
        encontrados_politica or encontrados_orientacao_sexual or encontrados_doencas or encontrados_rostos):

        grafico(encontrados_nomes, encontrados_cpf, encontrados_rostos, encontrados_etnias, encontrados_religioes, encontrados_genero, 
        encontrados_politica, encontrados_orientacao_sexual, encontrados_doencas, arquivo)

        return True
    else:
        print_to_textbox(textbox, f"\nNão foram encontrados dados sensíveis que possam ser associados a algum individuo")
        return False