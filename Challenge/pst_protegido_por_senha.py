from pypff import file

def esta_protegido_por_senha(arquivo_pst):
  try:
    pst_file = file.open(arquivo_pst)
    pst_file.close()
    return False  # Não protegido por senha
  except Exception as e:
    # Verifique o tipo de exceção ou mensagem de erro para ter mais certeza
    return True  # Provavelmente protegido por senha

# Exemplo de uso
arquivo_pst = "C:\\Users\\Gabriel\\Desktop\\FIAP - CyberSec\\Primeiro_Ano\\Nuclea\\gabriel@semc.com.br - Copia.pst"
if esta_protegido_por_senha(arquivo_pst):
    print(f"O arquivo {arquivo_pst} está protegido por senha.")
else:
    print(f"O arquivo {arquivo_pst} não está protegido por senha.")