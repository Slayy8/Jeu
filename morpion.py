#import tkinter as tk

jeu = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

J1,J2 = "X","O"

def gagner(jeu):
    if tour == 9:
        print("Égalité")
        return True
    if jeu[0][0] == jeu[0][1] == jeu[0][2]:     #Ligne haute
        print(f"J{tour%2+1} a gagné !")
        return True
    elif jeu[1][0] == jeu[1][1] == jeu[1][2]:   #Ligne milieu
        print(f"J{tour%2+1} a gagné !")
        return True
    elif jeu[2][0] == jeu[2][1] == jeu[2][2]:   #Ligne base
        print(f"J{tour%2+1} a gagné !")
        return True
    elif jeu[0][0] == jeu[1][1] == jeu[2][2]:   #Diagonale \
        print(f"J{tour%2+1} a gagné !")
        return True
    elif jeu[0][2] == jeu[1][1] == jeu[2][0]:   #Diagonale /
        print(f"J{tour%2+1} a gagné !")
        return True
    elif jeu[0][0] == jeu[1][0] == jeu[2][0]:   #Colonne gauche
        print(f"J{tour%2+1} a gagné !")
        return True
    elif jeu[0][1] == jeu[1][1] == jeu[2][1]:   #Colonne milieu
        print(f"J{tour%2+1} a gagné !")
        return True
    elif jeu[0][2] == jeu[1][2] == jeu[2][2]:   #Colonne droite
        print(f"J{tour%2+1} a gagné !")
        return True
    else: return False

tour = 0
while gagner(jeu) == False:
    tour += 1
    X = int(input(f"J{tour%2+1} où veux-tu jouer ? "))
    for ligne in range(3):
        for case in range(3):
            if X == jeu[ligne][case]:
                if tour%2+1 == 1:
                    jeu[ligne][case] = J1
                else: jeu[ligne][case] = J2
                break
            else:print("Désolé case indisponible")
    gagner(jeu)
    for ligne in jeu:
        print(ligne)