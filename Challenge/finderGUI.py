import os
import customtkinter
from tkinter import filedialog, messagebox
from PIL import Image
from controller import varrer_diretorio
from print_textbox import print_to_textbox

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CyberShield Finder")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # load logo image
        self.logo_image = customtkinter.CTkImage(Image.open("CyberShieldLOGO.png"), size=(200, 200))

        # create logo label with image
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, image=self.logo_image, text="Finder" ,compound="top", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=5, pady=0)

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Selecionar diretório", command=self.selecionar_diretorio)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Iniciar varredura", command=self.iniciar_varredura)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.botao_dashboard = customtkinter.CTkButton(self.sidebar_frame, text="Criar Dashboard", command=self.criar_dashboard)
        self.botao_dashboard.grid(row=3, column=0, padx=20, pady=10)
        self.botao_dashboard.grid_remove()  # torna o botão inicialmente invisível

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # create TEXTBOX
        self.textbox = customtkinter.CTkTextbox(self,width=250, state="disabled")
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["System", "Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Defina o valor inicial após a criação do CTkOptionMenu
        self.scaling_optionemenu.set("100%")
   
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def selecionar_diretorio(self):
        # Open the file dialog to select a directory
        directory = filedialog.askdirectory()
        if directory:  # Verifique se um diretório foi selecionado
            self.limpar_textbox()  # Clear the textbox
            self.entry.delete(0, 'end')  # Clear the current entry
            self.entry.insert(0, directory)  # Insert the selected
            self.textbox.delete('1.0', 'end')  # Clear the textbox
            print_to_textbox(self.textbox, f"Selecionado diretório: {directory}")

    def limpar_textbox(self):
        self.textbox.configure(state='normal')
        self.textbox.delete('1.0', 'end')  # Clear the textbox
        self.textbox.configure(state='disabled')

    def iniciar_varredura(self):
        directory = self.entry.get()
        if not directory:  # Verifique se um diretório foi selecionado
            # Mostre uma mensagem de erro e retorne
            messagebox.showerror("Erro", "Por favor, selecione um diretório antes de iniciar a varredura.")
            return
        self.limpar_textbox()
        # Chame a função varrer_diretorio do main.py
        varrer_diretorio(self.entry.get(), self.textbox)
        self.entry.delete(0, 'end')  # Clear the current entry
        self.botao_dashboard.grid()

    def criar_dashboard(self):
        # Lista todos os arquivos no diretório 'graficos' que começam com 'grafico_' e terminam com '.png'
        #graficos = [os.path.join('graficos', nome) for nome in os.listdir('graficos') if nome.startswith('grafico_') and nome.endswith('.png')]

        # Cria e executa o dashboard
        #dashboard = Dashboard(graficos)
        #dashboard.mainloop()
        print("CRIAR DASHBOARD")

    '''
    class Dashboard(Tk):
        def __init__(self, graficos):
            super().__init__()

            # Carrega as imagens dos gráficos
            self.images = [Image.open(grafico) for grafico in graficos]
            self.graficos = [ImageTk.PhotoImage(image) for image in self.images]

            # Cria labels para exibir as imagens
            self.labels = [Label(self, image=grafico) for grafico in self.graficos]

            # Posiciona as labels na janela
            for label in self.labels:
                label.pack()
    '''
    
if __name__ == "__main__":
    app = App()
    app.mainloop()