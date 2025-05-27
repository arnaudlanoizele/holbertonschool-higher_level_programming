#!/usr/bin/python3


class Chat:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    def presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")
        
    def miauler(self):
        print(f"{self.nom} dit : Miaou !")

chat1 = Chat("Mimi", 3)
chat1.presenter()
chat1.miauler()
