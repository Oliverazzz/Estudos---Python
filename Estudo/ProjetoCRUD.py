import os
import json
from pick import pick


class admin:
    def __init__(self):
        self.users = []

        if not os.path.exists("datausers.json"):  # verifica se o arquivo existe
            with open("datausers.json", 'w') as file:
                file.write("")
        # verifica se o arquivo não está vazio
        elif os.path.getsize("datausers.json") > 0:
            with open("datausers.json", 'r', encoding="Utf-8") as file:
                self.users = json.load(file)
                print(self.users[2])

    def saveuser(self):
        nome = input("Digite seu nome:\n")
        idade = input("Sua idade:\n")
        data = {
            "nome": nome,
            "idade": idade
        }
        self.users.append(data)

        with open("datausers.json", 'w', encoding="Utf-8") as file:
            json.dump(self.users, file, indent=4, ensure_ascii=False)

    def updateuser(self):
        userup = input("Qual usuário quer mudar?\n")
        indexuser = [i.strip() for i in self.users if (i == userup)]

    def pick(self):
        title = 'Use as setas para selecionar uma ação:'
        options = ['Salvar Usuário', 'Atualizar Usuário', 'Deletar Usuário', 'Sair']

        option, index = pick(options, title, indicator='>>', default_index=0)

        print(f"Você escolheu: {option} (Índice {index})")

        if index == 0:
            # Chama sua função saveuser()
            pass


admin = admin()
n = admin.pick()
