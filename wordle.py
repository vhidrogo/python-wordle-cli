from english_words import english_words_lower_set
import sys

class Wordle:
	"""Command line version of wordle classic.

	Attributes
    ----------
    MAX_LETTERS : int
        max number of letters for word
    MIN_LETTERS : int
        min number of letters for word
    PLACE_HOLDER : str
        string to print as placeholder in game board
    letter_count : int
        the number of letters for word
    tries : int
    	number of tries left in game
    game_board : list
    	list of list with rows and columns in game
    words : set
    	valid words
    word : int
    	word needed to win the game
    current_row : int
    	current row in game board
    is_word_found : boolean
    	whether the word has found or not
    keyboard : list
    	list of dictionaries arranged like a keyboard

    Methods
    -------
    main
        starts the game loop
	"""

	MAX_LETTERS = 7
	MIN_LETTERS = 4

	PLACE_HOLDER = '*'

	def __init__(self, letter_count):
		"""
        Parameters
        ----------
        letter_count : int
            Number of letters for word in game

        Raises
        ------
        TypeError
        	If letter count is not an integer.
        ValueError
            If letter count is between the min and max.
        """

		if not letter_count.isdigit():
			raise TypeError('Number of letters must be an integer.')

		self.letter_count = int(letter_count)

		if self.letter_count < self.MIN_LETTERS or self.letter_count > self.MAX_LETTERS:
			raise ValueError(
				f'Number of letters must be between {self.MIN_LETTERS} and {self.MAX_LETTERS}'
        		)

		self.tries = self.letter_count + 1

		self.game_board = [
			[self.PLACE_HOLDER] * self.letter_count for i in range(self.tries)
		]

		self.words = {
			w for w in english_words_lower_set if len(w) == self.letter_count
		}

		self.word = next(iter(self.words))

		self.current_row = 0

		self.is_word_found = False

		self.keyboard = [
			{'Q':'q', 'W':'w', 'E':'e', 'R':'r', 'T':'t', 'Y':'y', 'U':'u', 'I':'i', 'O':'o', 'P':'p'},
			{'A':'a', 'S':'s', 'D':'d', 'F':'f', 'G':'g',  'H':'h', 'J':'j', 'K':'k', 'L':'l'}, 
			{'Z':'z', 'X':'x', 'C':'c', 'V':'v', 'B':'b', 'N':'n', 'M':'m'}
		]

	def main(self):
		while self.tries > 0 and not self.is_word_found:
			word = input(
				f'\n{self.tries} Tries left. Enter a valid {self.letter_count} letter word: '
				).lower()
			
			if self._is_valid_word(word):
				self._update_game_board(word)
				self._update_keyboard(word)
				self._print_game_board()
				self._print_keyboard()

				self.tries -= 1
				self.current_row += 1
				
				if word == self.word:
					self.is_word_found = True
			else:
				print(f'Invalid input <{word}>.')

		self._end_game()

	def _is_valid_word(self, word):
		"""Checks if word is valid

	    Parameters
	    ----------
	    word : str
	        the user provided word

	    Returns
	    -------
	    boolean
	        true if correct length and in set of words, false othersie
	    """

		if len(word) != self.letter_count:
			return False
		if word not in self.words:
			return False
		return True

	def _update_game_board(self, word):
		"""Updates the current row with each letter in word

		If the letter is in the game word, it is changed to uppercase,
		but if its not in the correct index, then it is italicized.

	    Parameters
	    ----------
	    word : str
	        the user provided word
	    """

		for i, c in enumerate(word):
			if c in self.word:
				letter = c.upper()

				if c != self.word[i]:
					letter = self._italicize_letter(letter)
			else:
				letter = c
					
			self.game_board[self.current_row][i] = letter

	def _italicize_letter(self, letter):
		"""Returns italic letter

	    Parameters
	    ----------
	    letter : str
	        the letter to be italicized

	    Returns
	    -------
	    str
	        the letter preceded by the ansi escape code for italics and
	        appended with the code to return to normal characters
	    """

		return f'\x1B[3m{letter}\x1B[0m'

	def _update_keyboard(self, word):
		"""Updates keys on keyboard for each letter in word

		If the letter is in the game word, it is changed to uppercase,
		but if its not in the correct index, then it is italicized. If the
		letter is not in word the key is changed to the placeholder.

	    Parameters
	    ----------
	    word : str
	        the user provided word
	    """

		for i, c in enumerate(word):
			if c in self.word:
				key = c.upper()

				if c != self.word[i]:
					key = self._italicize_letter(key)
			else:
				key = self.PLACE_HOLDER
			
			c = c.upper()
			for r in self.keyboard:
				if c in r:
					r[c] = key
					break

	def _print_game_board(self):
		"""Prints game board rows/columns"""

		print('\n----Game Board----')

		for r in self.game_board:
			print(''.join(r))

	def _print_keyboard(self):
		"""Prints keyboard"""

		print('\n----Key Board-----')

		for r in self.keyboard:
			print(' '.join(r.values()))

	def _end_game(self):
		"""Prints win/lose message for user"""
		
		if self.is_word_found:
			print(f'\nYOU FOUND THE WORD WITH {self.tries} TRIES LEFT!!\n')
		else:
			print(f'\nNo more tries. The word was "{self.word.upper()}"\n')

if __name__ == '__main__':
	try:
		arg1 = sys.argv[1]
	except IndexError:
		print(f'Usage: {sys.argv[0]} <arg1>')
		sys.exit(1)

	wordle = Wordle(arg1)
	wordle.main()

