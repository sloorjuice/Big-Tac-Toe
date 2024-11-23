import tkinter as tk
import tkinter.messagebox

class Main:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Big Tac Toe")
        
        # Initialize the current player and the game board
        self.current_player = "X"
        self.board = [[" " for _ in range(9)] for _ in range(9)]  # 9 Tic Tac Toe boards
        
        # List to hold references to the buttons
        self.frames = []  # Hold references to each mini-board's frame
        self.buttons = []  # Hold references to each mini-board's buttons
        
        # Create the game board UI
        self.create_board()
    
    def create_board(self):
        # Create a 3x3 grid of frames for each of the 9 Tic Tac Toe boards
        for board_index in range(9):
            frame = tk.Frame(self.root, bd=3, relief="solid")
            frame.grid(row=board_index // 3, column=board_index % 3, padx=5, pady=5)
            self.frames.append(frame)

            board_buttons = []
            for i in range(9):
                button = tk.Button(
                    frame,
                    text=" ",
                    font=('normal', 20),
                    width=3,
                    height=1,
                    command=lambda i=i, b=board_index: self.on_button_click(b, i)  # Lambda to pass current index
                )
                button.grid(row=i // 3, column=i % 3)  # Place button in the correct row and column
                board_buttons.append(button)  # Add button to the list
            self.buttons.append(board_buttons)

    def on_button_click(self, board_index, index):
        # Handle a button click event
        if self.board[board_index][index] == " ":
            self.board[board_index][index] = self.current_player
            self.buttons[board_index][index].config(text=self.current_player)
            
            if self.check_winner(board_index):
                tkinter.messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins board {board_index + 1}!")
                self.display_big_mark(board_index, self.current_player)
                self.current_player = "O" if self.current_player == "X" else "X"
            elif " " not in self.board[board_index]:
                tkinter.messagebox.showinfo("Tic Tac Toe", f"It's a tie on board {board_index + 1}!")
                self.reset_board(board_index)
            else:
                # Switch to the other player
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, board_index):
        # Check if there's a winner by checking all possible winning combinations
        board = self.board[board_index]
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combination in winning_combinations:
            if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
                return True
        return False

    def display_big_mark(self, board_index, player):
        # Display a big X or O in the middle of the winning board
        for button in self.buttons[board_index]:
            button.grid_forget()  # Remove all small buttons from the frame

        big_label = tk.Label(
            self.frames[board_index],
            text=player,
            font=('normal', 60),
            width=5,
            height=2
        )
        big_label.grid(row=1, column=1)

    def reset_board(self, board_index):
        # Reset a board to its initial state
        self.board[board_index] = [" " for _ in range(9)]  # Clear the board
        for button in self.buttons[board_index]:
            button.config(text=" ")  # Clear the button text

if __name__ == "__main__":
    root = tk.Tk()
    game = Main(root)
    root.mainloop()
