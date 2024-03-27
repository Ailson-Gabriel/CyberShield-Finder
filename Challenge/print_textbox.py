def print_to_textbox(textbox, message):
    textbox.configure(state='normal')
    textbox.insert("end", message + "\n")
    textbox.configure(state='disabled')
    textbox.update_idletasks()