#!/usr/bin/python3

import checkmate

def main():

    # TEMPLATE for THE CHESS BOARD
    boardMap = [
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],   
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]

    # -----------------------------------
    #              COORDINATES
    #
    # ROW        1 2 3 4 5 6 7 8
    #            0 1 2 3 4 5 6 7
    #
    # COLUMN     TRANSLATION MAP
    #
    #            a b c d e f g h
    #            0 1 2 3 4 5 6 7
    #
    # -----------------------------------

    # CONTROLLER: For Position Testing [ROW] [COLUMN] - FLIP
    boardMap[6][6] = "K"
    boardMap[6][4] = "Q"
    boardMap[3][0] = "R"  
    boardMap[0][7] = "B"  
    boardMap[4][3] = "P"  

    # DECLARATION: INITIATION for VARIABLEs as HOLDER (ARRAY FORMAT) - NUMERIC
    posKing = None
    queens = []
    rooks = []
    bishops = []
    pawns = []

    # PROCESS: SORTING, PUTTING, and PACKING PAIRS of VARIABLES-VALUES as POSITION
    for i in range(8):
        for j in range(8):
            piece = boardMap[i][j]
            if piece == "K":
                posKing = (i, j)            # PACKING 2-ELEMENTS INTO 1-TUPLE
            elif piece == "Q":
                queens.append((i, j))       # TUPLE INSIDE - 2-ELEMENTS - COUNTED AS 1-ITEM
            elif piece == "R":
                rooks.append((i, j))        # APPEND to ADD DATA INSIDE
            elif piece == "B":
                bishops.append((i, j))
            elif piece == "P":
                pawns.append((i, j))

    # Print board
    print()                                 # SKIPPING 1-NEW LINE
    print("  a b c d e f g h")              # COLUMN LABEL
    for i in range(7, -1, -1):              # RECURSIVE ROW LOOP (i) and LABELLING ROW from 8 to 1
        print(i + 1, end=" ")               # RECURSIVE i + 1 to Make 8 LABEL
        for j in range(8):                  # COLUMN LOOP (j)
            print(boardMap[i][j], end=" ")  # START PRINTING the BOARD MAP DOTS + PIECE/s POSITIONS
        print()                             # SKIPPING 1-NEW LINE
    print("  a b c d e f g h\n")            # BOTTOM-SIDE LABEL

    if not posKing:
        print("No King Found")              # IF KING DOES NOT EXIST      
    else:  
        result = checkmate.checkmate(posKing, queens, rooks, bishops, pawns)    # CALL CHECKMATE
                                            # DO CALCULATION - WITH ALL PASSED PARAMETERS
        print(result)                       # OUTPUT THE RESULT of CALCULATION
        print()

if __name__ == "__main__":                  # FAILSAFE - CAN BE RUN ONLY FROM INSIDE THE FILE

    main()                                  # CALLING MAIN FUNCTION