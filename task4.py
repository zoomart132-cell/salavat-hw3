def printMatrix(n, m):
    num = 1
    for i in range(n):
        for j in range(m):
            print(num, end=' ')
            num += 1
        print()


n, m = map(int, input("N M = ").split())
printMatrix(n, m)