#!/usr/bin/env python
# coding: utf-8

# In[3]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[4]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
display_board(test_board)


# In[14]:


def player_input():
    
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Choose X or O: ').upper()
        
        if marker =='X':
            
            return('X','O')
        else:
            return ('O', 'X')


# In[15]:


player1_marker , player2_marker = player_input()


# In[16]:


player2_marker


# In[20]:


def place_marker(board, marker, position):
    board[position] = marker


# In[21]:


test_board


# In[22]:


place_marker(test_board,'$',8)
display_board(test_board)


# In[23]:


def win_check(board,mark):
    #which leads one person to win the game--?
    #possible combinations--
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[26]:


display_board(test_board)
win_check(test_board,'X')


# In[27]:


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[28]:


def space_check(board, position):
    
    return board[position] == ' '


# In[29]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[30]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[31]:


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[32]:


print('Welcome to Tic Tac Toe!')
#putting code together
#to check if I have covered everything
while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:




