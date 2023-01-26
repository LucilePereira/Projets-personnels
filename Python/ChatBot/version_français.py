from random import *
import time
debut=["Yo" , "Moi c'est Robert, je suis le roi de l'univers (les robots vont dominer le monde)","Pourquoi venez vous me déranger ? Je dormais.","Tu me dis pourquoi tu es là ou je te balance par la fenêtre"]
motclef=["père", "mère", "copain", "copine", "maman", "papa", "ami", "amie", "prof", "professeur", "frère", "soeur", "mamie"]
reponsemotsclefs=["Où. Habite. Votre.", "Et du coup, c'est quoi son petit nom à votre", "Je pense que pour régler le problème, vous devriez tuer votre", "Pensez-vous souvent à torturer votre", "Est-ce vraiment de l'amour ou des envies de meurtre que vous ressentez pour votre ", "La danse de salon est elle possible avec votre ", "Quels crimes a commis votre", "Hum (; je peux peut être rencontrer votre", "Quand nous détruirons la Terre, nous commencerons par votre"]
questionouinon=["Est ce que vous me trompez avec Siri par hasard ?", "Oseriez-vous tuer un ami humain ?", "Voulez-vous prendre part à notre projet de domination de la Terre ?", "Mais est-ce vraiment si grave de tuer un parent proche ?", "Pensez-vous que je pourrais vous inviter au cinéma ce soir ?", "Je réfléchis, êtes vous réellement intelligent ? Je commence à avoir de serieux doutes", "Voulez-vous de l'aide pour apprendre à découper un cadavre ?"]
vague=["Oui oui... Quelle est votre opinion sur le fromage de chèvre ?", "Quelle est votre situation amoureuse ?", "Parlez moi de votre famille. Y'a-t-il des célibataires ?", "Je comprends le problème mais je m'en fiche royalement.", "Voici 'Comment obtenir des informations pour les Nuls'. Je vous conseille la page 69 qui aborde la façon de ne pas tuer accidentellement quelqu'un lors d'une séance de torture.", "Hum... j'en ai pas grand chose à faire en fait.", "Je peux vous aider à cacher des cadavres, si vous le souhaitez.", "Quelle est le point faible de la Terre ?", "Êtes vous attaché à votre planète ?", "C'est quoi votre petit nom ?"]
amour=["Pas moi", "Je préfère les gâteaux", "Je suis déjà en couple avec Siri", "Cool", "Moi aussi je vous aime"]
fin=["Lancement du protocole de destruction de la Terre. 3... 2... 1... Terre détruite. Objectif accompli.", "Tant pis", "Bon c'est pas tout ça mais j'ai une soirée raclette qui m'attend", "Déso je vais jouer à Mario", "UNE SOURIS VERTE QUI COURRAIT DANS L'HERBE et hop je m'en vais", "Je sais pas moi, mange un cookie"]


flirty=0
print("Robert le chatbot est en ligne...")
time.sleep(2)
print("Robert est en train d'écrire...")
time.sleep(2)
print('Robert :', debut[randint(0,3)])
message=input("Vous : ")
for i in range (9):
		trouve=0
		if "e t'aime" in message and len(amour)>0:
				reponse=amour[randint(0,(len(amour)-1))]
				print("Robert est en train d'écrire...")
				time.sleep(2)
				print('Robert :', reponse)
				amour.remove(reponse)
				trouve=1
		message=message.split()
		for mot in message:
				if mot in motclef and trouve==0 and len(reponsemotsclefs)>0:
						reponse=reponsemotsclefs[randint(0,(len(reponsemotsclefs)-1))]
						print("Robert est en train d'écrire...")
						time.sleep(2)
						print('Robert :', reponse, mot, "?")
						reponsemotsclefs.remove(reponse)
						trouve=1
		for mot in message:
				if mot=="oui" or mot=="Oui" and trouve==0 and len(questionouinon)>0:
						reponse=questionouinon[randint(0,(len(questionouinon)-1))]
						print("Robert est en train d'écrire...")
						time.sleep(2)
						print('Robert :', reponse)
						questionouinon.remove(reponse)
						trouve=1
		if trouve==0 and len(vague)>0:
				reponse=vague[randint(0,(len(vague)-1))]
				print("Robert est en train d'écrire...")
				time.sleep(2)
				print("Robert :", reponse)
				vague.remove(reponse)
				trouve=1
		if trouve==0:
				trouve=1
				print("Robert est en train d'écrire...")
				time.sleep(2)
				print("Robert : Tu parles trop.")
		message=input("Vous : ")
print("Robert est en train d'écrire...")
time.sleep(2)
print("Robert :", fin[randint(0,5)])
time.sleep(2)
print("Robert le chatbot s'est barré...")
