import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import tkinter
from PIL import Image

# Função para descriptografar um arquivo criptografado
def descriptografar_arquivo(caminho_arquivo_chave, nome_arquivo_criptografado, nome_arquivo_descriptografado):
    with open(nome_arquivo_criptografado, 'rb') as arquivo:
        dados_criptografados = arquivo.read()

    with open(caminho_arquivo_chave, 'rb') as arquivo:
        chave = arquivo.read()

    fernet = Fernet(chave)
    dados_descriptografados = fernet.decrypt(dados_criptografados)

    with open(nome_arquivo_descriptografado, 'wb') as arquivo:
        arquivo.write(dados_descriptografados)

# Função para descriptografar arquivos em um diretório especificado
def descriptografar_arquivos_em_diretorio(diretorio):
    for arquivo in os.listdir(diretorio):
        if os.path.isdir(os.path.join(diretorio, arquivo)):
            descriptografar_arquivos_em_diretorio(os.path.join(diretorio, arquivo))
        else:
            if arquivo.endswith('.criptografado'):
                caminho_arquivo_criptografado = os.path.join(diretorio, arquivo)
                caminho_arquivo_original = caminho_arquivo_criptografado[:-len('.criptografado')]
                caminho_arquivo_chave = caminho_arquivo_original + '_chave'

                descriptografar_arquivo(caminho_arquivo_chave, caminho_arquivo_criptografado, caminho_arquivo_original)
                os.remove(caminho_arquivo_criptografado)
                os.remove(caminho_arquivo_chave)

