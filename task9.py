
def isArmstrong(n):
    original = n
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** 3
        n = n // 10

    return total == original


for i in range(100, 1000):
    if isArmstrong(i):
        print(i, end=" ")
