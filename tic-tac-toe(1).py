board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f"|{board[i]}|{board[i+1]}|{board[i+2]}|")
    print()

def player_move(icon):
    while True:
        choice = int(input(f"Your turn player {icon}. Enter your move (1-9): ")) - 1
        if 0 <= choice < 9 and board[choice] == " ":
            board[choice] = icon
            break
        print("Invalid move, try again.")

def is_victory(icon):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == icon for a, b, c in wins)

def is_draw():
    return " " not in board

while True:
    print_board()
    player_move("X")
    if is_victory("X"):
        print("Player 1 wins! Congratulations!")
        break
    if is_draw():
        print("It's a draw!")
        break
    print_board()
    player_move("O")
    if is_victory("O"):
        print("Player 2 wins! Congratulations!")
        break
    if is_draw():
        print("It's a draw!")
        break
