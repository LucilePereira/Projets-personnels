#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* verif verifie que le tableau tab contient bien les navires demandes
     retour : l'entier 1 si tab contient exactement 17 cases ne
     contenant pas un espace, et 0 sinon. */
int verif(char tab[][10]) {
  /* on cree un entier resultat, un compteur, et deux entiers pour les
     boucles for */
  int res = 0, cpt = 0, i, j;

  /* on parcourt tout le tableau */
  for (i = 0; i < 10; i++) {
    for (j = 0; j < 10; j++) {
      if (tab[i][j] != ' ') { 
	/* on ajoute 1 a cpt pour chaque case qui ne contient pas un espace */
        cpt++;
      }
    }
  }

  if (cpt == 17) { /* si il y a pile 17 cases ne contenant pas un espace */
    res = 1;       /* la variable resultat prend la valeur 1 */
  }

  return res;
}

/* afficheduo permet d'afficher cote a cote les tableaux t et p, sous forme de
     grilles de bataille navale. 
		 retour : vide */
void afficheduo(char t[][10], char p[][10]) {
	/* on cree deux entiers pour les boucles for */
  int i, j; 

	/* on affiche la premiere ligne de chaque tableau */
  printf("_|0|1|2|3|4|5|6|7|8|9|\t\t\t_|0|1|2|3|4|5|6|7|8|9|\n"); 
	
  for (i = 0; i < 10; i++) { /* on repete 10 fois */

		/* Premier tableau */
    printf("%c|", 'A' + i); /* on affiche la lettre qui correspond a la ligne */
    for (j = 0; j < 10; j++) { /* on parcourt chaque case de la ligne */
      switch (t[i][j]) {
	      case 'x': /* si la case contient un x : on affiche x */
	        printf("x|");
          break;
	      case '.': /* si la case contient un . : on affiche . */
	        printf(".|");
          break;
	      default: /* sinon : on affiche un espace */
	        printf(" |");
          break;
	    }
    }

		/* Deuxieme tableau */
    printf("\t\t\t%c|", 'A' + i); /* espace entre les deux tableaux */
    for (j = 0; j < 10; j++) {
      switch (p[i][j]) {
	      case 'x': /* si la case contient un x : on affiche x */
	        printf("x|");
					break;
	      case '.': /* si la case contient un . : on affiche . */
	        printf(".|");
					break;
	      default: /* sinon : on affiche un espace */
	        printf(" |");
					break;
      }
    }
    printf("\n");
		}
}

/* joueurJoueur permet a un joueur de jouer sur le tableau adv.
     retour : un entier, correspondant au Navire touche :
        -1 si le coup est a l'eau
        0 si le coup touche le Porte-Avion -> A
        1 si le coup touche le Croiseur -> C
        2 si le coup touche le Sous-Marin -> S
        3 si le coup touche le Mous-Sarin -> M
        4 si le coup touche le Torpilleur -> T
        -2 si la case contient un caractere non reconnu (ne devrait pas arriver) 
				-3 si le coup est hors plateau / sur une case deja touchee */
int jouerJoueur(char adv[][10]) {
	/* on cree un entier resultat et deux entiers pour les coordonnees */
	int res, x, y, i;
	/* on cree un tableau de caracteres pour la case entree par le joueur */
  char coordonnees[32]={};

	/* on enregistre la case entree par le joueur */
  scanf("%s", coordonnees); 

	/* on vide le buffer en faisant getchar jusqu'a arriver a un retour a la ligne */
	while ( getchar() != '\n' );
	
  /* si la case est hors limites ou le format pas valide */
  if (((coordonnees[0] < 'a' || coordonnees[0] > 'j') && (coordonnees[0] < 'A' || coordonnees[0] > 'J')) || (coordonnees[1] < '0' || coordonnees[1] > '9')) {
    /* on met res a -3 */
		res = -3;
  } 

	/* si la case est dans les limites */
	else {
		
		/* on convertit les coordonnees en entiers */
		if(coordonnees[0] >= 'a')
    {
			/* si la lettre est en minuscules */
			y=coordonnees[0]-'a';
		}
		else
    {
			/* si la lettre est en majuscules */
			y=coordonnees[0]-'A';
		}
		x=coordonnees[1]-'0';

		/* on lit le contenu de la case */
    switch (adv[y][x]) {
	    case ' ': /* si la case est vide */
				/* on met . dans la case et on met res a -1 */
	      adv[y][x] = '.';
	      res = -1;
				break;
			
	    case 'A': /* si la case contient le porte-avion */
				/* on met x dans la case et on met res a 0 */
	      adv[y][x] = 'x';
	      res = 0;
				break;
			
	    case 'C': /* si la case contient le croiseur */
				/* on met x dans la case et on met res a 1 */
	      adv[y][x] = 'x';
	      res = 1;
				break;
			
	    case 'S': /* si la case contient le sous-marin */
				/* on met x dans la case et on met res a 2 */
	      adv[y][x] = 'x';
	      res = 2;
				break;
			
	    case 'M': /* si la case contient le mous-sarin */
				/* on met x dans la case et on met res a 3 */
	      adv[y][x] = 'x';
	      res = 3;
				break;
			
	    case 'T': /* si la case contient le torpilleur */
				/* on met x dans la case et on met res a 4 */
	      adv[y][x] = 'x';
	      res = 4;
				break;
			
	    case '.': /* si la case est deja touchee */
				/* on met res a -3 */
	      res = -3;
				break;
			
			case 'x': /* si la case est deja touchee */
				/* on met res a -3 */
	      res = -3;
				break;
			
	    default: /* dans tous les autres cas */
				/* on met res a -2 */
	      res = -2;
				break;
    }
  }
  return res;
}

