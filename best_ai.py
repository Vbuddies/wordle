import pdb
import random
from venv import create
import utils
import time
import string

#make dictionary of letters that give a list of lists
#for instance "e" -> [ [e is the first letter], [e is the second letter], [e is the third letter], [e is the fourth letter], [e is the fifth letter] ]
letters2Words = {
	"A": [[], [], [], [], []], 
	"B": [[], [], [], [], []], 
	"C": [[], [], [], [], []], 
	"D": [[], [], [], [], []], 
	"E": [[], [], [], [], []], 
	"F": [[], [], [], [], []], 
	"G": [[], [], [], [], []], 
	"H": [[], [], [], [], []], 
	"I": [[], [], [], [], []], 
	"J": [[], [], [], [], []], 
	"K": [[], [], [], [], []], 
	"L": [[], [], [], [], []], 
	"M": [[], [], [], [], []], 
	"N": [[], [], [], [], []], 
	"O": [[], [], [], [], []], 
	"P": [[], [], [], [], []], 
	"Q": [[], [], [], [], []], 
	"R": [[], [], [], [], []], 
	"S": [[], [], [], [], []], 
	"T": [[], [], [], [], []], 
	"U": [[], [], [], [], []], 
	"V": [[], [], [], [], []], 
	"W": [[], [], [], [], []], 
	"X": [[], [], [], [], []], 
	"Y": [[], [], [], [], []], 
	"Z": [[], [], [], [], []]
}
ourWordList = utils.readwords("allwords5.txt")
#loop through wordlist adding them to letters to word
for i in ourWordList:
	for l in range(len(i)):
		letters2Words[i[l]][l].append(i)



#remove the words that do contain the given letter
def removeWordsWithLetter(guessList, letter):
	tmp = []
	for i in guessList:
		if letter in i:
			# add word to list to remove after
			tmp.append(i)
	#convert the 2 to sets and do a set subtraction
	r = set(guessList) - set(tmp)
	return list(r)


#remove the words that do not contain the given letter
def removeWordsWithoutLetter(guessList, letter):
	tmp = []
	for i in guessList:
		if letter not in i:
			# add word to list to remove after
			tmp.append(i)
	#convert the 2 to sets and do a set subtraction
	return list(set(guessList) - set(tmp))

#initialize guess list based on correct letters
def createGuessList(correctWord):
	#GET possible words for each correct letter
	tmp = []
	if(correctWord[0] != ""):
		#just add to the list
		tmp = letters2Words[correctWord[0]][0]
	if(correctWord[1] != ""):
		if(tmp == []):
			tmp = letters2Words[correctWord[1]][1]
		else:
			#intersect the lists
			tmp = list(set(tmp).intersection(letters2Words[correctWord[1]][1]))
	if(correctWord[2] != ""):
		if tmp == []:
			tmp = letters2Words[correctWord[2]][2]
		else:
			#intersect the lists
			tmp = list(set(tmp).intersection(letters2Words[correctWord[2]][2]))
	if(correctWord[3] != ""):
		if tmp == []:
			tmp = letters2Words[correctWord[3]][3]
		else:
			#intersect the lists
			tmp = list(set(tmp).intersection(letters2Words[correctWord[3]][3]))
	if(correctWord[4] != ""):
		if tmp == []:
			tmp= letters2Words[correctWord[4]][4]
		else:
			#intersect the lists
			tmp = list(set(tmp).intersection(letters2Words[correctWord[4]][4]))
	return tmp


