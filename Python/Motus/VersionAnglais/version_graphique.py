from random import randint
from turtle import *


def affichergrille():
    """
    -> grille : list
    renvoie la grille avec le nouveau mot ajouté et met à jour la grille
    """
    global grille
    changes = 0
    up()
    for i in range(8):
        if changes == 0 and grille[i] == ["-", "-", "-", "-", "-", "-"]:
            #on affiche le mot du joueur à la prochaine ligne du jeu
            grille[i] = mot
            changes = 1
        goto(0, 100 - i * 40)  #on revient à la ligne
        for j in range(6):
            down()
            pencolor('black')
            write(grille[i][j], font=("Arial", 30))
            up()
            forward(55)  #on affiche chaque lettre de la grille
    return grille  #on met à jour la grille


#Préparation de la liste des réponses
listemots = ['ADVICE', 'ANSWER', 'AUTHOR', 'BEAUTY', 'BRIDGE', 'CARPET', 'CASTLE', 'COUNTY',
    'CLIENT', 'DESIGN', 'DETAIL', 'DIRECT', 'DOUBLE', 'ENOUGH', 'FATHER', 'FAMILY', 'FAMOUS',
    'GARDEN', 'LAWYER', 'MASTER', 'MINUTE', 'MOTHER', 'NORMAL', 'ORANGE', 'PERSON', 'POCKET',
    'POETRY', 'POLICE', 'PRINCE', 'PUBLIC', 'PYTHON', 'RANDOM', 'RESULT', 'SEARCH', 'SHOULD',
    'SHOWER', 'SIMPLE', 'SOCIAL', 'SQUARE', 'SYMBOL', 'THANKS', 'THEORY', 'TRAVEL', 'UPDATE',
    'WEAPON', 'WEIGHT', 'WINTER', 'WONDER']

#Préparation de la liste vide
grille = []
for i in range(8):
    grille.append([])  #On ajoute 8 mots
    for j in range(6):
        grille[i].append("-")  #On rajoute 6 lettres par mot

bgcolor("LightSkyBlue")
proposition = []  #variable pour afficher toutes les propositions du joueur
reponse = listemots[randint(0, len(listemots) - 1)]  #mot aléatoire à trouver

#on affiche la grille vide au début du jeu
speed(0)
for i in range(8):
    up()
    goto(0, 100 - i * 40)
    down()
    for j in range(6):
        write(grille[i][j],
              font=("Arial", 30))  #écrire chaque lettre une par une
        up()
        forward(50)
        down()

coups = 1  #On met le compteur de coups à 1

#CORPS DU JEU

while coups < 9:  #On limite le nombre de coups à 8
    mot = textinput("Question", "Enter a 6 letter word: ").upper()
    #On enregistre le mot proposé par le joueur
    proposition.append(
        mot)  #On met la proposition dans la liste de propositions
    mot = list(mot)
    clearscreen()  #On remet à 0 l'écran
    bgcolor("LightSkyBlue")
    speed(0)

    #si le joueur trouve lebon mot, on affiche "gagné!"
    if mot == list(reponse):
        mot = list("YOUWON")
        coups = 9  #on arrête la boucle
        grille = affichergrille()
        pencolor('midnightblue')

    #Si le mot ne fait pas 6 lettres, on change toutes les lettres par des *
    elif len(mot) != 6:
        mot = ["*", "*", "*", "*", "*", "*"]
        grille = affichergrille()
        up()
        goto(-110, 200)
        down()
        pencolor('red')
        write("The word must have 6 letters", font=("Arial", 30, "bold"))
        #message d'erreur

    #Cas d'un mot de 6 lettres incorrect
    else:
        for i in range(6):
            #Si une lettre est mal placée, elle s'affiche avec un ?
            if mot[i] != list(reponse)[i] and mot[i] in list(reponse):
                mot[i] = mot[i] + "?"
                #Si la lettre n'est pas dans le mot on affiche "-" à la place
            elif mot[i] != list(reponse)[i]:
                mot[i] = "-"
        grille = affichergrille()
        pencolor('midnightblue')

    #On affiche la liste des propositions
    for i in range(len(proposition)):
        up()
        goto(-350, 100 - i * 30)
        down()
        write(proposition[i], font=('Arial', 20, 'bold'))
    coups += 1

#On affiche la bonne réponse à la fin
up()
goto(-355, -250)
down()
pencolor('purple')
write("The answer was:", font=("Arial", 35, "bold"))
up()
goto(60, -250)
down()
write(reponse, font=("Arial", 35, "bold"))
hideturtle()

exitonclick()
