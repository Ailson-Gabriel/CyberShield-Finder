import os
from processar_imagem import processar as processar_imagem
from processar_texto import processar as processar_texto
from processar_docx import processar as processar_docx
from processar_pdf import processar as processar_pdf
from processar_excel import processar as processar_excel

def varrer_diretorio(diretorio):
    for arquivo in os.listdir(diretorio):

        if os.path.isdir(os.path.join(diretorio, arquivo)):  # Se for um diretório
            print("-----------------------------------------------")
            print("-----------------------------------------------")
            print(f"Entrando no diretório: {arquivo}")
            varrer_diretorio(os.path.join(diretorio, arquivo))  # Chama a função de varredura novamente para o subdiretório
        else:
            if arquivo.endswith('.jpg') or arquivo.endswith('.jpeg') or arquivo.endswith('.png'):
                print("-----------------------------------------------")
                processar_imagem(os.path.join(diretorio, arquivo))
                print("\n_______________________________________________")
            
            elif arquivo.endswith('.txt'):
                print("-----------------------------------------------")
                processar_texto(os.path.join(diretorio, arquivo))
                print("\n_______________________________________________")
      
            elif arquivo.endswith('.docx'):
                print("-----------------------------------------------")
                processar_docx(os.path.join(diretorio, arquivo))
                print("\n_______________________________________________")
    
            elif arquivo.endswith('.pdf'):
                print("-----------------------------------------------")
                processar_pdf(os.path.join(diretorio, arquivo))
                print("\n_______________________________________________")
            
            elif arquivo.endswith('.xls') or arquivo.endswith('.xlsx'):
                print("-----------------------------------------------")
                processar_excel(os.path.join(diretorio, arquivo))
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
    