#set the positions list and dictionary
def setPositions(feedback, guesses, correctWord, positions, lettersInWord, lettersNotInWord):
	for i in range(len(feedback)):
		guess = guesses[i]
		feed = feedback[i]
		for i in range(len(guess)):
			if feed[i] == 0:
				#wrong letter
				#need to check if the letter appears twice, if it does then i can't directly do this, otherwise I can
				flag = True
				for j in range(len(guess)):
					if j != i and guess[j] == guess[i]:
						positions[guess[i]][i] = 0
						flag = False
				if(flag):
					lettersNotInWord.append(guess[i])
					positions[guess[i]][0] = 0
					positions[guess[i]][1] = 0
					positions[guess[i]][2] = 0
					positions[guess[i]][3] = 0
					positions[guess[i]][4] = 0
			elif feed[i] == 1:
				#right letter wrong position
				lettersInWord[guess[i]] = 1
				positions[guess[i]][i] = 0
			else:
				#correct position
				lettersInWord[guess[i]] = 1
				positions[guess[i]][i] = 2
				correctWord[i] = guess[i]


#method to remove any words that have letters that are in the word but wrong position
def removeWrongPositionWords(guessList, positions):
	#loop through guess list
	tmp = []
	for i in range(len(guessList)):
		word = guessList[i]
		#loop through word and see if it has a letter in word, but in wrong position
		for l in range(len(word)):
			if(positions[word[l]][l] == 0):
				tmp.append(guessList[i])
				continue

	return list(set(guessList) - set(tmp))


#method to help us find the last letter when all others are known and our number of guesses
# is <= 4
def findLastLetter(guessList, index, lettersInWord, correctWord):
	letters = []
	wordList = utils.readwords("allwords5.txt")
	#add to letters list the possible letters from that position in guess list and of letters in word
	for i in range(len(guessList)):
		if(guessList[i][index] not in letters):
			letters.append(guessList[i][index])

	#to remove duplicates
	letters = list(set(letters))

	#if one of the possible letters is already in the correct word list then remove that letter
	for i in letters:
		if(i in correctWord):
			letters.remove(i)
	# loop through words list
	max = 0
	tmp = []
	for i in range(len(wordList)):
		current = 0
		word = wordList[i]

		#count the number of unknown letters in each word
		for j in range(len(word)):
			if(word[j] in letters):
				current += 1

		#if its a new max add it to a list
		if(current >= max):
			if(current > max):
				tmp = []
				tmp.append(word)
				max = current
			else:
				max = current
				tmp.append(word)
	#remove words that have duplicate letters
	for i in range(0,len(tmp)):
		word = tmp[i]
		#set the index of that word to be an empty string
		for j in range(len(word)):
			if(word.count(word[j]) > 1):
				tmp[i] = ""
				break
	
	#add all words with all unique letters to result list
	result = []
	for i in range(len(tmp)):
		if(tmp[i] != ""):
			result.append(tmp[i])
		
	
	#return a random one of these guesses
	if(len(result) == 0):
		return ""
	return random.choice(result)


