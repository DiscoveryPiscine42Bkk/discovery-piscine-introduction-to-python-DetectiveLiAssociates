#!/usr/bin/python3

#------------------------------------------------#
# 42Bangkok - Python Class - May 5th-9th, 2025   #
#                                                #
# DEVOPS: saku- (Detective Li) | temeenku (Aun)  #
#------------------------------------------------#

import random, checkmate

#def board(alpha,tile,margin,posiQ,posjQ):
def board(alpha,tile,margin,display,xff0000,xffde21,x696969,xf9f9f9):

    boardMap=[
        ["·","·","·","·","·","·","·","·",],
        ["·","·","·","·","·","·","·","·",],
        ["·","·","·","·","·","·","·","·",],
        ["·","·","·","·","·","·","·","·",],
        ["·","·","·","·","·","·","·","·",],
        ["·","·","·","·","·","·","·","·",],
        ["·","·","·","·","·","·","·","·",],
        ["·","·","·","·","·","·","·","·",] 
    ]

    #boardMap[posiQ][posjQ]="Q"
    for piece, (i,j) in display.items():
        if piece=='K':
            paint=xffde21
        else:
            paint=xff0000
        boardMap[i][j]=paint+piece+xf9f9f9

    print()
    print(((margin+2)*" "),end="")
    for a in alpha:
        print(a,end=" ")
    print()

    for i in range((tile-1),-1,-1):
        print((margin*" "),end="")
        print(i+1,end=" ")
        for j in range(0,tile):
            if((i+j)%2)==0:
                alter=x696969
            else:
                alter=xf9f9f9
            print(f"{alter}{boardMap[i][j]}{xf9f9f9}",end=" ")
        print()

    print()
    
    title="Positions:"
    print((margin*" "),end="")
    print(f"{title:^18}")
    print((margin*" "),end="")
    print(f"{('-'*17):^18}")
    for piece, (i,j) in display.items():
        col=alpha[j]
        row=i+1
        print(((margin+3)*" "),end="")
        print(f"{piece} - is at {col}{row}")
    print((margin*" "),end="")
    print(f"{('-'*17):^18}")
    print()

if __name__=="__main__":

    tile=8
    margin=139

    xff0000="\033[91m"
    xf9f9f9="\033[0m"
    xffde21="\033[93m"
    x696969="\033[32m"
    x00ffff="\033[96m"

    alpha=['a','b','c','d','e','f','g','h']
    pieces=['Q','B','R','P']
    unique=set()
    display={}

    #Q-TESTING
    #posiQ=random.randint(0,(tile-1))
    #posjQ=random.randint(0,(tile-1))
    #board(tile,margin,posiQ,posjQ)

    for z in pieces:
        for f in range(999):
            posi=random.randint(0,(tile-1))
            posj=random.randint(0,(tile-1))
            if(posi,posj) not in unique:
                display[z]=(posi,posj)
                unique.add((posi,posj)) #THE ALMOST UNTHINKABLE TRICK to HACK THE ERROR
                if z=='Q':
                    posQueen=(posi,posj)
                elif z=='R':
                    posRook=(posi,posj)
                elif z=='P':
                    posPawn=(posi,posj)
                else:
                    posBishop=(posi,posj)    
                break

    board(alpha,tile,margin,display,xff0000,xffde21,x696969,xf9f9f9)

    while True:
        print(((margin-6)*" "),end="")
        put_king=input("Play King Position (e.g: d1): ").lower().strip()
        if put_king=="xx" or put_king=="XX":
            checkmate.reveal_safe_zones(tile,alpha,unique,display,margin,xff0000,xffde21,x696969,xf9f9f9)
            exit()
        if len(put_king)==2 and put_king[0] in alpha and put_king[1].isdigit():
            i=int(put_king[1])-1
            j=alpha.index(put_king[0])
            if 0 <= i < tile and (i,j) not in unique:
                display['K']=(i,j)
                unique.add((i,j))
                board(alpha,tile,margin,display,xff0000,xffde21,x696969,xf9f9f9)
                break
            else:
                alter=x00ffff
                message="Position Occupied - Please Try Again"
                print((margin-8)*" ",end="")
                print(f"{alter}{message}{xf9f9f9}",end="\n")
        else:
            alter=x00ffff
            message="Invalid Input - Please Try Board Number, e.g: d1 or c5"
            print((margin-17)*" ",end="")
            print(f"{alter}{message}{xf9f9f9}",end="\n")

    posKing=checkmate.distance_from_put_king(put_king)
    result=checkmate.checkmate(posKing,posQueen,posRook,posBishop,posPawn)

    if result=="R4":
        alter=xff0000
        message="Queen Checkmates King!"
        print((margin-1)*" ",end="")
        print(f"{alter}{message}{xf9f9f9}",end="\n")
    elif result=="R3":
        alter=xff0000
        message="Rook Checkmates King!"
        print((margin-1)*" ",end="")
        print(f"{alter}{message}{xf9f9f9}",end="\n")        
    elif result=="R2":
        alter=xff0000
        message="Bishop Checkmates King!"
        print((margin-1)*" ",end="")
        print(f"{alter}{message}{xf9f9f9}",end="\n")          
    elif result=="R1":
        alter=xff0000
        message="Pawn Checkmates King!"
        print((margin-1)*" ",end="")
        print(f"{alter}{message}{xf9f9f9}",end="\n")   
    else:
        alter=xffde21
        message="VICTORY!!! *** LONG-LIVE THE KING!!!"
        print((margin-8)*" ",end="")
        print(f"{alter}{message}{xf9f9f9}",end="\n")   

    #print(result)



