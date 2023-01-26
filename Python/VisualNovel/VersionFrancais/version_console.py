from tkinter import *
from arbre_binaire import ArbreBinaire



########################################################
##  Les fonctions appelées à l'appui sur les boutons  ##
########################################################

def gauche():
    """
    A l'appui sur le bouton gauche, affiche la suite de l'histoire en
    prenant le sous-arbre gauche de sequoia.
    """
    global sequoia, histoire, dessin, tableau, cadre_histoire

    sequoia = sequoia.get_gauche()

    dessin = PhotoImage(file=illustrations[sequoia.get_valeur()])
    img = tableau.create_image(450,225, image = dessin)
    tableau.itemconfigure(img, image = dessin)
    tableau.image = dessin

    cadre_histoire.configure(state = 'normal')
    cadre_histoire.delete(1.0, "end")
    cadre_histoire.insert("insert +1 chars", "\n" + histoire[sequoia.get_valeur()])
    cadre_histoire.configure(state = 'disabled')

    if '---'  in histoire[sequoia.get_valeur()]:
        rep1.config(state = DISABLED, bg = "#9f9f9f")
        rep2.config(state = DISABLED, bg = "#9f9f9f")

def droite():
    """
    A l'appui sur le bouton droit, affiche la suite de l'histoire en
    prenant le sous-arbre droit de sequoia.
    """
    global sequoia, histoire, dessin, tableau, cadre_histoire

    sequoia = sequoia.get_droite()

    dessin = PhotoImage(file = illustrations[sequoia.get_valeur()])
    img = tableau.create_image(450, 225, image = dessin)
    tableau.itemconfigure(img, image = dessin)
    tableau.image = dessin

    cadre_histoire.configure(state = 'normal')
    cadre_histoire.delete(1.0, "end")
    cadre_histoire.insert("insert +1 chars", "\n" + histoire[sequoia.get_valeur()])
    cadre_histoire.configure(state = 'disabled')

    if '---'  in histoire[sequoia.get_valeur()]:
        rep1.config(state = DISABLED, bg = "#9f9f9f")
        rep2.config(state = DISABLED, bg = "#9f9f9f")

def recommencer():
    """
    A l'appui sur le bouton du milieu, recommence toute l'histoire à 0.
    """
    global sequoia, histoire, dessin, tableau, cadre_histoire, ginko

    sequoia = ginko

    rep1.config(state = NORMAL, bg = "#DFCCF0")
    rep2.config(state = NORMAL, bg = "#DFCCF0")

    dessin = PhotoImage(file="images/image1.png")
    img=tableau.create_image(450,225, image=dessin)
    tableau.itemconfigure(img, image = dessin)
    tableau.image = dessin

    cadre_histoire.configure(state='normal')
    cadre_histoire.delete(1.0,"end")
    cadre_histoire.insert("insert +1 chars", "\n" + histoire[sequoia.get_valeur()])
    cadre_histoire.configure(state='disabled')



##############################################
##  Création de la fenetre graphique en TK  ##
##############################################

fun = Tk()                     # Création d'une fenêtre graphique nommée ici fun
fun.geometry("950x1000")       # Taille de la fenêtre
fun.title("Eldritch Fantasy")  # Titre de ma fenêtre
fun["background"] = "#CCF0CD"  # On change la couleur du fond



###########################################
##  Les Widgets utilisés pour le projet  ##
###########################################

tableau = Canvas(fun, width = 900, height = 450)                                       # Création d'une fenêtre de dessin dans la fenêtre graphique
rep1 = Button(fun, text = "Réponse 1", width = 20, command = gauche, bg = "#DFCCF0")   # A l'appui sur ce bouton, la fonction droite est déclenchée
rep2 = Button(fun, text = "Réponse 2", width = 20, command = droite, bg = "#DFCCF0")   # A l'appui sur ce bouton, la fonction gauche est déclenchée
restart = Button(fun, text = "Recommencer", width = 20, command = recommencer, bg = "#DFCCF0")   # A l'appui sur ce bouton, la fonction recommencer est déclenchée
cadre_histoire = Text(fun, width = 60, height = 10, font = ("Times New Roman", 20))    # Fenêtre de texte pour faire afficher du texte long
dessin = PhotoImage(file = "images/image1.png")                                        # Création d'une variable image en chargeant le fichier image
titre = Label(fun, text = " ELDRITCH  FANTASY ", font = ("Times New Roman", 30), bg = "#BAE5BB")



##################################
##  Les affichages des Widgets  ##
##################################

titre.grid(row = 0, column = 1, columnspan = 2, padx = 25, pady = 5)
cadre_histoire.grid(row = 2, column = 1, columnspan = 2, padx = 25, pady = 10)
rep1.grid(row = 3, column = 1, columnspan = 1, padx = 10, pady = 10)
rep2.grid(row = 3, column = 2, columnspan = 1, padx = 10, pady = 10)
restart.grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 10)