def makeguess(wordlist, guesses=[], feedback=[]):
	"""Guess a word from the available wordlist, (optionally) using feedback 
	from previous guesses.

	Parameters
	----------
	wordlist : list of str
		A list of the valid word choices. The output must come from this list.
	guesses : list of str
		A list of the previously guessed words, in the order they were made, 
		e.g. guesses[0] = first guess, guesses[1] = second guess. The length 
		of the list equals the number of guesses made so far. An empty list 
		(default) implies no guesses have been made.
	feedback : list of lists of int
		A list comprising one list per word guess and one integer per letter 
		in that word, to indicate if the letter is correct (2), almost 
		correct (1), or incorrect (0). An empty list (default) implies no 
		guesses have been made.

	Output
	------
	word : str
		The word chosen by the AI for the next guess.
	"""
	if(len(guesses) == 0):
		# RAISE, RAILE, ARISE, ARIEL
		return random.choice(["RAISE", "RAILE", "ARISE", "ARIEL"])
		return random.choice(["ROATE", "REAIS", "SLATE", "AEGIS", "LARES", "RALES", "TARES", "NARES", "ARLES", "SIREN", "RAISE", "QUERY", "RENTS", "SNARE", "EARNS", "STOAE", "SANER", "CANOE", "TEARS", "STEAM", "ADIEU", "SOARE", "AROSE", "IRATE"])
	
	correctWord=["", "", "", "", ""]
	lettersNotInWord = []
	lettersInWord = {}
	positions = {
		"A": [1, 1, 1, 1, 1],
		"B": [1, 1, 1, 1, 1],
		"C": [1, 1, 1, 1, 1],
		"D": [1, 1, 1, 1, 1],
		"E": [1, 1, 1, 1, 1],
		"F": [1, 1, 1, 1, 1],
		"G": [1, 1, 1, 1, 1],
		"H": [1, 1, 1, 1, 1],
		"I": [1, 1, 1, 1, 1],
		"J": [1, 1, 1, 1, 1],
		"K": [1, 1, 1, 1, 1],
		"L": [1, 1, 1, 1, 1],
		"M": [1, 1, 1, 1, 1],
		"N": [1, 1, 1, 1, 1],
		"O": [1, 1, 1, 1, 1],
		"P": [1, 1, 1, 1, 1],
		"Q": [1, 1, 1, 1, 1],
		"R": [1, 1, 1, 1, 1],
		"S": [1, 1, 1, 1, 1],
		"T": [1, 1, 1, 1, 1],
		"U": [1, 1, 1, 1, 1],
		"V": [1, 1, 1, 1, 1],
		"W": [1, 1, 1, 1, 1],
		"X": [1, 1, 1, 1, 1],
		"Y": [1, 1, 1, 1, 1],
		"Z": [1, 1, 1, 1, 1]
	}
	
	#set the possible positions and lettersNotInWord
	setPositions(feedback, guesses, correctWord, positions, lettersInWord, lettersNotInWord)
	

	#get an initial guess list using letters we know are correct
	guessList = createGuessList(correctWord)


	if(len(guessList) == 0):
		#have no correct letters, so just add all words and the filters will remove the letters we know don't work
		guessList = wordlist 


	#if a letter is in both the correct words and lettersNotInWord remove the letter from lettersNotInWord
	for i in correctWord:
		if(i in lettersNotInWord):
			lettersNotInWord.remove(i)

	#repeat above except for the lettersInWord Set
	for i in lettersInWord:
		if(i in lettersNotInWord):
			lettersNotInWord.remove(i)

	#FILTER GUESSLIST as much as possible to REDUCE possible words to return

	for j in lettersNotInWord:
		guessList = removeWordsWithLetter(guessList, j)

	

	#remove words that do not contain letters that are in the word(specifically the letters that we know are in the word but not what position)
	for j in lettersInWord:
		if(j != ""):
			guessList = removeWordsWithoutLetter(guessList, j)

	#remove words where letters don't correspond with positions dictionary
	guessList = removeWrongPositionWords(guessList, positions)






	#choose a word from the list of possible words
	#go with random or a better method of picking a word

	#perhaps if this is the second pick find a word with lots of consonants and few vowels that still has all the correct letters from the first guess
	#should only do this for limited information, i.e. on the second guess

	#added these lines for debugging
	# input("Continue")

	#TODO: for a simple AI we could just choose a random choice like the following, but we should probably make this smarter
	

	#if we are only missing one letter and have plenty of options and at least 2 guesses left
	#find a word that uses all or all-1 of the possible letters and use that so the next guess has much more information
	if(len(guesses) <= 4):
		#if there is only 1 letter we don't know
		if(correctWord.count("") == 1 and len(guessList) > 2):
			#print(guessList)
			index = 0
			for i in range(len(correctWord)):
				if(correctWord[i] == ""):
					index = i
			
			g = findLastLetter(guessList, index, lettersInWord, correctWord)
			print("guess should be" , g)
			return g

	# print("Returning random choice from guessList")
	if(len(guessList) == 0):
		return input("guessList Empty Select Value to pass: ")
	return random.choice(guessList)


if __name__ == "__main__":
	wordlist = utils.readwords("allwords5.txt")
	print(f"AI: 'My next choice would be {makeguess(wordlist)}'")

