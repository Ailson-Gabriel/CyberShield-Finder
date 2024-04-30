import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog
import customtkinter

# Função para descriptografar um arquivo criptografado
def descriptografar_arquivo(caminho_arquivo_chave, nome_arquivo_criptografado, nome_arquivo_descriptografado):
    # Abre o arquivo criptografado no modo de leitura binária ('rb') e lê os dados criptografados
    with open(nome_arquivo_criptografado, 'rb') as arquivo:
        dados_criptografados = arquivo.read()

    # Abre o arquivo da chave no modo de leitura binária ('rb') e lê a chave de criptografia
    with open(caminho_arquivo_chave, 'rb') as arquivo:
        chave = arquivo.read()

    fernet = Fernet(chave) # Cria uma instância da classe Fernet usando a chave fornecida
    dados_descriptografados = fernet.decrypt(dados_criptografados) # Descriptografa os dados criptografados usando a chave

    # Abre o arquivo especificado no modo de escrita binária ('wb') e escreve os dados descriptografados
    with open(nome_arquivo_descriptografado, 'wb') as arquivo:
        arquivo.write(dados_descriptografados)

# Função para descriptografar arquivos em um diretório especificado
def descriptografar_arquivos_em_diretorio(diretorio):
    for arquivo in os.listdir(diretorio): # Repete para os arquivos no diretório

        if os.path.isdir(os.path.join(diretorio, arquivo)):  # Se for um diretório
            descriptografar_arquivos_em_diretorio(os.path.join(diretorio, arquivo))  # Chama a função de varredura novamente para o subdiretório
        else:
            if arquivo.endswith('.criptografado'): # Verifica se o arquivo tem a extensão ".criptografado"
                caminho_arquivo_criptografado = os.path.join(diretorio, arquivo) # Obtém o caminho completo do arquivo criptografado
                caminho_arquivo_original = caminho_arquivo_criptografado[:-len('.criptografado')] # Remove a extensão ".criptografado" para obter o caminho do arquivo original
                caminho_arquivo_chave = caminho_arquivo_original + '_chave' # Obtém o caminho do arquivo da chave correspondente
                
                # Descriptografa o arquivo criptografado e salva o arquivo descriptografado
                descriptografar_arquivo(caminho_arquivo_chave, caminho_arquivo_criptografado, caminho_arquivo_original) 
                
                # Remove os arquivos criptografado e de chave após a descriptografia
                os.remove(caminho_arquivo_criptografado)
                os.remove(caminho_arquivo_chave)

def descriptografar_arquivo_por_caminho(caminho_arquivo, caminho_chave):
    # Verifica se o arquivo existe
    if os.path.exists(caminho_arquivo):
        # Verifica se o arquivo é um arquivo criptografado
        if caminho_arquivo.endswith('.criptografado'):
            # Verifica se o arquivo da chave existe
            if os.path.exists(caminho_chave):
                # Descriptografa o arquivo
                descriptografar_arquivo(caminho_chave, caminho_arquivo, caminho_arquivo[:-len('.criptografado')])
                return True
            else:
                print('Arquivo de chave não encontrado.')
        else:
            print('O arquivo não é um arquivo criptografado.')
    else:
        print('Arquivo não encontrado.')
    return False

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
        descriptografar_arquivos_em_diretorio(caminho_pasta)  # Colocando o varrer_diretorio(caminho_pasta) pela funcao do botao Procurar
    else:
        if label2 is not None:
            label2.destroy()
        label2 = customtkinter.CTkLabel(janela, text='Por favor, selecione a pasta Primeiro')
        label2.pack(pady=22)

#Botao Selecione a pasta
selecione_pasta = customtkinter.CTkButton(janela, text='Selecione a Pasta', command=abrir_caminho_pasta)
selecione_pasta.pack(pady=20)  # configura o botao


#Botao Procurar
iniciar_botao = customtkinter.CTkButton(janela, text='Descriptografar', command=comecar_procura)
iniciar_botao.pack(pady=20)  # espacos entre o botao

label = None           #Declara vazio para nao spamar a mensagem
label2 = None          #Declara vazio para nao spamar a mensagem
label3 = None          #Declara vazio para nao spamar a mensagem

janela.mainloop()  # mantém a janela sem fechar