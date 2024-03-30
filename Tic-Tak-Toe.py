from random import randrange

deboard = [
    [[1],[2],[3]],
    [[4],[5],[6]],
    [[7],[8],[9]]
    ]


def display_board(board):

    one = str(board[0][0])
    one = one.replace('[', '')
    one = one.replace(']', '')

    two = str(board[0][1])
    two = two.replace('[', '')
    two = two.replace(']', '')

    three = str(board[0][2])
    three = three.replace('[', '')
    three = three.replace(']', '')

    four = str(board[1][0])
    four = four.replace('[', '')
    four = four.replace(']', '')

    five = str(board[1][1])
    five = five.replace('[', '')
    five = five.replace(']', '')

    six = str(board[1][2])
    six = six.replace('[', '')
    six = six.replace(']', '')

    seven = str(board[2][0])
    seven = seven.replace('[', '')
    seven = seven.replace(']', '')

    eight = str(board[2][1])
    eight = eight.replace('[', '')
    eight = eight.replace(']', '')

    nine = str(board[2][2])
    nine = nine.replace('[', '')
    nine = nine.replace(']', '')


    print(f"+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {one}   |   {two}   |   {three}   |")
    print(f"|       |       |       |")
    print(f"+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {four}   |   {five}   |   {six}   |")
    print(f"|       |       |       |")
    print(f"+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {seven}   |   {eight}   |   {nine}   |")
    print(f"|       |       |       |")
    print(f"+-------+-------+-------+")
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):

    movelist = make_list_of_free_fields(board)
    while True:

        try:
            num = int(input("Make your move (Enter a value from 1-9): "))

            if num == 1 and (0,0) in movelist:
                board[0][0] = "◯"
                break
    
            elif num == 2 and (0,1) in movelist:
                board[0][1] = "◯"
                break

            elif num == 3 and (0,2) in movelist:
                board[0][2] = "◯"
                break

            elif num == 4 and (1,0) in movelist:
                board[1][0] = "◯"
                break

            elif num == 5 and (1,1) in movelist:
                board[1][1] = "◯"
                break

            elif num == 6 and (1,2) in movelist:
                board[1][2] = "◯"
                break

            elif num == 7 and (2,0) in movelist:
                board[2][0] = "◯"
                break

            elif num == 8 and (2,1) in movelist:
                board[2][1] = "◯"
                break

            elif num == 9 and (2,2) in movelist:
                board[2][2] = "◯"
                break
        
            else:
                print("There is already a marker there")
        except:
            print("No Input detected...Enter an number from 1-9")
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    newlist = []
    for i in range(3):
        for i2 in range(3):
            if board[i][i2] != "◯" and board[i][i2] != "╳":
                newlist.append((i,i2))
    return newlist
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):

        #OC 1
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        print(f'''
The Winner Is {sign}''')

    #OC 2
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        print(f'''
The Winner Is {sign}''')

    #OC 3
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        print(f'''
The Winner Is {sign}''')

    #OC 4
    elif board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        print(f'''
The Winner Is {sign}''')

    #OC 5
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        print(f'''
The Winner Is {sign}''')

    #OC 6
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        print(f'''
The Winner Is {sign}''')

    #OC 7
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        print(f'''
The Winner Is {sign}''')

    #OC 8
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        print(f'''
The Winner Is {sign}''')

    else:
        return 1
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    
    movelist = make_list_of_free_fields(board)
    while True:

        num = randrange(1,10)

        if num == 1 and (0,0) in movelist:
            board[0][0] = "╳"
            break
    
        elif num == 2 and (0,1) in movelist:
            board[0][1] = "╳"
            break

        elif num == 3 and (0,2) in movelist:
            board[0][2] = "╳"
            break

        elif num == 4 and (1,0) in movelist:
            board[1][0] = "╳"
            break

        elif num == 5 and (1,1) in movelist:
            board[1][1] = "╳"
            break

        elif num == 6 and (1,2) in movelist:
            board[1][2] = "╳"
            break

        elif num == 7 and (2,0) in movelist:
            board[2][0] = "╳"
            break

        elif num == 8 and (2,1) in movelist:
            board[2][1] = "╳"
            break

        elif num == 9 and (2,2) in movelist:
            board[2][2] = "╳"
            break
        else:
            None
    # The function draws the computer's move and updates the board.



playing = True
while playing == True:
    
    draw_move(deboard)
    display_board(deboard)

    v2 = victory_for(deboard,"╳")
    if v2 != 1:
        display_board(deboard)
        break

    if len(make_list_of_free_fields(deboard)) == 0:
        display_board(deboard)
        print("Game Over - DRAW")
        break

    enter_move(deboard)

    v1 = victory_for(deboard,"◯")
    if v1 != 1:
        display_board(deboard)
        break

    if make_list_of_free_fields(deboard) == 0:
        break


