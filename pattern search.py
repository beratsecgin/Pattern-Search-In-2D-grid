def pattern_search(P, I):
    image_row = len(I)
    image_column = len(I[0])
    rotated_ninety= list(zip(*P[::-1]))
    rotated_hundredeigthy = list(zip(*rotated_ninety[::-1]))
    rotated_twohundredseventy = list(zip(*rotated_hundredeigthy[::-1]))


    def helper1(P,I,i,j):
        for row in range(len(P)):
            for col in range(len(P[0])):

                if P[row][col] != I[row+i][col+j]:
                    return False
        return True

    def helper2(rotated_ninety,I,i,j):
        for row in range(len(rotated_ninety)):
            for col in range(len(rotated_ninety[0])):

                if rotated_ninety[row][col] != I[row+i][col+j]:
                    return False
        return True

    def helper3(rotated_hundredeigthy,I,i,j):
        for row in range(len(rotated_hundredeigthy)):
            for col in range(len(rotated_hundredeigthy[0])):

                if rotated_hundredeigthy[row][col] != I[row+i][col+j]:
                    return False
        return True

    def helper4(rotated_twohundredseventy,I,i,j):
        for row in range(len(rotated_twohundredseventy)):
            for col in range(len(rotated_twohundredseventy[0])):

                if rotated_twohundredseventy[row][col] != I[row+i][col+j]:
                    return False
        return True



    for i in range(image_row-len(P)+1):
        for j in range(image_column-len(P[0])+1):
            if I[i][j] == P[0][0]:
                if helper1(P, I, i, j):
                    return (i ,j ,0)
                elif helper2(rotated_ninety, I, i, j):
                    return (i,j,90)
                elif helper3(rotated_hundredeigthy,I,i,j):
                    return (i,j,180)
                elif helper4(rotated_twohundredseventy,I,i,j):
                    return (i,j,270)
    return False

