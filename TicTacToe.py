'''
Tic Tac Toe
Author David Sevey
'''

import random
import os

invalid = f"\n\033[91mChoice not valid.\033[0m\n"

#Changes color of x and o
def colors_of(board,i):
    if board[i] == 'X':
        return(f"\033[96mX\033[0m")
    elif board[i] == 'O':
        return(f"\033[95mO\033[0m")
    else:
        return(board[i])


#Display for board
def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{colors_of(board,9)}\033[32m|\033[0m{colors_of(board,8)}\033[32m|\033[0m{colors_of(board,7)}")
    print(f"\033[32m{'-'*5}\033[0m")
    print(f"{colors_of(board,6)}\033[32m|\033[0m{colors_of(board,5)}\033[32m|\033[0m{colors_of(board,4)}")
    print(f"\033[32m{'-'*5}\033[0m")
    print(f"{colors_of(board,3)}\033[32m|\033[0m{colors_of(board,2)}\033[32m|\033[0m{colors_of(board,1)}")

#Player selecting x or o
def player_input(p1):
    player1 = 'Nil'
    while player1 not in ['X','O']:
        player1 = input(f"{p1} please select either 'X' or 'O': ").upper()
        if player1 not in ['X','O']:
            print(invalid)
    if player1 == 'X':
        return ('X','O')
    else:
        return ('O','X')

#Picks position on the board
def place_marker(board, marker, position):
    board[position] = marker
    return board[position]

#Checks to see if a player has won the game
def win_check(board, mark):
    if board[9] == mark and board[8] == mark and board[7] == mark or \
        board[6] == mark and board[5] == mark and board[4] == mark or \
    board[3] == board[2] == board[1] == mark or \
    board[9] == board[5] == board[1] == mark or \
    board[7] == board[5] == board[3] == mark or \
    board[9] == board[6] == board[3] == mark or \
    board[8] == board[5] == board[2] == mark or \
    board[7] == board[4] == board[1] == mark:
        return True
    else:
        return False

#Pick random player to start, this mostly works
def choose_first(p1,p2):
    if random.randint(1,2) == 1:
        return p1
    else:
        return p2

#Check to see if space already chosen
def space_check(board, position):
    return board[position] in ['X','O']

#Full Board
def full_board_check(board):
    for i in board:
        if i in range(1,10):
            return False
    return True

def player_choice(board,turn_p):
    position = 0
    while True:
        try:
            while position not in range(1,10) or not space_check(board, position):
                position = int(input(f"{turn_p} please select a postion from 1-9: "))
                if board[position] in ['X','O']:
                    position = 0
                    print(f"\n\033[33mPosition Not Available!\033[0m\n")
                if board[position] not in ['X','O'] and position in range(1,10):
                    return position
        except:
            print(invalid)
            continue

def replay():
    p_replay = 'Nil'
    while p_replay not in ['N','Y']:
        p_replay = input(f"Would you like to play again? (Y/N) ").upper()
        if p_replay not in ['N','Y']:
            print(invalid)
    if p_replay == 'Y':
        return True
    else:
        return False

def main():   
    while True:
        stop_game = False
        player_1 = input(f"\nPlayer 1 enter your name: ").capitalize()
        player_2 = input("Player 2 enter your name: ").capitalize()
        p_board = [*range(0,10)]
        player1_marker, player2_marker = player_input(player_1)
        turn = choose_first(player_1,player_2)
        begin = input(f"{turn} will go first, press enter to continue")
        while not stop_game:
            if turn == player_1:
                display_board(p_board)
                position = player_choice(p_board,turn)
                place_marker(p_board,player1_marker,position)
                if win_check(p_board,player1_marker):
                    display_board(p_board)
                    print(f"\n{'*' * (len(player_1) + 6)}\n{player_1} wins!\n{'*' * (len(player_1) + 6)}\n")
                    stop_game = True
                else:
                    if full_board_check(p_board):
                        display_board(p_board)
                        print(f"\n{'*' * 15}\nGame is a draw!\n{'*' * 15}\n")
                        stop_game = True
                    else:
                        turn = player_2
            else:
                display_board(p_board)
                position = player_choice(p_board,turn)
                place_marker(p_board,player2_marker,position)
                if win_check(p_board,player2_marker):
                    display_board(p_board)
                    print(f"\n{'*' * (len(player_2) + 6)}\n{player_2} wins!\n{'*' * (len(player_2) + 6)}\n")
                    stop_game = True
                else:
                    if full_board_check(p_board):
                        display_board(p_board)
                        print(f"\n{'*' * 15}\nGame is a draw!\n{'*' * 15}\n")
                        stop_game = True
                    else:
                        turn = player_1
        if not replay():
            break

if __name__ == '__main__':
    main()