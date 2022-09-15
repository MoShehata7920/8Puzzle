def zeroPlace (puzzle):
    for i in range (len(puzzle)) :
        if puzzle[i] == 0 :
            return i

def applyAction (puzzle,selected_move) :
    whiteSpace = zeroPlace(puzzle) 
    if selected_move == "a" :
        puzzle[whiteSpace] , puzzle[whiteSpace - 1 ] = puzzle[whiteSpace - 1] , puzzle[whiteSpace]

    elif selected_move == "d" :
        puzzle[whiteSpace] , puzzle[whiteSpace + 1] = puzzle[whiteSpace + 1] , puzzle[whiteSpace]

    elif selected_move == "w" :
        puzzle[whiteSpace] , puzzle[whiteSpace - 3] = puzzle[whiteSpace - 3] , puzzle[whiteSpace]

    elif selected_move == "s" :
        puzzle[whiteSpace] , puzzle[whiteSpace + 3] = puzzle[whiteSpace + 3] , puzzle[whiteSpace]

    return puzzle 
