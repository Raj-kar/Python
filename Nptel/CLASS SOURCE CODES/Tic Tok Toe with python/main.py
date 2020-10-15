board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


def check_horizon(one, two, three, sign):
    if board[one] == sign and board[two] == sign and board[three] == sign:
        print(f" {sign} WINS !")
        return True


def check_verti(one, two, three, sign):
    if board[one] == sign and board[two] == sign and board[three] == sign:
        print(f" {sign} WINS !")
        return True


def check_digonal(one, two, three):
    if board[one] == 'X' and board[two] == 'X' and board[three] == 'X':
        print("X WINS !")
        return True
    elif board[one] == 'O' and board[two] == 'O' and board[three] == 'O':
        print(" O WINS !")
        return True


def check_win():
    flag = False
    for i in range(0, 9, 3):
        flag = check_horizon(i, i+1, i+2, 'X')
        if flag:
            return flag
        flag = check_horizon(i, i+1, i+2, 'O')
        if flag:
            return flag

    for i in range(0, 3):
        flag = check_verti(i, i+3, i+6, 'X')  # 0, 3, 6 --> 1, 4, 7 --> 2, 5, 8
        if flag:
            return flag
        flag = check_verti(i, i+3, i+6, 'O')  # 0, 3, 6 --> 1, 4, 7 --> 2, 5, 8
        if flag:
            return flag

    flag = check_digonal(0, 4, 8)
    if flag:
        return flag
    flag = check_digonal(2, 4, 6)
    if flag:
        return flag


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_move(sign):
    try:
        turn = int(input(f"Where you want to put {sign} ? [1/9]  "))
    except:
        print("Invalid Input")
        handle_move(sign)
    else:
        if turn > 0 and turn < 10 and board[turn - 1] == '-':
            board[turn - 1] = sign
        else:
            print("INVALID MOVE")
            handle_move(sign)


def play():
    counter = 0
    while True:
        counter += 1

        display_board()
        if counter > 2:
            if check_win() == True:
                break

        handle_move("X")
        display_board()

        if counter > 2:
            if check_win() == True:
                break

        if(counter == 5):
            print("DRAW !!!")
            break

        handle_move("O")


play()