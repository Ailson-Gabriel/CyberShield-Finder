import os
from processar_imagem import processar as processar_imagem
from processar_texto import processar as processar_texto
from processar_docx import processar as processar_docx
from processar_pdf import processar as processar_pdf
from processar_excel import processar as processar_excel
import tkinter as tk
from tkinter import filedialog
import customtkinter

def varrer_diretorio(diretorio):

    for arquivo in os.listdir(diretorio):
        if os.path.isdir(os.path.join(diretorio, arquivo)):  # Se for um diretório
            print("----------------------------------------------------------------------------------------------------------")
            print(f"\nACESSANDO SUBDIRETÓRIO {os.path.join(diretorio, arquivo)}\n")
            varrer_diretorio(os.path.join(diretorio, arquivo))

        elif arquivo.endswith('.jpg') or arquivo.endswith('.jpeg') or arquivo.endswith('.png'):
            print("----------------------------------------------------------------------------------------------------------")
            processar_imagem(os.path.join(diretorio, arquivo))

        elif arquivo.endswith('.txt'):
            print("----------------------------------------------------------------------------------------------------------")
            processar_texto(os.path.join(diretorio, arquivo))

        elif arquivo.endswith('.docx'):
            print("----------------------------------------------------------------------------------------------------------")
            processar_docx(os.path.join(diretorio, arquivo))

        elif arquivo.endswith('.pdf'):
            print("----------------------------------------------------------------------------------------------------------")
            processar_pdf(os.path.join(diretorio, arquivo))

        elif arquivo.endswith('.xls') or arquivo.endswith('.xlsx'):
            print("----------------------------------------------------------------------------------------------------------")
            processar_excel(os.path.join(diretorio, arquivo))


if __name__ == "__main__":
    #diretorio = input(r"Por favor, insira o caminho do diretório: ")
    janela = customtkinter.CTk()  # janela principal
    janela.title('CyberShield Finder')  # Nome do titulo 'Ferramenta'
    janela.geometry('500x280')  # tamanho da janela
    caminho_pasta = None

def abrir_caminho_pasta():
    global caminho_pasta, label3
    root = tk.Tk()
    root.withdraw()
    caminho_pasta = filedialog.askdirectory()  # função para abrir o Windows explorer e apenas pasta
    if label3 is not None:
        label3.destroy()
    label3 = customtkinter.CTkLabel(janela, text=f'{caminho_pasta}')
    label3.pack(pady=22)
    root.destroy()



#Funcao do botao Procurar
def comecar_procura():
    global label, label2

    if caminho_pasta is not None and os.path.exists(caminho_pasta):
        ## verifica se o caminho_pasta realmente existe se nao existir ele executa o ELSE
        if label is not None:
            label.destroy()
        label = customtkinter.CTkLabel(janela, text="Procurando por dados sensiveis")
        label.pack(pady=22)  # arrumar para pois se testar 2 vezes ele nao apaga e corrige o outro
        janela.destroy()
        varrer_diretorio(caminho_pasta)  # Colocando o varrer_diretorio(caminho_pasta) pela funcao do botao Procurar
    else:
        if label2 is not None:
            label2.destroy()
        label2 = customtkinter.CTkLabel(janela, text='Por favor, selecione a pasta Primeiro')
        label2.pack(pady=22)


#Criar TEXTO para encaixar os resultados
#texto_resultados = Text(janela, height=20, width=60) #tamanho do resultado no text
#texto_resultados.pack(pady=20) #tamanho do text na janela
#texto_resultados.insert(tk.END, output_text)


#Botao Selecione a pasta
selecione_pasta = customtkinter.CTkButton(janela, text='Selecione a Pasta', command=abrir_caminho_pasta)
selecione_pasta.pack(pady=20)  # configura o botao


#Botao Procurar
iniciar_botao = customtkinter.CTkButton(janela, text='Procurar', command=comecar_procura)
iniciar_botao.pack(pady=20)  # espacos entre o botao


label = None           #Declarar vazio para nao spamar a mensagem
label2 = None          #Declarar vazio para nao spamar a mensage
label3 = None          #Declarar vazio para nao spamar a mensage

janela.mainloop()  # mantém a janela sem fechar