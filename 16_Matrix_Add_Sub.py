def add_matrix(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Invalid"
    else:
        for i in range(len(mat1)):
           for j in range(len(mat1[0])):
                mat1[i][j] += mat2[i][j] 
        return mat1
    
def sub_matrix(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Invalid"
    else:
        return [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    
if __name__ == "__main__":
    mat1 = [[1, 2 , 3], [3, 4 , 5], [5, 6, 7]]
    mat2 = [[5, 6 ,7], [7, 8, 9], [9, 10, 11]]
    print("Matrix 1: ", mat1)
    print("Matrix 2: ", mat2)
    print()
    print("Addition of matrix: ", add_matrix(mat1, mat2))
    print()
    print("Subtraction of matrix: ", sub_matrix(mat1, mat2))