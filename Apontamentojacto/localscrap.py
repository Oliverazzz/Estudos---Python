import pandas as pd
import os
import json
from pathlib import Path
import xml.etree.ElementTree as et



def checkout(nprog):

    #tratamento de str (bugs por conta de "\" no caminho)
    file = str(r"\\jacvmprdft02\program$\3030\\")
    file = file[:-1]

    #1. uppercase no caractere L no começo da str
    #2. Formata o caminho completo do programa
    if nprog.strip().startswith("l"):
        nprog = nprog.capitalize()
    elif nprog[0] != "L":
        nprog = "L" + nprog
    prog = str(file.strip() + nprog + ".xml")
    
    if not os.path.exists(prog):
        return "Programa não existe"
    else:
        try:
            tree = et.parse(prog, parser="etree")
            root = tree.getroot()
            return root
        except Except as e:
            erro = type(e).__name__
            return f"Erro: {e}"

    scrap(root)


def scrap(root):
    dms = root.findall(".//PartoNo")


        


n = checkout(str("15413079"))
