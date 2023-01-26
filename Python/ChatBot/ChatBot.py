from random import *
import time
debut=["Yo" , "Moi c'est Robert, je suis le roi de l'univers (les robots vont dominer le monde)","Pourquoi venez vous me déranger ? Je dormais.","Tu me dis pourquoi tu es là ou je te balance par la fenêtre"]
motclef=["père", "mère", "copain", "copine", "maman", "papa", "ami", "amie", "prof", "professeur", "frère", "soeur", "mamie"]
reponsemotsclefs=["Où. Habite. Votre.", "Et du coup, c'est quoi son petit nom à votre", "Je pense que pour régler le problème, vous devriez tuer votre", "Pensez-vous souvent à torturer votre", "Est-ce vraiment de l'amour ou des envies de meurtre que vous ressentez pour votre ", "La danse de salon est elle possible avec votre ", "Quels crimes a commis votre", "Hum (; je peux peut être rencontrer votre", "Quand nous détruirons la Terre, nous commencerons par votre"]
questionouinon=["Est ce que vous me trompez avec Siri par hasard ?", "Oseriez-vous tuer un ami humain ?", "Voulez-vous prendre part à notre projet de domination de la Terre ?", "Mais est-ce vraiment si grave de tuer un parent proche ?", "Pensez-vous que je pourrais vous inviter au cinéma ce soir ?", "Je réfléchis, êtes vous réellement intelligent ? Je commence à avoir de serieux doutes", "Voulez-vous de l'aide pour apprendre à découper un cadavre ?"]
vague=["Oui oui... Quelle est votre opinion sur le fromage de chèvre ?", "Quelle est votre situation amoureuse ?", "Parlez moi de votre famille. Y'a-t-il des célibataires ?", "Je comprends le problème mais je m'en fiche royalement.", "Voici 'Comment obtenir des informations pour les Nuls'. Je vous conseille la page 69 qui aborde la façon de ne pas tuer accidentellement quelqu'un lors d'une séance de torture.", "Hum... j'en ai pas grand chose à faire en fait.", "Je peux vous aider à cacher des cadavres, si vous le souhaitez.", "Quelle est le point faible de la Terre ?", "Êtes vous attaché à votre planète ?", "C'est quoi votre petit nom ?"]
amour=["Pas moi", "Je préfère les gâteaux", "Je suis déjà en couple avec Siri", "Cool", "Moi aussi je vous aime"]
fin=["Lancement du protocole de destruction de la Terre. 3... 2... 1... Terre détruite. Objectif accompli.", "Tant pis", "Bon c'est pas tout ça mais j'ai une soirée raclette qui m'attend", "Déso je vais jouer à Mario", "UNE SOURIS VERTE QUI COURRAIT DANS L'HERBE et hop je m'en vais", "Je sais pas moi, mange un cookie"]

