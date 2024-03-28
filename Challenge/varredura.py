from print_textbox import print_to_textbox
from buscar import encontrar_nomes, encontrar_cpf, encontrar_cnpj, encontrar_etnias, encontrar_religiao

def varredura(textbox, texto):
    '''
    Função que realiza a varredura do texto extraido do arquivo em busca de nomes, CPFs, CNPJs, Etnias e Religiões
        Args:  
            textbox: Objeto Textbox onde será impresso o resultado da varredura
            texto: Texto extraido do arquivo
        Returns:
            True: Se encontrar associar dados sensíveis a um individuo
            False: Se não encontrar associar dados sensíveis a um individuo
    '''

    print_to_textbox(textbox, "BUSCANDO POR NOMES")
    encontrados_nomes = encontrar_nomes(texto) # Encontra nomes no texto extraido do arquivo
    if encontrados_nomes:
        print_to_textbox(textbox, f"\tNomes encontrados no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão foram encontrados nomes no arquivo")

    print_to_textbox(textbox, "BUSCANDO POR CPF")
    encontrados_cpf = encontrar_cpf(texto) # Encontra CPFs no texto extraido do arquivo
    if encontrados_cpf:
        print_to_textbox(textbox, f"\tCPF encontrado no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrado CPF no arquivo")

    print_to_textbox(textbox, "BUSCANDO POR CNPJ")
    encontrados_cnpj = encontrar_cnpj(texto) # Encontra CNPJs no texto extraido do arquivo
    if encontrados_cnpj:
        print_to_textbox(textbox, f"\tCNPJ encontrado no arquivo")
    else:
        print_to_textbox(textbox, f"\tNão encontrado CNPJ no arquivo")


    if encontrados_nomes or encontrados_cpf or encontrados_cnpj: # Se encontrar alguém que possa ser associado a algum dado sensível
        
        print_to_textbox(textbox, "BUSCANDO POR ETNIAS")
        encontrados_etnias = encontrar_etnias(texto) # Encontra Etnias no texto extraido do arquivo
        if encontrados_etnias:
            print_to_textbox(textbox, f"\tEtnia encontrada no arquivo")
        else:
            print_to_textbox(textbox, f"\tNão encontrada etnia no arquivo")

        print_to_textbox(textbox, "BUSCANDO POR RELIGIÕES")
        encontrados_religioes = encontrar_religiao(texto) # Encontra Religiões no texto extraido do arquivo
        if encontrados_religioes:
            print_to_textbox(textbox, f"\tReligião encontrada no arquivo")
        else:
            print_to_textbox(textbox, f"\tNão encontrada Religião no arquivo")


        if encontrados_etnias or encontrados_religioes:
            return True
        else:
            return False
    else:
        return False