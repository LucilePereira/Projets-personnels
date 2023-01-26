import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init()

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
# chargement de l'image de fond
fond = pygame.image.load('background.png')

# creation du joueur
player = space.Joueur()
# creation de la balle
tir = space.Balle(player)
tir.etat = "chargee"
# creation des ennemis
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)

### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))

    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement

    if player.vie!=0: #tant que le joueur a de la vie
       # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_SPACE : # espace pour tirer
                player.tirer()
                tir.etat = "tiree"

        ### Actualisation de la scene ###
        # Gestions des collisions
        for ennemi in listeEnnemis:
            if tir.toucher(ennemi):
                ennemi.disparaitre()
                player.marquer()
                print(f"Score = {player.score} points")
            #Fait perdre un point de vie au joueur si il est touché par un ennemi
            ennemi.crasher(player)

        # placement des objets
        # le joueur
        player.deplacer()
        screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
        # la balle
        tir.bouger()
        screen.blit(player.image,[player.position,500]) # appel de la fonction qui dessine le vaisseau du joueur
        # les ennemis
        for ennemi in listeEnnemis:
            ennemi.avancer()
            screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
    else: # si le joueur n'a plus de vie

        screen.blit(pygame.transform.scale(pygame.image.load('obseque.png'),(200,200)),[300,100]) # appel de la fonction qui dessine le message de fin
        screen.blit(pygame.transform.scale(pygame.image.load('tombe_du_lama.png'),(100,100)),[350,350]) # appel de la fonction qui dessine le bouton pour ressuciter
        # si on clique dans la zone du bouton
        if event.type == pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pos()[0] > 350 and pygame.mouse.get_pos()[0] < 450) and (pygame.mouse.get_pos()[1] > 350 and pygame.mouse.get_pos()[1] < 450):
            player.vie = 3 # la vie du joueur revient à 3 donc le jeu recommence


    pygame.display.update() # pour ajouter tout changement à l'écran

