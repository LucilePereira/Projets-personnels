from random import randint

def affichergrille():
    """
    -> grille : list
    renvoie la grille avec le nouveau mot ajouté et met à jour la grille
    """
    global grille
    changes=0
    for i in range (8):
        if changes==0 and grille[i]==["-", "-","-","-","-","-"]: #on affiche le mot du joueur à la prochaine ligne du jeu
            grille[i]=mot
            changes=1
        for lettre in grille[i]:
            print(lettre, end="") #on affiche chaque lettre de la grille
        print() #on revient à la ligne
    return grille #on met à jour la grille

listemots=['ACTEUR', 'AVIRON', 'BOXEUR', 'BRONZE', 'BUDGET','CARTON', 'CHAQUE', 'CHEVAL',
'CIMENT', 'CLIENT','COMPTE', 'CONTRE', 'CUPIDE', 'DESIGN', 'DICTER', 'DOSAGE', 'DOUCHE',
'DROITE', 'EXPORT', 'FLAQUE', 'FORAGE', 'GLAIVE', 'GRAINE', 'GROUPE', 'JARDIN', 'JUNGLE',
'LOUCHE', 'LUCIDE', 'MANCHE', 'MARQUE', 'MIRAGE', 'MOUCHE', 'NIVEAU', 'NOVICE', 'OISEAU',
'PAQUET', 'PILOTE', 'PLANTE', 'POTEAU', 'PROJET', 'PUBLIC', 'REGAIN', 'RYTHME', 'SATIRE',
'SENTIR', 'SIMPLE', 'SONGER', 'SOUPLE', 'SQUARE', 'TROUPE', 'VALEUR'] #On écrit la liste des réponses

grille=[]
for i in range(8):
    grille.append([])
    for j in range(6):
        grille[i].append("-") #On prépare la grille vide

reponse=listemots[randint(0,len(listemots)-1)] #on établit le mot aléatoire à trouver

for ligne in grille: #On affiche la grille vide au début du jeu
    for lettre in ligne:
        print(lettre, end="")
    print()

coups=1 #On met le compteur de coups à 1

while coups<9:  #On limite le nombre de coups à 8
    print("Essai n°",coups,":")
    mot=list(input("Entrer un mot de 6 lettres:").upper()) #On enregistre le mot proposé par le joueur
    if mot==list(reponse):
        mot=list("GAGNE!") #si le joueur trouve lebon mot, on affiche "gagné!"
        coups=9 #on arrête la boucle
        grille=affichergrille()
    elif len(mot)!=6: #Si le mot ne fait pas 6 lettres, on change toutes les lettres par des *
        mot=["*", "*", "*", "*", "*", "*"]
        grille=affichergrille()
        print("Le mot doit avoir 6 lettres")
    else:
        for i in range(6):
            if mot[i]!=list(reponse)[i] and mot[i] in list(reponse): #Si une lettre est mal placée, elle s'affiche avec un ?
                mot[i]=mot[i]+"?"
            elif mot[i]!=list(reponse)[i]: #Si la lettre n'est pas dans le mot on affiche "-" à la place
                mot[i]="-"
        grille=affichergrille()
    coups+=1

print("La réponse était", reponse) #On affiche la bonne réponse à la fin