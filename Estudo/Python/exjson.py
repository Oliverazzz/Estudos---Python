import json
import os

file = (r"C:\Users\luizf\Desktop\.vscode\python\dados\nomes.json")


def jsonfile():
    listaupdate = []
    if not os.path.exists(file):
        print("Arquivo não encontrado")
    else:
        with open(file, 'r', encoding="utf-8") as f:
            data = json.load(f)
            listaupdate.append(data)
            listaupdate.append(data)
    with open(file, 'w') as d:
        json.dump(listaupdate, d, indent=4, ensure_ascii=False)


jsonfile()
