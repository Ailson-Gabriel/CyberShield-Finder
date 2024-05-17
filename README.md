Aplicação CyberShield Finder
    Esta aplicação, denominada "CyberShield Finder", é um sistema que visa varrer diretórios e arquivos, procurando por dados sensíveis e potencialmente comprometedores, e criptografando-os para garantir a segurança da informação.
    
Funcionalidades Principais:
    •	Varredura de Diretórios: A aplicação permite que o usuário selecione um diretório e inicie a varredura de todos os arquivos e subdiretórios dentro dele.
    •	Detecção de Dados Sensíveis: O CyberShield Finder identifica dados como nomes, CPFs, rostos (através de reconhecimento facial), etnias, religiões, gêneros, posições políticas, orientações sexuais e doenças.
    •	Criptografia: Após a detecção de dados sensíveis, a aplicação criptografa os arquivos que os contêm, garantindo a segurança da informação.
    •	Dashboard: Um dashboard visual interativo é gerado para apresentar a análise dos dados, exibindo a quantidade de arquivos varridos, dados sensíveis encontrados e arquivos criptografados.
    Arquitetura da Aplicação:
    A aplicação é estruturada em diversos módulos Python, cada um com uma função específica:
    •	finder_gui.py: Interface gráfica principal da aplicação, responsável por receber a entrada do usuário (diretório a ser varrido), iniciar a varredura e exibir o resultado.
    •	controller.py: Controla o fluxo da varredura, chamando as funções de processamento para cada tipo de arquivo.
    •	processar_*.py: Módulos responsáveis por processar os diferentes tipos de arquivos:
    o	processar_imagem.py: Processa imagens usando OCR (Optical Character Recognition).
    o	processar_texto.py: Processa arquivos de texto.
    o	processar_docx.py: Processa arquivos DOCX.
    o	processar_pdf.py: Processa arquivos PDF.
    o	processar_excel.py: Processa arquivos Excel.
    o	processar_pst.py: Processa arquivos PST.
    •	varredura.py: Realiza a análise do texto extraído dos arquivos, buscando dados sensíveis e utilizando reconhecimento facial para imagens.
    •	buscar.py: Implementa funções de busca por padrões utilizando expressões regulares.
    •	criptografar_arquivo.py: Realiza a criptografia dos arquivos identificados como contendo dados sensíveis.
    •	grava_resultados.py: Armazena os resultados da varredura em um arquivo .txt, incluindo a contagem de dados sensíveis, arquivos criptografados e uma tabela de arquivos varridos.
    •	graficos.py: Gera gráficos para visualizar os resultados da varredura.
    •	ler_arquivo_txt.py: Lê o conteúdo de arquivos .txt.
    •	print_textbox.py: Imprime mensagens no Textbox da interface gráfica.
    •	valida_cpf.py: Valida CPFs utilizando algoritmos de verificação de dígitos.
    
Detalhes de Implementação:
    •	Interface Gráfica: A interface gráfica é construída com a biblioteca customtkinter, proporcionando uma aparência moderna e intuitiva.
    •	Varredura de Arquivos: A varredura é realizada de forma recursiva, percorrendo todos os arquivos e subdiretórios dentro do diretório selecionado.
    •	Reconhecimento Facial: O reconhecimento facial é implementado utilizando a biblioteca cv2 (OpenCV), e o classificador pré-treinado haarcascade_frontalface_default.xml é utilizado para detectar rostos nas imagens.
    •	Criptografia: A criptografia é realizada com a biblioteca cryptography, utilizando a classe Fernet para gerar uma chave e criptografar os dados.
    •	Gravação de Resultados: Os resultados da varredura são armazenados em um arquivo .txt, permitindo a recuperação e análise posterior dos dados.
    •	Visualização de Resultados: Gráficos são gerados para apresentar os resultados de forma visual e intuitiva.
    
Instruções de Uso:
    1.	Instale as dependências:
    pip install -r requirements.txt
    2.	Execute a aplicação:
    python finder_gui.py
    3.	Selecione um diretório: Utilize o botão "Selecionar diretório" para escolher o diretório que deseja varrer.
    4.	Inicie a varredura: Clique no botão "Iniciar varredura" para iniciar o processo de análise dos arquivos.
    5.	Visualize os resultados: Após a conclusão da varredura, o dashboard será exibido, mostrando a análise dos dados.
    
Considerações:
    •	A aplicação é um sistema de segurança, mas não deve ser considerada uma solução completa para todos os problemas de segurança.
    •	O reconhecimento facial pode ter uma precisão variável, dependendo da qualidade da imagem.
    •	É importante garantir a segurança da chave de criptografia, para evitar que os dados sejam descriptografados por usuários não autorizados.
    
Futuras Melhorias:
    •	Implementação de outros tipos de detecção: A aplicação pode ser aprimorada com a implementação de outros tipos de detecção de dados sensíveis, como números de cartão de crédito, números de telefone, endereços de e-mail, etc.
    •	Integração com sistemas de gerenciamento de arquivos: A aplicação pode ser integrada com sistemas de gerenciamento de arquivos, permitindo a varredura automática de arquivos e a criptografia em tempo real.
    •	Melhorias na interface gráfica: A interface gráfica pode ser aprimorada com a adição de funcionalidades como barra de progresso, avisos personalizados e personalização do tema.
    
Conclusão:
    O CyberShield Finder é uma ferramenta útil para ajudar a proteger a segurança da informação, identificando e criptografando dados sensíveis. A aplicação oferece uma interface gráfica amigável e ferramentas de análise visual para monitorar os resultados da varredura. Através de constantes aprimoramentos, a aplicação pode se tornar ainda mais robusta e eficiente na proteção de informações importantes.

