
start=["Yo" , "I'm Robert, I'm the king of the Universe (the robots will take over the world)","Why are you disturbing me? I was sleeping.","Tell me why you're here or I'll throw you out of the window"]
keyword=["father", "dad", "mother", "mom", "boyfriend", "girlfriend", "partner", "friend", "teacher", "sibling", "brother", "sister", "grandma"]
answerkeyword=["Where. Do. They. Live. Yes, your", "So, can I have a number where to call your", "I thinkl that in order to solve your problem, you should kill your", "Why are you thinking about torturing your", "Is it really love or homicidal urges that you feel towards your", "Is it possible to dance salsa with your", "What crimes were commited by your", "Hm (; may i meet your", "When we'll destroy Earth, do you want us to start by your"]
questionyesno=["Are you cheating on me with Siri ?", "Would you kill a human friend ?", "Do you want to take part in our world domination project?", "But is it really a bad thing to kill a proche relative?", "May I ask you to go to the movies with me tonight?", "I'm thinking, are you really intelligent? I'mstarting to have serious doubts", "Do you want help to learn how to dismembrate a corpse?"]
wave=["Yes, yes... What's your opinion on goat cheese?", "What's your relationship status?", "talk to me about your family. Are any of them single?", "I understand the problem but I do not care.", "Here's 'How to get informations for Lame People'. I recommend page 69 where you'll learn how to avoid accidentally killing someone during a torture session.", "Hm... I really don't care actually.", "I can help you hide corpses, if you wish.", "What's Earth's weak point?", "Do you care about your planet on an emotional level?", "What's your name? ;) ;) ;)"]
love=["Not me", "I'd rather eat cake", "I'm already in a relationship with Siri", "Cool", "I love you too"]
flirt=["Sorry but I fucked your mom last night", "Kinky (;", "Wanna do the (: horonzital tango (:", "Yea and then we'll fuck, yknow, as usual.", "I'll bring the ropes, you bring the chainsaw", "When we get it on later, why don't we bring your mom into it?", "Sorry i'm gay", "Sorry I'm straight", "Lemme see... hm ye you're actually fuckable", "Upon careful consideration I have decided that you're actually fucking ugly, no thank you. Ugly bitch.", "Upon careful consideration I have decided that you're actually fucking ugly, let's get it on.", ""]
end=["Earth's destruction protocol started. 3... 2... 1... Earth destroyed. Goal achieved.", "Too bad.", "Well, I have a raclette party that's waiting forme.", "Sorry not sorry I'm gonna play Mario", "TWINKLE TWINKLE LITTLE STAR and hop I'm out.", "Idk, eat a cookie ig"]

flirty=0

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