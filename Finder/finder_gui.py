import os # Módulo que fornece funções para interagir com o sistema operacional
import customtkinter #  Biblioteca para criar interfaces gráficas
from tkinter import filedialog, messagebox # Módulo que fornece caixas de diálogo para abrir e salvar arquivos
from PIL import Image # Módulo para abrir, manipular e salvar imagens
import subprocess # Módulo para criar processos, iniciar programas e comandos
from grava_resultados import inicia_dados # Função que inicializa o dicionário de resultados
from controller import varrer_diretorio # Função que varre um diretório em busca de arquivos
from print_textbox import print_to_textbox # Função que imprime mensagens em um Textbox

customtkinter.set_appearance_mode("System")  # Modos: "System" (Padrão), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Temas: "blue" (Padrão), "green", "dark-blue"

class App(customtkinter.CTk): # Classe principal da aplicação
    def __init__(self): # Método construtor
        super().__init__() # Chama o método construtor da classe pai
        # Configurações da janela principal
        self.title("CyberShield Finder")
        self.geometry(f"{1100}x{580}")

        # Configuração do layout da janela principal
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Cria um frame para a barra lateral
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Cria um frame para o logo
        self.logo_image = customtkinter.CTkImage(Image.open("assets\\CyberShieldLOGO.png"), size=(200, 200))

        # Cria um label para o logo
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, image=self.logo_image, text="Finder" ,compound="top", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=5, pady=0)

        # Cria um botão para selecionar diretório
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Selecionar diretório", command=self.selecionar_diretorio)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        # Cria um botão para iniciar a varredura
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Iniciar varredura", command=self.iniciar_varredura)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        # Cria um botão para criar o dashboard
        self.botao_dashboard = customtkinter.CTkButton(self.sidebar_frame, text="Criar Dashboard", command=self.criar_dashboard)
        self.botao_dashboard.grid(row=3, column=0, padx=20, pady=10)
        self.botao_dashboard.grid_remove()  # torna o botão inicialmente invisível

        # Cria um campo de entrada de usuário para informar o caminho do diretório
        self.entry = customtkinter.CTkEntry(self, placeholder_text="")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Cria um TextBox para exibir o resultado da varredura
        self.textbox = customtkinter.CTkTextbox(self,width=250, state="disabled")
        self.textbox.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # Cria um botão para alterar o modo de aparência
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["System", "Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        # Cria um botão para alterar a escalabilidade da interface
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Defina o valor inicial após a criação do CTkOptionMenu
        self.scaling_optionemenu.set("100%")

    def change_appearance_mode_event(self, new_appearance_mode: str): # Método para alterar o modo de aparência
        customtkinter.set_appearance_mode(new_appearance_mode) # Altera o modo de aparência

    def change_scaling_event(self, new_scaling: str): # Método para alterar a escalabilidade da interface
        new_scaling_float = int(new_scaling.replace("%", "")) / 100 # Converte a string para um valor flutuante
        customtkinter.set_widget_scaling(new_scaling_float) # Altera a escalabilidade da interface

    def selecionar_diretorio(self):
        directory = filedialog.askdirectory()
        if directory:  # Verifique se um diretório foi selecionado
            self.limpar_textbox()  # Limpa o TextBox
            self.entry.delete(0, 'end')  # Limpa a entrada atual
            self.entry.insert(0, directory)  # Insere o diretório selecionado na entrada
            self.textbox.delete('1.0', 'end')  # Limpa o TextBox
            print_to_textbox(self.textbox, f"Selecionado diretório: {directory}")

    def limpar_textbox(self): # Método para limpar o TextBox
        self.textbox.configure(state='normal') # Habilita a edição do TextBox
        self.textbox.delete('1.0', 'end')  # Limpa o TextBox
        self.textbox.configure(state='disabled') # Desabilita a edição do TextBox

    def iniciar_varredura(self): # Método para iniciar a varredura
        directory = self.entry.get() # Obtém o diretório inserido pelo usuário
        if not directory:  # Verifique se um diretório foi selecionado
            # Mostre uma mensagem de erro e retorne
            messagebox.showerror("Erro", "Por favor, selecione um diretório antes de iniciar a varredura.")
            return
        self.limpar_textbox() # Limpa o TextBox
        inicia_dados() # Inicializa o dicionário de resultados
        varrer_diretorio(self.entry.get(), self.textbox) # Varre o diretório em busca de arquivos
        self.entry.delete(0, 'end')  # Limpa a entrada atual
        self.botao_dashboard.grid() # Torna o botão de criação do dashboard visível
        self.criar_botoes_graficos() # Cria os botões para visualizar os gráficos

    def criar_botoes_graficos(self): # Método para criar os botões para visualizar os gráficos
        # Obtém a lista de arquivos .png no diretório "graficos"
        arquivos_png = [arq for arq in os.listdir("graficos") if arq.endswith(".png")]

        # Cria um frame para os botões
        self.frame_botoes = customtkinter.CTkFrame(self)
        self.frame_botoes.grid(row=2, column=1, padx=(20, 20), pady=(10, 0), sticky="nsew")

        # Cria um botão para cada arquivo .png
        j = 0  # Coluna atual
        for i, arquivo in enumerate(arquivos_png): # Repete sobre a lista de arquivos .png
            if i % 4 == 0 and i > 0:  # Verifica se é o início de uma nova coluna
                j += 1 # Incrementa a coluna
            nome_arquivo_sem_extensao, _ = os.path.splitext(arquivo) # Separa o nome do arquivo da extensão
            nome_botao = nome_arquivo_sem_extensao[8:]  # Obtém a string a partir do 8º caractere (após "grafico_")
            botao = customtkinter.CTkButton(self.frame_botoes, text=nome_botao, command=lambda a=arquivo: self.visualizar_grafico(a))
            botao.grid(row=i % 4, column=j, padx=5, pady=5)  # Usa i % 3 para reiniciar a linha a cada 3 botões

    def visualizar_grafico(self, nome_arquivo): # Método para visualizar um gráfico
        imagem = Image.open(os.path.join("graficos", nome_arquivo)) # Abre a imagem
        imagem.show() # Mostra a imagem

    def criar_dashboard(self): # Método para criar o dashboard
        subprocess.Popen(["FinderDash.exe"], shell=True) # Abre o dashboard

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    app = App() # Cria uma instância da classe App
    app.mainloop() # Inicia o loop principal da aplicação
