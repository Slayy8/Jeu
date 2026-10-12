from random import randint
from objet import objait

reward = [5,2,15,3]
class entitie:
    def __init__(self,nom):
        self.nom = nom
        self.atk = randint(3,17)+2
        self.dfn = randint(3,12)
        self.spd = randint(1,5)
        self.vie = randint(80,105)
        self.vieM = self.vie
        
    def est_mort(self):
        return self.vie <= 0
    
class perso(entitie):
    def __init__(self,nom):
        super().__init__(nom)
        self.inv = []

    def attaque(self,cible):            #self attaque cible  cible pouvant être un objet ou un perso
        cible.vie -= (self.atk/cible.dfn)+2
        cible.vie = round(cible.vie, 2)
        if cible.est_mort():
            cible.vie = 0
            print(f"{cible.nom} n'est plus en état de se battre, {self.nom} remporte le combat")
            self.reward()

    def reward(self):
        n = randint(0,4)
        if n == 0: 
            self.atk += reward[n]
            self.inv.append("Épée")
            print(f"{self.nom} a obtenu une épée ! Il gagne {reward[n]} d'attaque.")
        elif n == 1: 
            self.spd += reward[n]
            self.inv.append("Bottes")
            print(f"{self.nom} a obtenu des bottes ! Il gagne {reward[n]} de vitesse.")
        elif n == 2: 
            self.vieM += reward[n]
            self.inv.append("Talisman")
            self.vie = self.vieM
            print(f"{self.nom} a obtenu un talisman ! Il gagne {reward[n]} de vie max et sa santé est restorée.")
        elif n == 3: 
            self.dfn += reward[n]
            self.inv.append("Armure")
            print(f"{self.nom} a obtenu une armure ! Il gagne {reward[n]} de défense")
        else:
            potion = objait("Potion",0)
            self.inv.append(potion)
            print(f"{self.nom} a obtenu une potion ! Il peut l'utiliser à n'importe quel moment pour se soigner.")

    def __repr__(self):                 #Pour un print(self) lisible
        return (
            f"Joueur {self.nom} (HP: {self.vie}/{self.vieM}, ATK: {self.atk}, "
            f"DEF: {self.dfn}, SPD : {self.spd})")

class gobelin(entitie):
    def __init__(self,nom):
        super().__init__(nom)
        self.vie = randint(60,70)
        self.vieM = self.vie

    def __repr__(self):
        return(
            f"Gobelin {self.nom} (HP : {self.vie}/{self.vieM}, ATK: {self.atk}, "
            f"DEF: {self.dfn}, SPD : {self.spd})")


def soigner(x):
    if potion in x.inv:
        for i in x.inv:
            if potion == x.inv:
                x.vie += x.inv[i].vie

var = perso("Leo")
print(var)
var2 = gobelin("Mouir")
print(var2)
var2.est_mort()
while not var2.est_mort():
    var.attaque(var2)
    print(var2.vie)

print(var.inv)
soigner(var)
print(var.vie)
print(var.vieM)