tableau.grid(row = 1, column = 1, columnspan = 2, padx = 25, pady = 5)
tableau.create_image(450, 225, image = dessin)                                          # Pour afficher l'image à la position donnée



#############################################################################
##  On implémente la liste histoire avec toutes les phrases de l'histoire  ##
#############################################################################

histoire = ["Tu te réveilles en sursaut. Tu t'es endormi cet après-midi dans ton \
cours de littérature anglaise. Personne ne t'a remarqué, et il fait maintenant \
nuit. Le silence est pesant. Que fais-tu ? \n1. Je reste au lycée et j'attends \
le matin. \n2. Je tente de sortir.", "\nTu t'assieds, et tu te rendors. Tu ne te \
réveilleras plus, ton corps se dissipant lentement pour disparaître à jamais.\
\n  \n ---TU AS PERDU---", "\nTu tentes d' ouvrir la porte, mais la poignée ne bouge pas.\
\n1. Je vais chercher si la clé est dans le bureau. \n2. J'essaie d'enfoncer \
la porte.", "\nTu ouvres tous les tiroirs un à un. Dans l'un d'eux, tu trouves \
le corps endormi de ta professeure de littérature anglaise. Enfin... tu \
penses qu'elle est endormie. Un bruit lointain de ricanements te met mal à \
l'aise, et tu hésites. \n1. Je ferme vite le tiroir. \n2. Je fouille ma \
professeure.", "\nTa main sur la poignée, tu vas pour enfoncer la porte, quand \
tu sens la poignée qui t'attrape la main. Tu tentes tout de même d'enfoncer \
la porte, seulement pour passer au travers. Tu fusionnes avec la porte, et \
vous ne faites plus qu'un jusqu'à la fin des temps. \n  \n ---TU AS PERDU---", "\nTu \
refermes brutalement le tiroir, et le bruit se réverbère sur les murs. Le \
bureau semble soudainement plus grand. Au bout de quelques instants, il est \
plus grand que toi. Ses tiroirs s'ouvrent à nouveau, et il t'avale tout entier. \
\n ---TU AS PERDU---", "\nTu trouves les copies du bac blanc, et la clé de la salle. Elle \
semble étrangement visqueuse. Avant de sortir, tu jettes un œil par la fenêtre \
et tu remarques que le soleil brille. Le ciel est toujours d'encre, et tu \
t'écartes rapidement de cette vision qui te fait frissonner. Tu ouvres la porte \
et te retrouves dans le couloir. Des chuchotements insistants te parviennent \
depuis la salle A312i. Tu ouvres la porte, et les bruits s'arrêtent. Tu te \
retournes, et te retrouves face à une foule de silhouettes dont tu ne peux \
discerner les traits. \n1. Je les pousse et je fuis vers l'escalier. \n2. Je \
rentre dans la salle et je ferme la porte derrière moi.", "\nTu écartes les \
figures, qui semblent s'évanouir dès que tu les touches. Tu cours vers \
l'escalier, ton cœur battant à vive allure. Par la fenêtre, tu vois la cour \
baignée d'une étrange lueur violette. Tu te retournes, et tu t'aperçois que la \
porte de l'ascenseur est ouverte. Tu hésites. \n1. Je prends l'escalier. \n2. \
Je monte dans l'ascenseur.", "\nLes chuchotements reprennent, malgré le fait \
que tu sois seul dans la salle. Ils deviennent de plus en plus insupportables. \
\n1. Je décide de dire CHUUTTT. \n2. Je me couvre les oreilles pour ne plus \
les entendre.", "\nTu commences à descendre l'escalier quand tu entends des \
bruits de pas rapides derrière toi. Tu te retournes, mais tu ne vois rien. Tu \
continues à descendre. \n1. Je ne me presse pas, mais je reste prudent. \n2. \
Je me mets à courir.", "\nA peine es-tu entré que les portes de l'ascenseur se \
ferment. Il commence à descendre, mais au lieu de s'arrêter au rez-de-chaussée, \
il continue. De plus en plus vite, tu descends, à tel point qu'il te semble \
désormais être en chute libre. La vitesse commence à te faire perdre conscicence \
de ton corps, et finalement, tu perds l'esprit, alors que tu restes bloqué dans \
une chute infinie. \n  \n ---TU AS PERDU---", "\nLes chuchotements s'intensifient et tu sens \
tes cordes vocales incapable de produire un quelconque son, et tu n'es pas \
capable de crier alors même que ton visage, à l'image de tes cordes vocales, \
fond. Tu deviens l'une des figures. \n  \n ---TU AS PERDU---", "\nTu sens que tes mains sont \
en train de fusionner avec tes oreilles, tu t'écroules au sol de douleur et \
sens chacun de tes membres lentement fusionner avec le reste de ton corps. \
Finalement, tu ne formes plus qu'une masse de chair informe. \n  \n ---TU AS PERDU---", "\nTu \
sens que tu ne peux plus avancer. Tu marches, mais tu ne descends plus. Pris de \
panique, tu te retournes, et la dernière image que tu vois avant de tomber en \
arrière est celle de tes professeures de NSI en train de se fuir elles-même. Tu \
te fracasses le crâne sur le sol, et ton sang tâchera à jamais ces escaliers. \
\n  \n ---TU AS PERDU---", "\nTu arrives en bas essoufflé, et tu poses ta main sur le mur pour \
retrouver tes forces. Le mur semble spongieux, et tu vois du sang couler depuis \
le plafond. Lorsque des yeux commencent à s'ouvrir dans le mur, tu enlèves ta \
main, horrifié. Tu décides de continuer. Tu as deux options. Tu peux sortir par \
la porte, qui est grande ouverte et dont émane une aveuglante lumière blanche. \
Sinon, tu vois une fenêtre au bout du couloir par laquelle tu peux voir \
la cour, qui semble baignée dans une inquiétante lumière orange. \n1. Je sors \
par la porte. \n2. J'ouvre la fenêtre et je l'enjambe.", "\nTu te retrouves à \
nouveau dans la salle de littérature anglaise, tu entends une sonnerie de \
téléphone vers le bureau de ta professeure. Tu décroches et une voix féminine \
t'informes que tu t'apprêtes à recommencer encore et encore le même chemin, et \
ce, à tout jamais. \n  \n ---TU AS PERDU---", "\nTu tombes dans un petit parterre de fleurs \
grises. Autour de toi, tout semble avoir perdu sa couleur. Au loin, tu aperçois \
le portail. Tu vois la réalité onduler et se déformer sous tes yeux, et un vide \
se forme là où se tenaient précédemment les escaliers. Pas de lumière, pas \
d'ombre, rien. Le reste du lycée commence à tourbillonner, comme aspiré par ce \
trou béant dans la toile de l'univers. Le temps presse. \n1. Je décide de sauter \
à pieds joints dans le vide. \n2. Je cours vers le portail en évitant le \
tourbillon.", "\nTu rentres dans le vide et tu observes des milliers de lumières \
filer à toute vitesse autour de toi. Tu te rends compte que ces lumières sont \
en réalité des baleines blanches, nageant à toute allure vers un but inconnu. \
Tu t'assieds en tailleur et dépéris lentement, admirant la nage des baleines de \
l'espace.\n ---TU AS PERDU---", "\nTu fonces vers le portail, toujours fermé. Tu slalomes \
entre les débris de ce qui reste de ton lycée. Tu traverses le métal sans \
t'arrêter, et tu es soudainement ébloui par une vive lumière pourpre. Tu entends \
du bruit, et tu te retournes. Tu te tiens désormais devant ton lycée, comme il a \
toujours été. Les élèves entrent et sortent, la sonnerie retentit. Il est 8h25 \
du matin, et tu as cours de philosophie. \n ---TU AS GAGNÉ---"]