def descriptografar_arquivo_por_caminho(caminho_arquivo, caminho_chave):
    if os.path.exists(caminho_arquivo):
        if caminho_arquivo.endswith('.criptografado'):
            if os.path.exists(caminho_chave):
                descriptografar_arquivo(caminho_chave, caminho_arquivo, caminho_arquivo[:-len('.criptografado')])
                os.remove(caminho_arquivo)
                os.remove(caminho_chave)
                return True
            else:
                print('Arquivo de chave não encontrado.')
        else:
            print('O arquivo não é um arquivo criptografado.')
    else:
        print('Arquivo não encontrado.')
    return False

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('CyberShield Finder_Decrypter')
        self.geometry('300x400')
        self.resizable(False, False)

        self.caminho_pasta = None
        self.label = None
        self.label2 = None
        self.label3 = None
        self.caminho_arquivo = None
        self.caminho_chave = None

        # Carrega a imagem do logo
        self.logo_image = ctk.CTkImage(Image.open("assets\\descriptografia.ico"), size=(200, 200))
        # Cria um label com a imagem do logo e adiciona à interface gráfica
        self.logo_label = ctk.CTkLabel(self, image=self.logo_image, text="Finder Decrypter", compound="top", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack()

        self.opcao1 = ctk.CTkButton(self, text='Diretório', command=self.mostrar_botoes)
        self.opcao1.pack(pady=20)

        self.opcao2 = ctk.CTkButton(self, text='Arquivo', command=self.mostrar_botoes_opcao2)
        self.opcao2.pack(pady=20)

        self.voltar_botao = ctk.CTkButton(self, text='Voltar', command=self.voltar)
        self.voltar_botao.pack(pady=20)
        self.voltar_botao.pack_forget()

        self.selecione_pasta = ctk.CTkButton(self, text='Selecione o diretório', command=self.abrir_caminho_pasta)
        self.selecione_pasta.pack(pady=20)
        self.selecione_pasta.pack_forget()

        self.iniciar_botao = ctk.CTkButton(self, text='Descriptografar', command=self.comecar_procura)
        self.iniciar_botao.pack(pady=20)
        self.iniciar_botao.pack_forget()

        self.selecione_arquivo = ctk.CTkButton(self, text='Selecione o Arquivo', command=self.abrir_caminho_arquivo)
        self.selecione_arquivo.pack(pady=20)
        self.selecione_arquivo.pack_forget()

        self.selecione_chave = ctk.CTkButton(self, text='Selecione a Chave', command=self.abrir_caminho_chave)
        self.selecione_chave.pack(pady=20)
        self.selecione_chave.pack_forget()

        self.descriptografar_botao = ctk.CTkButton(self, text='Descriptografar', command=self.descriptografar_arquivo)
        self.descriptografar_botao.pack(pady=20)
        self.descriptografar_botao.pack_forget()

        self.entry = ctk.CTkEntry(self, placeholder_text="", width=220, justify=tkinter.CENTER)
        #self.entry.pack(fill=tkinter.BOTH, padx=10, pady=10)
        self.entry.pack_forget()

        self.entry_chave = ctk.CTkEntry(self, placeholder_text="", width=220, justify=tkinter.CENTER)
        #self.entry_chave.pack(fill=tkinter.BOTH, padx=10, pady=10)
        self.entry_chave.pack_forget()

    def mostrar_botoes(self):
        self.opcao1.pack_forget()
        self.opcao2.pack_forget()

        self.selecione_pasta.pack(pady=20)
        self.entry.pack(side='top')

        self.iniciar_botao.pack(pady=20)
        self.voltar_botao.pack(side='bottom', pady=20)
        self.geometry('300x475')

    def voltar(self):
        self.geometry('300x375')
        self.selecione_pasta.pack_forget()
        self.iniciar_botao.pack_forget()
        self.selecione_arquivo.pack_forget()
        self.selecione_chave.pack_forget()
        self.voltar_botao.pack_forget()
        self.descriptografar_botao.pack_forget()
        self.opcao1.pack(pady=20)
        self.opcao2.pack(pady=20)
        self.entry.delete(0, 'end')
        self.entry.pack_forget()
        self.entry_chave.pack_forget()
        if self.label2 is not None:
            self.label2.destroy()
        if self.label3 is not None:
            self.label3.destroy()

    def abrir_caminho_pasta(self):
        self.caminho_pasta = filedialog.askdirectory()
        self.entry.delete(0, 'end')  # Limpa o valor atual do CTkEntry
        self.entry.insert(0, os.path.basename(self.caminho_pasta))  # Insere o nome do diretório no CTkEntry

    def comecar_procura(self):
        if self.caminho_pasta is not None and os.path.exists(self.caminho_pasta):
            if self.label is not None:
                self.label.destroy()
            self.label = ctk.CTkLabel(self, text="Procurando por dados sensiveis")
            self.label.pack(pady=22)
            self.destroy()
            descriptografar_arquivos_em_diretorio(self.caminho_pasta)
        else:
            if self.label2 is not None:
                self.label2.destroy()
            self.label2 = ctk.CTkLabel(self, text='Por favor, selecione a pasta Primeiro')
            self.label2.pack(pady=22)

    def mostrar_botoes_opcao2(self):
        self.opcao1.pack_forget()
        self.opcao2.pack_forget()

        self.selecione_arquivo.pack(pady=10)
        self.entry.pack(side='top')

        self.selecione_chave.pack(pady=10)
        self.entry_chave.pack(side='top')

        self.descriptografar_botao.pack(pady=40)
        self.voltar_botao.pack(side='bottom', pady=20)
        self.geometry('300x570')

    def abrir_caminho_arquivo(self):
        self.caminho_arquivo = filedialog.askopenfilename()
        self.entry.delete(0, 'end')
        self.entry.insert(0, os.path.basename(self.caminho_arquivo))

    def abrir_caminho_chave(self):
        self.caminho_chave = filedialog.askopenfilename()
        self.entry_chave.delete(0, 'end')
        self.entry_chave.insert(0, os.path.basename(self.caminho_chave))

    def descriptografar_arquivo(self):
        if self.caminho_arquivo and self.caminho_chave:
            descriptografar_arquivo_por_caminho(self.caminho_arquivo, self.caminho_chave)

if __name__ == "__main__":
    app = App()
    app.mainloop()
