def valida_cnpj(cnpj):
    """
    Processa a validação de um possível CNPJ

    Argumentos:
        cnpj (str): 14 dígitos do CNPJ
    Retorno:
        bool: True se o CNPJ é válido, False caso contrário
    """
    # Remove caracteres não numéricos do CNPJ
    cnpj = ''.join(filter(str.isdigit, cnpj))
    
    # Cálculo do primeiro dígito verificador
    soma = 0
    peso = 5
    for i in range(12):
        soma += int(cnpj[i]) * peso
        peso -= 1
        # A cada dois passos, o peso é ajustado
        if peso == 1:
            peso = 9
    resto = soma % 11
    dv1 = 0 if resto < 2 else 11 - resto
    
    # Cálculo do segundo dígito verificador
    soma = 0
    peso = 6
    for i in range(13):
        soma += int(cnpj[i]) * peso
        peso -= 1
        # A cada dois passos, o peso é ajustado
        if peso == 1:
            peso = 9
    resto = soma % 11
    dv2 = 0 if resto < 2 else 11 - resto
    
    # Verificação dos dígitos verificadores
    if int(cnpj[12]) == dv1 and int(cnpj[13]) == dv2:
        return True
    else:
        return False