/* affiche permet d’afficher sur la sortie standard le plateau de jeu t, sous
forme de grille de bataillenavale */
void affiche(char grilleJn[10][10]) {
  /*Affichage des coordonnees en abscisse.*/
  printf("_|0|1|2|3|4|5|6|7|8|9|\n");
  int i, j;
  /*Affichage des coordonnees en ordonnee.*/
  for (i = 0; i < 10; i++) {
    printf("%c|", 'A' + i);
    /*Affichage du caractere de la grille.*/
    for (j = 0; j < 10; j++) {
      printf("%c|", grilleJn[i][j]);
    }
    printf("\n");
  }
	printf("\n");
}

/* On declare une variable globale car les noms des bateaux sont statiques */
char bateau[5][32]={"Porte-Avion","Croiseur","Sous-Marin","Mous-Sarin","Torpilleur"};

/* navire renvoie une chaîne de caracteres correspondant a Navire, selon l'entier
entre : resultat : selon l'entier i donne en argument, navire renvoie : 0
Porte-Avion, 1 Croiseur, 2 Sous-Marin, 3 Mous-Sarin, 4 Torpilleur */
char* navire(int num_bateau){
  if((num_bateau>=0)&&(num_bateau<=4)){
    return bateau[num_bateau];
  }
  return "Fausse entree";
}

/*
ajoutNavireAleatoire permet d'ajouter au tableau tab un Navire de taille t, et represente par le caractere b.

resultat : t cases consecutives de tab reçoivent le caractere b.

fonctionnement : 
La fonction choisit aleatoirement si le navire sera horizontal ou vertical,
puis en fonction de cela choisit aleatoirement la position de façon a ce que le navire ne depasse pas du tableau.
retour : vide
*/
void ajoutNavireAleatoire(char grilleJn[][10]){
  int sens, x, y, i=0, fin, n, erreur;
  srand(time(NULL));
  char pion[5]={'A','C','S','M','T'};
  int len[5]={5,4,3,3,2};
  
	while(i<5){
		/*Generer 0 ou 1 pour la direction, vertical ou horizontal.*/
    
		sens=rand()%2;

    /*Generer x de 0 a 9, pour les coordonees en abscisse allant de 0 a 9.*/
    /*Generer y de 0 a 9 pour ABCD..., pour les coordonnees en ordonnee.*/
		if (sens==0){
			x=rand()%10;
			y=rand()%(10-len[i]);
		}
		else{
			x=rand()%(10-len[i]);
			y=rand()%10;
		}
/*On verifie qu'il n'y a pas deja un bateau, ou qu'on empiete pas sur un bateau proche.*/
		erreur=0;
    if (sens==1)
    {
      fin = x+len[i];

      for (n=x; n<fin; n++)
      {
        if(grilleJn[y][n]!=' ')
        {
          erreur=1;
        }
      }
    }
    else
    {
      fin = y+len[i];

      for (n=y; n<fin; n++)
      {
        if(grilleJn[n][x]!=' ')
        {
          erreur=1;
        }
      }
    }

		if(erreur==0){
			if (sens==1)
    {
      fin = x+len[i];
      for (n=x; n<fin; n++)
      {
        grilleJn[y][n]=pion[i];
      }
    }
    else
    {
      fin = y+len[i];
      for (n=y; n<fin; n++)
      {
        grilleJn[n][x]=pion[i];
      }
    }
			i++;
		}
	}
}

