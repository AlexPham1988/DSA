import os


N = 4

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

matrix = [
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16],
]



def displayMatrix( mat ): 
    for i in range(0, N):      
        for j in range(0, N):
            print '{:4}'.format(mat[i][j]),
        print ("")
     

def rorate1(matrix):
    for layer in range(N/2):
        last = N - 1 - layer
        for i in range(layer,last):
            offset = i - layer
            # save top
            top = matrix[layer][i]
            # left -> top
            matrix[layer][i] = matrix[last-offset][layer]
            # bottom -> left
            matrix[last-offset][layer] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # left - > right
            matrix[i][last] = top
    return matrix


def rorate2(matrix): 
    for layer in range(0, int(N/2)):
        last = N - 1 - layer
        for i in range(layer, last):
            offset = i - layer
            # save top
            top = matrix[layer][i]
            # right -> top
            matrix[layer][i] = matrix[i][last]
            # bottom -> right
            matrix[i][last] = matrix[last][last-offset]
            # left -> bottom
            matrix[last][last - offset] = matrix[last-offset][layer]
            # right -> left
            matrix[last-offset][layer] = top
    return matrix


displayMatrix(matrix)
# matrix1 = rorate1(matrix)
print '*'*10
matrix = rorate1(matrix)
displayMatrix(matrix)
