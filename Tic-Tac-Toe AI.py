import tkinter as tk
from tkinter import messagebox
import random
class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("625x625")
        self.window.configure(bg='skyblue')
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text=" ", font=("Helvetica", 26), width=9, height=4,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j, padx=10, pady=10)
                button.configure(bg='lightgrey')
                self.buttons.append(button)
        self.window.mainloop()
    def make_move(self, row, col):
        index = 3 * row + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.switch_player()
                self.make_computer_move()
    def make_computer_move(self):
        empty_cells = [i for i in range(9) if self.board[i] == " "]
        if empty_cells:
            index = self.minimax(self.board, "O")[1]
            self.board[index] = "O"
            self.buttons[index].config(text="O")
            if self.check_winner():
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.switch_player()
    def minimax(self, board, player):
        empty_cells = [i for i in range(9) if board[i] == " "]
        if self.check_winner(board, "X"):
            return -1, None
        elif self.check_winner(board, "O"):
            return 1, None
        elif not empty_cells:
            return 0, None
        moves = []
        for cell in empty_cells:
            new_board = board.copy()
            new_board[cell] = player
            score, _ = self.minimax(new_board, "X" if player == "O" else "O")
            moves.append((score, cell))
        if player == "O":
            return max(moves)
        else:
            return min(moves)
    def check_winner(self, board=None, player=None):
        if board is None:
            board = self.board
        if player is None:
            player = self.current_player
        for i in range(3):
            if all(board[i * 3 + j] == player for j in range(3)) or all(board[j * 3 + i] == player for j in range(3)):
                return True
        if all(board[i * 4] == player for i in range(3)) or all(board[i * 2 + 2] == player for i in range(3)):
            return True
        return False
    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"
    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"
        if random.choice([True, False]):
            self.make_computer_move()
if __name__ == "__main__":
    TicTacToe()