/*
initPlateau permet a un joueur d'initialiser le tableau plat, en y plaçant ses
navires.

resultat : A la fin de la fonction, le tableau plat contient les 5 navires de la
bataille navale, places selon les regles.

retour : vide

fonctionnement :
Le joueur peut placer ses navires de deux façons :
        - Aleatoirement, auquel cas la fonction appelle ajoutNavireAleatoire de
façon adaptee afin d'obtenir le resultat.
        - A la main, auquel cas le joueur doit dire si son navire est horizontal
ou vertical, et donner la coordonnee la plus nord-ouest. Si l'utilisateur place
mal son Navire, il lui est demande de le replacer.
*/
void initPlateau(char grilleJn[10][10]) {
  /*Declaration des variables*/
  char choix;
  int choix_boucle=1;

  char coordonnees[32]; /*tableau des coordonnees entrees par l'utilisateur, de taille 32 pour eviter des erreurs avec le buffer d'entree et eviter les depassements de memoire.*/

  /*Variables dediees aux boucles de placement et aux conditions.*/
  int placement; 
  int cptnav=0;
  int erreur=0;
  int i,x,y;
  int ybeg,yend,xbeg,xend;
  
  /*Variables contenant les informations relatives aux pions.*/
  char pion[5]={'A','C','S','M','T'};
  int longueur_pion[5]={5,4,3,3,2};
  
/*Initialiser la grille*/
  for (y = 0; y < 10; y++) {
		for(x=0;x<10;x++)
		{
			grilleJn[y][x]=' ';
		}
  }

/*On demande a l'utilisateur de choisir entre placement manuel ou aleatoire.*/
  while(choix_boucle==1){
    printf("Souhaitez-vous placer vos navires a la (M)ain, ou (A)leatoirement ?\n");
    scanf("%c",&choix);
		/* on vide le buffer en faisant getchar jusqu'a arriver a un retour a la ligne */
		while ( getchar() != '\n' );
    /*On verifie que l'entree est parmi les choix donnes a l'utilisateur.*/
    if ((choix=='A')||(choix=='a')||(choix=='M')||(choix=='m'))
    {
      choix_boucle=0;
    }
    else{
      printf("Entrez un choix valide (M ou A).\n");
    }
  }
  /*L'utilisateur choisi un placement aleatoire alors on utilise la fonction ajoutNavireAleatoire*/
  if ((choix=='A')||(choix=='a'))
	{
    ajoutNavireAleatoire(grilleJn);
  }
	/*L'utilisateur choisi un placement manuel, on entre dans la boucle de placement, dans laquelles il y a des conditions verifiant la conformite de l'entree.*/
  if ((choix=='M')||(choix=='m'))
  {  
    printf("Exemple de syntaxte des coordonnees : h,B9\nVertical \'v\'.\nHorizontal \'h\'.\n");
    for(i=0;i<5;i++)
    {
      placement=1;
      while(placement==1)
			{
				cptnav=0;
				erreur=0;
				affiche(grilleJn);
				printf("Placer le %s (longueur %d)\n",navire(i),longueur_pion[i]);
				scanf("%s",coordonnees);
        /*On vide le buffer en faisant getchar jusqu'a arriver a un retour a la ligne, pour eviter certaines erreurs.*/
        while ( getchar() != '\n' );
	
/*Gestion des erreurs d'entree !*/
        /*Cas où la coordonnees est incomplete.*/
				if((coordonnees[0]==' ')||(coordonnees[2]==' ')||(coordonnees[3]==' '))
				{
					printf("X Coordonnees incompletes.\n");
					erreur++;
				}
        /*Cas où il n'y as pas de virgule.*/
        if(coordonnees[1]!=',')
				{
					printf("X Les coordonnees doivent être separees par une virgule : v,H2.\n");
					erreur++;
				}
        /*Cas où la direction est mauvaise.*/
				if((coordonnees[0]!='v'&& coordonnees[0]!='V')&&(coordonnees[0]!='h'&& coordonnees[0]!='H'))
				{
					printf("X Mauvaise direction, pour vertical vous devez saisir \'v\' et pour horizontal \'h\'.\n");
					erreur++;
				}
        /*Cas où une majuscule est entree pour la direction, conversion en minuscule.*/
				if((coordonnees[0]=='V')||(coordonnees[0]=='H'))
				{
					coordonnees[0]=(coordonnees[0]-'A')+'a';
				}
        /*Cas où une majuscule est entree pour les coordonnees en ordonnee, conversion en majuscule.*/
				if((coordonnees[2]>='a')&&(coordonnees[2]<='j'))
				{
					coordonnees[2]=(coordonnees[2]-'a')+'A';
				}
        /*Cas où on donne une mauvaise lettre pour les coodonnees en ordonnee.*/
				if((coordonnees[2] < 'A' || coordonnees[2] > 'J'))
				{
					printf("X Mauvaises coordonnees. L'entree en ordonnees doit être entre A et J.\n");
					erreur++;
				}
        /*Cas où le caractere donnee pour les coordonees en abscisse est un mauvais caracere. Ne prendra pas en charge les nombres 88 par exemple car cela fait deux caracteres.*/
				if((coordonnees[3]<'0')||(coordonnees[3]>'9'))
				{
					printf("X L'entree en abscisse doit être entre 0 et 9.\n");
					erreur++;
				}
/*Gestion des limites aux coordonnees.*/
				if(((coordonnees[0]=='v')&&((coordonnees[2]+(longueur_pion[i]-1))>'J'))||((coordonnees[0]=='h')&&((coordonnees[3]+(longueur_pion[i]-1))>'9')))
				{
					printf("X %s sortant des limites.\n",navire(i));
					erreur++;
				}
	/*Cas où il y a deja un bateau et cas où on empiete sur un bateau. On utilise le même raisonnement que pour le placement de notre bateau mais en comptant juste le nombre de fois où il y a un caractere.*/
				if(erreur==0)
				{
					if (coordonnees[0]=='h')
					{
						/*On converti les caracteres en entier,  pour boucler correctement.*/
						y=coordonnees[2] - 'A';
						xbeg = coordonnees[3] - '0';
						xend = xbeg+longueur_pion[i];
	
						for (x=xbeg;x<xend;x++)
						{
              /*Si il y a un caractere on augmente le compteur de bateau present sur les coodonnees où se trouvera le bateau*/
							if(grilleJn[y][x]!=' ')
							{
								cptnav++;
							}
						}
					}
						
					else
					{
            /*On converti les caracteres en entier, pour boucler correctement*/
						x=coordonnees[3] - '0';
						ybeg=coordonnees[2]-'A';
						yend=ybeg+longueur_pion[i];
	
						for (y=ybeg;y<yend;y++)
						{
              /*Si il y a un caractere on augmente le compteur de bateau present sur les coodonnees où se trouvera le bateau*/
							if(grilleJn[y][x]!=' ')
							{
								cptnav++;
							}
						}
					}
          /*On a empiete sur un bateau, alors on a une erreur.*/
					if (cptnav!=0)
					{
						erreur++;
						printf("X Empiete sur un autre navire.\n");
					}
					
/*Fin du placement d'un navire, on n'a plus d'erreur.*/
					if (erreur==0)
					{
						placement=0;
					}
				}
	   }
/*Tout va bien, on place.*/
			if (coordonnees[0]=='h')
			{
				/*On converti les caracteres en entier.*/
				y=coordonnees[2] - 'A';
				xbeg = coordonnees[3] - '0';
				xend = xbeg+longueur_pion[i];

				for (x=xbeg;x<xend;x++)
				{
					grilleJn[y][x]=pion[i];
				}
			}
			else
			{
        /*On converti les caracteres en entier.*/
				x=coordonnees[3] - '0';
				ybeg= coordonnees[2]-'A';
				yend= ybeg+longueur_pion[i];

				for (y=ybeg;y<yend;y++)
				{
					grilleJn[y][x]=pion[i];
				}
			}
		}
	}
}

