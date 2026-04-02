import os
import json

class admin:
    def __init__(self):
        self.users = []

        if not os.path.exists("datausers.json"):
            with open("datausers.json", 'w') as file:
                file.write()
        else:
            with open("datausers.json", 'r', encoding="Utf-8") as file:
                filer = json.load(file)
                self.users = [i for i in filer]
        

    def saveuser(self):
        nome = input("Digite seu nome:\n")
        idade = input("Sua idade:\n")
        data = {
            "nome":nome,
            "idade":idade
        }
        self.users.append(data)

        with open("datausers.json", 'w', encoding="Utf-8") as file:
            for i in self.users:
                json.dump(i, file)


    def updateuser(self):
        userup = input("Qual usuário quer mudar?\n")
        indexuser = [i.strip() for i in self.users if (i == userup)]


admin = admin()
n = admin.saveuser()