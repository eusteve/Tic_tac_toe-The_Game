#python implementation of the tic tac toe game

import random # module is used in the cpu making random choices.

#define game rules 
game_rules =' select a position on the board between 1 and 9.\n'+'win if 3 totems are lined up vertical ,diagonally or horizontally '#number represents the position on the board
#implementation ~ python lists 
 #1 single row 
player='X' #default player symbol
cpu='O'
winner=None #anyone's game at the beginning 
global game_board=["-","-","-","-","-","-","-","-","-"]
#game starts here 
print('hello user , welcome to tic_tac_toe_TheGame')
print(game_rules)
def print_board(): #boards work okay 
    print(game_board[0]+"|"+game_board[1]+"|"+game_board[2])
    print("--- ---")
    print(game_board[3]+"|"+game_board[4]+"|"+game_board[5])
    print("--- ---")
    print(game_board[6]+"|"+game_board[7]+"|"+game_board[8])

#user handling 
def checkHorizontal ():
    if game_board[0]==game_board[1]==game_board[2] or game_board[3]==game_board[4]==\
    game_board[5] or game_board [6]==game_board[7]==game_board[8] ==player:
        print()

    pass

def checkVertical():
    if game_board[0]==game_board[3]==game_board[6] or game_board[1]==game_board[4]==\
    game_board[7] or game_board [2]==game_board[5]==game_board[8] ==player:
        print()
    pass

def checkDiagonal():
    if game_board[0]==game_board[4]==game_board[8] or game_board[2]==game_board[4]==\
    game_board[6]==player: 
        print()
    pass 

def check_win():
    print_board()
    checkHorizontal()
    checkVertical()
    checkDiagonal()
    pass

def checkDraw():
    for i in range(1,9):
        while (game_board[user_pos_index]!=" " or game_board[cpu_pos_index] !=" "):#boards is not empty
            #check win returns false 
            if check_win()==False and draw==True:
                return False  
            #assuming that check drums is ready




def takeInput():
    turns =9
    while turns!=0 :  #when is the game play not true ~when the board is full 
        user_pos_index=input("select a position on the board on the board:\n")#player goes first 
        game_board[user_pos_index-1]=player #assigns player symbol to the index chosen

        cpu_pos_index= random.choice(game_board) #assign a random value from the board 
        while cpu_pos_index ==user_pos_index: 
            cpu_pos_index=random.choice(game_board) #get assigned another variable
            game_board[cpu_pos_index-1]=cpu 

        print_board()#print board with updated values 
        turns = turns-1 #update the turns counter 
        
def someFunction():
        check_win()
        answer = input(" do you wish to continue ? \n 'y' or 'n' :") 
        if answer !='n':
            gameRunning() 

gameRunning()   




