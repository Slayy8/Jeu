from random import randint
reward = [5,2,15,3]
class perso:
    def __init__(self,nom):
        self.nom = nom
        self.atk = randint(3,17)+2
        self.dfn = randint(3,12)
        self.spd = randint(1,5)
        self.vie = randint(100,175)
        self.vieM = self.vie
        self.inv = []

    def est_mort(self):
        return self.vie <= 0

    def attaque(self,cible):            #self attaque cible  cible pouvant être un objet ou un perso
        cible.vie -= (self.atk/cible.dfn)+2
        cible.vie = round(cible.vie, 2)
        if cible.est_mort():
            cible.vie = 0
            print(f"{cible.nom} n'est plus en état de se battre, {self.nom} remporte le combat")
            self.reward()

    def reward(self):
        n = randint(0,3)
        if n == 0: 
            self.atk += reward[n]
            self.inv.append("Épée")
        elif n == 1: 
            self.spd += reward[n]
            self.inv.append("Bottes")
        elif n == 2: 
            self.vieM += reward[n]
            self.inv.append("Talisman")
        else: 
            self.dfn += reward[n]
            self.inv.append("Armure")

    def __repr__(self):                 #Pour un print(self) lisible
        return (
            f"Joueur {self.nom} (HP: {self.vie}/{self.vieM}, ATK: {self.atk}, "
            f"DEF: {self.dfn}, SPD : {self.spd})")


'''
var = perso("Leo")
print(var)
var2 = perso("Lea")
print(var2)

while not var2.est_mort():
    var.attaque(var2)
    print(var2.vie)

print(var.inv)'''