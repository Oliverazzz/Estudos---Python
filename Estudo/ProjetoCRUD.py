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

    def saveuser(self):
        print("\n***Salvar usuário***\n")
        nome = input("\nDigite seu nome:\n")
        idade = input("Sua idade:\n")
        data = {
            "nome": nome,
            "idade": idade
        }
        self.users.append(data)

        try:
            with open("datausers.json", 'w', encoding="Utf-8") as file:
                json.dump(self.users, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print("Não foi possível cadastrar um novo usuário\n")
            print(f"Erro:{type(e).__name__}\n")
        finally:
            print("\nUsuário cadastrado com sucesso\n")

    def updateuser(self):
        if os.path.getsize(self.users) > 0:
            title = 'Qual usuário quer mudar?'
            users = [i['Nome'] for i in self.users if self.users]
        else:
            print("\nNão há usuários cadastrados\n")
            quit()

        user, index = pick(users, title, indicator='>>>', defalt_index=0)    

    def pick(self):
        title = 'Use as setas para selecionar uma ação:'
        options = ['Salvar Usuário', 'Atualizar Usuário', 'Banco de dados', 'Deletar Usuário', 'Sair']

        option, index = pick(options, title, indicator='-->', default_index=0)

        #print(f"Você escolheu: {option} (Índice {index})")

        match index:
            case 0:
                self.saveuser()
            case 1:
                self.updateuser()
            case 2:
                self.listusers()
            case 3:
                self.delusers()
            case 4:
                print("Operação cancelada")
                pass

admin = admin()
while 1:
    n = admin.pick()
