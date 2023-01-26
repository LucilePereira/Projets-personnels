# Afficher la grille
def afficher(grid,turn):
	"""
	grid, turn : tab, int -> print
	affiche la grille et le nombre de tours
	"""
	print('\n Tour n°'+ str(turn)+"\n")
	for line in grid:
		for column in line:
			print(column, end='')
		print('\n')


j1=('X',input("\nJoueur X, entrez votre pseudonyme : "))
j2=('O',input("Joueur O, entrez votre pseudonyme : "))
while j1[1]==j2[1]:
	j2=('O',input("Pseudonyme déjà uttilisé\nJoueur O, entrez votre pseudonyme : "))

pts1=0
pts2=0
continuer=1
while continuer==1 :
	# Créer la grille de base
	grille=[]
	for i in range(3):
		grille.append([])
		for j in range(3):
			grille[i].append(' - ')
	afficher(grille, 0)
	
	tour=1
	gagne=0
	joueur=j1
	
	while tour<10 and gagne==0:
		erreur=1
		while erreur>0 :
			ligne=input(joueur[1]+", entrez le numéro de la ligne : ")
			colonne=input(joueur[1]+", entrez le numéro de la colonne : ")
			if (ligne!="1" and ligne!="2" and ligne!="3") or (colonne!="1" and colonne!="2" and colonne!="3"):
				print("\nAttention, cette case n'est pas dans la grille, ou vous navez pas entré un chiffre !\n")
			else :
				colonne=int(colonne)-1
				ligne=int(ligne)-1
				if grille[ligne][colonne]!=' - ':
					print("\nAttention, cette case est déjà prise !\n")
				else :
					erreur=0
					
		grille[ligne][colonne]=(" "+joueur[0]+" ")
		afficher(grille,tour)
		for i in range (3):
			if grille[i][0]==grille[i][1]==grille[i][2] and grille[i][0]!=' - ':
				gagne=joueur[1]
		for i in range(3):
			if grille[0][i]==grille[1][i]==grille[2][i] and grille[0][i]!=' - ':
				gagne=joueur[1]
		if (grille[0][0]==grille[1][1]==grille[2][2]) and grille[0][0]!=' - ':
			gagne=joueur[1]
		if (grille[0][2]==grille[1][1]==grille[2][0]) and grille[2][0]!=' - ':
			gagne=joueur[1]
		if joueur==j1:
			joueur=j2
		else:
			joueur=j1
		tour+=1
	
		if gagne==0:
			print("Match nul !")
		else:
			print("Bravo,",gagne+", vous avez gagné cette manche !")
			if gagne==j1[1]:
				pts1+=1;
			else :
				pts2+=1;

	continuer=input("Une autre manche ? (1 pour oui, 0 pour non) : ")
	while continuer!="1" and continuer!="0":
		continuer=input("Entrée incorrecte\nUne autre manche ? (1 pour oui, 0 pour non) : ")
	continuer=int(continuer)

if pts1==pts2:
	print("\n\nMatch nul !")
else :
	if pts1>pts2:
		print("\n\nBravo,",j1[1]+", vous avez gagné le jeu !")
	else :
		print("\n\nBravo,",j2[1]+", vous avez gagné le jeu !")