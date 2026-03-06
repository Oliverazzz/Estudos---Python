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


def scrap(root): #scrap no xml (Dms, ordens, blank minimo, material, dimensão por peça)

    
    dmsall = root.findall(".//PartoNo") #encontra todos os DMS das peças
    listdms = []
    for dms in dmsall:                  #Formarta os DMS
        indexdms = dms.find("-")
        dms = dms[indexdms:]
        listdms.append(dms)

    
    orderall = root.findall(".//CustomerName") #encontra todas as ordens das peças
    listorders = []
    for order in orderall:
        lastindex = 0 
        count = order.count(",")
        orderunit = []
        for a in range (0, (count + 1)):
            if (a <= count):
                orderindex = order.find(lastindex, ",")
                order1 = order[lastindex:orderindex].strip()
                lastindex = orderindex + 1
                orderunit.append(order1) 
            else:
                order1 = [lastindex:]
                orderunit.append(order1)

    blankall = 
                
        
        


        


n = checkout(str("15413079"))
