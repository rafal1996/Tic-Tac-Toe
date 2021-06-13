X = 'X'
O = 'O'
EMPTY = ' '
DRAW = 'DRAW'
NUM_SQUARES = 9

def display_instruction():
    print(
        """
        Welcome in game Tic Tac Toe. Your opponent will be the Computer.
        
        You indicate your moves by choosing the number 0-8.
        This number corresponds to the position on the board.
        
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8
            
            
        """
    )

def ask_yes_no(question):
    # Ask a question with a YES or NO answer
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    # Choose number 0-8
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    #Choose who have first move, computer or human
    go_first = ask_yes_no("Do you want start first? (y/n): ")
    if go_first == 'y':
        print("First move is yours")
        human = X
        computer = O
    else:
        print("Computer starts the game")
        computer = X
        human = O
    return computer, human

def new_board():
    #Creates a new game board
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def dispaly_board(board):
    #Displays the game boards on the screen
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\n\t", board[6], "|", board[7], "|", board[8])

def legal_moves(board):
    #List of allowed moves
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    WAYS_TO_WIN = (
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return DRAW
    return None

def human_move(board, human):
    #Read move human
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Your move (0-8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("This field is already taken, select other")
        print("Great")
        return move

def computer_moves(board, computer, human):
    #copy list
    board = board[:]
    BEST_MOVES = (4, 0 , 2, 6, 8, 1, 3, 5, 7)
    print("Computer pick field number ", end=" ")

    #if computer can win
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    #if human can win
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    #if no one can win
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner,  computer, human):
    if the_winner != DRAW:
        print(the_winner, " is winner")
    else:
        print("DRAW! \n")

def main():
    display_instruction()
    computer, human = pieces()
    turn = X
    board = new_board()
    dispaly_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_moves(board, computer, human)
            board[move] = computer
        dispaly_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

#start game
main()

