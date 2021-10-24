gameboard = [
    ['', '', '', 'X'],
    ['', '', 'X', ''],
    ['', 'X', '', ''],
    ['', '', '', '']
]

turn = 'X'


def print_gameboard(gameboard):
    print(gameboard[0])
    print(gameboard[1])
    print(gameboard[2])
    print(gameboard[3])


def winner_exists(gameboard, player):
    n = len(gameboard)

    # for rows
    for i in range(n):
        win = True
        for j in range(n):
            if gameboard[i][j] != player:
                win = False
                break
        if win:
            return win

    # for columns
    for i in range(n):
        win = True
        for j in range(n):
            if gameboard[i][j] != player:
                win = False
                break
        if win:
            return win

    # for diagonal
    for i in range(n):
        win = True
        if gameboard[i][i] != player:
            win = False
            break
        if win:
            return win

    for i in range(n):
        win = True
        if gameboard[i][n-1-i] != player:
            win = False
            break
        if win:
            return win


turn_counter = 0

game_end = False
print_gameboard(gameboard)
while not game_end:
    print('Igrac', turn, 'je na potezu, unesite koordinate')

    x = int(input())
    y = int(input())

    while (x > 3 and y > 3) or gameboard[x][y] != '':
        print('Unos je pogresan - polje je zauzeto il ste unijeli nevalidno polje.')
        x = int(input())
        y = int(input())

    gameboard[x][y] = turn
    turn_counter += 1
    if winner_exists(gameboard, turn):
        print(turn, 'is the winner!!!')
        print_gameboard(gameboard)
        gameboard = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        print_gameboard(gameboard)
        continue
    elif turn_counter == 16:
        print('Draw game!!!')
        print_gameboard(gameboard)
        gameboard = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        print_gameboard(gameboard)
        continue
    if turn == 'Y':
        turn = 'X'
    else:
        turn = 'Y'
    print_gameboard(gameboard)
