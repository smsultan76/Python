def matrix_mul(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    q = len(B)
    if n == q:
        c = []
        for i in range(m):
            c.append([])
            for j in range(p):
                c[i].append(0)
                for k in range(n):
                    c[i][j] += A[i][k] * B[k][j]
        
        return c
    else:
        return None

if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]
    print(matrix_mul(A, B))