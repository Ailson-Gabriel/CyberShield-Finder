def print_to_textbox(textbox, message):
    '''
    Print a message to the textbox.
        args:
            textbox: The textbox to print the message to.
            message: The message to print.
    '''
    textbox.configure(state='normal')
    textbox.insert("end", message + "\n")
    textbox.configure(state='disabled')
    textbox.update_idletasks()