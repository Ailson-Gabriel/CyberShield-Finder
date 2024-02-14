def valida_cpf(cpf):
    """
    Processa a validação de um possível CPF

    Argumentos:
        cpf (str): 11 dígitos do CPF
    Retorno:
        bool: True se o CPF é válido, False caso contrário
    """

    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calculando o primeiro dígito verificador
    soma = 0
    peso = 10
    for i in range(9): # Multiplica cada dígito do CPF pelos pesos (10 a 2)
        soma += int(cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2: # Se o resto da divisão for menor que 2, o dígito verificador será 0
        digito_verificador1 = 0
    else:
        digito_verificador1 = 11 - resto

    # Verifica se o primeiro dígito verificador calculado é igual ao fornecido no CPF
    if int(cpf[9]) != digito_verificador1:
        return False

    # Calculando o segundo dígito verificador
    soma = 0
    peso = 11
    for i in range(10): # Multiplica cada dígito do CPF (incluindo o primeiro dígito verificador) pelos pesos (11 a 2)
        soma += int(cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2: # Se o resto da divisão for menor que 2, o dígito verificador será 0
        digito_verificador2 = 0
    else:
        digito_verificador2 = 11 - resto

    if int(cpf[10]) != digito_verificador2: # Verificando se o segundo dígito verificador calculado é igual ao fornecido no CPF
        return False

    return True

"""
# EXEMPLO DE USO: *******************(NÃO NECESSÁRIO NO PROJETO FINAL)*******************
cpf = input("Digite o CPF (apenas números): ")
if valida_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")
"""
