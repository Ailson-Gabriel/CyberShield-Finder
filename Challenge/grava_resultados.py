import json
import os
 
def grava_dados(dado, qntd):
  """
  Função para gravar os dados encontrados em um arquivo JSON
  Cria um Dicionário com os dados encontrados e a quantidade de cada tipo acrescentando os dados no .json
  Args:
      dado: Dado sensível encontrado
      qntd: Quantidade de vezes que o dado foi encontrado
  Returns:
      None
  """
  dados = {}
  dados[dado] = qntd
  if os.path.exists('db\\base.json'):
      with open('db\\base.json', 'r') as json_file:
          dados_existente = json.load(json_file)
      dados_existente.update(dados)
      dados = dados_existente
  with open('db\\base.json', 'w') as json_file:
      json.dump(dados, json_file)

  return None

def inicia_dados():
  """
  Função para iniciar o arquivo JSON
  Cria um arquivo JSON com um Dicionário vazio
  Args:
      None
  Returns:
      None
  """
  dados = {}
  with open('db\\base.json', 'w') as json_file:
      json.dump(dados, json_file)
  return None