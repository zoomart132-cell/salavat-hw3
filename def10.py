
def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


print("GCD =", gcd(24, 36))
