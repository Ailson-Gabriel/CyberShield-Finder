def print_to_textbox(textbox, message):
    '''
    Imprime mensagem no textbox
        args:
            textbox: Objeto Textbox onde será impresso o resultado da varredura
            message: A mensagem a ser impressa
    '''
    textbox.configure(state='normal') # Habilita a edição do Textbox
    textbox.insert("end", message + "\n") # Insere a mensagem no final do Textbox
    textbox.configure(state='disabled') # Desabilita a edição do Textbox
    textbox.update_idletasks() # Atualiza o Textbox