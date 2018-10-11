print "Chose username"
username = raw_input("  >")
print "Hi %r" %username
def startgame():
	print "The game is starting"
	print "Race is loading beep boop"
	print "It's a racing game and here are your options"
	print"you are in twelth place"
	print "one.start on red light"
	print "two.start at yellow light"
	print "three.start on  green light"
	option = raw_input ("  >")
	if option == "one":
		print "you are disqualifed"
		lostgame()
	if option == "two":
		print"you get a speedboost"
		print speedboost
		print"you are now in 11th place"
		race2()
	elif option == "three":
		print "you are still in 12th place , but are cathing up"
		race3()
	else :
		print"you can't even choose a corret option"
		print"you suck"
		lostgame()
		
		
speedboost = "you zoom ahead by one place"

def lostgame():
	print "Game over %r" %username
	quit(0)

def wingame():
	print "Congratuations %r you won" %username
	read(win.txt)


def race2():
	print"you slowly work your way up to 5th place"
	print"to boost further answer the question correctly"
	print "Does not(true and false) return true or false"
	if raw_input("  >") == 't' or 'T':
		print speedboost  * 11
		wingame()
	else :
		print "your car starts smoking and the car breaks down"
		lostgame()
def race3():
	print"you are in 8th place"
	print"you can awnser this question to boost"
	print "what is your username"
	if raw_input("  >") == username:
		wingame()
	else:
		print"wrong answer"
		lostgame()
	
	
	
startgame()

	

	
 