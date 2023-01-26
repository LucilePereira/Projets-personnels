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

listemots = ['ADVICE', 'ANSWER', 'AUTHOR', 'BEAUTY', 'BRIDGE', 'CARPET', 'CASTLE', 'COUNTY',
    'CLIENT', 'DESIGN', 'DETAIL', 'DIRECT', 'DOUBLE', 'ENOUGH', 'FATHER', 'FAMILY', 'FAMOUS',
    'GARDEN', 'LAWYER', 'MASTER', 'MINUTE', 'MOTHER', 'NORMAL', 'ORANGE', 'PERSON', 'POCKET',
    'POETRY', 'POLICE', 'PRINCE', 'PUBLIC', 'PYTHON', 'RANDOM', 'RESULT', 'SEARCH', 'SHOULD',
    'SHOWER', 'SIMPLE', 'SOCIAL', 'SQUARE', 'SYMBOL', 'THANKS', 'THEORY', 'TRAVEL', 'UPDATE',
    'WEAPON', 'WEIGHT', 'WINTER', 'WONDER'] #On écrit la liste des réponses

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
    print("Try n°",coups,":")
    mot=list(input("Enter a 6 letter word:").upper()) #On enregistre le mot proposé par le joueur
    if mot==list(reponse):
        mot=list("YOUWON") #si le joueur trouve lebon mot, on affiche "gagné!"
        coups=9 #on arrête la boucle
        grille=affichergrille()
    elif len(mot)!=6: #Si le mot ne fait pas 6 lettres, on change toutes les lettres par des *
        mot=["*", "*", "*", "*", "*", "*"]
        grille=affichergrille()
        print("The word must have 6 letters")
    else:
        for i in range(6):
            if mot[i]!=list(reponse)[i] and mot[i] in list(reponse): #Si une lettre est mal placée, elle s'affiche avec un ?
                mot[i]=mot[i]+"?"
            elif mot[i]!=list(reponse)[i]: #Si la lettre n'est pas dans le mot on affiche "-" à la place
                mot[i]="-"
        grille=affichergrille()
    coups+=1

print("The answer was", reponse) #On affiche la bonne réponse à la fin