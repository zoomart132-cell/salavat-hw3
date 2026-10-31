def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def countPrimes(a, b):
    count = 0
    for n in range(a, b + 1):
        if isPrime(n):
            count += 1
    return count


a, b = map(int, input("A B = ").split())
print("Prime Count =", countPrimes(a, b))