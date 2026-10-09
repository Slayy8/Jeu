from random import randint
from perso import *

class objet:
    def __init__(self,nom,mvt):
        self.nom = nom
        self.vie = randint(6,23)
        self.vieM = self.vie
        if mvt == 0:
            self.mvt = "touchable"
        else: self.mvt = "intouchable"
    
    def __repr__(self):                 #Pour un print(self) lisible
        return (
            f"Objet {self.nom} (HP : {self.vie}/{self.vieM}, {self.mvt})"
        )
    
    def stock(self,cible):              #On met self dans l'inventaire de cible
        if isinstance(cible, perso):
            if self.mvt == "touchable":
                cible.inv.append(self)
            else: print(f"{self.nom} ne peut pas être placé dans l'inventaire de {cible.nom}")
        else:
            print(f"{cible.nom} ne possède pas d'inventaire")


'''
P = perso("Leo")

var = objet("Table",0)
var2 = objet("Air",1)

print(var)
print(var2)
print(P)

var.stock(P)
print(P.inv)
var2.stock(P)
print(P.inv)
var2.stock(var)'''