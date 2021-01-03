# Tic Tac Toe AI using the minimax algorithm. It will always either win or draw.
# Users can choose to be 'X' or 'O.' 'X' always goes first, whether it's the user or the AI.
# Players input coordinates between ([0,2], [0,2]) == (row, column) for their turns.
# By Nate Yeo

import sys
import os
import math

depth = 9                                               # depth is number of empty tiles
human = ''
ai = ''



"""RETURNS 1 IF X WINS, -1 IF O WINS, AND 0 IF ITS A TIE. RETURNS 2 IF GAME IS NOT OVER"""
def gameOver(board):
    global depth

    # game over if someone gets diagonal win
    if ((board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][0])) and (board[1][1] == 'X' or board[1][1] == 'O'):
        if board[1][1] == 'X':
            return 1
        else:
            return -1

    # game over if someone gets horizonal win
    for i in board:
        if i[0] == i[1] and i[1] == i[2] and (i[0] == 'X' or i[0] == 'O'):
            if i[0] == 'X':
                return 1
            else:
                return -1

    # game over if someone gets vertical win
    boardTranspose = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]           # transpose of a matrix from GeeksforGeeks
    for i in boardTranspose:
        if i[0] == i[1] and i[1] == i[2] and (i[0] == 'X' or i[0] == 'O'):
            if i[0] == 'X':
                return 1
            else:
                return -1

    # game is over if all spots are no longer empty (tie)
    if depth == 0:
        return 0

    return 2



"""UPDATES THE GAME BOARD, THEN CHECKS IF A PLAYER HAS WON OR LOST"""
def updateBoard(board, player, row, col):
    board[row][col] = player
    gameOver(board)



"""PRINTS THE GAME BOARD"""
def printBoard(board):
    print()
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("--|---|--")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("--|---|--")
    print(board[2][0], "|", board[2][1], "|", board[2][2])
    print()



"""PROMPTS USER FOR INPUT THEN EXECUTES THE MOVE BY CALLING UPDATEBOARD"""
def userMove(board):
    global depth
    while True:
        userInput = input("(Type 'quit' to quit) Input row col: ")

        if userInput == "quit":                                         # if user inputs quit, end the game with a tie
            depth = 0
            return
        try:
            userInput = userInput.split()
            row = int(userInput[0])
            col = int(userInput[1])
            
            if (row < 0 or row > 2) or (col < 0 or col > 2):            # ensures the user inputs the correct format --> row col
                print("Incorrect input, please try again.")
                continue
            if board[row][col] != ' ':
                print("There is already a piece there, please try again.")
                continue
        except IndexError:
            print("Incorrect input, please try again.")
        else:
            break

    depth -= 1
    updateBoard(board, human, row, col)



"""EXECUTES AI MOVE BY CALLING THE MINIMAX ALGORITHM"""
def AIMove(board):
    global depth
    bestScore = math.inf
    bestMove = [-1, -1]

    if depth == 9:                                                          # saves time, best first move is in the corner
        updateBoard(board, ai, 0, 0)
        depth -= 1
    else:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ' ':
                    updateBoard(board, ai, i, j)
                    if gameOver(board) == 1 or gameOver(board) == -1:
                        bestScore = gameOver(board)
                        bestMove = [i, j]
                        return
                    result = minimax(board, depth - 1, True, human)
                    updateBoard(board, ' ', i, j)
                    if result < bestScore:
                        bestScore = result
                        bestMove = [i, j]
                    if bestMove[0] == -1:                                   # if ai has no good moves, just choose one
                        bestMove = [i, j]
        depth -= 1
        updateBoard(board, ai, bestMove[0], bestMove[1])



"""ALGORITHM THAT TELLS THE AI WHICH MOVE IS BEST"""
def minimax(board, tempDepth, isMax, player):
    if gameOver(board) == 1 or gameOver(board) == -1:
        if human == 'X':
            return gameOver(board)
        else:
            return -1*gameOver(board)
    if tempDepth == 0:
        return 0

    if isMax:
        bestScore = -1*math.inf
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ' ':
                    updateBoard(board, player, i, j)
                    score = minimax(board, tempDepth - 1, False, ai)
                    updateBoard(board, ' ', i, j)
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = math.inf
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ' ':
                    updateBoard(board, player, i, j)
                    score = minimax(board, tempDepth - 1, True, human)
                    updateBoard(board, ' ', i, j)
                    bestScore = min(score, bestScore)
        return bestScore



if __name__ == "__main__":

    board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

    # PLAYER CHOOSES TO BE X OR O.
    while True:
        user = input("Would you like to be 'X' or 'O'? ")
        if user == 'X':
            human = 'X'
            ai = 'O'
            break
        elif user == 'O':
            human = 'O'
            ai = 'X'
            break
        else:
            print("Invalid input, please type 'X' or 'O.'")
    

    # DIFFERENT LOOPS DEPENDING ON WHO GOES FIRST
    if human == 'X':
        printBoard(board)
        while True:
            userMove(board)
            if depth == 0 or gameOver(board) != 2:
                printBoard(board)
                break
            AIMove(board)
            if depth == 0 or gameOver(board) != 2:
                printBoard(board)
                break
            printBoard(board)
    else:
        while True:
            AIMove(board)
            if depth == 0 or gameOver(board) != 2:
                printBoard(board)
                break
            printBoard(board)
            userMove(board)
            if depth == 0 or gameOver(board) != 2:
                printBoard(board)
                break
    
    # PRINTS WIN OR LOSS
    if gameOver(board) == 1:
        print("X wins!")
    elif gameOver(board) == -1:
        print("O wins!")
    else:
        print("Tie!")
