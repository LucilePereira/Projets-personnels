from arbre_binaire import ArbreBinaire

# On implémente la liste histoire avce toutes les pharses de l'histoire

histoire = ["\n \nTu te réveilles en sursaut. Tu t'es endormi cet après-midi dans ton \
cours de littérature anglaise. Personne ne t'a remarqué, et il fait maintenant \
nuit. Le silence est pesant. Que fais-tu ? \n1. Je reste au lycée et j'attends \
le matin. \n2. Je tente de sortir.", "\n \nTu t'assieds, et tu te rendors. Tu ne te \
réveilleras plus, ton corps se dissipant lentement pour disparaître à jamais.\
\n  \n ---TU AS PERDU---", "\n \nTu tentes d' ouvrir la porte, mais la poignée ne bouge pas.\
\n1. Je vais chercher si la clé est dans le bureau. \n2. J'essaie d'enfoncer \
la porte.", "\n \nTu ouvres tous les tiroirs un à un. Dans l'un d'eux, tu trouves \
le corps endormi de ta professeure de littérature anglaise. Enfin... tu \
penses qu'elle est endormie. Un bruit lointain de ricanements te met mal à \
l'aise, et tu hésites. \n1. Je ferme vite le tiroir. \n2. Je fouille ma \
professeure.", "\n \nTa main sur la poignée, tu vas pour enfoncer la porte, quand \
tu sens la poignée qui t'attrape la main. Tu tentes tout de même d'enfoncer \
la porte, seulement pour passer au travers. Tu fusionnes avec la porte, et \
vous ne faites plus qu'un jusqu'à la fin des temps. \n  \n ---TU AS PERDU---", "\n \nTu \
refermes brutalement le tiroir, et le bruit se réverbère sur les murs. Le \
bureau semble soudainement plus grand. Au bout de quelques instants, il est \
plus grand que toi. Ses tiroirs s'ouvrent à nouveau, et il t'avale tout entier. \
\n \n ---TU AS PERDU---", "\n \nTu trouves les copies du bac blanc, et la clé de la salle. Elle \
semble étrangement visqueuse. Avant de sortir, tu jettes un œil par la fenêtre \
et tu remarques que le soleil brille. Le ciel est toujours d'encre, et tu \
t'écartes rapidement de cette vision qui te fait frissonner. Tu ouvres la porte \
et te retrouves dans le couloir. Des chuchotements insistants te parviennent \
depuis la salle A312i. Tu ouvres la porte, et les bruits s'arrêtent. Tu te \
retournes, et te retrouves face à une foule de silhouettes dont tu ne peux \
discerner les traits. \n1. Je les pousse et je fuis vers l'escalier. \n2. Je \
rentre dans la salle et je ferme la porte derrière moi.", "\n \nTu écartes les \
figures, qui semblent s'évanouir dès que tu les touches. Tu cours vers \
l'escalier, ton cœur battant à vive allure. Par la fenêtre, tu vois la cour \
baignée d'une étrange lueur violette. Tu te retournes, et tu t'aperçois que la \
porte de l'ascenseur est ouverte. Tu hésites. \n1. Je prends l'escalier. \n2. \
Je monte dans l'ascenseur.", "\n \nLes chuchotements reprennent, malgré le fait \
que tu sois seul dans la salle. Ils deviennent de plus en plus insupportables. \
\n1. Je décide de dire CHUUTTT. \n2. Je me couvre les oreilles pour ne plus \
les entendre.", "\n \nTu commences à descendre l'escalier quand tu entends des \
bruits de pas rapides derrière toi. Tu te retournes, mais tu ne vois rien. Tu \
continues à descendre. \n1. Je ne ne presse pas, mais je reste prudent. \n2. \
Tu te mets à courir.", "\n \nA peine es-tu entré que les portes de l'ascenseur se \
ferment. Il commence à descendre, mais au lieu de s'arrêter au rez-de-chaussée, \
il continue. De plus en plus vite, tu descends, à tel point qu'il te semble \
désormais être en chute libre. La vitesse commence à te faire perdre conscicence \
de ton corps, et finalement, tu perds l'esprit, alors que tu restes bloqué dans \
une chute infinie. \n  \n ---TU AS PERDU---", "\n \nLes chuchotements s'intensifient et tu sens \
tes cordes vocales incapable de produire un quelconque son, et tu n'es pas \
capable de crier alors même que ton visage, à l'image de tes cordes vocales, \
fond. Tu deviens l'une des figures. \n  \n ---TU AS PERDU---", "\n \nTu sens que tes mains sont \
en train de fusionner avec tes oreilles, tu t'écroules au sol de douleur et \
sens chacun de tes membres lentement fusionner avec le reste de ton corps. \
Finalement, tu ne formes plus qu'une masse de chair informe. \n  \n ---TU AS PERDU---", "\n \nTu \
sens que tu ne peux plus avancer. Tu marches, mais tu ne descends plus. Pris de \
panique, tu te retournes, et la dernière image que tu vois avant de tomber en \
arrière est celle de tes professeures de NSI en train de se fuir elles-même. Tu \
te fracasses le crâne sur le sol, et ton sang tâchera à jamais ces escaliers. \
\n  \n ---TU AS PERDU---", "\n \nTu arrives en bas essoufflé, et tu poses ta main sur le mur pour \
retrouver tes forces. Le mur semble spongieux, et tu vois du sang couler depuis \
le plafond. Lorsque des yeux commencent à s'ouvrir dans le mur, tu enlèves ta \
main, horrifié. Tu décides de continuer. Tu as deux options. Tu peux sortir par \
la porte, qui est grande ouverte et dont émane une aveuglante lumière blanche. \
Sinon, tu vois une fenêtre au bout du couloir par laquelle tu peux voir \
la cour, qui semble baignée dans une inquiétante lumière orange. \n1. Je sors \
par la porte. \n2. J'ouvre la fenêtre et je l'enjambe.", "\n \nTu te retrouves à \
nouveau dans la salle de littérature anglaise, tu entends une sonnerie de \
téléphone vers le bureau de ta professeure. Tu décroches et une voix féminine \
t'informes que tu t'apprêtes à recommencer encore et encore le même chemin, et \
ce, à tout jamais. \n  \n ---TU AS PERDU---", "\n \nTu tombes dans un petit parterre de fleurs \
grises. Autour de toi, tout semble avoir perdu sa couleur. Au loin, tu aperçois \
le portail. Tu vois la réalité onduler et se déformer sous tes yeux, et un vide \
se forme là où se tenaient précédemment les escaliers. Pas de lumière, pas \
d'ombre, rien. Le reste du lycée commence à tourbillonner, comme aspiré par ce \
trou béant dans la toile de l'univers. Le temps presse. \n1. Je décide de sauter \
à pieds joints dans le vide. \n2. Je cours vers le portail en évitant le \
tourbillon.", "\n \nTu rentres dans le vide et tu observes des milliers de lumières \
filer à toute vitesse autour de toi. Tu te rends compte que ces lumières sont \
en réalité des baleines blanches, nageant à toute allure vers un but inconnu. \
Tu t'assieds en tailleur et dépéris lentement, admirant la nage des baleines de \
l'espace.\n \n ---TU AS PERDU---", "\n \nTu fonces vers le portail, toujours fermé. Tu slalomes \
entre les débris de ce qui reste de ton lycée. Tu traverses le métal sans \
t'arrêter, et tu es soudainement ébloui par une vive lumière pourpre. Tu entends \
du bruit, et tu te retournes. Tu te tiens désormais devant ton lycée, comme il a \
toujours été. Les élèves entrent et sortent, la sonnerie retentit. Il est 8h25 \
du matin, et tu as cours de philosophie. \n \n ---TU AS GAGNÉ---"]

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
        reponse = int(input('\nEntrez votre choix : ')) # On demande le choix du joueur

        # On redemande la réponse du joueur si la réponse n'est pas 1 ou 2
        while reponse != 1 and reponse != 2:
            reponse = int(input('\nVeuillez entrer une réponse valide (1 ou 2).\n'))

        # On affiche la suite de l'histoire selon la réponse du joueur
        if reponse == 2:
            horror_begins (question.get_droite(), histoire)
        else:
            horror_begins (question.get_gauche(), histoire)

# On lance le jeu
horror_begins(sequoia, histoire)
