import pdb
import random
from venv import create
import utils


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
	for i in guessList:
		if letter in i:
			#remove the word from the list
			guessList.pop(i)

#remove the words that do not contain the given letter
def removeWordsWithoutLetter(guessList, letter):
	for i in guessList:
		if(letter not in i):
			#remove the word from the list
			guessList.pop(i)

#initialize guess list based on correct letters
def createGuessList(correctWord):
	#GET possible words for each correct letter
	tmp = []
	tmp1 = []
	tmp2 = []
	tmp3 = []
	tmp4 = []
	tmp5 = []
	if(correctWord[0] != ""):
		tmp1.append(letters2Words[correctWord[0]][0])
	if(correctWord[1] != ""):
		tmp2.append(letters2Words[correctWord[1]][1])
	if(correctWord[2] != ""):
		tmp3.append(letters2Words[correctWord[2]][2])
	if(correctWord[3] != ""):
		tmp4.append(letters2Words[correctWord[3]][3])
	if(correctWord[4] != ""):
		tmp5.append(letters2Words[correctWord[4]][4])
	
	#intersect the lists to get only the common words to ensure no words that do not fit
	tmp = list(set(tmp1).intersection(set(tmp2)))
	tmp = list(set(tmp).intersection(set(tmp3)))
	tmp = list(set(tmp).intersection(set(tmp4)))
	tmp = list(set(tmp).intersection(set(tmp5)))

	return tmp

#use possible letters to add to guessList
def addMoreGuessList(guessList):
	#could loop through words list and whichever word has the most matching letters we add to the guessList
	#for example if we know where 2 letters are and know that 1 other letter is somewhere in the word
	#from the possible words, the 'score' for a good guess would be a 5, the word has the 2 matching letters and includes the letter we know is in the word
	#only add words to the guess list that have the same 'score' or criteria we know
	pass


#set the positions list and dictionary
def setPositions(feedback, guesses, correctWord, positions, lettersInWord, lettersNotInWord):
	for i in range(len(feedback)):
		guess = guesses[i]
		feed = feedback[i]
		for i in range(len(guess)):
			if feed[i] == 0:
				#wrong letter
				lettersNotInWord.append(guess[i])
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
	for i in range(len(guessList)):
		word = guessList[i]
		#loop through word and see if it has a letter in word, but in wrong position
		for l in range(len(word)):
			if(positions[word[l]][l] == 1):
				guessList.remove(i)
				continue



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
		#have no correct letters, try to get some more guesses
		addMoreGuessList(guessList) 
		#TODO: Complete this function 


	#FILTER GUESSLIST as much as possible to REDUCE possible words to return

	#remove words with letters not allowed
	for j in lettersNotInWord:
		removeWordsWithLetter(guessList, j)

	#remove words that do not contain one of the correct letters
	for j in correctWord:
		if(j != ""):
			removeWordsWithoutLetter(guessList, j)

	#remove words where letters don't correspond with positions dictionary
	removeWrongPositionWords(guessList, positions)








	#choose a word from the list of possible words
	#go with random or a better method of picking a word



	#return random.choice(guessList)
	return random.choice(wordlist)


if __name__ == "__main__":
	wordlist = utils.readwords("allwords5.txt")
	print(f"AI: 'My next choice would be {makeguess(wordlist)}'")

