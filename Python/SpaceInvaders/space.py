import pygame
import random
class Joueur:

    """
    Une classe pour les joueurs
    attributs :
        sens -> str "droite","gauche","O"
        image -> pygame.image
        position -> int
        score -> int
        vitesse -> int
        vie -> int
    """

    def __init__(self):
        """Joueur(sens, image, position) crée un joueur qui est représenté par
        une image, qui setrouve à la position position et qui est immobile"""
        self.sens = 0
        self.image = pygame.transform.scale(pygame.image.load('lama.png'), (50,50))
        self.position = 350
        self.score = 0
        self.vitesse = 1
        self.vie = 3

    def deplacer(self):
        """déplace le joueur dans le sens self.sens"""
        if self.sens == 'droite' and self.position < 750:
            self.position += 1 * self.vitesse  #le vaisseau se déplace vers la droite
        elif self.sens  == 'gauche' and self.position > 0:
            self.position -= 1 * self.vitesse  #le vaisseau se déplace vers la gauche

    def tirer(self):
        """arrête le vaisseau pendant que la balle est tirée"""
        self.vitesse = 0

    def marquer(self):
        """ajoute 1 au score"""
        self.score += 1


class Balle:
    """
    une classe pour les balles
    attributs :
        tireur -> Joueur
        depart -> int
        hauteur -> int
        image -> pygame.image
        etat -> str "chargee", "tiree"
    """
    def __init__(self, tireur):
        """
        Balle(tireur) crée une balle chargée, représentée par une image
        dont le tireur est tireur, qui est à une hauteur de 500, et au même
        endroit que son tireur
        """
        self.tireur = tireur
        self.image = pygame.transform.scale(pygame.image.load('balle.png'), (30,30))
        self.depart = self.tireur.position + 10
        self.hauteur = 500
        self.etat = 'chargee'

    def bouger(self):
        """
        Fait bouger la balle avec le vaisseau, vers le haut de l'écran quand
        elle est tirée, et la fait revenir au niveau du vaisseau quand elle
        atteind le bord de la fenêtre
        """
        self.depart = self.tireur.position + 10   #la position de la balle est la même que celle du vaisseau : ils se déplacent ensemble
        if self.etat == "tiree" and self.hauteur > 0: #la balle est tirée
            self.hauteur -= 10   #la balle se dirige vers le haut de l'écran
        if self.hauteur == 0:    #lorsque l'ennemi est en haut de l'écran
            self.hauteur = 500
            self.etat = "chargee"  #l'état de la balle change
            self.tireur.vitesse = 1

    def toucher(self, Ennemi):
        """faire revenir la balle au vaisseau quand elle touche un ennemi"""
        #si la balle et l'ennemi ont la même position, et que la balle est tirée
        if (Ennemi.hauteur > self.hauteur - 25 and Ennemi.hauteur < self.hauteur + 25) and (500 > self.depart - 25 and 450 < self.depart + 25) and self.etat == "tiree":
            self.hauteur = 500
            self.etat = "chargee"
            self.tireur.vitesse = 1   #la balle revient au joueur, chargée
            return True


class Ennemi:
    """
    une classe pour les ennemis
    attributs:
        depart -> int
        hauteur -> int
        type -> int
        image -> pygame.image
        vitesse -> int
    """
    NbEnnemis = 6

    def __init__(self):
        """Ennemi() crée un ennemi représenté par une image, qui démarre à une
        position aléatoire en haut de l'écran, avec une vitesse et un type
        aléatoires"""
        self.depart = random.randint(0,750)     #la position de départ de l'ennemi est aléatoire
        self.hauteur = 0
        self.type = random.randint(1,2)    #le type de l'ennemi est aléatoire
        if self.type == 1:
            self.image = pygame.transform.scale(pygame.image.load('puma.png'), (50,50))  #l'ennemi prend l'image de son type
            self.vitesse = 1 #l'ennemi prend la vitesse de son type
        else:
            self.image = pygame.transform.scale(pygame.image.load('ocelot.png'), (50,50))  #l'ennemi prend l'image de son type
            self.vitesse = 2 #l'ennemi prend la vitesse de son type

    def avancer(self):
        """fait avancer verticalement l'ennemi et le ramène en haut si il
        atteint le bas de la fenêtre"""
        self.hauteur += 0.25*self.vitesse    #l'ennemi avance vers le bas de l'écran
        if self.hauteur > 600:               #lorsqu'il atteint le bas de l'écran
            self.depart = random.randint(0,750)  #il réapparaît en haut de l'écran
            self.hauteur = 0
            self.type = random.randint(1,2)   #le type de l'ennemi est aléatoire
            if self.type == 1:
                self.image = pygame.transform.scale(pygame.image.load('puma.png'), (50,50))  #l'ennemi prend l'image de son type
                self.vitesse = 1 #l'ennemi prend la vitesse de son type
            else:
                self.image = pygame.transform.scale(pygame.image.load('ocelot.png'), (50,50))  #l'ennemi prend l'image de son type
                self.vitesse = 2 #l'ennemi prend la vitesse de son type


    def disparaitre(self):
        """fait disparaitre l'ennemi et le ramène en haut de la fenêtre"""
        self.depart = random.randint(0,750)   #la position de départ de l'ennemi est aléatoire
        self.hauteur = 0
        self.type = random.randint(1,2)       #le type de l'ennemi est aléatoire
        if self.type == 1:
            self.image = pygame.transform.scale(pygame.image.load('puma.png'), (50,50))  #l'ennemi prend l'image de son type
            self.vitesse = 1
        else:
            self.image = pygame.transform.scale(pygame.image.load('ocelot.png'),  (50,50))  #l'ennemi prend l'image de son type
            self.vitesse = 2

    def crasher(self,Joueur):
        """Fait perdre un point de vie au joueur, réinitialise l'ennemi quand
        le joueur est touché"""
        if (Joueur.position < self.depart and Joueur.position + 25 > self.depart) and (500 > self.hauteur and 450 < self.hauteur):   #lorsque l'ennemi touche le joueur
            Joueur.vie -= 1      #le joueur perd un point de vie
            self.disparaitre()    #l'ennemi revient en tant que nouvel ennemi
