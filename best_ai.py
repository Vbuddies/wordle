import pdb
import random
from venv import create
import utils
import time


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
		return "ADIEU"
	
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



	#FILTER GUESSLIST as much as possible to REDUCE possible words to return

	#remove words with letters not allowed
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
	print(guessList)
	input("Continue")

	#TODO: for a simple AI we could just choose a random choice like the following, but we should probably make this smarter

	print("Returning random choice from guessList")
	return random.choice(guessList)


if __name__ == "__main__":
	wordlist = utils.readwords("allwords5.txt")
	print(f"AI: 'My next choice would be {makeguess(wordlist)}'")

