#Elo calculator
def elocalc(elo1, elo2, gameresult):
    expectedresult = (1/(1+pow(10,((elo2-elo1)/400))))
    newelorating = (elo1 + round(100*(gameresult - expectedresult)))
    return newelorating

namefile = open('namelist.txt', 'r')
namelist = []
nametext = namefile.readline()
while nametext:
  namelen = len(nametext)
  if (nametext.find("\n") > -1):
    namevar = namelen-1
    namereplace = str(nametext[:(namevar)])
    namelist.append(namereplace)
  else:
    namelist.append(str(nametext))
  nametext = namefile.readline()
namefile.close()
namelistamount = (len(namelist))

roundwinnersfile = open('roundwinners.txt', 'r')
roundwinnerslist = []
roundwinnerstext = roundwinnersfile.readline()
while roundwinnerstext:
  roundwinnerslen = len(roundwinnerstext)
  if (roundwinnerstext.find("\n") > -1):
    roundwinnersvar = roundwinnerslen-1
    roundwinnersreplace = str(roundwinnerstext[:(roundwinnersvar)])
    roundwinnerslist.append(roundwinnersreplace)
  else:
    roundwinnerslist.append(str(roundwinnerstext))
  roundwinnerstext = roundwinnersfile.readline()
roundwinnersfile.close()
roundwinnerslistamount = (len(roundwinnerslist))


roundlosersfile = open('roundlosers.txt', 'r')
roundloserslist = []
roundloserstext = roundlosersfile.readline()
while roundloserstext:
  roundloserslen = len(roundloserstext)
  if (roundloserstext.find("\n") > -1):
    roundlosersvar = roundloserslen-1
    roundlosersreplace = str(roundloserstext[:(roundlosersvar)])
    roundloserslist.append(roundlosersreplace)
  else:
    roundloserslist.append(str(roundloserstext))
  roundloserstext = roundlosersfile.readline()
roundlosersfile.close()
roundloserslistamount = (len(roundloserslist))


elofile = open('elolist.txt', 'r')
elolist = []
elotext = elofile.readline()
while elotext:
 elolen = len(elotext)
 if (elotext.find("\n") > -1):
   elovar = elolen-1
   eloreplace = (elotext[:(elovar)])
   elolist.append(int(eloreplace))
 else:
   elolist.append(int(elotext))
 elotext = elofile.readline()
elofile.close()
 
elolistamount = (len(elolist))

elocalculator = -1

if (elolistamount > 1 and namelistamount > 1 and namelistamount == elolistamount):
  elocalculator = 1
elif (elolistamount > namelistamount):
  elocalculator = 0
  print("ERROR: There are more ELO list elements than NAME list elements.")
elif (namelistamount > elolistamount):
  elocalculator = 0
  print("ERROR: There are more NAME list elements than ELO list elements.")
else:
  elocalculator = 0
  print("External error has occured.")

def eloscrape(winner, loser):
	global elocalculator
	global elolistamount
	global namelistamount

	changefile = open('changelog.txt', 'r')
	changelist = []
	changetext = changefile.readline()
	while changetext:
		changelist.append(changetext)
		changetext = changefile.readline()
	changefile.close()
	changenumber = len(changelist)
	if (elocalculator == 1):
		player1 = winner
		if ((player1 in namelist) == False):
			print("Error: " + player1 + " not in namelist")
			player1confirm = 0
		else:
			player1confirm = 1
		player2 = loser
		if ((player2 in namelist) == False):
			print("Error: " + player2 + " not in namelist")
			player1confirm = 0
		else:
			player2confirm = 1
		
		if (player1confirm == 1 and player2confirm == 1):
			matchresult1 = 1
			matchresult2 = 0

			position1 = namelist.index(player1)
			position2 = namelist.index(player2)
			elo1 = elolist[position1]
			elo2 = elolist[position2]
			newelo1 = elocalc(elo1, elo2, matchresult1)
			newelo2 = elocalc(elo2, elo2, matchresult2)

			elolist[position1] = int(newelo1)
			elolist[position2] = int(newelo2)

			changefile = open('changelog.txt', 'w')
			for changeitems in range(changenumber):
				changefile.write(changelist[changeitems])
			changefile.write("\n\nMATCH: " + player1 + " vs " + player2)
			if (matchresult1 > matchresult2):
				changefile.write("\n" + player1 + " won")
			else:
				changefile.write("\n" + player2 + " won")
			changefile.write("\n\nELO CHANGES:")
			changefile.write("\n" + player1 + ": " + str(elo1) + " -> " + str(newelo1))
			changefile.write("\n" + player2 + ": " + str(elo2) + " -> " + str(newelo2))
			changefile.close()

			elofile = open('elolist.txt', 'w')
			for eloitems in range (elolistamount):
				elofile.write(str(elolist[eloitems]))
				if(eloitems != elolistamount - 1): 
					elofile.write("\n")
			elofile.close()

			print("ELO CHANGES:")
			print(player1 + ": " + str(elo1) + " -> " + str(newelo1))
			print(player2 + ": " + str(elo2) + " -> " + str(newelo2))
		else:
			changefile = open('changelog.txt', 'w')
			for changeitems in range(changenumber):
				changefile.write(changelist[changeitems])
			changefile.write("\nFIX THIS MATCHUP: " + player1 + " vs " + player2)
			changefile.close()
			print("FIX THIS MATCHUP: " + player1 + " vs " + player2)

			
if (roundwinnerslistamount == roundloserslistamount):
	for repeats in range(roundwinnerslistamount):
		eloscrape(roundwinnerslist[repeats], roundloserslist[repeats])
elif (roundwinnerslistamount > roundloserslistamount):
	print("Error: there are more round winners than round losers")
elif (roundwinnerslistamount < roundloserslistamount):
	print("Error: there are more round losers than round winners")
else:
	print("External round error has ocurred")
