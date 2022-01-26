import pdb
import random
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
	"O":[[], [], [], [], []], 
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
	

	#get a guess list
	#if we know a letters position then find words that fit that
	guessList = []
	for i in range(5):
		if(correctWord[i] != ""):
			#we have a letter that is in the correct position
			guessList.append(letters2Words[correctWord[i]][i])






	



	#choose a word from the list of possible words



	return random.choice(wordlist)


if __name__ == "__main__":
	wordlist = utils.readwords("allwords5.txt")
	print(f"AI: 'My next choice would be {makeguess(wordlist)}'")
