from string import whitespace
from turtle import pu

def zeroPlace (puzzle):
    for i in range (len(puzzle)) :
        if puzzle[i] == 0 :
            return i

def availableMoves (puzzle):
    whitespace = zeroPlace(puzzle)

    if whitespace == 0 :
        available_moves = {"d", "s"}
    elif whitespace == 1 :
        available_moves = {"a" , "d" , "s"}
    elif whitespace == 2 :
            available_moves = {"a" , "s"}
    elif whitespace == 3 :
        available_moves = {"w" , "s" , "d"}
    elif whitespace == 4 :
        available_moves = {"a" , "w" , "s" , "d"}
    elif whitespace == 5 :
        available_moves = {"w" , "s" , "a"}
    elif whitespace == 6 :
        available_moves = {"w","d"}
    elif whitespace == 7 :
        available_moves = {"w", "a", "d"}
    else :
        available_moves = {"w", "a"}

    return available_moves 
