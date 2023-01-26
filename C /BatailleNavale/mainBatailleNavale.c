#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* On inclut les prototypes du .o */
int verif(char tab[][10]);
void afficheduo(char t[][10], char p[][10]);
int jouerJoueur(char adv[][10]);
void affiche(char grilleJn[10][10]);
char* navire(int num_bateau);
void ajoutNavireAleatoire(char grilleJn[][10]);
void initPlateau(char grilleJn[10][10]);
int compterPts_finirTour(int etat, int cptrJn[6]);


int main(void) {
	navire(1);
  /* INITIALISATION DES VARIABLES */

  /* On prepare les grilles vides des deux joueurs */
  char grilleJ1[10][10], grilleJ2[10][10];

  /* On prepare un compteur pour chaque joueur :
  - la case [5] correspond au nombre total de cases touchees
    contenant un bateau
  - les cases de [0] a [4] correspondent au
    nombre de cases touchees contenant un certain bateau :
      cptJn[0] = compteur Porte avion,
      cptJn[1] = compteur Croiseur,
      cptrJn[2] = compteur Sous-Marin
      cptrJn[3] = compteur Mous-Sarin
      cptrJn[4] = compteur Torpilleur

  On prepare une variable etat pour l'etat de la case touchee par
  un joueur (conforme aux valeurs renvoyees par la fonction
  jouerJoueur) et une variable tour pour savoir quel joueur doit jouer
  */

  int cptJ1[6] = {}, cptJ2[6] = {}, etat, tour = 1;

  /* On initialise les grilles */
  /* J1  */
  printf("Joueur 1 : \n");
  initPlateau(grilleJ1);
  affiche(grilleJ1);

  /* On efface la grille remplie avant le tour d'apres */
  printf("Entrer pour continuer...");
  getchar();
  system("clear");

  /* J2 */
  printf("Joueur 2 : \n");
  initPlateau(grilleJ2);
  affiche(grilleJ2);

  /* On efface la grille remplie avant le tour d'apres */
  printf("Entrer pour continuer...");
  getchar();
  system("clear");


  /*  BOUCLE DE LA PARTIE  */

  while (cptJ1[5] < 17 && cptJ2[5] < 17) {
    /* On affiche la grille et le nom du joueur qui joue au debut de chaque tour
     */
    printf("Le joueur %d joue.\n", tour);
    afficheduo(grilleJ1, grilleJ2);

    /* Si tour vaut 1, J1 joue
      Si compterPts_finirTour renvoie 1 on passe au Joueur 2 via
      l'addition
      Si compterPts_finirTour renvoie 0 le joueur 1 rejoue.
    */

    if (tour == 1) {

      etat = jouerJoueur(grilleJ2);
      tour += compterPts_finirTour(etat, cptJ1);
    }

    /* Le J2 joue, tour vaut 2, si etat renvoie 1 on passe au Joueur 1, via la
      soustraction, si renvoie 0 le joueur 2 rejouera. */
    else {
      etat = jouerJoueur(grilleJ1);
      tour -= compterPts_finirTour(etat, cptJ2);
    }
  }

  /* On affiche un message pour annoncer la victoire d'un joueur */
  int gagnant = (cptJ1[5] == 17) ? 1 : 2;
  printf("Bravo joueur %d ! Vous avez gagne !\n", gagnant);

  return 0;
}
