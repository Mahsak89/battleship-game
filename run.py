# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


class GameBoard:
    """making and printing the game board
    """
    def __init__(self, board):
        self.board = board

    def print_board(self):
        # visualise the board
        print("  1 2 3 4 5")
        row_number = 1
        for row in self.board:
            # learned from youtube
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    """
    making the battleship class to craet and guess the ships location
    """

    def __init__(self, board):
        self.board = board

    def create_ships(self):
        # creat five random ships for both the user and the computer
        for ship in range(5):
            self.row = random.randint(0, 4)
            self.column = random.randint(0, 4)
            while self.board[self.row][self.column] == "X":
                self.row = random.randint(0, 4)
                self.column = random.randint(0, 4)
            self.board[self.row][self.column] = "X"
        return self.board

    def get_user_input(self):
        while True:
            try:
                row = input("Enter the row of the ship(1-5):\n ")
                if row in '12345':
                    row = int(row) - 1
                    break
                else:
                    print('Enter a valid number between 1-5')
            except ValueError:
                print('Enter a valid number between 1-5')
        while True:
            try:
                column = input("Enter the column of the ship(1-5):\n ")
                if column in '12345':
                    column = int(column) - 1
                    break
                else:
                    print('Enter a valid number between 1-5')
            except ValueError:
                print('Enter a valid number between 1-5')
        return row, column

    def count_ruined_ships(self):
        # count how many ship were guessed correctly
        ruined_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    ruined_ships += 1
        return ruined_ships


# create to type of board for each gamer : the guess board
# and the one with the ships place on it.
print("THE RULES OFF THE GAME:")
print("There is 5 hidden ships placed for both (You and the computer)")
print("Whoever guessess the location of all the 5 ships correctly " +
      "will be the winner.")
print("If you guess wrongly it will be shown with (-)")
print("And if you guess correctly it will be shown with (X)")
computer_board = GameBoard([[" "] * 5 for i in range(5)])
player_guess_board = GameBoard([[" "] * 5 for i in range(5)])
player_board = GameBoard([[" "] * 5 for i in range(5)])
computer_guess_board = GameBoard([[" "] * 5 for i in range(5)])
Battleship.create_ships(computer_board)
Battleship.create_ships(player_board)
print("where the computer's battleships are hidden")
GameBoard.print_board(player_board)

# GameBoard.print_board((computer_board))
# main game logic
while True:
    # user turn
    while True:
        print('Guess a battleship location')
        GameBoard.print_board(player_guess_board)
        # get user input
        player_row, player_column = Battleship.get_user_input(object)

        # check if the user entered the same location or not
        while (player_guess_board.board[player_row][player_column] == "-" or
               player_guess_board.board[player_row][player_column] == "X"):
            print("You guessed that one already")
            player_row, player_column = Battleship.get_user_input(object)

        # check if the user guesses the ships location correct or not
        if computer_board.board[player_row][player_column] == "X":
            print("You sunk one of my ships!")
            player_guess_board.board[player_row][player_column] = "X"
            print('your guess board')
            GameBoard.print_board(player_guess_board)
            break
        else:
            print("You missed my battleship!")
            player_guess_board.board[player_row][player_column] = "-"
            print('your guess board')
            GameBoard.print_board(player_guess_board)
            break

    # check if the user wins or not
    if Battleship.count_ruined_ships(player_guess_board) == 5:
        GameBoard.print_board(player_guess_board)
        print("You won!")
        print("You guessed all 5 battleships!")
        break
    # computer turn
    while True:
        print('Computer guess board')

        # make computer guess randomly
        computer_row = random.randint(0, 4)
        computer_column = random.randint(0, 4)
        # check if the computer chose the same location or not
        while (computer_guess_board.board[computer_row][computer_column] == "-"
               or computer_guess_board.board[computer_row][computer_column] ==
               "X"):
            computer_row = random.randint(0, 4)
            computer_column = random.randint(0, 4)
        # check if the user guesses the ships location correct or not
        if player_board.board[computer_row][computer_column] == "X":
            computer_guess_board.board[computer_row][computer_column] = "X"
            GameBoard.print_board(computer_guess_board)
            break
        else:
            computer_guess_board.board[computer_row][computer_column] = "-"
            GameBoard.print_board(computer_guess_board)
            break
    # check if computer won or not
    if Battleship.count_ruined_ships(computer_guess_board) == 5:
        GameBoard.print_board(computer_guess_board)
        print("Sorry, the computer won.")
        break
