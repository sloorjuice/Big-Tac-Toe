import random
import tkinter as tk
import tkinter.messagebox

class TicTacToe:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Initialize the current player and the game board
        self.current_player = "X"
        self.board = [" " for i in range(9)]  # List to hold the board state
        
        # List to hold references to the buttons
        self.buttons = []
        
        # Create the game board UI
        self.create_board()

    def create_board(self):
        # Create a 3x3 grid of buttons for the game board
        for i in range(9):
            button = tk.Button(
                self.root, 
                text=" ", 
                font=('normal', 40), 
                width=5, 
                height=2,
                command=lambda i=i: self.on_button_click(i)  # Lambda to pass current index
            )
            button.grid(row=i//3, column=i%3)  # Place button in the correct row and column
            self.buttons.append(button)  # Add button to the list

    def on_button_click(self, index):
        # Handle a button click event
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            
            if self.check_winner():
                tkinter.messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                tkinter.messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                # Switch to the other player
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check if there's a winner by checking all possible winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != " ":
                return True
        return False

    def reset_game(self):
        # Reset the game to its initial state
        self.board = [" " for i in range(9)]  # Clear the board
        for button in self.buttons:
            button.config(text=" ")  # Clear the button text
        self.current_player = "X"  # Reset the current player

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
