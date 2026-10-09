from entities.perso import *
#from entities.objet import *

var = perso("Leo")
#print(var)
var2 = perso("Lea")
#print(var)

tour = 0
def combat(p1,p2):
    if p1.spd >= p2.spd:
        p1.attaque(p2)
        return p2.est_mort()
    else: 
        p2.attaque(p1)
        return p1.est_mort()

while (not var.est_mort()) and (not var2.est_mort()):
    tour += 1
    combat(var,var2)
    #print(f"{var.nom} à {var.vie}")
    #print(f"{var2.nom} à {var2.vie}")
print(tour)