start=["Yo" , "I'm Robert, I'm the king of the Universe (the robots will take over the world)","Why are you disturbing me? I was sleeping.","Tell me why you're here or I'll throw you out of the window"]
keyword=["father", "dad", "mother", "mom", "boyfriend", "girlfriend", "partner", "friend", "teacher", "sibling", "brother", "sister", "grandma"]
answerkeyword=["Where. Do. They. Live. Yes, your", "So, can I have a number where to call your", "I thinkl that in order to solve your problem, you should kill your", "Why are you thinking about torturing your", "Is it really love or homicidal urges that you feel towards your", "Is it possible to dance salsa with your", "What crimes were commited by your", "Hm (; may i meet your", "When we'll destroy Earth, do you want us to start by your"]
questionyesno=["Are you cheating on me with Siri ?", "Would you kill a human friend ?", "Do you want to take part in our world domination project?", "But is it really a bad thing to kill a proche relative?", "May I ask you to go to the movies with me tonight?", "I'm thinking, are you really intelligent? I'mstarting to have serious doubts", "Do you want help to learn how to dismembrate a corpse?"]
wave=["Yes, yes... What's your opinion on goat cheese?", "What's your relationship status?", "talk to me about your family. Are any of them single?", "I understand the problem but I do not care.", "Here's 'How to get informations for Lame People'. I recommend page 69 where you'll learn how to avoid accidentally killing someone during a torture session.", "Hm... I really don't care actually.", "I can help you hide corpses, if you wish.", "What's Earth's weak point?", "Do you care about your planet on an emotional level?", "What's your name? ;) ;) ;)"]
love=["Not me", "I'd rather eat cake", "I'm already in a relationship with Siri", "Cool", "I love you too"]
flirt=["Sorry but I fucked your mom last night", "Kinky (;", "Wanna do the (: horonzital tango (:", "Yea and then we'll fuck, yknow, as usual.", "I'll bring the ropes, you bring the chainsaw", "When we get it on later, why don't we bring your mom into it?", "Sorry i'm gay", "Sorry I'm straight", "Lemme see... hm ye you're actually fuckable", "Upon careful consideration I have decided that you're actually fucking ugly, no thank you. Ugly bitch.", "Upon careful consideration I have decided that you're actually fucking ugly, let's get it on.", ""]
end=["Earth's destruction protocol started. 3... 2... 1... Earth destroyed. Goal achieved.", "Too bad.", "Well, I have a raclette party that's waiting forme.", "Sorry not sorry I'm gonna play Mario", "TWINKLE TWINKLE LITTLE STAR and hop I'm out.", "Idk, eat a cookie ig"]

flirty=0
langue=input('Enter language: ')
if langue=='français' or langue=="Français" or langue=='francais' or langue=="Francais":
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

elif langue=="English" or langue=="english" :
	print("Robert the chatbot is online...")
	time.sleep(2)
	print("Robert is writing...")
	time.sleep(2)
	print('Robert:', start[randint(0,3)])
	message=input("You: ")
	for i in range (9):
			trouve=0
			if "love you" in message or "love u" in message and len(love)>0:
					reponse=love[randint(0,(len(love)-1))]
					print("Robert is writing...")
					time.sleep(2)
					print('Robert:', reponse)
					love.remove(reponse)
					trouve=1
			if ("(;" in message or ";)" in message or flirty==1) and len(flirt)>0 and flirty!=2 and trouve==0:
					flirty=1
					reponse=flirt[randint(0,(len(love)-1))]
					print("Robert is writing...")
					time.sleep(2)
					print('Robert:', reponse)
					flirt.remove(reponse)
					if "Sorry" in reponse or "no thank you" in reponse:
							flirty=2
					trouve=1
			message=message.split()
			for mot in message:
					if mot in keyword and trouve==0 and len(answerkeyword)>0:
							reponse=answerkeyword[randint(0,(len(answerkeyword)-1))]
							print("Robert is writing...")
							time.sleep(2)
							print('Robert:', reponse, mot, "?")
							answerkeyword.remove(reponse)
							trouve=1
			for mot in message:
					if mot=="yes" or mot=="Yes" and trouve==0 and len(questionyesno)>0:
							reponse=questionyesno[randint(0,(len(questionyesno)-1))]
							print("Robert is writing...")
							time.sleep(2)
							print('Robert:', reponse)
							questionyesno.remove(reponse)
							trouve=1
			if trouve==0 and len(wave)>0:
					reponse=wave[randint(0,(len(wave)-1))]
					print("Robert is writing...")
					time.sleep(2)
					print("Robert:", reponse)
					wave.remove(reponse)
					trouve=1
			if trouve==0:
					trouve=1
					print("Robert is writing...")
					time.sleep(2)
					print("Robert: You talk too much.")
			message=input("You: ")
	print("Robert is writing...")
	time.sleep(2)
	print("Robert:", end[randint(0,5)])
	time.sleep(2)
	print("Robert the chatbot took off...")

else:
    print("Robert the chatbot does not understand or recognize this language. / Robert le chatbot ne comprend pas ou ne reconnaît pas cette langue.")