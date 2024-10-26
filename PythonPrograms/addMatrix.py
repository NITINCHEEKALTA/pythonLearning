def main():

    matrix1 = [[13,21,16],
               [41,53,67],
               [38,91,22]
               ]
    
    matrix2 = [[1,10,1],
               [1,3,6],
               [3,1,2]
               ]
    addMatrix(matrix1, matrix2)
    


def addMatrix(M1,M2):
    if len(M1) != len(M2) or len(M1[0]) != len(M2[0]):
        return "Matrices must have the same dimensions for additions"
    
    result = []

    for i in range(len(M1)):
        row = []

        for j in range(len(M1[0])):
            row.append(M1[i][j] + M2[i][j])
        
        result.append(row)
    
    for rw in result:
        print(rw)
    
    return result

    

if __name__ == "__main__":
    main()

