class ArbreBinaire:
    """
    La classe de l'arbre qui constitue le cheminement de notre récit

    """

    def __init__(self, racine):
        self.racine = racine
        self.ag = None
        self.ad = None

    def ajouter_gauche(self, valeur):
        """
        Insère un sous arbre gauche à gauche de la racine
        """
        self.ag = ArbreBinaire(valeur)

    def ajouter_droite(self, valeur):
        """
        Insère un sous arbre droit à droite de la racine
        """
        self.ad = ArbreBinaire(valeur)

    def __str__(self):
        """
        Affiche l'arbre
        """
        return str(self.racine)

    def get_valeur(self):
        """
        Renvoie le noeud où l'on se trouve
        """
        return self.racine

    def get_gauche(self):
        """
        Renvoie le sous arbre gauche
        """
        return self.ag

    def get_droite(self):
        """
        Renvoie le sous arbre droit
        """
        return self.ad