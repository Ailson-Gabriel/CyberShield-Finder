import os
from processar_imagem import processar as processar_imagem
from processar_texto import processar as processar_texto
from processar_docx import processar as processar_docx
from processar_pdf import processar as processar_pdf

def varrer_diretorio(diretorio):
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        if arquivo.endswith('.jpg') or arquivo.endswith('.jpeg'):
            print("-----------------------------------------------")
            processar_imagem(caminho_arquivo)
            print("\n_______________________________________________")

        elif arquivo.endswith('.txt'):
            print("-----------------------------------------------")
            processar_texto(caminho_arquivo)
            print("\n_______________________________________________")

        elif arquivo.endswith('.docx'):
            print("-----------------------------------------------")
            processar_docx(caminho_arquivo)
            print("\n_______________________________________________")

        elif arquivo.endswith('.pdf'):
            print("-----------------------------------------------")
            processar_pdf(caminho_arquivo)
            print("\n_______________________________________________")

if __name__ == "__main__":
    #diretorio = input(r"Por favor, insira o caminho do diretório: ")
    diretorio = r"C:\Users\Gabriel\Desktop\FIAP - CyberSec\Primeiro_Ano\Nuclea\TESTES" #ALTERAR AQUI O CAMINHO DA PASTA DE TESTE DE VARREDURA
    print("   ____      _               ____  _     _      _     _ ")
    print("  / ___|   _| |__   ___ _ __/ ___|| |__ (_) ___| | __| |")
    print(" | |  | | | | '_ \ / _ \ '__\___ \| '_ \| |/ _ \ |/ _` |")
    print(" | |__| |_| | |_) |  __/ |   ___) | | | | |  __/ | (_| |")
    print("  \____\__, |_.__/ \___|_|  |____/|_| |_|_|\___|_|\__,_|")
    print("       |___/                                            ")
    varrer_diretorio(diretorio)
    