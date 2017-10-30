# -*- coding: utf-8 -*-
__author__ = "Pablo Leon Alcaide"
__version__ = "1.0"

"""Juego de El Ahorcado escrito en Python, experimento de aprendizaje propio """
import random
DRAW = ['''
*------*
|      |
|      |
       |
       |
       |
       |
       |
       |
       |
==============''', '''
*------*
|      |
|      |
O      |
       |
       |
       |
       |
       |
       |
       |
       |
==============''', '''
*------*
|      |
|      |
O      |
|      |
|      |
|      |
       |
       |
       |
       |
       |
       |
==============''', '''
*------*
  |    |
  |    |
  O    |
 /|    |
/ |    |
       |
       |
       |
       |
       |
       |
       |
==============''', '''
*------*
  |    |
  |    |
  O    |
 /|\   |
/ | \  |
  |    |
       |
       |
       |
       |
       |
       |
       |
==============''', '''
*------*
  |    |
  |    |
  O    |
 /|\   |
/ | \  |
  |    |
 /|    |
/      |
       |
       |
       |
       |
       |
       |
==============''', '''
*------*
  |    |
  |    |
  |    |
  |    |
  O    |
 /|\   |
/ | \  |
  |    |
 /|\   |
/   \  |
       |
       |
       |
==============''']
words = 'jedi sith vader skywalker alderaan starkiller chewaka yoda tatooine dantooine palpatine lightsaber kyloren endor wookie ewok twilek obiwan corelia yavin hoth calrissian fett jabba quigon sidious anakin amidala stormtrooper'.split()

def randomWord(wordList):
	# Return a random word from the list
	randomWord = random.randint(0, len(wordList) - 1)
	return wordList[randomWord]

def showHanging(DRAW, badWords, goodWords, secretWord):
	# Show the draw
	print DRAW[len(badWords)]
	print
	print 'Errores:',
	print 
	for word in badWords:
		print word,
		print
	holes = '_' * len(secretWord)
	#replace the holes with the correct letters
	for i in range(len(secretWord)): 
		if secretWord[i] in goodWords:
			holes = holes[:i] + secretWord[i] + holes[i+1:]
	
	for word in holes: 
		print word,
	print

def tryWord(tried):
	# Confirm that the input is a letter
	while True:
		print 'Intenta con una letra.'
		choosenWord = raw_input()
		choosenWord = choosenWord.lower()
		if len(choosenWord) != 1:
			print 'Por favor, introduce sólo una letra.'
		elif choosenWord in tried:
			print 'Ya has intentado esa letra. Elige otra.'
		elif choosenWord not in 'abcdefghijklmnñopqrstuvwxyz':
			print 'Por favor, introduce una LETRA.'
		else:
			return choosenWord

def playAgain():
	# Return True if the player  want to play again
	print '¿Quieres jugar otra vez? (s ó n)'
	return raw_input().lower().startswith('s')

print 'E L   A H O R C A D O  D E   S T A R  W A R S'
print 'Adivina la palabra oculta, ¿Cuánto sabes de Star Wars?'
wordsFailed = ''
correctWords = ''
secretWord = randomWord(words)
gameFinished = False

while True:
	showHanging(DRAW, wordsFailed, correctWords, secretWord)
	
	userWord = tryWord(wordsFailed + correctWords)

	if userWord in secretWord:
		correctWords = correctWords + userWord
		# Look if the player has won
		allFound = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctWords:
				allFound = False
				break
		if allFound:
			print 'Acertaste! era:  '+'"' + secretWord + '"'
			gameFinished = True
	else:
		wordsFailed = wordsFailed + userWord
		# Look if the player has lost
		if len(wordsFailed) == len(DRAW) - 1:
			showHanging(DRAW, wordsFailed, correctWords, secretWord)
			print '¡Demasiados intentos!\nDespués de ' + str(len(wordsFailed)) + \
			' intentos fallidos y ' + str(len(correctWords)) + \
			' intentos correctos, la palabra era ' + secretWord
			gameFinished = True
	
	if gameFinished:
		if playAgain():
			wordsFailed = ''
			correctWords = ''
			gameFinished = False
			secretWord = randomWord(words)
		else:
			break
