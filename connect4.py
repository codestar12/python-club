
# creates a matrix of * characters
# to represent the game
matrix = []
playedMoves = []
for rows in range(6):

    matrix.append([])

    for columns in range(6):

        matrix[rows].append("*")


def printMatrix(matrix):
    for rows in range(7):
        for columns in range(6):
            if(rows == 0):  # prints characters for Columns
                print chr(65 + columns) + " ",

            else:
                print matrix[rows - 1][columns] + " ",

        print " ",
        if(rows != 0):  # prints numbers to the side
            print(7 - rows)

        else:
            print" "

# places piece into game matrix


def playPiece(matrix, piece, column):

    for i in range(6):

        if(matrix[5 - i][column] == '*'):
            playedMoves.append([(5 - i), column])
            matrix[5 - i][column] = piece
            break

#	return matrix


def checkWin(matrix, playedMoves):

    lastMove = len(playedMoves) - 1
    row = playedMoves[lastMove][0]
    column = playedMoves[lastMove][1]
    piece = matrix[row][column]
    count = 0

    # checks down
    for i in range(4):
        if row + i < 6:  # checks in bounds
            if matrix[row + i][column] != piece:
                count = 0
            else:
                count += 1
        else:
            count = 0

    if count == 4:
        print "you have won vertically"

    count = 0  # resets count

    # checks horizantally
    for i in range(7):
        # checks that the column is in bounds
        if (column - 3 + i) >= 0 and (column - 3 + i) < 6:
                # if you past the middle and you hit a wrong piece
                # you can stop checking you cant win
            if i > 3:
                if matrix[row][column - 3 + i] != piece:
                    break
                else:
                    count += 1
            elif matrix[row][column - 3 + i] != piece:
                count = 0
            else:
                count += 1
        if count == 4:
            break

    if count == 4:
        print "you have won horizantally"

    count = 0

    # check up and right
    for i in range(-3, 4):
        #counts from - 3 to 3 by 1
        if ((column + i >= 0 and row - i >= 0) and
                (column + i < 6 and row - i < 6)):

            if matrix[row - i][column + i] != piece:
                count = 0
            else:
                count += 1
        if count == 4:
            break
    if count == 4:
        print "you have won diagonally"

    count = 0
    # check up and right
    for i in range(3, -4, -1):  # counts from 3 to -3 by -1
        if ((column + i >= 0 and row + i >= 0) and
                (column + i < 6 and row + i < 6)):
            if matrix[row + i][column + i] != piece:
                count = 0
            else:
                count += 1
        if count == 4:
            break
    if count == 4:
        print "you have won diagonally"

    count == 0


def runGame(matrix):

    moves = 1
    while(True):

        column = raw_input("player " + str(moves) + " make a move: ")

        column = ord(column) - 65
        if(moves % 2 == 1):
            playPiece(matrix, 'x', column)
            moves = moves + 1

        else:
            playPiece(matrix, 'O', column)
            moves = moves + 1

        printMatrix(matrix)
        # print(playedMoves)
        checkWin(matrix, playedMoves)

printMatrix(matrix)
runGame(matrix)
