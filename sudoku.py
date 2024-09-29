from math import sqrt, floor
from copy import deepcopy
from random import shuffle, random

small = [[1, 0, 0, 0],
         [0, 4, 1, 0],
         [0, 0, 0, 3],
         [4, 0, 0, 0]]

small2 = [[0, 0, 1, 0],
          [4, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 3, 0, 0]]

big = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [4, 0, 0, 7, 8, 9, 0, 0, 0],
       [7, 8, 0, 0, 0, 0, 0, 5, 6],
       [0, 2, 0, 3, 6, 0, 8, 0, 0],
       [0, 0, 5, 0, 0, 7, 0, 1, 0],
       [8, 0, 0, 2, 0, 0, 0, 0, 5],
       [0, 0, 1, 6, 4, 0, 9, 7, 0],
       [0, 0, 0, 9, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 3, 0, 0, 0, 2]]

big2 = [[7, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 5, 0, 0, 0, 9, 0, 0, 0],
        [8, 0, 0, 0, 3, 0, 0, 4, 0],
        [0, 0, 0, 7, 6, 0, 0, 0, 8],
        [6, 2, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 7, 0],
        [0, 0, 0, 6, 0, 0, 9, 8, 0],
        [0, 0, 0, 0, 2, 7, 3, 0, 0],
        [0, 0, 2, 0, 8, 0, 0, 5, 0]]

big3 = [[0, 0, 8, 1, 9, 0, 0, 0, 6],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 6, 0, 0, 1, 3, 0],
        [0, 0, 6, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 2, 0, 0, 5],
        [0, 0, 0, 0, 3, 0, 9, 0, 0],
        [0, 1, 0, 4, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 5, 7]]

