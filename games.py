import random

def tictactoe(val):  
    print("\n")  
    print("\t     |     |")  
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2]))  
    print('\t_____|_____|_____')  
   
    print("\t     |     |")  
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5]))  
    print('\t_____|_____|_____')  
   
    print("\t     |     |")  
   
    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8]))  
    print("\t     |     |")  
    print("\n")  

def check_for_win(board):
	return ((board[0] == board[1] == board[2] in ('X','O')) or \
		    (board[3] == board[4] == board[5] in ('X','O')) or \
			(board[6] == board[7] == board[8] in ('X','O')) or \
			(board[0] == board[3] == board[6] in ('X','O')) or \
			(board[1] == board[4] == board[7] in ('X','O')) or \
			(board[2] == board[5] == board[8] in ('X','O')) or \
			(board[0] == board[4] == board[8] in ('X','O')) or \
			(board[2] == board[4] == board[6] in ('X','O')))

def verify_space_free(board,space):
	if board[space] == '-':
		return True
	else:
		return False

def check_for_tie(board):
	for i in range (0,9):
		if verify_space_free(board,i):
			return False
	return True

def check_play_again():
	answer = input("Play again? (Yes/no) ")
	if (str.lower(answer) in ('y','yes') or answer == ''):
		return True
	elif str.lower(answer) in ('n','no'):
		return False
	else:
		print("Not a valid response.")
		if check_play_again():
			return True
		else:
			return False

def print_current_score():
	print("Current score:")
	print("  Wins for X: " + str(results[1]))
	print("  Wins for Y: " + str(results[2]))
	print("  Ties: " + str(results['ties']))

player_symbols = {1: 'X', 2: 'O'}

def turn(board,player):
	pretty_print_board(current_board)
	alg_move = input('Player ' + str(player) + ' [' + player_symbols[player] + ']: ')
	if str.istitle(alg_move):
		alg_move = str.lower(alg_move)
	if alg_move not in algebraic_dictionary:
		print("'" + alg_move + "' is not a valid space.")
		turn(current_board,current_player)
	else:
		move = algebraic_dictionary[alg_move]
		if verify_space_free(current_board,move):
			current_board[move] = player_symbols[player]
		elif not verify_space_free(current_board,move):
			print(alg_move + " is already taken by " + current_board[move] + "!")
			turn(current_board,current_player)
		else:
			print("I didn't understand that.")
			turn(current_board,current_player)


play_again = True

results = {1: 0, 2: 0, 'ties': 0}

current_board = ['-','-','-','-','-','-','-','-','-']
current_player = 1

while True:
	turn(current_board,current_player)
	if check_for_win(current_board):
		pretty_print_board(current_board)
		print(player_symbols[current_player] + " wins!")
		results[current_player] = results[current_player] + 1
		print_current_score()
		if not check_play_again():
			break
		else:
			current_board = ['-','-','-','-','-','-','-','-','-']
			current_player = 1
	elif check_for_tie(current_board):
		print("Tie game!")
		results['ties'] = results['ties'] +1
		print_current_score()
		if not check_play_again():
			break
		else:
			current_board = ['-','-','-','-','-','-','-','-','-']
			current_player = 1
	else:
		if current_player == 1:
			current_player = 2
		else:
			current_player = 1