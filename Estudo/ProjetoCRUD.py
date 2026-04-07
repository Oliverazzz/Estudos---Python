import os
import json
from pick import pick
import numpy as np


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

    def newuser(self):
        print("\n***Salvar usuário***\n")
        nome = input("\nDigite seu nome:\n")
        idade = input("Sua idade:\n")

        #Gera um novo ID com valor crescente em relação ao último usuário cadastrado
        if os.path.getsize("datausers.json") > 0:
            id = max(user["id"] for user in self.users) + 1 
        else:
            id = 0

        data = {
            "id": id,
            "nome": nome,
            "idade": idade
        }

        self.users.append(data)
        self.savefile(self.users, save)
      
    def updateuser(self):
        if os.path.getsize("datausers.json") > 0:
            title = 'Qual usuário quer mudar?'
            users = [(f"ID:{i['id']} | Nome:{i['nome']} | Idade:{i['idade']}") for i in self.users]
        else:
            print("\nNão há usuários cadastrados ainda\n")
            quit()

        user, index = pick(users, title, indicator='>>>', default_index=0)

        titlealt = 'Escolha a alteração:'
        param = [(f"Nome:{self.users[index]['nome']}"), (f"Idade:{self.users[index]['idade']}"), 'Cancelar']
        useralt, indexalt = pick(param, titlealt, indicator='>>>', default_index=0)

        match indexalt:
            case 0:
                nomealt = input("\n\n\nNovo nome:\n")
                self.users[index]["nome"] = nomealt
                print("\n\n\nNome alterado com sucesso")
                print(f"Usuário: {self.users[index]}")
            case 1:
                idadealt = input("\n\n\nNova idade:\n")
                self.users[index]["idade"] = idadealt
                print("\n\n\nIdade alterada com sucesso")
                print(f"Usuário: {self.users[index]}")
            case 2:
                print("\n\n\nOperação cancelada")
                quit()
        self.savefile(self.users, update)


    def delete(self):
         if os.path.getsize("datausers.json") > 0:
            title = 'Qual usuário quer DELETAR?'
            users = [(f"ID:{i['id']} | Nome:{i['nome']} | Idade:{i['idade']}") for i in self.users]
        else:
            print("\nNão há usuários cadastrados ainda\n")
            quit()

        user, index = pick(users, title, indicator='>>>', default_index=0)

        
    def savefile(self, dict, method):  #Função própria para salvar no arquivo .json
        try:
            with open("datausers.json", 'w', encoding="Utf-8") as file:
                json.dump(save, file, indent=4, ensure_ascii=False)
                print("Ateração salva")
        except Exception as e:
            match method:
                case save:
                    print("\n\n\nNão foi possível salvar novo usuário")
                case update:
                    print("\n\n\nNão foi possível atualizar usuário")
                case delete:
                    print("\n\n\nNão foi possível deletar usuário")
        finally:
            print(f"Erro:{type(e).__name__}\n")


    def pick(self):
        title = 'Use as setas para selecionar uma opção:'
        options = ['Salvar Usuário', 'Atualizar Usuário',
                   'Banco de dados', 'Deletar Usuário', 'Sair']

        option, index = pick(options, title, indicator='-->', default_index=0)

        # print(f"Você escolheu: {option} (Índice {index})")

        match index:
            case 0:
                self.newuser()
            case 1:
                self.updateuser()
            case 2:
                self.listusers()
            case 3:
                self.delusers()
            case 4:
                print("\n\n\nOperação cancelada")
                return True


admin = admin()
while 1:
    n = admin.pick()
    if n:
        break
