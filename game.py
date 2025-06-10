import random

class TicTacToe:
    def __init__(self):
        """Initialize the game board and set the starting player."""
        self.board = [" " for _ in range(9)]  # 3x3 board represented as a list
        self.current_player = "X"  # X starts the game
        self.game_mode = None  # 1 for single-player, 2 for two-player
        self.winner = None

    def print_board(self):
        """Display the current state of the board."""
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")

    def is_board_full(self):
        """Check if the board is full (draw condition)."""
        return " " not in self.board

    def check_winner(self):
        """Check if there's a winner and return the winning player (X or O) or None."""
        # Check all possible winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]

        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != " ":
                self.winner = self.board[a]
                return self.board[a]
        return None

    def is_valid_move(self, position):
        """Check if a move is valid (position is empty and within range)."""
        return 0 <= position < 9 and self.board[position] == " "

    def make_move(self, position):
        """Make a move on the board if it's valid."""
        if self.is_valid_move(position):
            self.board[position] = self.current_player
            # Check if the move resulted in a win
            if self.check_winner():
                return True
            # Switch players
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def player_move(self):
        """Handle player's move input."""
        while True:
            try:
                position = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
                if self.is_valid_move(position):
                    self.make_move(position)
                    break
                else:
                    print("Invalid move. That position is already taken or out of range.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

    def ai_move(self):
        """Simple AI move - tries to win, block, or make a random move."""
        print(f"Player {self.current_player} (AI) is making a move...")
        
        # 1. First, check if AI can win in the next move
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                if self.check_winner():
                    self.board[i] = "O"
                    return
                self.board[i] = " "  # undo the move

        # 2. Check if player can win in next move and block them
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "X"
                if self.check_winner():
                    self.board[i] = "O"
                    return
                self.board[i] = " "  # undo the move

        # 3. Try to take the center if available
        if self.board[4] == " ":
            self.make_move(4)
            return

        # 4. Try to take a corner if available
        corners = [0, 2, 6, 8]
        random.shuffle(corners)  # Randomize corner selection
        for corner in corners:
            if self.board[corner] == " ":
                self.make_move(corner)
                return

        # 5. Take any available edge
        edges = [1, 3, 5, 7]
        random.shuffle(edges)  # Randomize edge selection
        for edge in edges:
            if self.board[edge] == " ":
                self.make_move(edge)
                return

    def choose_game_mode(self):
        """Let the player choose between single-player and two-player mode."""
        while True:
            try:
                mode = int(input("Choose game mode:\n1. Single-player (vs AI)\n2. Two-player\nEnter 1 or 2: "))
                if mode in [1, 2]:
                    self.game_mode = mode
                    break
                else:
                    print("Please enter either 1 or 2.")
            except ValueError:
                print("Please enter a number (1 or 2).")

    def play(self):
        """Main game loop."""
        print("Welcome to Tic Tac Toe!")
        self.choose_game_mode()
        
        while True:
            self.print_board()
            
            # Check if the game is over
            winner = self.check_winner()
            if winner:
                print(f"Player {winner} wins!")
                break
            if self.is_board_full():
                print("It's a draw!")
                break

            # Handle player/AI moves
            if self.current_player == "X" or self.game_mode == 2:
                self.player_move()
            else:
                self.ai_move()

        self.print_board()
        print("Game over!")

    def reset_game(self):
        """Reset the game state to play again."""
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.winner = None


def main():
    """Main function to start and manage the game."""
    while True:
        game = TicTacToe()
        game.play()
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing!")
            break
        game.reset_game()


if __name__ == "__main__":
    main()