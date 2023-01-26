from arbre_binaire import ArbreBinaire

# On implémente la liste histoire avce toutes les pharses de l'histoire

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

# On implémente l'arbre binaire sequoia avec tous les indices de la liste histoire
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


def horror_begins (question, histoire):
    """
    question : ArbreBinaire, histoire : list -> None
    affiche l'histoire en prenant en compte les choix du joueur
    """
    print(histoire[question.get_valeur()]) # On affiche la suite de l'histoire

    if '---' not in histoire[question.get_valeur()]: # Si ce n'est pas une fin
        reponse = int(input('\nEnter your choice: ')) # On demande le choix du joueur

        # On redemande la réponse du joueur si la réponse n'est pas 1 ou 2
        while reponse != 1 and reponse != 2:
            reponse = int(input('\nPlease enter a valid answer (1 or 2).\n'))

        # On affiche la suite de l'histoire selon la réponse du joueur
        if reponse == 2:
            horror_begins (question.get_droite(), histoire)
        else:
            horror_begins (question.get_gauche(), histoire)

# On lance le jeu
horror_begins(sequoia, histoire)