big4 = [[0, 0, 0, 6, 0, 0, 2, 0, 0],
        [8, 0, 4, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [4, 0, 5, 0, 0, 0, 0, 0, 7],
        [7, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 5, 0, 0, 0, 8],
        [3, 0, 0, 0, 7, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 1, 9, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 6, 0]]

giant = [[ 0,  0, 13,  0,  0,  0,  0,  0,  2,  0,  8,  0,  0,  0, 12, 15],
         [ 7,  8, 12,  2, 10,  0,  0, 13,  0,  0, 14, 11,  6,  9,  0,  4],
         [11, 10,  0,  0,  0,  6, 12,  5,  0,  3,  0,  0,  0, 14,  0,  8],
         [ 1,  0,  0,  0, 14,  0,  2,  0,  0,  4,  6,  0, 16,  3,  0, 13],
         [12,  6,  0,  3,  0,  0, 16, 11,  0, 10,  1,  7, 13, 15,  0,  0],
         [ 0, 13,  0,  0,  0, 15,  8,  0, 14,  0,  0,  0,  0, 16,  5, 11],
         [ 8,  0, 11,  9, 13,  0,  7,  0,  0,  0,  0,  3,  2,  4,  0, 12],
         [ 5,  0,  0, 16, 12,  9,  0, 10, 11,  2, 13,  0,  0,  0,  8,  0],
         [ 0,  0,  0,  0, 16,  8,  9, 12,  0,  0,  0,  0,  0,  6,  3,  0],
         [ 2, 16,  0,  0,  0, 11,  0,  0,  7,  0, 12,  6,  0, 13, 15,  0],
         [ 0,  0,  4,  0,  0, 13,  0,  7,  3, 15,  0,  5,  0,  0,  0,  0],
         [ 0,  7,  0, 13,  4,  5, 10,  0,  1,  0, 11, 16,  9,  0, 14,  2],
         [ 0,  2,  8,  0,  9,  0,  0,  0,  4,  0,  7,  0,  0,  5,  0,  0],
         [14,  0,  0,  0, 15,  2, 11,  4,  9, 13,  3,  0, 12,  0,  0,  0],
         [ 0,  1,  9,  7,  0,  0,  5,  0,  0, 11, 15, 12,  0,  0,  0,  0],
         [16,  3, 15,  0,  0, 14, 13,  6, 10,  1,  0,  2,  0,  8,  4,  9]]

giant2 = [[ 0,  5,  0,  0,  0,  4,  0,  8,  0,  6,  0,  0,  0,  0,  9, 16],
          [ 1,  0,  0,  0,  0,  0,  0, 13,  4,  0,  0,  7, 15,  0,  8,  0],
          [13,  0,  0,  0,  0,  7,  3,  0,  0,  0,  0,  9,  5, 10,  0,  0],
          [ 0, 11, 12, 15, 10,  0,  0,  0,  0,  0,  5,  0,  3,  4,  0, 13],
          [15,  0,  1,  3,  0,  0,  7,  2,  0,  0,  0,  0,  0,  5,  0,  0],
          [ 0,  0,  0, 12,  0,  3,  0,  5,  0, 11,  0, 14,  0,  0,  0,  9],
          [ 4,  7,  0,  0,  0,  0,  0,  0, 12,  0, 15, 16,  0,  0,  0,  0],
          [ 0,  0,  0,  0, 14,  0, 15,  0,  6,  9,  0,  0,  0,  0, 12,  0],
          [ 3,  0, 15,  4,  0, 13, 14,  0,  0,  0,  0,  1,  0,  0,  7,  8],
          [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 10,  0,  0,  0,  0],
          [11,  0, 16, 10,  0,  0,  0,  0,  0,  7,  0,  0,  0,  3,  5,  0],
          [ 0,  0, 13,  0,  0,  0,  0,  0, 14,  0, 16, 15,  0,  9,  0,  1],
          [ 9,  0,  2,  0,  0, 14,  0,  4,  8,  0,  0,  0,  0,  0,  0,  0],
          [ 0, 14,  0,  0,  0,  0,  0, 10,  9,  0,  3,  0,  0,  0,  1,  7],
          [ 8,  0,  0,  0, 16,  0,  0,  1,  2, 14, 11,  4,  0,  0,  0,  3],
          [ 0,  0,  0,  1,  0,  0,  5,  0,  0, 16,  0,  6,  0, 12,  0,  0]]

giant3 = [[ 0,  4,  0,  0,  0,  0,  0, 12,  0,  1,  0,  0,  9,  0,  8,  0],
          [15, 14,  0,  0,  9,  0,  0, 13,  8,  0,  0, 10,  1,  0,  0,  0],
          [ 0,  7,  0,  0,  0,  0,  0,  8, 16,  0, 14,  0,  0,  2,  0,  0],
          [ 0,  0,  0,  9,  0,  0, 11,  0,  0,  0,  0,  0,  5,  0,  0, 15],
          [ 3,  0, 12,  0,  7,  0, 10,  0,  0, 11,  2,  0,  0,  0,  0,  6],
          [14,  8,  0,  0,  0, 12,  0,  6,  0,  0,  0, 16,  0,  0,  0, 10],
          [ 0, 16,  0,  0, 13,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12,  0],
          [ 6,  0,  0,  0,  0,  8,  0,  5,  1,  7, 13,  0, 11,  0,  0, 14],
          [ 0,  0,  0,  2,  0,  0, 16,  0, 15, 12,  0,  3, 10,  7,  0,  0],
          [ 0,  9,  0,  5, 11,  0,  3,  0,  4, 13, 16,  0,  0, 15,  6,  0],
          [ 0,  0,  0,  0,  5,  4,  0,  0,  9,  6,  0,  2,  0,  0,  0,  0],
          [ 1,  0,  0,  0,  0, 15, 12,  0,  0,  0,  5,  0,  0,  0,  9,  0],
          [12, 10,  0, 15,  0,  1,  0,  0,  2,  9,  3,  4,  0,  0,  5,  0],
          [ 0,  0,  0,  3, 10,  0,  4,  0,  0, 15,  0,  0,  0,  0,  0,  0],
          [ 0,  0,  0,  0, 16,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10, 11],
          [11,  6,  8,  0,  0,  0, 15,  0, 14,  0,  0,  0,  0, 13,  0,  2]]

sudokus = [[], [], [small, small2], [big, big2, big3, big4], [giant, giant2, giant3]]

#################################### PRINT BOARD ####################################
def print_board(board):
    
    k = (len(board))                                              
    sudokuBoard = ""

    horizontalStr = " -" * 2 * k                                # First horizontal line 
    # print(horizontalStr)       
    sudokuBoard += "{}\n".format(horizontalStr)                 # Print first horizonatal line

    for x in range(0, k):                                       # x-value (horizontal)

        verticalStr = ""

        for y in range(0, k):                                   # y-value (vertical)

            if board[x][y] == 0:                                # Change 0 to space
                verticalStr += "   "
            elif board[x][y] == 10:                             # Case check (eg. 10 -> A etc)
                verticalStr += " A "
            elif board[x][y] == 11:
                verticalStr += " B "
            elif board[x][y] == 12:
                verticalStr += " C "
            elif board[x][y] == 13:
                verticalStr += " D "
            elif board[x][y] == 14:
                verticalStr += " E "
            elif board[x][y] == 15:
                verticalStr += " F "
            elif board[x][y] == 16:
                verticalStr += " G "
            else:   
                verticalStr += " {} ".format(board[x][y])       # Append board value into vertical string


            if (y + 1) % sqrt(k) == 0:                          # Check if the remainder is 0, if yes, print | (| 1 2 3 | <-- )
                verticalStr += "|"
            else: 
                verticalStr += " "

        verticalStr = '|' + verticalStr                        # Add | in front of vertical string
        # print(verticalStr)
        sudokuBoard += "{}\n".format(verticalStr)

        if (x + 1) % sqrt(k) == 0:                             # Check if the remainder is 0, if yes, print horizontal line
            # print(horizontalStr)
            sudokuBoard += "{}\n".format(horizontalStr)

    print(sudokuBoard)

# print_board(big)

#################################### SUBGRID VALUE ####################################

''' By finding the subgrid value for any size of sudoku, at first we need to know which specific subgrid for the
 given row and column value (r and c). For example, I need to know what is the which subgrid for a 9x9 board
 at row 5 and column 1. By using "floor(n / sqrtk) * sqrtk", I can find the value for the starting point subgrid value.
 
 Using the given example, the value of starting point subgrid value for row 5 will be 3 and column 1 will be 0.
 | -  -  - |
 | -  -  - |             # The point or index is at (1, 5)
 | -  -  - |             # Starting point will be at (0, 3)
 -----------             # x is horizontal
 | SP -  - |             # y is veritcal
 | -  -  - |
 | -  o  - |

# Then, we only need to use the point value from starting point to find our subgrid value. So, we can use range of 3 to 5 
# for row value and range of 0 to 2 for column value (range(x, x + sqrt(k)) and range(y, y + sqrt(k))
# where k is square root of the board length). In the for loop, it will check if the point is not 0, it will append inside
# a new number list. Lastly, a number list of the subgrid value will be return. '''

def subgrid_value(board, r, c):

    sqrtk = int(sqrt(len(board)))                           # Find sqrt of k
    rowDivision = floor(r / sqrtk) * sqrtk                  # Finding the starting subgrid row value. Floor is to make sure that min is 0
    columnDivision = floor(c / sqrtk) * sqrtk               # Finding the starting subgrid column value. Floor is to make sure that min is 0
    global numList
    numList = []

    # print("k: {}, Row: {}, Column: {}".format(sqrtk, rowDivision, columnDivision))

    for x in range(rowDivision, rowDivision + sqrtk):           # Range: subgrid row value Ex. rowDivision = 6, sqrtk = 3, range(6, 9)
        for y in range(columnDivision, columnDivision + sqrtk): # Same applied to range above but with column

            # print("x: {}, y: {}".format(x, y))

            if board[x][y] != 0:                            # Check if its not 0, append the number
                numList.append(board[x][y])

    # print(numList)
    return numList
# subgrid_value(big, 5, 1)


#################################### OPTION ####################################
''' Find the number at row r and column c and subgrid at the point, zero will be excluded.
    Then find the number that is not visible at row, column and subgrid. '''


def options(board, r, c):

    k = len(board)
    
    row = []
    column = []
    global missingNumber
    missingNumber = []

    # For range and column
    for x in range(k):
        
        if board[r][x] != 0:                # Find the number at row r, zero is excluded
            row.append(board[r][x]) ;       

        if board[x][c] != 0:                # Find the number at column c, zero is excluded
            column.append(board[x][c])

    # print(row)
    # print(column)
    
    # For subgrid
    subgrid_value(board, r, c)          # Find subgrid number
    # print(numList)

    for x in range(1, k + 1):
 
        if x not in row and x not in column and x not in numList:   # Find the number thats not in row column and subgrid
            missingNumber.append(int(x))


    return missingNumber

# options(giant2, 1, 5)

#################################### HINT ####################################

'''I had implemented a hint function that finds every grid that has the least number that can be placed.
   So, I used options function to find the missing numbers and assign the point of row and column that has
   the least number that can be input. '''

def hint(board):

    k = len(board)

    global num1
    global num2
    num1 = 0
    num2 = 0
    minNumber = k

    for x in range(k):
        for y in range(k):

            if board[x][y] == 0:
                options(board, x, y)
                
                
                if len(missingNumber) < minNumber:
                    minNumber = len(missingNumber)
                    num1 = x
                    num2 = y

    return num1, num2
############################################################################

def value_by_single(board, i, j):

    length = len(board)
    sqrtk = int(sqrt(len(board)))
    rowDivision = floor(i / sqrtk) * sqrtk    
    columnDivision = floor(j / sqrtk) * sqrtk

    # FORWARD SINGLE
    missNum = options(board, i, j)
        
    if len(missNum) == 1:
        return missNum[0]
    
    # BACKWARD SINGLE R
    rowList = []

    for y in range(length):
        if board[i][y] != 0:
            rowList.append(None)
        else:
            rowList.append(options(board, i, y))

    for numCheck in range(1, length + 1):

            counter = 0

            for subNumList in rowList: 
                if subNumList != None and numCheck in subNumList: counter += 1

    if counter == 1:

            missingNum = options(board, i, j)
            if numCheck in missingNum: return numCheck

    # BACKWARD SINGLE C
    columnList = []

    for x in range(length):
        if board[x][i] != 0:
            columnList.append(None)
        else:
            columnList.append(options(board, x, i))

    for numCheck in range(1, length + 1):

            counter = 0

            for subNumList in columnList:
                if subNumList != None and numCheck in subNumList:
                        counter += 1

    if counter == 1:

            missingNum = options(board, i, j)
            if numCheck in missingNum: return numCheck

    
    # BACKWARD SINGLE SUBGRID       
    missNumList = []
    for x in range(rowDivision, rowDivision + sqrtk):
                
        for y in range(columnDivision, columnDivision + sqrtk): 
            # print("x: {}, y: {}".format(x, y))
            if board[x][y] != 0:
                missNumList.append(None)
            else:
                missNumList.append(options(board, x, y))
    
    for numCheck in range(1, length + 1):

        counter = 0

        for subNumList in missNumList:
            if subNumList != None and numCheck in subNumList:
                counter += 1

        # print("Number: {}, Count: {}".format(numCheck, counter))
                
        if counter == 1:

            missingNum = options(board, i, j)
            if numCheck in missingNum: return numCheck

    return None
    
    

def forward_single(board):

    length = len(board)

    def func(board, i, j):
        missNum = options(board, i, j)
        
        if len(missNum) == 1:
            return missNum[0]
        else:
            return 0
    
    for x in range(length):
        for y in range(length):

            if board[x][y] == 0:
                num = func(board, x, y)
                board[x][y] = num

                if num != 0:
                    return False

    return True

def backward_single_horizontal(board):

    counter = 0
    length = len(board)

    for x in range(length):

        missNumList = []

        for y in range(length):
            if board[x][y] != 0:
                missNumList.append(None)
            else:
                missNumList.append(options(board, x, y))

        for numCheck in range(1, length + 1):

            counter = 0

            for subNumList in missNumList:
                if subNumList != None and numCheck in subNumList:
                        counter += 1

            # print("Number: {}, Count: {}".format(numCheck, counter))
            
            if counter == 1:

                for y in range(len(board)):
                    missingNum = options(board, x, y)

                    if board[x][y] == 0:
                        missingNum = options(board, x, y)

                        if numCheck in missingNum:
                        
                            board[x][y] = numCheck

                            return False
    return True

def backward_single_vertical(board):

    counter = 0
    length = len(board)

    for y in range(length):

        missNumList = []

        for x in range(length):
            if board[x][y] != 0:
                missNumList.append(None)
            else:
                missNumList.append(options(board, x, y))

        for numCheck in range(1, length + 1):

            counter = 0

            for subNumList in missNumList:
                if subNumList != None and numCheck in subNumList:
                        counter += 1

            # print("Number: {}, Count: {}".format(numCheck, counter))
            
            if counter == 1:
                for x in range(len(board)):
                    missingNum = options(board, x, y)

                    if board[x][y] == 0:
                        missingNum = options(board, x, y)

                        if numCheck in missingNum:
                        
                            board[x][y] = numCheck

                            return False
    return True



def backward_single_subgrid(board):

    
    length = len(board)
    sqrtk = int(sqrt(len(board))) 
    r = c = range(0, length, sqrtk) 

    for row in r:
        for column in c:
            
            rowDivision = floor(row / sqrtk) * sqrtk                  # Finding the starting subgrid row value. Floor is to make sure that min is 0
            columnDivision = floor(column / sqrtk) * sqrtk
            
            # print("k: {}, Row: {}, Column: {}".format(sqrtk, rowDivision, columnDivision))
           
            missNumList = []
            for x in range(rowDivision, rowDivision + sqrtk): 
                
                for y in range(columnDivision, columnDivision + sqrtk): # Same applied to range above but with column
                    # print("x: {}, y: {}".format(x, y))
                    if board[x][y] != 0:
                        missNumList.append(None)
                    else:
                        missNumList.append(options(board, x, y))
            # print(missNumList)

            for numCheck in range(1, length + 1):

                counter = 0

                for subNumList in missNumList:
                    if subNumList != None and numCheck in subNumList:
                            counter += 1

                # print("Number: {}, Count: {}".format(numCheck, counter))
                
                if counter == 1:
                    for x in range(rowDivision, rowDivision + sqrtk):              
                        for y in range(columnDivision, columnDivision + sqrtk):

                            if board[x][y] == 0:
                                missingNum = options(board, x, y)

                                if numCheck in missingNum:

                                    board[x][y] = numCheck
                                    return False
    return True


def inferred(board):

    check1 = False
    check2 = False
    check3 = False
    check4 = False


    while not check1 and not check2 and not check3 and not check4:
        check1 = forward_single(board)

        if check1:
            check2 = backward_single_horizontal(board) 


            if not check2:
                check1 = False
            else:
                check3 = backward_single_vertical(board)

                if not check3:
                    check1 = check2 = False
                else:
                    check4 = backward_single_subgrid(board)

                    if not check4:
                        check1 = check2 = check3 = False
    
    
    print_board(board)

def empty_fields(board):
    """
    Input : Sudoku board
    Output: list of fields, i.e., pairs of row and column indices, that are not
            empty (i.e., value is not equal to 0)
    """
    n = len(board)
    k = int(sqrt(n))
    res = []
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                res.append((i, j))
    return res

def completed(board):
    
    length = len(board)
    for x in range(length):
        for y in range(length):
            if board[x][y] == 0:
                return False
        return True

## SUB BACKTRACK ##
def bt(board):

    if len(empty_fields(board)) == 0:
        
        return board
    else:
        coordinates = empty_fields(board)
        
        x = coordinates[0][0]
        y = coordinates[0][1]

        option = options(board, x, y)

        for num in option:
            
            if len(option) == 0:
                return False
                
            board[x][y] = num
            
            bt(board)
            
            if len(empty_fields(board)) == 0:                            
                return board
            
                
            board[x][y] = 0

        if len(empty_fields(board)) == 0:  
            board[x][y] = 0                          
            return board

def backtrack(board):
    copyBoard = deepcopy(board)
    print("Inferred: ")
    inferred(copyBoard)
    if len(empty_fields(copyBoard)) != 0:
        bt(copyBoard)
        
    print("Done! ")
    print(copyBoard)
    print_board(copyBoard)
    return copyBoard

'''
- Instead of brute forcing by trying every value for every single boxes, I use options function to find the possible options for the value so that
  number can't be put can be removed from the missing number list. Then, I can find the first box that have the smallest options or less number possible
  to put inside the box (len(options(board, x, y)) so that it will start from the box and reduce the time complexity. 
- By implementing the inferred inside my backtracking, it will find the value of the boxes using inferred first with 3 rules. After
  that, it will start finding using the backtracked if inferred can't find all the value. So, it can definitely reduce the time complexity
  for easier board but big board such as giant3 still needs some time to complete it. 
'''

def generate(k):
    
    if k > 1:
        kSqr = k ** 2
        sudoku = []
        randomRow = int(random() * kSqr)
        numList = []
        for x in range(1, kSqr + 1):
            numList.append(x)
        shuffle(numList)
        
        # append the number list into a random row in sudouku
        for x in range(kSqr):
            lst = []
            for y in range(kSqr):
                
                if randomRow == x:
                    lst.append(numList[y])
                else:
                    lst.append(0)
            sudoku.append(lst)
        sudoku = backtrack(sudoku)
        
        # Change the value to 0 by random
        for x in range(kSqr):
            for y in range(kSqr):
                check = int(random() * 2)
                
                if check == 1:
                    sudoku[x][y] = 0
        print("Random sudoku board: ")
        print_board(sudoku)
    else:
        print("The value of the parameter must be bigger than 1.")    

'''
The first step that I did for my generate function is to find the k square which will be used for the number of value per subgrid, row or column. Then, a list will be created
with k** 2 numbers of element. Let say we use k = 2, k square will be 4 and it will be the number of value per subgrid, row or column. It will be shuffled using the shuffle function. 
Next I created a random number range depends on the k value for my randomRow. It will determine where the number list should append. After finish appending, I run the backtrack to
find the solution of the board. Lastly, I create a random check variable range from 0 to 1 to change the number to 0 if the check equals to 1. It means that for every boxes in the 
sudoku board, it will have a 50% chance to make the value to 0. 
'''

#################################### PLAY ####################################
def play(board):
    """
    Input : Sudoku board
    Effect: Allows user to play board via console
    """
    print_board((board))
    
    global restartBoard
    restartBoard = deepcopy(board)
    
    global undoBoard
    undoBoard = deepcopy(board)

    global solveBoard
    solveBoard = deepcopy(board)

    while True:

        inp = input().split(' ')

        if len(inp) == 3 and inp[0].isdecimal() and inp[1].isdecimal() and inp[2].isdecimal():

            undoBoard = deepcopy(board)

            i = int(inp[0])
            j = int(inp[1])
            x = int(inp[2])

            options(board, i, j)   # New option function implementation

            if board[i][j] == 0 or board[i][j] == '*':
                if x in missingNumber:
                    board[i][j] = x
                else: 
                    print("Invalid input: There are duplicate numbers.")
            else:
                     print("Invalid input: Space has been occupied")

            print_board(board)

        elif len(inp)==3 and (inp[0] == 'n' or inp[0] == 'new') and inp[1].isdecimal() and inp[2].isdecimal():
            
            k = int(inp[1])
            d = int(inp[2])

            if k < len(sudokus) and 0 < d <= len(sudokus[k]):
                board = sudokus[k][d-1]
                
                print_board(board)
                restartBoard = deepcopy(board) # For restart
            else:

                print('board not found')

        elif inp[0] == 'q' or inp[0] == 'quit':
            return

        elif inp[0] == 'r' or inp[0] == 'restart':  # Restart function 
            
            board.clear()
            board = deepcopy(restartBoard)
            print_board(board)

        elif inp[0] == 'u' or inp[0] == 'undo':
            board.clear()
            board = deepcopy(undoBoard)
            print_board(board)

        elif inp[0] == 'h' or inp[0] == 'hint':
            
            hint(board)
            board[num1][num2] = '*'
            print_board(board)

        elif inp[0] == 'i' or inp[0] == 'infer':
            inferred(solveBoard)

        elif inp[0] == 's' or inp[0] == 'solve':
            backtrack(board)

        elif inp[0] == 'g' or inp[0] == 'generate' and inp[1].isdecimal():
            print(inp[1])
            generate(int(inp[1]))

        else:
            print('Invalid input')

play(big)