illustrations = ["images/image1.png", "images/image2.png", "images/image3.png",
"images/image4.png", "images/image5.png", "images/image6.png",
"images/image7.png","images/image8.png", "images/image9.png",
"images/image10.png", "images/image11.png","images/image12.png",
"images/image13.png", "images/image14.png", "images/image15.png",
"images/image16.png", "images/image17.png", "images/image18.png",
"images/image19.png"]



########################################################################################
##  On implémente l'arbre binaire sequoia avec tous les indices de la liste histoire  ##
########################################################################################

sequoia = ArbreBinaire(0)

sequoia.ajouter_gauche(1)
sequoia.ajouter_droite(2)
branche = sequoia.get_droite()

branche.ajouter_gauche(3)
branche.ajouter_droite(4)
branche = branche.get_gauche()

branche.ajouter_gauche(5)
branche.ajouter_droite(6)
branche = branche.get_droite()

branche.ajouter_gauche(7)
branche.ajouter_droite(8)
feuille = branche.get_droite()

feuille.ajouter_gauche(11)
feuille.ajouter_droite(12)
branche = branche.get_gauche()

branche.ajouter_gauche(9)
branche.ajouter_droite(10)
branche = branche.get_gauche()

branche.ajouter_gauche(13)
branche.ajouter_droite(14)
branche = branche.get_droite()

branche.ajouter_gauche(15)
branche.ajouter_droite(16)
branche = branche.get_droite()

branche.ajouter_gauche(17)
branche.ajouter_droite(18)



#############################################################################
##  On crée une copie de sequoia pour pouvoir recommencer le jeu à la fin  ##
#############################################################################

ginko = sequoia


cadre_histoire.insert("insert +1 chars", "\n" + histoire[sequoia.get_valeur()])
cadre_histoire.configure(state = 'disabled')

fun.mainloop() # La fenêtre est maintenant "à l'affût" de ce qui se passe
