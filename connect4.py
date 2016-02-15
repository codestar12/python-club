
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
    	for columns in range (6):
	
	    if(rows == 0): # prints characters for Columns
	        print chr(65 + columns) + " ",
	    
	    else:
		 print matrix[rows-1][columns] + " ",


        print " ",
	if(rows != 0): # prints numbers to the side 
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
    
	
    lastMove = len(playedMoves)-1
    row = playedMoves[lastMove][0]
    column = playedMoves[lastMove][1]
    win = True
    piece = matrix[row][column]
    
    # checks down
    for i in range(4):

        if(row + i <=  5): # checks in bounds

            if(matrix[row + i][column] != piece):

                win = False
                break
        else:
            win = False

    # checks right
    for i in range(4):

        if(column + i <=  5): # checks in bounds

            if( matrix[row][column + i] != piece ):

                win = False
                break
        else:
            win = False        


   # checks left
#    for i in range(4):
#
#        if(column - i <  0): # checks in bounds
#
#            if( matrix[row][column - i] != piece ):
#
#                win = False
#                break
#        else:
#            win = False

    if(win):
	print("you've won")  

     	
def runGame(matrix):

	moves = 1
	while(True):

	    column = raw_input("player " + str(moves) + " make a move: ")
	    
	    column = ord(column) - 65	
	    if(moves%2 == 1):
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
            


