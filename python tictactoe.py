import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.player_names = ['Player 1', 'Player 2']
        self.create_gui()

    def create_gui(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # Create the player name input labels and textboxes
        player1_label = tk.Label(self.window, text="Player 1 (X):", font=('Helvetica', 16))
        player1_label.grid(row=0, column=0, padx=10, pady=10)
        self.player1_entry = tk.Entry(self.window, font=('Helvetica', 16))
        self.player1_entry.grid(row=0, column=1, padx=10, pady=10)
        player2_label = tk.Label(self.window, text="Player 2 (O):", font=('Helvetica', 16))
        player2_label.grid(row=1, column=0, padx=10, pady=10)
        self.player2_entry = tk.Entry(self.window, font=('Helvetica', 16))
        self.player2_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create the start button
        start_button = tk.Button(self.window, text="Start Game", font=('Helvetica', 16), command=self.start_game)
        start_button.grid(row=2, column=1)

        # Create the board buttons (disabled by default)
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", font=('Helvetica', 40), width=3, height=1, command=lambda x=i, y=j: self.button_click(x, y))
                button.grid(row=i+3, column=j)
                button.configure(state='disabled')
                row.append(button)
            self.buttons.append(row)

        # Create the restart button (disabled by default)
        self.restart_button = tk.Button(self.window, text="Restart", font=('Helvetica', 16), command=self.restart_game)
        self.restart_button.grid(row=6, column=1)
        self.restart_button.configure(state='disabled')

    def start_game(self):
        # Get the player names
        self.player_names[0] = self.player1_entry.get() or 'Player 1'
        self.player_names[1] = self.player2_entry.get() or 'Player 2'

        # Enable the board buttons and the restart button
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(state='normal')
        self.restart_button.configure(state='normal')

        # Hide the player name input labels and textboxes, and the start button
        self.window.grid_slaves(row=0, column=0, padx=10, pady=10)[0].grid_forget()
        self.window.grid_slaves(row=0, column=1, padx=10, pady=10)[0].grid_forget()
        self.window.grid_slaves(row=1, column=0, padx=10, pady=10)[0].grid_forget()
        self.window.grid_slaves(row=1, column=1, padx=10, pady=10)[0].grid_forget()
        self.window.grid_slaves(row=2, column=1)[0].grid_forget()

        def button_click(self, x, y):
        button = self.buttons[x][y]
        if button["text"] == "":
            button["text"] = self.current_player
            self.board[x][y] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Congratulations!", f"{self.player_names[0] if self.current_player == 'X' else self.player_names[1]} has won!")
                self.restart_game()
            elif self.check_tie():
                messagebox.showinfo("Tie!", "The game is tied!")
                self.restart_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

    def restart_game(self):
        # Reset the board and current player
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text="", state='disabled')

        # Disable the restart button
        self.restart_button.configure(state='disabled')

        # Show the player name input labels and textboxes, and the start button
        self.window.grid_slaves(row=0, column=0, padx=10, pady=10)[0].grid()
        self.window.grid_slaves(row=0, column=1, padx=10, pady=10)[0].grid()
        self.window.grid_slaves(row=1, column=0, padx=10, pady=10)[0].grid()
        self.window.grid_slaves(row=1, column=1, padx=10, pady=10)[0].grid()
        self.window.grid_slaves(row=2, column=1)[0].grid()

        # Clear the player name textboxes
        self.player1_entry.delete(0, tk.END)
        self.player2_entry.delete(0, tk.END)

    def play(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
