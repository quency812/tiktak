
def check_win(pla, board):
    for row in range(3):
        if (all(pla == board[i][row] for i in range(3)) or all(pla == board[row][i] for i in range(3)) or
                all(pla == board[i][i] for i in range(3)) or all(pla == board[i][2 - i] for i in range(3))):
            return True


def start():
    board = [["[ ]" for i in range(3)] for _ in range(3)]
    player = "[+]"
    while True:
        move = input(f"Ход игрока Player {player} : ")
        if len(move) == 3:
            row, col = map(int, move.split(","))

            if board[row][col] == "[ ]":
                board[row][col] = player
                res = "".join(board[0]) + "\n" + "".join(board[1]) + "\n" + "".join(board[2])
            else:
                print("Клетка уже занята!!!")
                player = "[+]" if player == "[-]" else "[-]"
            print(res)
            if check_win(player, board):
                print(f"WIN {player}")
                print(f"============\n"
                      f"==NEW GAME==\n"
                      f"============\n")
                start()
            player = "[+]" if player == "[-]" else "[-]"
        else:
            print("[!] WRONG [!]")


if __name__ == "__main__":
    start()
