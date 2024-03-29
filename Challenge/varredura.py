import cv2
import os
from graficos import grafico
from print_textbox import print_to_textbox
from buscar import encontrar_dados_sensiveis, encontrar_cpf, encontrar_cnpj

def varredura(textbox, texto, arquivo):
    '''
    Função que realiza a varredura do texto extraido do arquivo em busca de nomes, CPFs, CNPJs, Etnias e Religiões
        Args:  
            textbox: Objeto Textbox onde será impresso o resultado da varredura
            texto: Texto extraido do arquivo
            arquivo: Nome do arquivo
        Returns:
            True: Se encontrar individuos
            False: Se não encontrar individuos
    '''
    print_to_textbox(textbox, "\t\t\tINICIANDO VARREDURA")

    return busca_por_individuos(textbox, texto, arquivo)
    
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
    classificador_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    imagem = cv2.imread(caminho_imagem) # Carrega a imagem

    # Verifica se a imagem foi carregada corretamente
    if imagem is None:
        print_to_textbox(textbox, f"Erro: Não foi possível carregar a imagem.")
        return False

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # Converte a imagem para escala de cinza

    # Detecta rostos na imagem
    faces = classificador_face.detectMultiScale(imagem_cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Retorna True se pelo menos um rosto for detectado
    if len(faces) > 0:
        print_to_textbox(textbox, f"\tRosto detectado no arquivo {os.path.basename(caminho_imagem)}")
        return True
    else:
        print_to_textbox(textbox, f"\tNenhum rosto detectado no arquivo {os.path.basename(caminho_imagem)}")
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
    encontrados_nomes = encontrar_dados_sensiveis(texto, "nomes") # Encontra nomes no texto extraido do arquivo
    if encontrados_nomes:
        print_to_textbox(textbox, f"\tNomes encontrados no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão foram encontrados nomes no arquivo")

    print_to_textbox(textbox, "BUSCANDO POR CPF")
    encontrados_cpf = encontrar_cpf(texto) # Encontra CPFs no texto extraido do arquivo
    if encontrados_cpf:
        print_to_textbox(textbox, f"\tCPF encontrado no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrado CPF no arquivo")

    print_to_textbox(textbox, "BUSCANDO POR CNPJ")
    encontrados_cnpj = encontrar_cnpj(texto) # Encontra CNPJs no texto extraido do arquivo
    if encontrados_cnpj:
        print_to_textbox(textbox, f"\tCNPJ encontrado no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrado CNPJ no arquivo")

    if arquivo.endswith('.jpg') or arquivo.endswith('.png') or arquivo.endswith('.jpeg'):
        encontrados_rostos = reconhecimento_facial(textbox, arquivo)
    else:
        encontrados_rostos = False

    if encontrados_nomes or encontrados_cpf or encontrados_cnpj or encontrados_rostos:
        verificador = busca_por_dados_sensiveis(textbox, texto, encontrados_nomes, encontrados_cpf, 
                                     encontrados_cnpj, encontrados_rostos, arquivo)
        if not verificador and encontrados_rostos:
            print_to_textbox(textbox, "Mas foram encontrados rostos no arquivo.")
            return True
        elif verificador:
            return True
        else:
            return False
    else:
        print_to_textbox(textbox, f"\nNão foram encontrados individuos que possam ser associados a dados sensíveis")
        return False
        
def busca_por_dados_sensiveis(textbox, texto, encontrados_nomes, encontrados_cpf, encontrados_cnpj, encontrados_rostos, arquivo):
    
    print_to_textbox(textbox, "BUSCANDO POR ETNIAS")
    encontrados_etnias = encontrar_dados_sensiveis(texto, "etnias") # Encontra Etnias no texto extraido do arquivo
    if encontrados_etnias:
        print_to_textbox(textbox, f"\tEtnia encontrada no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrada etnia no arquivo")

    print_to_textbox(textbox, "BUSCANDO POR RELIGIÕES")
    encontrados_religioes = encontrar_dados_sensiveis(texto, "religiao") # Encontra Religiões no texto extraido do arquivo
    if encontrados_religioes:
        print_to_textbox(textbox, f"\tReligião encontrada no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrada Religião no arquivo")

    print_to_textbox(textbox, "BUSCANDO POR GENERO")
    encontrados_genero = encontrar_dados_sensiveis(texto, "genero")
    if encontrados_genero:
        print_to_textbox(textbox, f"\tGenero encontrado no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrado Genero no arquivo")

    print_to_textbox(textbox, "BUSCANDO POR POSIÇÕES POLÍTICAS")
    encontrados_politica = encontrar_dados_sensiveis(texto, "politica")
    if encontrados_politica:
        print_to_textbox(textbox, f"\tPosição politica encontrada no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrada Posição politica no arquivo")
    
    print_to_textbox(textbox, "BUSCANDO POR ORIENTAÇÃO SEXUAL")
    encontrados_orientacao_sexual = encontrar_dados_sensiveis(texto, "orientacao_sexual")
    if encontrados_orientacao_sexual:
        print_to_textbox(textbox, f"\tOrientação sexual encontrada no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrada Orientação sexual no arquivo")

    if encontrados_etnias or encontrados_religioes or encontrados_genero or encontrados_politica or encontrados_orientacao_sexual:
        grafico(encontrados_nomes, encontrados_cpf, encontrados_cnpj, encontrados_rostos, encontrados_etnias, encontrados_religioes, encontrados_genero, encontrados_politica, encontrados_orientacao_sexual, arquivo)
        return True
    else:
        print_to_textbox(textbox, f"\nNão foram encontrados dados sensíveis que possam ser associados aos individuos encontrados.")
        return False