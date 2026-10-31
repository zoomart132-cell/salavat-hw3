
def printXPattern(n):
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


printXPattern(5)
