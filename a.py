import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        
    def print_board(self):
        print('\n')
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print('\n')
    
    def print_board_nums(self):
        # Shows what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        print('\n')
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        print('\n')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False


def minimax(state, player):
    """
    Minimax Algorithm Implementation
    - Maximizes AI score (O)
    - Minimizes Player score (X)
    """
    max_player = 'O'  # AI
    other_player = 'X' if player == 'O' else 'O'
    
    # Base cases
    if state.current_winner == other_player:
        return {'position': None, 
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player 
                        else -1 * (state.num_empty_squares() + 1)}
    elif not state.empty_squares():
        return {'position': None, 'score': 0}
    
    if player == max_player:
        best = {'position': None, 'score': -math.inf}
    else:
        best = {'position': None, 'score': math.inf}
    
    for possible_move in state.available_moves():
        # Make a move
        state.make_move(possible_move, player)
        
        # Recurse using minimax to simulate game
        sim_score = minimax(state, other_player)
        
        # Undo the move
        state.board[possible_move] = ' '
        state.current_winner = None
        sim_score['position'] = possible_move
        
        # Update best move
        if player == max_player:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score
    
    return best


def play_game():
    """Main game loop"""
    game = TicTacToe()
    player_score = 0
    ai_score = 0
    draws = 0
    
    print("=" * 40)
    print("   TIC TAC TOE - MINIMAX AI")
    print("=" * 40)
    print("\nYou are X, AI is O")
    print("The AI uses Minimax algorithm and is unbeatable!")
    
    while True:
        game = TicTacToe()
        game.print_board_nums()
        
        # Player goes first
        letter = 'X'
        
        while game.empty_squares():
            if letter == 'X':
                # Player's turn
                valid_square = False
                while not valid_square:
                    try:
                        square = int(input(f'\nYour turn (X). Choose position (0-8): '))
                        if square not in range(9):
                            print("Invalid position! Choose 0-8")
                            continue
                        if game.board[square] != ' ':
                            print("Position already taken!")
                            continue
                        valid_square = True
                    except ValueError:
                        print("Invalid input! Enter a number 0-8")
                
                game.make_move(square, letter)
                
            else:
                # AI's turn using Minimax
                print("\nAI is thinking...")
                square = minimax(game, 'O')['position']
                game.make_move(square, letter)
                print(f"AI chose position {square}")
            
            game.print_board()
            
            if game.current_winner:
                if game.current_winner == 'X':
                    print("🎉 YOU WIN! 🎉")
                    player_score += 1
                else:
                    print("🤖 AI WINS! 🤖")
                    ai_score += 1
                break
            
            # Switch turns
            letter = 'O' if letter == 'X' else 'X'
        
        if not game.current_winner:
            print("🤝 IT'S A DRAW! 🤝")
            draws += 1
        
        # Show scores
        print("\n" + "=" * 40)
        print(f"SCORE - You: {player_score} | AI: {ai_score} | Draws: {draws}")
        print("=" * 40)
        
        # Ask to play again
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing!")
            print(f"Final Score - You: {player_score} | AI: {ai_score} | Draws: {draws}")
            break


if __name__ == "__main__":
    play_game()