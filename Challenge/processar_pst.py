import os
import subprocess
from email import policy
from email.parser import BytesParser
from varredura import varredura
from criptografar_arquivo import criptografar_arquivo_caminho
import tkinter as tk
from print_textbox import print_to_textbox

def processar(arquivo, textbox):
    output_dir = os.path.dirname(os.path.abspath(arquivo))
    pst_to_eml(arquivo, output_dir)

    for eml_file in os.listdir(output_dir):
        if eml_file.endswith(".eml"):
            with open(eml_file, "rb") as f:
                msg = BytesParser(policy=policy.default).parse(f)
                # Agora você pode acessar o conteúdo do email com `msg`

def pst_to_eml(pst_file, output_dir):
    subprocess.run(["readpst", "-o", output_dir, "-e", "-h", pst_file])