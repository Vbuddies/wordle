import pdb
import random
import utils


#make dictionary of letters that give a list of lists
#for instance "e" -> [ [e is the first letter], [e is the second letter], [e is the third letter], [e is the fourth letter], [e is the fifth letter] ]
letters2Words = {
	"a": [[], [], [], [], []], 
	"b": [[], [], [], [], []], 
	"c": [[], [], [], [], []], 
	"d": [[], [], [], [], []], 
	"e": [[], [], [], [], []], 
	"f": [[], [], [], [], []], 
	"g": [[], [], [], [], []], 
	"h": [[], [], [], [], []], 
	"i": [[], [], [], [], []], 
	"j": [[], [], [], [], []], 
	"k": [[], [], [], [], []], 
	"l": [[], [], [], [], []], 
	"m": [[], [], [], [], []], 
	"n": [[], [], [], [], []], 
	"o":[[], [], [], [], []], 
	"p": [[], [], [], [], []], 
	"q": [[], [], [], [], []], 
	"r": [[], [], [], [], []], 
	"s": [[], [], [], [], []], 
	"t": [[], [], [], [], []], 
	"u": [[], [], [], [], []], 
	"v": [[], [], [], [], []], 
	"w": [[], [], [], [], []], 
	"x": [[], [], [], [], []], 
	"y": [[], [], [], [], []], 
	"z": [[], [], [], [], []]
}
ourWordList = utils.readwords("allwords5.txt")


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
		return "adieu"


	






	return random.choice(wordlist)


if __name__ == "__main__":
	wordlist = utils.readwords("allwords5.txt")
	print(f"AI: 'My next choice would be {makeguess(wordlist)}'")
