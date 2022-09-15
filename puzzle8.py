"""
Puzzle8 Game
-------------
| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
"""

from functions import *
from functions.availableMoves import availableMoves
from functions.applyAction import applyAction
from functions.goalPuzzle import goalPuzzle

def print_puzzle(puzzle):
	p=''
	for i in puzzle:
		if i==0: p+=' '
		else: p+=str(i)
	print (
		'-'*13 + '\n' +
		'| ' + p[0] + ' | ' + p[1] + ' | ' + p[2] + ' |' + '\n' +
		'-'*13 + '\n' +
		'| ' + p[3] + ' | ' + p[4] + ' | ' + p[5] + ' |' + '\n' +
		'-'*13 + '\n' +
		'| ' + p[6] + ' | ' + p[7] + ' | ' + p[8] + ' |' + '\n' +
		'-'*13
		)

def human_play(puzzle):
	while (True):
		print_puzzle(puzzle)
		available_moves=availableMoves(puzzle) # returns the possible actions in the current state of the puzzle
		print('available moves: ',available_moves)
		selected_move=input('select a move: ')
		if selected_move not in available_moves:
			print('Game Over'); break
		puzzle=applyAction(puzzle,selected_move) # apply the action to the current state and returns the new state of the puzzle
		if goalPuzzle(puzzle): # returns True only if the state of the puzzle satisfy the goal condition
			print_puzzle(puzzle); print("You win"); break

if __name__ == '__main__':
	puzzle=[
	3,1,2,
	4,0,5,
	6,7,8
	]
	human_play(puzzle)
