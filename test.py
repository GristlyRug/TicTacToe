import random

def print_board(board):
    print("\n")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < 2:
            print("-----------")
    print("\n")

def print_field_numbers():
    print("Field numbers:")
    print(" 1 | 2 | 3")
    print("-----------")
    print(" 4 | 5 | 6")
    print("-----------")
    print(" 7 | 8 | 9")
    print("\n")

def is_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_positions(board):
    positions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                positions.append((i, j))
    return positions

def ai_move(board):
    positions = get_empty_positions(board)
    if positions:
        row, col = random.choice(positions)
        board[row][col] = "O"
        print(f"AI places O at position {row * 3 + col + 1}")

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print("Welcome to Tic Tac Toe!")
    print_field_numbers()
    
    while True:
        print_board(board)
        
        # Player move
        while True:
            try:
                position = int(input("Enter field number (1-9): "))
                if position < 1 or position > 9:
                    print("Please enter a number between 1 and 9!")
                    continue
                row = (position - 1) // 3
                col = (position - 1) % 3
                if board[row][col] != " ":
                    print("That field is already taken!")
                    continue
                board[row][col] = "X"
                print(f"Player places X at position {position}")
                break
            except ValueError:
                print("Please enter a valid number!")
        
        print_board(board)
        
        if is_winner(board, "X"):
            print("Player wins!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        # AI move
        ai_move(board)
        
        if is_winner(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