/* On utilise la fonction compterPts_finirTour qui prend en arguement l'etat de
  la partie apres qu'un joueur ai joue, par le biai de la fonction jouerJoueur.

  Elle renvoie au joueur l'etat de la grille du joueur adverse apres sont tour.
  Elle ajoute aux compteur +1 a cptrJn[5] et cptrJn[etat] si un bateau est
  touche. Ensuite, elle retournera 1 si tout va bien on passe au tour suivant, 0
  si le Jn doit rejouer. */
int compterPts_finirTour(int etat, int cptrJn[6]) {
  int passage = 0;

  if (etat == -1) {
    printf("A l'eau !\n");
    passage = 1;
  }
  
  /* On gere les cas où le joueur rejoue, et où on renvoie un tour. */

  /*Les erreurs : */
  if (etat == -2) {
    printf("Mauvais coup, vous avez deja joue sur cette case. Rejouez.\n");
  }
  if (etat == -3) {
    printf("Hors du plateau ou entree incorrecte. Rejouez.\n");
  }

  /*Les touches et les bateaux coules.*/
  if (etat >= 0) {
    printf("Touche !\n");
    cptrJn[5]++;
    cptrJn[etat]++;

    if ((cptrJn[0] == 5) || (cptrJn[1] == 4) || (cptrJn[2] == 3) ||
        (cptrJn[3] == 3) || cptrJn[4] == 2) {
      /* Si un bateau a ete coule, on l'annonce et on rajoute 1 au compteur de
    coups sur ce bateau */
      printf("Tu as coule le %s.\n", navire(etat));
      cptrJn[etat]++;
    }
  }
  return passage;
}