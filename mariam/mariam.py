import numpy as np 

# header for the game
print("     tic tac toe!    ")
print("choose number from 0 to 9" + "\n")
# making board
board = [[0 for i in range(3)]for i in range(3)]
for i in range(3):
    print(*board[i])
print("\n")

# turns for two players
game_over = np.False_
turn = 0
choose = True
counter = 0
while not game_over:
    # player one
    if turn == 0:     
        nom = int(input("player 1 (odd numbers): "))
        while nom > 9 or nom % 2 == 0:   # if the number is bigger than 9 or the remainder is 0 print not valied
           print("\n" + "not valied!try again")
           nom = int(input("player 1 (odd numbers): "))
        col = int(input("which column do you want? "))
        row = int(input("which row do you want? "))
        cell = board[row - 1][col - 1] = nom   # print the number on the board
        for i in range(3):
            print(*board[i])
        print("\n")
    
    # player two    
    else:            
        nom = int(input("player 2 (even numbers): "))
        while nom > 9 or nom % 2 == 1:   # if the number is bigger than 9 or the remainder is 1 print not valied
            print("\n" + "not valied!try again")
            nom = int(input("player 2 (even numbers): "))
        col = int(input("which column do you want? "))
        row = int(input("which row do you want? "))
        cell = board[row - 1][col - 1] = nom    # print the number on the board
        for i in range(3):
            print(*board[i])
        print("\n")

# check for a winner      
    counter += 1

    if counter >= 3:
        if (board[0][0] + board[0][1] + board[0][2] == 15 or
            board[1][0] + board[1][1] + board[1][2] == 15 or
            board[2][0] + board[2][1] + board[2][2] == 15 or
            board[0][0] + board[1][0] + board[2][0] == 15 or
            board[0][1] + board[1][1] + board[2][1] == 15 or
            board[0][2] + board[1][2] + board[2][2] == 15):
            print("player" + " " + str(turn + 1) + "  " + "is the winner!")
            game_over = np.True_
# check for a tie        
    if counter == 9 and cell==nom:
        tie = True
        print("Game Over..")
        game_over = np.True_

   
    turn += 1
    turn = turn % 2
