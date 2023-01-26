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
rep1 = Button(fun, text = "Answer 1", width = 20, command = gauche, bg = "#DFCCF0")   # A l'appui sur ce bouton, la fonction droite est déclenchée
rep2 = Button(fun, text = "Answer 2", width = 20, command = droite, bg = "#DFCCF0")   # A l'appui sur ce bouton, la fonction gauche est déclenchée
restart = Button(fun, text = "Restart", width = 20, command = recommencer, bg = "#DFCCF0")   # A l'appui sur ce bouton, la fonction recommencer est déclenchée
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

histoire = ["\n \nYou wake up with a start. You feel asleep this afternoon in \
english literature class. Nobody noticed you, and it is now night time. \
The silence is heavy. What do you do ? \n1. I stay at school and I wait for \
the morning. \n2. I try to get out.", "\n \nYou sit down and fall back asleep. \
You won't ever wake up again, your body dissipates slowly and disappears forever.\
\n  \n ---FIN---", "\n \nYou try to open the door, but the handle will not budge.\
\n1. I look for the key in the desk. \n2. I try to knock down the door", \
"\n \nYou open every drawer one by one. In one of them, you find your \
english literature teacher's sleeping body'. Well... you \
think she is asleep. Distant snickers makes you uneasy, and you hesitate. \
\n1. I quickly close the drawer \n2. I search my teacher in hopes of finding \
the key.", "\n \nYour hand on the handle, you go to break down the door, when \
you feel the handle griping your hand. You still try to force the door, \
only to slide through it. You fuse with the door, and \
you will now be one until the end of times. \n  \n ---THE END---", "\n \nYou \
slam the drawer shut, and the sound reverberates on the walls. The \
desk suddenly seems bigger. After a few instants, it is \
taller than you. Its drawers open again, and it swallows you whole. \
\n \n ---THE END---", "\n \nYou find your exam's papers, and the room's key. It \
seems strangely slimy. Before leaving, you take a look through the window \
and notice the sun shinning. The sky is still ink black, and you \
quickly get away from this vision makes you shiver. You open the door \
and find yourself in the hall. Insistant whispers come from the A312i room. \
You open the door, and the noises stop. You turn back, \
and find yourself in front of a crowd of silhouettes whose traits you can't \
decipher. \n1. I push them and escape towards the stairs. \n2. I \
step into the room and close the door behind me.", "\n \nYou push away the \
shapes, that seem to vanish as soon as you touch them. You run towards \
the stairs, your heart pounding wildly in your chest. Through the window, you see \
the playground basking in a strange violet glow. You turn back, and you realize \
the elevator's doors are open. You hesitate. \n1. I take the stairs. \n2. \
I get in the elevator.", "\n \nThe whispers start again, despite the fact \
that you are alone in the room. They become more and more insufferable. \
\n1. I try to shush them. \n2. I cover my ears so as to not hear \
them.", "\n \nYou start to go down the stairs when you hear quick \
steps behind you. You turn back, but don't see anything. You \
continue to go down. \n1. I don't hurry, but I stay careful. \n2. \
You start to run.", "\n \nAs soon as you get inside, the doors close. The \
elevator starts to go down, but instead of stopping at the ground floor, \
it continues. Faster and faster , you go down, to such an extent that it seems \
to you that you are now in free fall. The speed starts to make you lose conscience \
of your body, and finally, you lose your mind, while you stay stuck in an \
infinite fall. \n  \n ---THE END---", "\n \nThe whispers intensify and you feel \
vocal cords are unable to make a sound. You cannot scream just as \
your face, like your vocal cords, \
melts. You become of one the shapes. \n  \n ---THE END---", "\n \nYou feel your \
hands fusing with your ears. Out of pain, you collapse to the floor, and you \
slowly feel each of your limbs fusing with the rest of your body. Finally, you \
are nothing more than a shapeless bundle of flesh. \n  \n ---THE END---", "\n \nYou \
feel you cannot move forward anymore. You walk but don't seem to move. Seized \
with panic, you turn back, and your last vision before falling backwards is your \
computing science teachers chasing themselves. You \
bang your crane on the floor, and your blood will forever stain these steps. \
\n  \n ---THE END---", "\n \nOut of breath, you get at the foot of the stairs \
and put your hand on the wall to regain your forces. the wall seem squishy and \
you see blood dripping from the ceiling. When eyes start to open in the wall, you \
remove your hand, horrified. You decide to continue. You have two options. You \
leave by the door, which is wide open and from which radiates a blinding white \
light. Otherwise, you see a window at the end of the hall through which you can \
see the playground, which seems basked in a troubling orange light. \n1. I leave \
by the door. \n2. I open the window and get out through it.", "\n \nYou find \
yourself back in the english literature room. You hear a phone ringing \
towards your teacher's desk. You pick up, and a feminine voice informs you \
are cursed to take the same path over and over again, until \
the end of times. \n  \n ---THE END---", "\n \nYou fall onto a small patch of \
grey flowers. Around you, everything seems to have lost its colors. In the \
distance, you catch a glimpse of the gate. You see reality undulating and \
twisting under your eye, and a void forms in the stairs' place. No light, no \
shade, nothing. The buildings start to distort, sucked into this gaping hole \
in the canvas of the universe. Time is running out. \n1. I hop into the \
void. \n2. I run towards the still closed gate, avoiding the whirlwind of \
reality.", "\n \nYou enter the void and watch as thousands of lights \
rush around you. You realize these lights are in reality white whales, \
swimming at full speed towards an unknown goal. \
You sit down and slowly decay, taking in the sight of the floating space \
whales.\n \n ---YOU LOSE---", "\n \nYou run towards the gate at full speed, \
zigzagging between the fragments of what remains of your school. You cross the \
metal gate without stopping, and you are suddenly blinded by a bright purple \
light. You hear some noise, and you turn back. You are now in front of your \
school, as it had always been. The students come and go, the bell rings. It is \
8:25am, and you have to go to philosophy class. \n \n ---YOU WON---"]

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
