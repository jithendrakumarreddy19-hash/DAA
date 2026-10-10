# Out of Boundary Paths

def paths(m, n, N, i, j):
    if i < 0 or i >= m or j < 0 or j >= n:
        return 1

    if N == 0:
        return 0

    return (paths(m, n, N - 1, i + 1, j) +
            paths(m, n, N - 1, i - 1, j) +
            paths(m, n, N - 1, i, j + 1) +
            paths(m, n, N - 1, i, j - 1))


m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
N = int(input("Enter maximum moves: "))

i = int(input("Enter starting row: "))
j = int(input("Enter starting column: "))

print("Number of paths:", paths(m, n, N, i, j))