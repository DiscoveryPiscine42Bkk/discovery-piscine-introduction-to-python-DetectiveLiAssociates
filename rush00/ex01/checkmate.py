def distance_from_put_king(put_king):
    #i=8-(int(put_king[1]))
    i=int(put_king[1])-1
    j=ord(put_king[0].lower())-ord('a')
    return (i,j)

def rook_eats_king(king,rook):
    return king[0]==rook[0] or king[1]==rook[1]

def bishop_eats_king(king,bishop):
    return abs(king[0]-bishop[0])==abs(king[1]-bishop[1])

def pawn_eats_king(king,pawn):
    return (king[0]-pawn[0]==1) and abs(king[1]-pawn[1])==1

def queen_eats_king(king,queen):
    return rook_eats_king(king,queen) or bishop_eats_king(king,queen)

def checkmate(posKing,posQueen,posRook,posBishop,posPawn):
    if rook_eats_king(posKing,posQueen) or bishop_eats_king(posKing,posQueen):
        return "R4"
    elif rook_eats_king(posKing,posRook):
        return "R3"
    elif bishop_eats_king(posKing,posBishop):
        return "R2"
    elif pawn_eats_king(posKing,posPawn):
        return "R1"
    else:
        return "R0"

def reveal_safe_zones(tile,alpha,unique,display,margin,xff0000,xffde21,x696969,xf9f9f9): 
    
    x00ff00="\033[102m"
    
    safe_tiles=[]

    for i in range(tile):
        for j in range(tile):
            if (i,j) not in unique:
                king_pos = (i,j)
                if checkmate(king_pos,
                                        display['Q'],
                                        display['R'],
                                        display['B'],
                                        display['P']) == "R0":
                    safe_tiles.append((i,j))

    boardMap=[["·" for _ in range(tile)] for _ in range(tile)]

    for piece, (i,j) in display.items():
        if piece=='K':
            paint=xffde21
        else:
            paint=xff0000
        boardMap[i][j]=paint+piece+xf9f9f9

    for i, j in safe_tiles:
        boardMap[i][j]=x00ff00+"K"+xf9f9f9

    print("\n"+((margin+2)*" "),end="")
    for a in alpha:
        print(a,end=" ")
    print()

    for i in range((tile-1),-1,-1):
        print((margin*" "),end="")
        print(i+1, end=" ")
        for j in range(tile):
            if (i+j)%2==0:
                bg=x696969
            else:
                bg=xf9f9f9
            print(f"{bg}{boardMap[i][j]}{xf9f9f9}",end=" ")
        print()

    print()
    title="SAFE ZONES FOR KING"
    resolution="GAME OVER"
    print(((margin-1)*" ")+f"{title:^18}")
    print(((margin-1)*" ")+("="*19))
    print(((margin-1)*" ")+f"{resolution:^20}")
    print(((margin-1)*" ")+("="*19))