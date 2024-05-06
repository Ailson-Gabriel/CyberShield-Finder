from pathlib import Path # Importa a classe Path do módulo pathlib
import ast # Módulo que fornece funções para analisar strings que contêm expressões literais de Python
import sys # Módulo que fornece funções e variáveis usadas para manipular diferentes partes do ambiente Python
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, messagebox # Módulo que fornece classes para criar interfaces gráficas
from matplotlib.figure import Figure # Módulo para criar figuras de gráficos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Módulo para criar um canvas para exibir figuras de gráficos
from matplotlib.ticker import MaxNLocator # Módulo para definir o número máximo de intervalos no eixo
import numpy as np # Módulo para realizar operações matemáticas

OUTPUT_PATH = Path(__file__).parent # Obtém o diretório do arquivo atual
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame0") # Obtém o diretório dos arquivos de imagem

def relative_to_assets(path: str) -> Path: # Função para obter o caminho relativo dos arquivos de imagem
    return ASSETS_PATH / Path(path) # Retorna o caminho relativo dos arquivos de imagem


def dash(): # Função para criar o dashboard
    dados_sensiveis_encontrados = load_data_from_txt('db\\base.txt', 'dados_sensiveis_encontrados') # Carrega os dados sensíveis encontrados
    quantidade_por_tipo = load_data_from_txt('db\\base.txt', 'quantidade_por_tipo') # Carrega a quantidade de cada tipo de dado sensível encontrado
    criptografados = load_data_from_txt('db\\base.txt', 'criptografados') # Carrega a lista de arquivos criptografados
    qntd_total = load_data_from_txt('db\\base.txt', 'qntd_total') # Carrega a quantidade total de arquivos verificados
    tabela_de_arquivos = load_data_from_txt('db\\base.txt', 'tabela_de_arquivos') # Carrega a tabela de arquivos verificados

    if not dados_sensiveis_encontrados or not quantidade_por_tipo or not criptografados or not qntd_total or not tabela_de_arquivos:
        # Se um ou mais conjuntos de dados estiverem vazios ou não forem encontrados, exibe uma mensagem de erro e encerra o programa
        messagebox.showerror("Erro", "Um ou mais conjuntos de dados estão vazios ou não foram encontrados. Por favor, execute a varredura novamente.")
        sys.exit(1)
    window = Tk()

    window.geometry("1000x550") # Define o tamanho da janela
    window.configure(bg = "#1A1A1A") # Define a cor de fundo da janela


    canvas = Canvas(
        window,
        bg = "#1A1A1A",
        height = 550,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        500.0,
        36.0,
        image=image_image_1
    )
    
    canvas.create_text(
        81.0,
        17.0,
        anchor="nw",
        text="Finder DashBoard",
        fill="#FFFFFF",
        font=("Inter Bold", 30 * -1)
    )
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        43.0,
        36.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        160.0,
        135.0,
        image=image_image_3
    )

    canvas.create_text(
        130.0,
        107.0,
        anchor="nw",
        text="Dados Encontrados\n",
        fill="#FFFFFF",
        font=("Inter Bold", 10 * -1)
    )

    canvas.create_text(
        127.0,
        129.0,
        anchor="nw",
        text=f"{sum(dados_sensiveis_encontrados.values())} Dados", #Imprime a soma de todos os valores do dicionário
        fill="#FFFFFF",
        font=("Inter Bold", 22 * -1)
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        500.0,
        135.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        160.0,
        364.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        500.0,
        364.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        840.0,
        364.0,
        image=image_image_7
    )

    canvas.create_text(
        460.0,
        129.0,
        anchor="nw",
        text=f"{len(tabela_de_arquivos)} Arquivos",
        fill="#FFFFFF",
        font=("Inter Bold", 22 * -1)
    )

    canvas.create_text(
        469.0,
        107.0,
        anchor="nw",
        text="Arquivos Verificados",
        fill="#FFFFFF",
        font=("Inter Bold", 10 * -1)
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        68.0,
        135.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        840.0,
        135.0,
        image=image_image_9
    )

    canvas.create_text(
        801.0,
        107.0,
        anchor="nw",
        text="Arquivos Criptografados",
        fill="#FFFFFF",
        font=("Inter Bold", 10 * -1)
    )

    canvas.create_text(
        800.0,
        129.0,
        anchor="nw",
        text=f"{len(criptografados)} Arquivos",
        fill="#FFFFFF",
        font=("Inter Bold", 22 * -1)
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        748.0,
        135.0,
        image=image_image_10
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(
        408.0,
        135.0,
        image=image_image_11
    )

    # Primeiro gráfico (vertical)
    fig_1 = Figure(figsize=(2.5, 2.2), facecolor='#15375C') # Cria uma figura com um tamanho específico
    ax_1 = fig_1.add_subplot() # Adiciona um subplot à figura
    ax_1.set_facecolor('#15375C') # Define a cor de fundo do subplot
    ax_1.fill_between(x=list(dados_sensiveis_encontrados.keys()), y1=list(dados_sensiveis_encontrados.values()), alpha=0.7) # Preenche a área entre os valores do eixo y
    ax_1.tick_params(labelsize=6, colors='white') # Define o tamanho e a cor dos rótulos dos eixos
    fig_1.autofmt_xdate() # Formata a data no eixo x
    ax_1.plot(list(dados_sensiveis_encontrados.keys()), list(dados_sensiveis_encontrados.values()), color='deepskyblue') # Plota um gráfico de linha
    ax_1.grid(visible=True) # Exibe as linhas de grade

    # Forçar o número máximo de intervalos no eixo y a ser um número inteiro
    canvas = FigureCanvasTkAgg(figure=fig_1, master=window) # Cria um canvas para exibir a figura
    canvas.draw() # Desenha o canvas
    canvas.get_tk_widget().place(x=30, y=240) # Posiciona o canvas na janela


    # Segundo gráfico (horizontal)
    fig_2 = Figure(figsize=(2.5, 2.2), facecolor='#15375C') # Cria uma figura com um tamanho específico
    ax_2 = fig_2.add_subplot() # Adiciona um subplot à figura
    ax_2.set_facecolor('#15375C') # Define a cor de fundo do subplot

    categorias = list(quantidade_por_tipo.keys()) # Obtém as categorias do dicionário
    valores = list(quantidade_por_tipo.values()) # Obtém os valores do dicionário

    y_pos = np.arange(len(categorias)) # Cria um array com a quantidade de categorias

    ax_2.barh(y_pos, valores, align='center', color='#356B9E', edgecolor='deepskyblue', linewidth=1.5, alpha=0.7) # Cria um gráfico de barras horizontais
    ax_2.set_yticks(y_pos, labels=categorias) # Define os rótulos do eixo y
    ax_2.invert_yaxis() # Inverte a direção do eixo y
    ax_2.tick_params(labelsize=6.5, colors='white') # Define o tamanho e a cor dos rótulos dos eixos
    ax_2.grid(visible=True) # Exibe as linhas de grade

    # Forçar o número máximo de intervalos no eixo y a ser um número inteiro
    ax_2.xaxis.set_major_locator(MaxNLocator(integer=True))

    fig_2.autofmt_xdate() # Formata a data no eixo x
    canvas = FigureCanvasTkAgg(figure=fig_2, master=window) # Cria um canvas para exibir a figura
    canvas.draw() # Desenha o canvas
    canvas.get_tk_widget().place(x=720, y=240) # Posiciona o canvas na janela

    # Terceiro gráfico (Tabela)
    table_coluna=["Arquivo", "Criptografado"] # Define as colunas da tabela
    table = ttk.Treeview(master=window, columns=table_coluna, show="headings") # Cria uma tabela com as colunas definidas

    for column in table_coluna: # Adiciona os cabeçalhos das colunas à tabela
        table.heading(column=column, text=column) # Adiciona os cabeçalhos das colunas à tabela
        table.column(column, width=125) # Define a largura das colunas

    # Centralizando o texto da segunda coluna
    table.column("Criptografado", anchor='center')

    for row_data in tabela_de_arquivos: # Adiciona as linhas de dados à tabela
        table.insert(parent="", index="end", values=row_data) # Adiciona as linhas de dados à tabela

    table.place(x=375, y=230, height=260) # Posiciona a tabela na janela

    style = ttk.Style() # Cria um objeto de estilo
    style.theme_use("default") # Define o tema padrão
    style.configure("Treeview", background="#23518D", fieldbackground="#23518D", foreground="white") # Configura o estilo da tabela
    style.configure("Treeview.Heading", background="#23518D", fieldbackground="#23518D", foreground="white") # Configura o estilo dos cabeçalhos da tabela
    style.map("Treeview", background=[('selected', '#A1A6F9')]) # Mapeia o estilo da tabela
    style.configure("Treeview", font=("Inter", 8)) # Configura a fonte da tabela

    window.title("CyberShield Finder Dashboard") # Define o título da janela
    window.resizable(False, False) # Impede que a janela seja redimensionada
    window.mainloop() # Inicia o loop principal da janela

def load_data_from_txt(caminho_arquivo, nome_variavel): # Função para carregar dados de um arquivo de texto
  with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: # Abre o arquivo no modo de leitura
    for linha in arquivo: # Lê cada linha do arquivo
      if linha.startswith(nome_variavel + ' ='): # Verifica se a linha começa com o nome da variável
        valor = ast.literal_eval(linha.partition('=')[2]) # Obtém o valor da variável
        return valor
  return None  # Retorna None se a variável não for encontrada

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    dash() # Chama a função para criar o dashboard
