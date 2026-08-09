import requests
import os
import json

url = "https://official-joke-api.appspot.com/random_joke"

def piada():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        piada = {"p:" : (data["setup"]), "r:" : (data["punchline"])}
        return piada
    else:
        print("\nA piada não foi encontrada")
        return None

def save(piada):
    piadas = []
    if not os.path.exists("piadas.json"):
        with open("piadas.json", 'w') as d:
            json.dump(piada, d, ensure_ascii=False, indent=4)
    else:
         with open("piadas.json", 'r') as d:
            piadas = json.load(d)
            if not isinstance(piadas, list):
                    piadas = [piadas]
            piadas.append(piada)
            with open("piadas.json", 'w') as d:
                 json.dump(piadas, d, ensure_ascii=False, indent=4)


file = piada()

if file:
    try:
        save(file)
    except Exception as e:
        print(f"\nOcorreu um erro do tipo: {type(e).__name__}")
    else:
        print("\nPiada adicionada!")
    finally:
        print("\nPrograma finalizado")
else:
    print("\nNada adicionado ao txt")